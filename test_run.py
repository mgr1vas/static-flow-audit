import ast

source_code = """
x = 10
y = 20
print(x + y)
"""

tree = ast.parse(source_code)

print("--- Analyzing Variables ---")
for node in ast.walk(tree):
    if isinstance(node, ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name):
                print(f"Found variable assignment: {target.id}")
