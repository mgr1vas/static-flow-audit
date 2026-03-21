import ast

code = """
def calculate(x):
    if x > 10:
        return x * 2
        print("I am dead code")
    return x
"""

class DeadCodeFinder(ast.NodeVisitor):
    # This method is called for each function definition found
    def visit_FunctionDef(self, node):
        print(f"🔍 Analyzing function: {node.name}")
        # Continues visiting the body of the function
        self.generic_visit(node)

    # This method is called for each return statement found
    def visit_Return(self, node):
        print(f"✅ Found a 'return' statement at line {node.lineno}")

# 1. Convert code to an Abstract Syntax Tree
tree = ast.parse(code)

# 2. Create an instance of our custom visitor
finder = DeadCodeFinder()

# 3. Start visiting the nodes
finder.visit(tree)