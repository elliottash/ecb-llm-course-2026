# Problem Set: Text as Data and Claim Graphs

*Language Modelling for Economics, ECB DG Research, 19–20 November 2026*

The problem set has two parts. Work in groups of two to three. You are encouraged to use AI coding agents throughout; document how you used them and how you checked their output.

# Part 1: Text as data

## Data

Bring your own dataset: a collection of documents relevant to your work, such as central bank speeches or statements, news articles, firm filings, earnings call transcripts, survey responses, or social media posts. Aim for at least a few thousand documents with some metadata (date, source, author, or an outcome) so that you can compare groups or track change over time. Use only data you are allowed to share with your group and to process with external AI services.

If you do not have a suitable dataset, use our [news videos dataset](https://github.com/elliottash/zrh_ai_econ/blob/main/assignments/news_videos.csv.gz): titles and descriptions of 23,689 YouTube videos posted by Fox News and MSNBC from January to August 2026, with dates and engagement counts.

Describe the dataset: where it comes from, how you collected and cleaned it, what one observation is, and its main descriptive statistics.

## Questions

1. **Representations.** Represent your documents as vectors (bag-of-words, Word2Vec, BERT, sentence transformers, or another method; explain your choice). Record the exact model versions.

2. **Clustering.** Cluster the representations (PCA, k-means, and so on). Can you name the clusters after reading the documents nearest each centroid? Do cluster shares differ across groups in your metadata, or over time?

3. **Prediction.** Train a model (logistic regression, random forest, gradient boosting) to predict a variable in your metadata, such as the source, the period, or an outcome, from the document representations. Report held-out performance. Inspect what drives the predictions before you believe them: a model can score well by finding a superficial marker (a template phrase, a signature, a date format) rather than the content you care about.

4. **Zero-shot measures.** Score documents against short descriptions of a concept (for example, with embedding similarity) to build a continuous measure without training data. Report the descriptions you used and check that your result survives reasonable rewordings.

5. **Labelling with an LLM (required).** Using a model through an API (for example, a free model on OpenRouter), label a reproducible random sample of 40 documents.
   a. Define one construct (for example, topic, tone, or stance), with clear labels and an uncertain/other option.
   b. Write one fixed prompt asking for exactly one label. Save the prompt, the requested model, and the model reported in the API response. Do not put your API key in the notebook.
   c. Label at least 15 of the same documents by hand. Report agreement, inspect the disagreements, and explain one recurring source of error.
   d. Use the model labels for one simple comparison. Say what it suggests and why the labels still require validation.

6. **Optional: a webpage.** Use an AI coding agent to turn one finding into a small interactive webpage. Check that it represents your analysis accurately.

Off-the-shelf models may be unreliable on tasks they were not built for. Validate their output on a subsample you have looked at yourself.

# Part 2: Extending claim graphs beyond economic theory

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

# Deliverables

- A short write-up (at most six pages) covering Part 1 and Part 2.
- Your code, notebooks, and JSON graphs in a repository or zip file.
