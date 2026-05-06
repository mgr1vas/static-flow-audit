import ast

code_to_test = """ # Sample code to be analyzed by the script
def used_function():
    print("I am being called!")

def unused_function():
    print("No one ever calls me...")

def another_unused_one(x):
    return x + 1

# Main execution
used_function()
"""

# Create a class to traverse the Abstract Syntax Tree
class FunctionAudit(ast.NodeVisitor):
    def __init__(self):
        self.defined_functions = {} # {name: lineno}
        self.called_functions = set()

    def visit_FunctionDef(self, node):
        # Write down the name and line number of the function definition
        self.defined_functions[node.name] = node.lineno
        self.generic_visit(node)

    def visit_Call(self, node):
        # Write down the name of the function being called
        #Check if the function being called is a simple name (not an attribute or lambda)
        if isinstance(node.func, ast.Name):
            self.called_functions.add(node.func.id)
        self.generic_visit(node)

    def report(self):
        print ("\nFunction Usage Audit Report")
        found_dead = False
        
        for func_name in self.defined_functions:
            if func_name not in self.called_functions:
                line = self.defined_functions[func_name]
                print (f"DEAD CODE: Function '{func_name}' defined at line {line} is never called!")
                found_dead = True
        
        if not found_dead:
            print (" All functions are reachable and called.")

# Step 1: Parse the source code into an AST objecttree
tree = ast.parse(code_to_test)
# Step 2: Initialize the custom auditor and visit the tree
auditor = FunctionAudit()
# Step 3: Generate the report
auditor.visit(tree)
# Step 4: Print the report
auditor.report()
