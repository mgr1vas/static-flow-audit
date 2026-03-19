# Thesis Roadmap: Static-Flow-Audit

This roadmap outlines the strategic phases for the research, development, and documentation of my undergraduate thesis on **Static Analysis and Dead Code Detection**.

## Phase 1: Research & Theory (Months 1-2)
*Focus: Mastering the "Compiler mindset" and Python Internals.*

### Month 1: The Building Blocks
- [ ] **AST Mastery:** Learn to use Python's `ast` module. Practice parsing strings into trees and using `ast.walk()`.
- [ ] **Compiler Theory:** Study Lexical Analysis, Parsing, and the differences between Static and Dynamic Analysis.
- [ ] **Documentation:** Summarize findings in `/theory/ast_basics.md`.

### Month 2: Advanced Logic
- [ ] **Control Flow Graphs (CFG):** Understand how programs map execution paths (nodes and edges).
- [ ] **Dead Code Taxonomy:** Categorize "Unreachable code" (post-return) vs. "Unused code" (uncalled functions).
- [ ] **Academic Review:** Search and link 3-5 key papers in `/papers/`.


## Phase 2: Benchmarking & Tools Audit (Month 3)
*Focus: Evaluating industry standards (Vulture, Ruff).*

- [ ] **Environment Setup:** Install and configure **Vulture**, **Ruff**, and **Bandit** on local test samples.
- [ ] **Comparative Audit:** Run tools against "dirty" code samples and document where they fail or succeed.
- [ ] **Gap Analysis:** Identify specific dead code patterns that current tools miss.
- [ ] **Upload Results:** Record findings in `/tools_benchmark/vulture_audit.md`.


## Phase 3: Engine Development (Months 4-5)
*Focus: Building the custom Static Analysis Backend.*

### Month 4: Rule Implementation
- [ ] **Custom AST Checkers:** Write scripts to detect code blocks following `return`, `break`, and `raise`.
- [ ] **Function Mapper:** Create a script to map all `def` statements and cross-reference them with `Call` nodes.

### Month 5: API & Integration
- [ ] **Backend Framework:** Set up a **FastAPI** server to orchestrate the scan process.
- [ ] **JSON Export:** Standardize scan results into a JSON format for frontend consumption.


## Phase 4: Frontend & Visualization (Month 6)
*Focus: Creating the "Comparison Dashboard" in React.*

- [ ] **Dashboard UI:** Build a web interface to upload Python files.
- [ ] **Code Highlighting:** Integrate `Prism.js` or `Monaco Editor` to highlight "dead zones" in red.
- [ ] **Comparison Matrix:** Display a side-by-side table comparing Custom Engine results vs. Vulture.


## Phase 5: Writing & Final Evaluation (Months 7-8)
*Focus: Completing the 60+ page thesis document.*

- [ ] **Thesis Writing:** Draft chapters on Theory, Methodology, Architecture, and Results.
- [ ] **Real-world Testing:** Run the platform against 5 large Open Source projects and record metrics.
- [ ] **Final Polish:** Prepare the presentation slides and perform a dry-run of the live demo.


## 🛠 Tech Stack Summary
* **Languages:** Python (Backend/Analysis), JavaScript/React (Frontend)
* **Core Libraries:** `ast`, `FastAPI`, `PyYAML`, `TailwindCSS`
* **Analysis Tools:** Vulture, Ruff, Bandit