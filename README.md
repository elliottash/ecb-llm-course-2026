# Language Modelling for Economics

[PDF version](syllabus.pdf)

European Central Bank, DG Research, Frankfurt, 19–20 November 2026

Instructor: Elliott Ash (ETH Zurich)

## Overview

Recent advances in artificial intelligence are reshaping both the economy and the empirical toolkit available to economists. Machine learning, natural language processing, and generative AI expand the range of what economists can measure and enable new research designs. This two-session course introduces language modelling for economic research: from representing text as data, through embeddings and transformer models, to using large language models and AI agents in the research workflow. Each session combines lecture and hands-on work.

## Preparation

1. Bring a laptop suitable for coding, and a dataset of documents relevant to your work for the problem set.
2. Have access to at least one capable AI service (e.g., ChatGPT Plus or Claude Pro, or an institutional equivalent).
3. If possible, install a coding agent (Codex and/or Claude Code), Git, and a working Python/Jupyter environment.

## Session 1: Thursday 19 November, 14:00–18:00
### From text to embeddings

- **Introduction:** AI and the empirical toolkit of economics; text, images, and other unstructured data as economic data.
- **Introduction to economics with AI agents:** what coding and research agents can do for economists today; a live demo of an agent carrying out a small empirical task end to end, and how to supervise and check its work.
- **Machine-learning basics:** supervised and unsupervised learning, prediction versus inference, and validation.
- **Text as data:** tokenization, document-term representations, and dictionary and classifier approaches.
- **Embeddings:** Word2Vec, sentence embeddings, similarity, and clustering for measurement.
- **Transformers:** contextual embeddings, self-attention (queries, keys, and values), and masked-language-model training (BERT).
- **ML and econometrics:** using machine-learned measures in downstream regressions; measurement error and inference.
- **Hands-on:** computing embeddings and similarity on an economic text corpus in Python.

## Session 2: Friday 20 November, 09:00–13:00
### Large language models in economic research

- **LLMs and alignment:** pretraining, instruction tuning, and preference alignment; what this means for research use.
- **LLMs as measurement tools:** zero- and few-shot labelling, prompt design, validation against human labels, and reproducibility.
- **Working with AI agents:** coding agents for data collection, cleaning, and analysis; agentic research workflows and their failure modes.
- **Software development with AI:** building research tools and pipelines with AI assistance.
- **Hands-on:** labelling a sample of documents with an LLM API, validating a subset by hand, inspecting disagreements, and using the labels in a substantive comparison.
- **Application: mapping economic theory with AI.** Representing a theory paper as a claim graph of assumptions, intermediate results, and conclusions; measuring yield, depth, and fragility; auditing errors and assessing repairs (Ash, Ciccarone, and Galletta 2026). Hands-on: [`code/claim_graph.py`](code/claim_graph.py) computes the paper's structure and fragility measures on an example graph and extracts a graph from a paper with an LLM.
- **Wrap-up:** open questions and discussion.

## Problem set

[Part 1: text as data, on your own dataset; Part 2: extending claim graphs to another field of economics or finance](problem_set.md) ([PDF](problem_set.pdf)).

## Readings

- Ash, E., A. Ciccarone, and S. Galletta (2026). "Mapping Economic Theory with AI." Working paper.
- Ash, E., and S. Hansen (2023). "Text Algorithms in Economics." *Annual Review of Economics* 15: 659–688.
- Gentzkow, M., B. Kelly, and M. Taddy (2019). "Text as Data." *Journal of Economic Literature* 57(3): 535–574.
- Ludwig, J., S. Mullainathan, and A. Rambachan (2025). "Large Language Models: An Applied Econometric Framework." NBER Working Paper 33344.
- Asirvatham, H., E. Mokski, and A. Shleifer (2026). "GPT as a Measurement Tool." NBER Working Paper 34834.
