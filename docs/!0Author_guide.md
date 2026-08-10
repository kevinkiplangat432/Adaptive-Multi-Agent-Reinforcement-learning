<!-- markdownlint-disable -->
<p align="center">
  <img src="LookMind.png" alt="LookMind" width="300" />
</p>


# ARVIS Research Documentation Guide

> **Purpose:** This document serves as the authoring guide for every document contained in the `docs/` directory. It defines the purpose, scope, and expected content of each file, ensuring that the research remains organized, avoids unnecessary repetition, and evolves consistently over the lifetime of the ARVIS project.

---

# Research Philosophy

The documents in this repository are **not** a thesis, user manual, or software documentation.

They collectively form the **research blueprint** of ARVIS.

Each document answers a different question about the system. No document should attempt to explain the entire project. Instead, each should focus on one aspect in depth and refer to other documents where appropriate.

A useful rule while writing is:

> **Every document should answer one primary question exceptionally well.**

Avoid copying large sections between files. Instead, briefly summarize related concepts and reference the appropriate document.

---

# Document Overview

---

## 00_research_overview.md

### Purpose

Provides a high-level introduction to the entire research project.

### Primary Question

> **What is ARVIS, why does it exist, and what is the overall vision?**

### Should Contain

* Project summary
* Research motivation
* Overall architecture overview
* Research goals
* Timeline
* Relationship between all documents

### Should Not Contain

* Mathematical details
* Implementation details
* Dataset specifications
* Algorithm descriptions

Think of this as the table of contents and executive summary for the research.

---

## 01_problem_statement.md

### Purpose

Defines the problem being investigated.

### Primary Question

> **What problem are we trying to solve?**

### Should Contain

* Background
* Existing limitations
* Research gap
* Objectives
* Research questions
* Scope
* Expected outcomes

### Should Not Contain

* Detailed solutions
* Graph architecture
* Reinforcement learning design

The focus is on the problem, not the implementation.

---

## 02_system_architecture.md

### Purpose

Describes the overall system from a high level.

### Primary Question

> **How is the proposed system organized?**

### Should Contain

* Major components
* Layered architecture
* Data flow
* High-level diagrams
* Responsibilities of each subsystem

### Should Not Contain

* Mathematical derivations
* Graph schema
* Reward equations

This document explains how all components fit together.

---

## 03_graph_design.md

### Purpose

Defines the digital representation of the AI ecosystem.

### Primary Question

> **How is reality represented inside ARVIS?**

### Should Contain

* Node types
* Edge types
* Dynamic graph updates
* Feature engineering
* Graph construction
* Design principles

### Should Not Contain

* GNN implementation details
* RL algorithms
* Production deployment

This document defines the language that the rest of the system understands.

---

## 04_mathematical_foundation.md

### Purpose

Introduces the mathematical concepts that underpin the research.

### Primary Question

> **What mathematics does ARVIS rely upon?**

### Should Contain

* Graph theory
* Linear algebra
* Probability
* Bayesian inference
* Optimization
* Markov Decision Processes
* Reinforcement Learning fundamentals

### Should Not Contain

* Model-specific implementation
* Hyperparameters
* Experimental results

This document builds intuition rather than proving theorems.

---

## 05_literature_review.md

### Purpose

Summarizes existing research relevant to ARVIS.

### Primary Question

> **What has already been done, and where does this work fit?**

### Should Contain

* AI observability
* AI safety
* Graph Neural Networks
* Reinforcement Learning
* Bayesian uncertainty
* Multi-agent systems
* Comparative analysis
* Identified research gaps

### Should Not Contain

* Personal opinions without evidence
* Implementation details

The literature review should justify the research direction.

---

## 06_dataset_design.md

### Purpose

Defines the data used throughout the project.

### Primary Question

> **What data does the system learn from?**

### Should Contain

* Data sources
* Feature definitions
* Labels
* Graph generation
* Synthetic data generation
* Data preprocessing
* Dataset splits

