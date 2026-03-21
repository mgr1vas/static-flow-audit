# Understanding ast.NodeVisitor

### What is the NodeVisitor?
The `ast.NodeVisitor` is a class provided by Python's standard library that implements the **Visitor Design Pattern**. Its primary purpose is to provide a structured way to traverse an **Abstract Syntax Tree (AST)** and execute specific logic for different types of nodes.

### Core Principles

#### 1. Automatic Dispatching
Instead of using manual `if-else` or `isinstance()` checks for every node in a tree, `NodeVisitor` uses a **dispatcher**. When the visitor encounters a node (e.g., a `Return` node), it automatically looks for a method named `visit_Return`.

#### 2. Depth-First Traversal
The visitor starts at the root of the tree and moves downwards through the branches. This is crucial for **Static Analysis** because it preserves the hierarchical context (e.g., knowing that a certain block of code belongs to a specific function).

### Why we use it for Dead Code Detection

For our research on **Static-Flow-Audit**, the `NodeVisitor` is superior to a simple flat search because:

1. **State Persistence:** We can maintain an internal "state" (e.g., `self.terminator_found = True`) as we walk through a function's body.
2. **Block Scope:** We can reset the analysis state every time we enter a new function (`visit_FunctionDef`), ensuring that a `return` in one function doesn't flag code in another function as "dead".
3. **Execution Flow Simulation:** By visiting nodes in order, we can simulate the "path" a program takes and identify where that path is prematurely cut off.
