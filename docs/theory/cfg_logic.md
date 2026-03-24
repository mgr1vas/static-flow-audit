# Control Flow Analysis (CFA) & Graphs

### Introduction to CFG
A Control Flow Grapsh is a directed graph that represents all paths that might be traversed through a program during its execution. In a CFG, each node represents a **Basic Block**.

### Basic Blocks
A Basic Block is a maximal sequence of instructions where:
- Control enters only at the first instruction.
- Control leaves at the last instruction.
- There are no jumps or branches into or out of the middle of the sequence.

### Reachability Analysis
In the contect of Static-Flow-Audit, we use reachability analysis to indentify dead code.
- **Reachable Node**: A node `v` is reachable if there exists a path from the start node `s` to `v`.
- **Unreachable Node**: If no such path exists, the code contained within that block is "Dead Code"/

### Visualizing Flow with If Statements
When an If Condition is encountered:
1. The current block ends.
2. Two new edges are created:
   - One leading to the 'Then' block.
   - One leading tho the 'Else' block (or the next instruction if no else exists).
3. Both blocks eventually converge back to a "join Node".

**Crucial Logic:** If a block ends with a `return`, the edge to the "Join Node" is severed, potentially making all subsequent nodes in the parent block unreachable.
