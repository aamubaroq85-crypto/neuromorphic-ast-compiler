import numpy as np

class NengoSNNAdapter:
    """
    Adapter untuk mengekspor sinyal modulasi pi_eff ke format input Nengo / SNN.
    """
    def __init__(self, dt=0.001):
        self.dt = dt

    def convert_to_nengo_input(self, spike_sequence):
        """
        Mengonversi daftar spike train dari AST Compiler menjadi matriks sinyal
        yang siap dibaca oleh Nengo Node / Array.
        """
        formatted_nodes = []
        
        for step_idx, step_data in enumerate(spike_sequence):
            node_info = step_data['node']
            spikes = step_data['spikes']
            phase = step_data['phase']
            
            # Menghitung durasi sinyal berdasarkan panjang array spike
            duration_s = len(spikes) * self.dt
            firing_rate = np.mean(spikes) / self.dt  # Hz
            
            formatted_nodes.append({
                'step': step_idx + 1,
                'type': f"{node_info[0]}:{node_info[1]}",
                'phase_rad': float(phase),
                'duration_s': duration_s,
                'firing_rate_hz': firing_rate,
                'spike_pattern': spikes.tolist()
            })
            
        return formatted_nodes

# ==========================================
# CONTOH INTEGRASI
# ==========================================
if __name__ == "__main__":
    from test_parser import MathASTParser, NeuromorphicASTCompiler

    # 1. Parse & Compile
    parser = MathASTParser()
    compiler = NeuromorphicASTCompiler()
    
    nodes = parser.parse_expression("x * 2 + y")
    compiled_spikes = compiler.compile_ast_to_spikes(nodes, {'x': 3, 'y': 4})

    # 2. Konversi ke Format Adapter Nengo
    adapter = NengoSNNAdapter()
    nengo_config = adapter.convert_to_nengo_input(compiled_spikes)

    print("=== HASIL EKSPOR NENGO SNN ADAPTER ===")
    for item in nengo_config:
        print(f"Node {item['step']} [{item['type']:<10}] | Fasa: {item['phase_rad']:.3f} rad | Firing Rate: {item['firing_rate_hz']:.1f} Hz")
