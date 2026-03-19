# Static-Flow-Audit
### Undergraduate Thesis: Research on Static Analysis & Dead Code Detection
![Sample-Logo](iamges/sample-uoi.jpg)

This repository is dedicated to the **Research Phase** of my undergraduate thesis. It serves as a centralized hub for documenting theory, analyzing existing tools, and mapping the technical requirements for detecting unreachable and unused code.

> **Note:** This repository is currently for research and documentation purposes only. Implementation will follow based on the findings recorded here.


## Project Structure
To maintain a clean and academic workflow, the repository follows this structure:

```text
/
├── theory/              # Research on Compiler Theory (AST, CFG, Parsing)
│   ├── ast_basics.md    # Documentation on Abstract Syntax Trees
│   └── cfg_logic.md     # Logic for Control Flow Graphs
├── tools_benchmark/     # In-depth analysis of industry tools
│   ├── vulture_audit.md # Testing Vulture (Unused code)
│   ├── ruff_audit.md    # Testing Ruff (Performance & Linting)
│   └── bandit_audit.md  # Testing Bandit (Security-focused analysis)
├── samples/             # Code samples (Python/C++) with intentional dead code
├── papers/              # Summaries and links to academic papers
└── README.md            # Project overview and roadmap
```
