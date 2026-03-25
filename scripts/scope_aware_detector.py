import ast
code_test = """
x = 10          # Global x (Defined but never used)
def funcLocal():
    x = 5       # Local x (Defined and used)
    return x
y = 20          # Global y (Used)
print(y)
"""

class ScopeAwareAnalyzer(ast.NodeVisitor):
    def __init__(self):
        # A list of dictionaries. The last one is the current scope.
        self.scopes = [{}] # We start with the Global Scope
    def visit_FunctionDef(self, node):
        print(f"Entering Scope: {node.name}")
        self.scopes.append({}) # Push new scope
        self.generic_visit(node)
        # Before exiting the function, check for unused variables in this scope
        current_scope = self.scopes.pop() # Pop scope
        self.report_unused(current_scope, scope_name=node.name)
    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                var_name = target.id
                # Record the definition in the current (last) scope
                self.scopes[-1][var_name] = {'line': node.lineno, 'used': False}
        self.generic_visit(node)
    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            var_name = node.id
            # Search from the current scope towards the outside (LEGB rule)
            for scope in reversed(self.scopes):
                if var_name in scope:
                    scope[var_name]['used'] = True
                    break
        self.generic_visit(node)
    def report_unused(self, scope, scope_name="Global"):
        for var, info in scope.items():
            if not info['used']:
                print(f"UNUSED in {scope_name}: Variable '{var}' at line {info['line']}")

# Execution
tree = ast.parse(code_test)
analyzer = ScopeAwareAnalyzer()
analyzer.visit(tree)
# At the end, check the Global scope
analyzer.report_unused(analyzer.scopes[0])
