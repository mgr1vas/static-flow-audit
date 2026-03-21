# Research Roadmap: Static-Flow-Audit

This roadmap outlines the strategic research phases for my undergraduate thesis. The goal is to complete the theoretical and benchmarking research by **September 2026**.

## Phase 1: Research & Theory
**Timeline: March 21, 2026 - May 31, 2026**
*Focus: Mastering the "Compiler mindset" and Python Internals.*

### [March 21 - April 30, 2026] - Month 1: The Building Blocks
- [x] **AST Mastery:** Learn to use Python's `ast` module. Practice parsing strings into trees.
- [x] **Node Exploration:** Identify core nodes (`Return`, `Assign`, `Call`, `FunctionDef`).
- [ ] **Compiler Theory:** Study Lexical Analysis, Parsing, and the differences between Static and Dynamic Analysis.
- [ ] **Documentation:** Summarize initial findings in `/theory/ast_basics.md`.

### [May 1 - May 31, 2026] - Month 2: Advanced Logic
- [ ] **Control Flow Graphs (CFG):** Understand how programs map execution paths (nodes and edges).
- [ ] **Dead Code Taxonomy:** Categorize "Unreachable code" (post-termination) vs. "Unused code" (uncalled functions).
- [ ] **Academic Review:** Search and link 3-5 key academic papers in `/papers/`.


## Phase 2: Benchmarking & Tools Audit
**Timeline: June 1, 2026 - July 15, 2026**
*Focus: Evaluating industry standards (Vulture, Ruff).*

- [ ] **Environment Setup:** Install and configure **Vulture**, **Ruff**, and **Bandit** on local test samples.
- [ ] **Comparative Audit:** Run tools against "dirty" code samples and document where they fail or succeed.
- [ ] **Gap Analysis:** Identify specific dead code patterns that current tools miss.
- [ ] **Deliverable:** Record all findings in `/tools_benchmark/vulture_audit.md`.

## Phase 3: Engine Research & Prototyping
**Timeline: July 16, 2026 - September 15, 2026**
*Focus: Mapping the logic for the custom Static Analysis Backend.*

### [July 16 - August 20, 2026] - Month 4: Rule Logic
- [ ] **Custom Logic Design:** Design scripts to detect code blocks following `return`, `break`, and `raise`.
- [ ] **Function Mapper Research:** Research how to map all `def` statements and cross-reference them with `Call` nodes via AST.

### [August 21 - September 15, 2026] - Month 5: Architecture & Integration
- [ ] **Backend Planning:** Define the **FastAPI** structure to orchestrate the scan process.
- [ ] **JSON Schema:** Define the standard JSON format for scan results (Bridge to Frontend).

## Future Phases (Post-Research)
**Timeline: October 2026 - Early 2027**

### Phase 4: Full Development & Visualization
- [ ] Build the **React** Dashboard and integrate code highlighting (Prism.js).
- [ ] Implement the Comparison Matrix (Custom Engine vs. Vulture).

### Phase 5: Writing & Final Evaluation
- [ ] Draft the 60+ page thesis document.
- [ ] Perform real-world testing on large Open Source projects.
