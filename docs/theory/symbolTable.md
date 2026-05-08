# Symbol Table Management


### Overview
The **Symbol Table** is a crucial data structure used by compilers to store information about the identifiers occurring in the source code. In the context of static analysis, it acts as a tracking mechanism for variable lifecycles.

### Key Roles in Static-Flow-Audit
1. **Identifier Tracking:** Storing the name, type, and scope of every variable and function discovered during AST traversal.
2. **Def-Use Chain Analysis:** By maintaining a `used` flag for each entry, the analyzer can determine if a "Definition" (assignment) is followed by a "Use" (reference). If no reference exists before the scope closes, it is flagged as a **Dead Store**.
3. **Scope Resolution:** Handling nested environments. Our analyzer uses a **Stack-based Symbol Table** approach to manage local and global scopes independently, ensuring that variables with the same name in different functions are not confused.

### Data Structure Implementation
In Python-based analysis, the Symbol Table is typically implemented as a **Dictionary** where:
* **Key:** The name of the identifier (string).
* **Value:** An object or dictionary containing metadata (line number, scope depth, usage status).

### Impact on Optimization
By identifying entries in the Symbol Table that are never marked as "used," the compiler can safely perform **Dead Code Elimination**, reducing the memory footprint of the final program.
