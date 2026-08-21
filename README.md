<!-- markdownlint-disable -->
<p align="center">
  <img src="LookMind.png" alt="LookMind" width="300" />
</p>


# ARVIS Intelligence Layer

**Graph Neural Networks · Bayesian Uncertainty Estimation · Reinforcement Learning**

**Status: Early build · Proprietary · Companion to [ARVIS](https://github.com/kevinkiplangat432/arvis)**

The system that will let ARVIS watch relationships between AI actions, not just isolated events, and know how much to trust its own judgment.

---

## The Problem This Solves

ARVIS today watches one request at a time. That's the right starting point, but it has a ceiling: a chain of individually unremarkable actions, an agent calling a tool, that tool reaching a database, that result feeding another agent, can add up to something worth stopping, while every single step in that chain looks fine in isolation. Watching events one at a time can never catch that. Watching the shape of the whole chain can.

This is the system built to see that shape, and to know, honestly, when it isn't sure.

## What This Is Building

Three capabilities, developed together as one system, not three separate tools:

**A structural view of activity.** AI activity gets represented as a living graph, agents, tools, data sources, and the calls between them, rather than a flat log of independent events. A model built for reasoning over graph structure, drawing on established architectures like GraphSAGE and GAT, learns to spot patterns that only exist across connected actions.

**Honest confidence.** Every judgment this system makes carries a genuine measure of how much it should be trusted, not just a score. A confident, wrong answer is worse than an honest "not sure" in a compliance context specifically, so the system is built to tell those two apart, and to say clearly when a human should look instead of guessing.

**Smart attention under a limited budget.** As activity scales, nothing can be scrutinized equally. This piece learns where the system's limited inspection capacity is best spent right now, given what's uncertain and what's changed. Its job stops there, deliberately. It decides where to look, never what to do about what it finds.

## Where the Line Sits, Permanently

This system can recommend, flag, and prioritize. It cannot warn, restrict, pause, or block anything. That authority belongs entirely to ARVIS's own governance layer, a separate, deterministic, fully auditable system. This isn't a policy that could be relaxed later, it's how the two systems are built to fit together: this repository has no code path that produces an intervention, because intervention was never included in what it's capable of outputting.

```
Activity → Graph representation → Structural analysis
         → Confidence estimate → Attention decision
                                        │
                                        ▼
                    (handed to ARVIS's governance layer,
                     which decides, acts, and records —
                     never this system)
```

## How This Fits With ARVIS

[ARVIS](https://github.com/kevinkiplangat432/arvis) is the product in front of an organization's AI traffic today, intercepting, logging, and enforcing policy. This repository is what makes ARVIS's judgment smarter over time, eventually exported as a model ARVIS's Go binary runs inference against. Two repositories, two responsibilities: this one reasons about what deserves attention, ARVIS decides what happens next and keeps the record of it.

## Technology

| Component | Technology |
|---|---|
| Language | Python 3.12 |
| Deep Learning | PyTorch |
| Graph Learning | PyTorch Geometric |
| Reinforcement Learning | Stable-Baselines3 |
| RL Environment | Gymnasium |
| Uncertainty Estimation | TorchUncertainty / Monte Carlo Dropout |
| Data Processing | NumPy, Pandas |
| Graph Processing | NetworkX |
| Experiment Tracking | MLflow |
| Model Export | ONNX |

Integrates with ARVIS's production stack (Go, Chi, PostgreSQL, Redis, ONNX Runtime, NATS) via exported ONNX models, not a shared codebase.

## Repository Layout

```
├── src/            ← the system being built
├── research/        ← literature, experiment notes, design exploration
├── models/          ← trained model artifacts
├── training/
├── evaluation/
└── exports/         ← ONNX exports for ARVIS integration
```

The `research/` folder holds the thinking behind decisions made here, worth reading if you need to understand *why*, but it's reference material, not the front door. The front door is a system being built, not a paper being written.

## Status

Early build. No trained model exists yet. This repository is honest about that rather than dressing up design work as a finished capability, the same standard ARVIS's own README holds itself to.

## License

This project is proprietary and confidential. All rights reserved. No part of this repository may be reproduced, distributed, or used to create derivative works without prior written permission from the author.

See [`LICENSE`](LICENSE) for the full text.

## Contact

Kevin - <kiplangatkevin335@gmail.com>

Joe   - <ngunojoe@gmail.com>

