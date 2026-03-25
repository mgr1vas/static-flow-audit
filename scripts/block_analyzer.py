import ast
code_to_test = """
def complex_logic(x):
    print("Step 1")
    if x > 10:
        return "Greater than 10"
        print("Dead inside IF") # DEAD
    
    print("Step 2 - Alive") 
    return "Done"
    print("Dead Body from now on") # DEAD
"""

class BlockAnalyzer(ast.NodeVisitor):
    def visit_FunctionDef(self, node):
        print(f"\n Checking Blocks in function: {node.name}")
        self.check_body_for_dead_code(node.body)
        # Continue visiting the rest of the function body
        self.generic_visit(node)
    def visit_If(self, node):
        # Check the body of the 'if' statement
        self.check_body_for_dead_code(node.body)
        # Check the body of the 'else' statement (if it exists)
        if node.orelse:
            self.check_body_for_dead_code(node.orelse)
        self.generic_visit(node)
    def check_body_for_dead_code(self, body_list):
        terminator_found = False
        for statement in body_list:
            if terminator_found:
                print(f"DEAD CODE ALERT: Statement '{type(statement).__name__}' at line {statement.lineno} is unreachable!")
            # If the statement is Return, Break, or Raise, the block "closes"
            if isinstance(statement, (ast.Return, ast.Break, ast.Raise)):
                print(f"Block termination found at line {statement.lineno} ({type(statement).__name__})")
                terminator_found = True

# Execution
tree = ast.parse(code_to_test)
analyzer = BlockAnalyzer()
analyzer.visit(tree)
