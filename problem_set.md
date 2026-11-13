# Problem Set: Extending Claim Graphs Beyond Economic Theory

*Language Modelling for Economics, ECB DG Research, 19–20 November 2026*

## Background

Ash, Ciccarone, and Galletta (2026), "Mapping Economic Theory with AI," represent a theory paper as a **claim graph**: a directed hypergraph whose nodes are statements (assumptions, definitions, lemmas, propositions, economic claims) and whose hyperedges are derivations, each deriving one target from a set of sources used jointly. Several derivations into the same target are alternatives. On this structure they define descriptive measures (yield, depth, fan-in, coverage, redundancy) and an intervention measure, **network fragility**: the weighted share of headline and major claims that lose support when a premise or derivation is removed.

The repository's [`code/claim_graph.py`](code/claim_graph.py) implements these measures and a one-call LLM extraction step.

## Task

Extend this approach to a different kind of economic or financial text, where conclusions also rest on chains of premises. Work in groups of two to three. Suggested domains (or choose your own):

1. **Monetary policy communication.** Map an ECB monetary policy statement or account of a Governing Council meeting: which projections, risk assessments, and judgements support the policy decision and the forward guidance?
2. **Financial stability reports.** Map the argument from indicators and stress-test results to the stated vulnerabilities and policy recommendations.
3. **Empirical papers.** Map the argument from data, identifying assumptions, and estimates to the headline causal claims. Which identifying assumption carries the most weight?
4. **Equity research or credit rating reports.** Map how forecasts and assumptions support a valuation, rating, or recommendation.
5. **Legal and regulatory texts.** Map a court ruling on central bank powers or a supervisory decision from legal premises to holdings.

## Questions

1. **Representation (design).** Adapt the representation to your domain. What are the node types (replacing or extending the paper's 23 types)? What counts as a "headline" claim, and what counts as a premise? Is the AND/OR hyperedge structure appropriate, or does your domain need something else (for example, probabilistic or weighted support, or evidence that strengthens rather than establishes a claim)? Justify each choice in a few sentences.

2. **Extraction.** Modify the extraction prompt in `claim_graph.py` for your domain and apply it to at least three documents. Save each graph as JSON.

3. **Validation.** For one document, build the graph by hand (or carefully correct the LLM's graph) and compare it with the automated version. Report agreement on nodes, on headline claims, and on edges. Where does the model go wrong?

4. **Measurement.** Compute the structural measures and fragility for each graph. Which premise has the largest load? Interpret one result substantively: what would it mean for the document's conclusions if that premise were wrong?

5. **An economic question.** Use your measures to say something about your domain. Examples: do policy statements become more or less fragile over time, or in crises? Do empirical papers with more robustness checks have higher route redundancy? Do rating changes rest on fewer premises than affirmations? With only a handful of documents, state this as a well-motivated hypothesis and describe the data and design you would need to test it.

6. **Limits.** In half a page, discuss what the graph does not capture in your domain, and the main risks of relying on LLM-extracted graphs for policy or investment decisions.

## Deliverables

- A short write-up (at most four pages) answering questions 1–6.
- Your code and JSON graphs in a repository or zip file.

You are encouraged to use AI coding agents throughout. Document how you used them and how you checked their output.
