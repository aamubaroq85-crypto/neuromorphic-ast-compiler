import numpy as np
import matplotlib.pyplot as plt
from test_parser import MathASTParser, NeuromorphicASTCompiler

def generate_spike_plot(expr_str, variables, output_file="spike_plot.png"):
    # 1. Parse & Compile
    parser = MathASTParser()
    compiler = NeuromorphicASTCompiler()
    
    parsed_nodes = parser.parse_expression(expr_str)
    compiled_spikes = compiler.compile_ast_to_spikes(parsed_nodes, variables)

    # 2. Visualisasi Spike Train
    fig, ax = plt.subplots(figsize=(10, 5))
    
    time_steps = np.linspace(0, 10, 50)
    for idx, item in enumerate(compiled_spikes):
        op_label = f"{item['node'][0]}:{item['node'][1]}"
        # Shift bertingkat di sumbu Y agar antar-node terpisah jelas
        ax.plot(time_steps, item['spikes'] + idx * 1.5, drawstyle='steps-post', label=f"Step {idx+1}: {op_label}")

    ax.set_title(f"Neuromorphic Spike Train Output (pi_eff Modulated)\nExpression: '{expr_str}'")
    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("Execution Steps / Neurons")
    ax.set_yticks([idx * 1.5 for idx in range(len(compiled_spikes))])
    ax.set_yticklabels([f"Node {idx+1}" for idx in range(len(compiled_spikes))])
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend(loc='upper right')

    plt.tight_layout()
    plt.savefig(output_file)
    print(f"Grafik spike berhasil disimpan sebagai '{output_file}'")
    plt.close()

if __name__ == "__main__":
    generate_spike_plot("(x + 5) * (y - 2)", {'x': 10, 'y': 8})
