"""Claim graphs for economic theory papers.

A teaching implementation of the framework in Ash, Ciccarone and Galletta (2026),
"Mapping Economic Theory with AI". A paper's argument is a directed hypergraph:
nodes are statements, and each route (hyperedge) derives one target from a set of
sources used jointly (AND). Several routes into one target are alternatives (OR).

Usage:
    python claim_graph.py example_graph.json            # structure and fragility
    python claim_graph.py --extract paper.txt out.json  # LLM extraction (needs OPENROUTER_API_KEY)
"""
import json
import os
import sys
from functools import lru_cache

PRIMITIVE = {"primitive", "assumption", "parameter restriction", "scope condition"}
RESULT = {"lemma", "proposition", "corollary", "existence result", "uniqueness result",
          "comparative static", "welfare result", "extension result"}
ALPHA = 0.5  # weight of a major claim relative to a headline claim


def load(path):
    g = json.load(open(path))
    nodes = {n["id"]: n for n in g["nodes"]}
    routes = g["routes"]
    for r in routes:
        for v in r["sources"] + [r["target"]]:
            assert v in nodes, f"route {r['id']} uses unknown node {v}"
    return nodes, routes


def incoming(nodes, routes):
    inc = {v: [] for v in nodes}
    for r in routes:
        inc[r["target"]].append(r)
    return inc


def support(nodes, routes, removed_nodes=(), removed_routes=()):
    """Equation (1): s(v)=0 if removed; 1 if no incoming route; else max over
    surviving routes of min over their sources."""
    inc = incoming(nodes, routes)
    D, X = set(removed_nodes), set(removed_routes)

    @lru_cache(None)
    def s(v):
        if v in D:
            return 0
        if not inc[v]:
            return 1
        return max((min(s(u) for u in r["sources"]) for r in inc[v] if r["id"] not in X),
                   default=0)

    return {v: s(v) for v in nodes}


def weight(node):
    return {"headline": 1.0, "major": ALPHA}.get(node.get("role"), 0.0)


def fragility(nodes, routes, removed_nodes=(), removed_routes=()):
    """Equation (3): weighted share (0-100) of headline and major claims losing support."""
    s = support(nodes, routes, removed_nodes, removed_routes)
    W = sum(weight(n) for n in nodes.values())
    return 100 * sum(weight(nodes[v]) * (1 - s[v]) for v in nodes) / W


def structure(nodes, routes):
    inc = incoming(nodes, routes)
    n, m = len(nodes), len(routes)
    H = [v for v, x in nodes.items() if x.get("role") == "headline"]
    P = [v for v, x in nodes.items() if x["type"] in PRIMITIVE]
    R = [v for v, x in nodes.items() if x["type"] in RESULT]
    premises = [v for v in nodes if not inc[v] and nodes[v].get("role") != "contextual"]

    @lru_cache(None)
    def depth(v):  # hyperedges on the longest path from a premise
        return max((1 + max(depth(u) for u in r["sources"]) for r in inc[v]), default=0)

    @lru_cache(None)
    def ancestors(v):
        out = set()
        for r in inc[v]:
            for u in r["sources"]:
                out |= {u} | ancestors(u)
        return frozenset(out)

    anc_H = set().union(*(ancestors(h) for h in H)) - set(H) if H else set()
    derived = [v for v in nodes if inc[v]]
    loads = {p: fragility(nodes, routes, removed_nodes=[p]) for p in premises}
    top = max(loads, key=loads.get) if loads else None
    return {
        "statements n": n, "routes m": m, "headline claims": len(H),
        "result yield |R|/|P|": round(len(R) / len(P), 2) if P else None,
        "headline yield |H|/|P|": round(len(H) / len(P), 2) if P else None,
        "density m/n": round(m / n, 2),
        "mean fan-in": round(sum(len(r["sources"]) for r in routes) / m, 2) if m else 0,
        "max headline depth": max((depth(h) for h in H), default=0),
        "mean headline depth": round(sum(depth(h) for h in H) / len(H), 2) if H else 0,
        "route redundancy": round(sum(len(inc[v]) >= 2 for v in derived) / len(derived), 2) if derived else 0,
        "headline coverage": round(len(anc_H) / (n - len(H)), 2) if n > len(H) else 0,
        "max load (fragility of most consequential premise)": round(loads[top], 1) if top else 0,
        "most consequential premise": top,
    }


EXTRACT_PROMPT = """You reconstruct the argument of an economic theory paper as a claim graph.
Return JSON only: {"nodes": [{"id", "type", "role", "text"}], "routes": [{"id", "sources", "target"}]}.
- Each node is one atomic statement. type is one of: research question, primitive, definition,
  assumption, parameter restriction, equilibrium concept, formal condition, lemma, proposition,
  corollary, existence result, uniqueness result, equilibrium selection, comparative static,
  welfare result, mechanism claim, substantive claim, interpretation claim, policy claim,
  scope condition, extension result, illustration, external input.
- role is headline (the paper's main contributions), major, supporting, auxiliary or contextual.
- A route lists the statements used JOINTLY to derive its target. Give a second route into the same
  target only if the paper presents a genuinely alternative derivation. Only derivations, never
  links that merely motivate or illustrate. The graph must be acyclic.
- Keep formal propositions and the economic claims derived from them as separate nodes.
"""


def extract(paper_txt, out_json, model="anthropic/claude-sonnet-5.5"):
    """One-shot extraction. The paper uses an agentic, multi-pass system with checks;
    this single call is a classroom approximation."""
    from openai import OpenAI
    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.environ["OPENROUTER_API_KEY"])
    text = open(paper_txt).read()[:200_000]
    reply = client.chat.completions.create(
        model=model, response_format={"type": "json_object"},
        messages=[{"role": "system", "content": EXTRACT_PROMPT}, {"role": "user", "content": text}])
    g = json.loads(reply.choices[0].message.content)
    json.dump(g, open(out_json, "w"), indent=2)
    print(f"wrote {out_json}: {len(g['nodes'])} statements, {len(g['routes'])} routes")


if __name__ == "__main__":
    if sys.argv[1] == "--extract":
        extract(sys.argv[2], sys.argv[3])
        sys.exit()
    nodes, routes = load(sys.argv[1])
    for k, v in structure(nodes, routes).items():
        print(f"{k:55s} {v}")
    print("\nFragility of removing each route:")
    for r in routes:
        print(f"  {r['id']} -> {r['target']:6s} {fragility(nodes, routes, removed_routes=[r['id']]):5.1f}")
