# AST Mastery Cheat Sheet

## Essential Node Types for Dead Code Detection
- `ast.Return`: The primary "terminator" of a block.
- `ast.Raise`: Also terminates execution in its current block.
- `ast.Break` / `ast.Continue`: Terminators for loop iterations.
- `ast.If.body` vs `ast.If.orelse`: Exploring paths that might be unreachable.

## Traversal Strategies
1. **Shallow Search:** Using `ast.walk` to find all function definitions.
2. **Deep Semantic Analysis:** Overriding `ast.NodeVisitor` to track state and scope.

## How to identify Unreachable Nodes (Algorithm Idea)
1. Traverse a block of statements (list of nodes).
2. Flag a `terminator_found` boolean when a `Return` or `Raise` is encountered.
3. Any subsequent nodes in the same list while `terminator_found == True` are flagged as **Unreachable**.
