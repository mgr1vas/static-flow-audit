# Advanced AST Mastery Cheat Sheet

Mastering the Abstract Syntax Tree (AST) involves moving from simple structural parsing to **Semantic Analysis** and **Data Flow Tracking**.


### 1. Essential Node Types for Flow Audit

#### Execution Terminators
These nodes signal the end of a "Basic Block". Anything following them in the same scope is **Unreachable Code**.
* `ast.Return`: Exits the current function.
* `ast.Raise`: Terminates the block by throwing an exception.
* `ast.Break` / `ast.Continue`: Interrupt the linear flow of loops.

#### Scope & Logic Containers
* `ast.FunctionDef`: Defines a local scope. Essential for resetting "Dead Zone" flags.
* `ast.If.body` vs `ast.If.orelse`: Distinct execution paths. A `return` in one does not necessarily kill the other.
* `ast.Module`: The root node representing the entire file.

#### Data Flow Nodes (Def-Use)
* `ast.Name(ctx=ast.Store())`: Represents a **Definition (Def)**. A value is being assigned to a variable.
* `ast.Name(ctx=ast.Load())`: Represents a **Use**. A variable's value is being accessed.

### 2. Advanced Traversal Strategies

| Strategy | Method | Best Used For... |
| :--- | :--- | :--- |
| **Flat Search** | `ast.walk()` | Quick, order-independent searches (e.g., "Does this file use `eval`?"). |
| **Hierarchical Visitor** | `ast.NodeVisitor` | Pattern matching and stateful analysis (e.g., "Am I currently inside a loop?"). |
| **Structural Transformer** | `ast.NodeTransformer` | Modifying the tree (e.g., automatically removing identified Dead Code). |


### 3. Reachability Algorithm (The "State Machine" Logic)

To detect **Unreachable Code**, we implement a state-aware visitor:
1. **Enter Block:** Initialize `terminator_found = False`.
2. **Iterate Nodes:** For each statement in `node.body`:
   - If `terminator_found == True` ⮕ Flag current node as **Unreachable**.
   - If node is `ast.Return` or `ast.Raise` ⮕ Set `terminator_found = True`.
3. **Handle Branching:** If node is `ast.If`, recursively check `body` and `orelse` independently.


### 4. Data Flow Analysis (The "Symbol Table" Logic)

To detect **Dead Stores (Unused Variables)**:
1. **Map Definitions:** Store every `ast.Store` occurrence in a Dictionary (Symbol Table) with its line number.
2. **Track Usages:** Every time an `ast.Load` is encountered, mark that variable as "Used" in the Symbol Table.
3. **Audit:** At the end of the scope (`visit_FunctionDef` exit), any variable remaining "Unused" is flagged as a **Dead Store**.

### Pro-Tip for the Thesis
When explaining AST Mastery, always distinguish between **Control Flow** (how the program jumps) and **Data Flow** (how variables travel). Dead code detection requires both.
