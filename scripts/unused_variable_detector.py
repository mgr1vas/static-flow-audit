import ast
code_test = """
def process_data(a):
    b = a + 1       # 'b' is used later
    c = 10          # 'c' is NEVER used -> DEAD STORE
    print(b)
    d = 20          # 'd' is defined but not used
    return a
"""

class UnusedVariableFinder(ast.NodeVisitor):
    def __init__(self):
        # Our "Symbol Table"
        # { 'variable_name': {'line': 5, 'used': False} }
        self.symbols = {}
    def visit_Assign(self, node):
        # Record the definition of a variable (Definition)
        for target in node.targets:
            if isinstance(target, ast.Name):
                var_name = target.id
                self.symbols[var_name] = {
                    'line': node.lineno,
                    'used': False
                }
        self.generic_visit(node)
    def visit_Name(self, node):
        # Check if the variable is being read (used) or written (defined)
        # The ast.Load context means the variable is being read
        if isinstance(node.ctx, ast.Load):
            if node.id in self.symbols:
                self.symbols[node.id]['used'] = True
        self.generic_visit(node)
    def report(self):
        print("\nVariable Usage Report:")
        for var, info in self.symbols.items():
            status = "USED" if info['used'] else "UNUSED (DEAD STORE)"
            print(f"Variable '{var}' at line {info['line']}: {status}")

# Execution
tree = ast.parse(code_test)
finder = UnusedVariableFinder()
finder.visit(tree)
finder.report()
