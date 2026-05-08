# System Architecture
The tool follows a three-step process:
1. **Parsing:** Converting source code into an AST using Python's `ast` module.
2. **Analysis:** Traversing the tree to build Symbol Tables and Control Flow Graphs.
3. **Reporting:** Comparing definitions with usages to flag unreachable or unused code.
