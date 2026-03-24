# What is a Compiler?
A compiler is a software that translates a program written in high level language (eg. Python, C) into a low level language (eg. Machine Code, Bytecode, Assembly). The primary goal is to create an executable program that the computer's CPU can understand, while ensuring the original logic of the code remains intact.

### Lexical Analysis / Scanning
- The compiler needs the source code as a stream of characters and groups them into meaningful sequences called **Tokens**.
  - Example: `x = 5 + 2` becomes into `[ID(x), ASSIGN, NUM(5), PLUS, NUM(2)]`.

### Syntax Analysis / Parsing
- The compiler checks if the tokens follow the grammatical rules of the language. This phase produces the **Abstract Syntax Tree (AST)**.
  - Relevance to this Thesis: This is our primary data structure. We use the AST to represent the program's structure without necessary syntax details (like semicolons or parenthesis).

### Semantic Analysis
- The compiler checks for logical errors that syntax rules cannot catch such as **Type Checking** (eg. ensuring that someone does not add a string to an integer) and **Scope Resolution**.

### Intermediate Code Generation (IR)
- The compiler translates the AST into an Intermediate Representation. This is a language independent version of the code that makes optimization easier.

### Code Optimization
- This is the core of our project. The compiler analyzes the IR to make the program more efficient.
  - **Dead Code Elimination** (DCE): Identifying and removing instructions that do not affect the program's results (unreachable/unused code).
  - **Constant Folding**: Evaluating expressions with constant values at compile-time (eg. chancing 3+4 to 7).
 
### Code Generation
The final phase where the IR is translated into the target machine language or bytecode.
