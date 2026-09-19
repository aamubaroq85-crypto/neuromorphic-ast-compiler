import ast
import math
import numpy as np

PI_EFF = math.pi * 1.05

class MathASTParser(ast.NodeVisitor):
    def __init__(self):
        self.operations = []

    def visit_BinOp(self, node):
        self.visit(node.left)
        self.visit(node.right)
        op_type = type(node.op).__name__
        self.operations.append(('BIN_OP', op_type))

    def visit_Constant(self, node):
        self.operations.append(('CONST', node.value))

    def visit_Name(self, node):
        self.operations.append(('VAR', node.id))

    def parse_expression(self, expr_str):
        self.operations = []
        tree = ast.parse(expr_str, mode='eval')
        self.visit(tree)
        return self.operations

class NeuromorphicASTCompiler:
    def __init__(self, pi_eff=PI_EFF):
        self.pi_eff = pi_eff
        self.op_weights = {
            'Add': 1.0,
            'Sub': 1.5,
            'Mult': 2.0,
            'Div': 2.5,
            'Pow': 3.0
        }

    def compile_ast_to_spikes(self, parsed_ops, var_values=None):
        if var_values is None:
            var_values = {}

        spike_sequence = []
        
        for op_type, val in parsed_ops:
            if op_type == 'CONST':
                base_val = float(val)
            elif op_type == 'VAR':
                base_val = float(var_values.get(val, 1.0))
            elif op_type == 'BIN_OP':
                base_val = self.op_weights.get(val, 1.0)
            else:
                base_val = 1.0

            phase = (base_val * self.pi_eff) % (2 * np.pi)
            time_steps = np.linspace(0, 10, 50)
            wave = np.sin(2 * np.pi * 0.5 * time_steps + phase)
            spikes = (wave > 0.8).astype(int)
            
            spike_sequence.append({
                'node': (op_type, val),
                'phase': phase,
                'spikes': spikes
            })
            
        return spike_sequence

if __name__ == "__main__":
    math_expr = "(x + 5) * (y - 2)"
    variables = {'x': 10, 'y': 8}

    print(f"Input Ekspresi: {math_expr}")
    
    parser = MathASTParser()
    parsed_nodes = parser.parse_expression(math_expr)

    compiler = NeuromorphicASTCompiler()
    compiled_spikes = compiler.compile_ast_to_spikes(parsed_nodes, variables)

    print("\n--- Hasil Kompilasi AST ke Spike Train ---")
    for idx, item in enumerate(compiled_spikes):
        op_name = f"{item['node'][0]}:{item['node'][1]}"
        total_spikes = np.sum(item['spikes'])
        print(f"Step {idx+1} [{op_name:<12}] -> Fasa: {item['phase']:.4f} rad | Total Spike: {total_spikes}")
