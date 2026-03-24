# Introduction to Abstract Syntax Trees (AST)

### What is an AST?
An **Abstract Syntax Tree (AST)** is a hierarchical tree representation of the abstract syntactic structure of source code. Each node in the tree denotes a construct occurring in the source code, such as variable assignments, function definitions, or control flow statements (if/else, loops).

### Role in Static Analysis
Unlike concrete syntax trees, ASTs omit "punctuation" details like semicolons, braces, and parentheses, focusing purely on the **logic** and **structure** of the program. This makes ASTs the primary data structure used by static analysis tools to:
* **Identify Patterns:** Search for dangerous function calls or insecure coding patterns.
* **Analyze Scope:** Track where variables are defined and used.
* **Detect Dead Code:** Traversal of the tree allows us to find code blocks that are logically unreachable (e.g., code following a `return` statement).

### Python's `ast` Module
Python provides a built-in library, the `ast` module, which allows us to:
1. **Parse:** Convert source code into an AST object.
2. **Walk:** Traverse every node in the tree using `ast.walk()`.
3. **Inspect:** Examine the properties of each node (line number, variable names, etc.).

*Next Research Goal: Building a Control Flow Graph (CFG) from the AST nodes.*
