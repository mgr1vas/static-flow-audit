import ast

# The source code we want to analyze
code = "x = 10\ny = 20\nprint(x + y)"

# Step 1: Parse the string into an Abstract Syntax Tree (AST)
tree = ast.parse(code)

# Step 2: Initialize an empty dictionary to act as our Symbol Table
symbol_table = {}

# Step 3: Iterate through every node in the tree using ast.walk
for node in ast.walk(tree):
    # We only care about assignment statements (e.g., x = 10)
    if isinstance(node, ast.Assign):
        # An assignment can have multiple targets (e.g., a = b = 1)
        for target in node.targets:
            # Check if the target is a simple variable name
            if isinstance(target, ast.Name):
                # Store the variable name and its definition line number
                symbol_table[target.id] = node.lineno

# Step 4: Display the collected symbols
print ("Simple Symbol Table")
for name, line in symbol_table.items():
    print ("Variable:", name, "| Defined on Line:", line)