### Should Not Contain

* Training procedures
* Reward design

---

## 07_rl_environment.md

### Purpose

Defines the reinforcement learning problem.

### Primary Question

> **What environment is the agent learning within?**

### Should Contain

* State space
* Action space
* Observation space
* Transition function
* Episodes
* Terminal conditions

### Should Not Contain

* Reward engineering
* GNN implementation

---

## 08_reward_function.md

### Purpose

Defines how success is measured during reinforcement learning.

### Primary Question

> **What behavior should the agent learn?**

### Should Contain

* Reward equations
* Positive rewards
* Negative rewards
* Reward shaping
* Trade-offs

### Should Not Contain

* RL algorithm details

---

## 09_uncertainty_estimation.md

### Purpose

Defines how the system reasons about confidence.

### Primary Question

> **When should ARVIS trust its own predictions?**

### Should Contain

* Bayesian inference
* Confidence estimation
* Calibration
* Human escalation criteria

### Should Not Contain

* RL reward logic

---

## 10_gnn_architecture.md

### Purpose

Defines the graph learning model.

### Primary Question

> **How is knowledge extracted from the graph?**

### Should Contain

* Candidate GNN architectures
* Message passing
* Embedding generation
* Architecture comparison
* Final model selection

### Should Not Contain

* Dataset generation

---

## 11_multi_agent_design.md

### Purpose

Defines collaboration between monitoring agents.

### Primary Question

> **How do specialized agents work together?**

### Should Contain

* Agent roles
* Communication
* Coordination
* Failure handling

### Should Not Contain

* Reinforcement learning mathematics

---

## 12_training_pipeline.md

### Purpose

Defines the complete research workflow.

### Primary Question

> **How is the system trained from raw data to deployment?**

### Should Contain

* Data pipeline
* Graph construction
* Model training
* Evaluation
* ONNX export

---

## 13_experiment_design.md

### Purpose

Plans every experiment before implementation.

### Primary Question

> **How will hypotheses be tested?**

### Should Contain

* Baselines
* Ablation studies
* Experimental variables
* Hypotheses

---

## 14_evaluation_metrics.md

### Purpose

Defines how performance is measured.

### Primary Question

> **How do we know the system is successful?**

### Should Contain

* Accuracy
* Precision
* Recall
* F1
* ROC-AUC
* RL metrics
* Latency
* Resource usage

---

## 15_production_architecture.md

### Purpose

Bridges research and engineering.

### Primary Question

> **How does the research become a production system?**

### Should Contain

* Python research stack
* ONNX export
* Go runtime
* APIs
* Databases
* Deployment architecture

---

## 16_research_roadmap.md

### Purpose

Defines the long-term evolution of the project.

### Primary Question

> **Where is this research going?**

### Should Contain

* Milestones
* Phases
* Timeline
* Dependencies
* Long-term goals

---

## 17_future_work.md

### Purpose

Captures ideas beyond the current scope.

### Primary Question

> **What comes next after this research?**

### Should Contain

* Future models
* Graph Transformers
* World Models
* Federated learning
* New research directions

---

## 18_glossary.md

### Purpose

Provides consistent definitions for terminology used throughout the project.

### Primary Question

> **What does each technical term mean within the context of ARVIS?**

This should become the project's shared vocabulary.

---

## 19_bibliography.md

### Purpose

Maintains a centralized list of references.

### Primary Question

> **Which sources support this research?**

Include books, journal articles, conference papers, technical reports, and other references cited throughout the documentation.

---

# Final Guiding Principle

When writing any document, always ask:

> **If this document disappeared tomorrow, what unique knowledge about ARVIS would be lost?**

The answer to that question defines the document's purpose.

If the answer overlaps significantly with another document, move that content to the appropriate place instead of duplicating it.

Over time, these documents should evolve into a coherent research manual that explains not only **what ARVIS is**, but also **why every architectural and scientific decision was made**.
