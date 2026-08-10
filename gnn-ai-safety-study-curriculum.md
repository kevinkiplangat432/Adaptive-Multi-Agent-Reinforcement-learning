<!-- markdownlint-disable -->
<p align="center">
  <img src="LookMind.png" alt="LookMind" width="300" />
</p>


# Study Curriculum: Graph Neural Networks for AI Safety Monitoring

This is the full landscape, listed flat, with nothing assumed as already covered. Work through it in this order.

---

## 1. Mathematical Foundations

- **Linear algebra**: vectors, matrices, eigenvalues/eigenvectors, matrix decomposition (SVD), vector spaces
  - Gilbert Strang, *Introduction to Linear Algebra* (book, or free MIT OCW 18.06 lecture series)
- **Calculus**: derivatives, partial derivatives, chain rule, gradients, Jacobians
  - Stewart, *Calculus* (book), or 3Blue1Brown's "Essence of Calculus" video series (free, YouTube)
- **Probability and statistics**: random variables, distributions, expectation, variance, Bayes' theorem, conditional probability
  - Blitzstein & Hwang, *Introduction to Probability* (free PDF, Harvard Stat 110 companion)
- **Optimization**: gradient descent, convexity, Lagrange multipliers, constrained optimization
  - Boyd & Vandenberghe, *Convex Optimization* (free PDF) — at least the intro chapters

## 2. Graph Theory

- Basic definitions: graphs, directed/undirected, weighted, multigraphs, adjacency matrices/lists
- Graph properties: connectivity, paths, cycles, degree distribution, centrality measures
- Heterogeneous graphs: multiple node/edge types (directly relevant to your ARVIS graph schema)
- Resources:
  - Diestel, *Graph Theory* (free PDF from author's website)
  - Any discrete mathematics course covering graph theory (e.g., MIT OCW 6.042)

## 3. Neural Network Fundamentals

- Perceptrons, feedforward networks, backpropagation
- Activation functions, loss functions, gradient descent variants (SGD, Adam, RMSprop)
- Regularization: dropout, weight decay, batch normalization
- Representation learning and embeddings
- Resources:
  - Michael Nielsen, *Neural Networks and Deep Learning* (free online book)
  - Goodfellow, Bengio, Courville, *Deep Learning* (free online, MIT Press)
  - Andrew Ng's Deep Learning Specialization (Coursera) as a structured alternative

## 4. Graph Representation Learning and Graph Neural Networks

- Node embeddings: DeepWalk, node2vec
- Message passing framework
- Graph Convolutional Networks (GCN)
- GraphSAGE (inductive learning on graphs)
- Graph Attention Networks (GAT)
- Heterogeneous Graph Transformer (HGT) — directly relevant since your graph has multiple node types
- Temporal Graph Neural Networks (TGNN) — relevant since your graph evolves over time
- Resources:
  - Stanford CS224W: Machine Learning with Graphs (free lectures, slides, and assignments online)
  - William L. Hamilton, *Graph Representation Learning* (free PDF)
  - Original papers: Kipf & Welling (GCN, 2017), Hamilton et al. (GraphSAGE, 2017), Veličković et al. (GAT, 2018), Hu et al. (HGT, 2020)

## 5. Bayesian Deep Learning and Uncertainty Estimation

- Why point predictions aren't enough for safety-critical decisions
- Monte Carlo Dropout
- Deep ensembles
- Evidential deep learning
- Bayesian neural networks (weight uncertainty)
- Resources:
  - Yarin Gal, *Uncertainty in Deep Learning* (PhD thesis, free online) — the standard reference
  - Gal & Ghahramani, "Dropout as a Bayesian Approximation" (2016 paper)
  - Blundell et al., "Weight Uncertainty in Neural Networks" (2015 paper)
  - Lakshminarayanan et al., "Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles" (2017 paper)

## 6. Reinforcement Learning

- Markov Decision Processes (MDPs)
- Value functions, Q-learning
- Policy gradient methods
- Proximal Policy Optimization (PPO)
- Constrained/safe RL (relevant to your intervention-policy design)
- Multi-agent RL basics
- Resources:
  - Sutton & Barto, *Reinforcement Learning: An Introduction* (free PDF, the standard text)
  - David Silver's RL course (UCL, free lectures on YouTube)
  - OpenAI Spinning Up in Deep RL (free, practical companion to the theory)

## 7. Applied Tooling

- PyTorch (general deep learning framework)
- PyTorch Geometric (graph neural network library)
- NetworkX (graph construction and manipulation, used in early-stage experimentation)
- Resources:
  - PyTorch official tutorials
  - PyTorch Geometric official documentation and example notebooks (GCN, GAT, heterogeneous graph examples)
  - NetworkX documentation

## 8. Adjacent Literature (Closest Existing Work)

Read directly, not just as citations:

- Systematic literature review on GNNs, Transformers, and RL in network threat detection (2025, *Electronics*/MDPI)
- GS-MARL: Graph-based Safe Multi-Agent Reinforcement Learning (2026, *Neural Networks*)
- Safety-Contract Graph MARL for Autonomous Network Security Response (2026, arXiv), including the CybORG/CAGE Challenge simulation environment it's built on
- Graph attention network-based MARL for smart contract vulnerability detection (2025, *Scientific Reports*)

## 9. Domain Context (AI Agent Ecosystem Specifics)

- Prompt injection and jailbreak attack taxonomies
- LLM observability/tracing concepts: what current tools (Langfuse, Arize/Phoenix, LangSmith, Datadog LLM Observability) actually capture and where they fall short
- AI governance and compliance frameworks relevant to Kenyan financial regulation (for ARVIS positioning specifically)

## 10. Capstone: Prototype

- Represent real or synthetic ARVIS proxy logs as a small heterogeneous graph
- Train a basic GNN classifier for risk detection
- Compare against a simple non-graph baseline classifier
- Get one honest, reproducible result before making any public claims
