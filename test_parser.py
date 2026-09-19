import unittest
import ast
import math
import numpy as np

# ==========================================
# 1. CORE COMPILER & PARSER (Standalone)
# ==========================================
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

# ==========================================
# 2. UNIT TESTING
# ==========================================
class TestNeuromorphicASTCompiler(unittest.TestCase):

    def setUp(self):
        self.parser = MathASTParser()
        self.compiler = NeuromorphicASTCompiler()

    def test_complex_algebraic_expression(self):
        """Uji fungsi aljabar rumit: (x**2 + 3*x - 4) / (y + 1)"""
        expr = "(x**2 + 3*x - 4) / (y + 1)"
        variables = {'x': 4, 'y': 3}

        parsed_nodes = self.parser.parse_expression(expr)
        compiled_spikes = self.compiler.compile_ast_to_spikes(parsed_nodes, variables)

        self.assertTrue(len(parsed_nodes) > 0)
        self.assertTrue(len(compiled_spikes) == len(parsed_nodes))

        op_types = [node[1] for node in parsed_nodes if node[0] == 'BIN_OP']
        self.assertIn('Pow', op_types)
        self.assertIn('Div', op_types)

    def test_nested_parentheses(self):
        """Uji fungsi bersarang: ((a + b) * (c - d)) ** 2"""
        expr = "((a + b) * (c - d)) ** 2"
        variables = {'a': 2, 'b': 3, 'c': 10, 'd': 5}

        parsed_nodes = self.parser.parse_expression(expr)
        compiled_spikes = self.compiler.compile_ast_to_spikes(parsed_nodes, variables)

        for item in compiled_spikes:
            self.assertGreaterEqual(item['phase'], 0)
            self.assertLessEqual(item['phase'], 2 * math.pi)

    def test_spike_generation_validity(self):
        """Uji output spike train berupa array biner (0 atau 1)"""
        expr = "x * y + z"
        variables = {'x': 5, 'y': 2, 'z': 1}

        parsed_nodes = self.parser.parse_expression(expr)
        compiled_spikes = self.compiler.compile_ast_to_spikes(parsed_nodes, variables)

        for item in compiled_spikes:
            spikes = item['spikes']
            unique_values = set(spikes)
            self.assertTrue(unique_values.issubset({0, 1}))

if __name__ == '__main__':
    unittest.main()
