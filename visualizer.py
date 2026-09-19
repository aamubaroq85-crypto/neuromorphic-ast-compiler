import matplotlib.pyplot as plt
import numpy as np

def plot_spike_train(spike_data, time_steps, expression_str="x + 5"):
    """
    Membuat visualisasi Spike Train dengan keterangan parameter dan pelabelan sumbu yang detail.
    """
    plt.figure(figsize=(10, 6))
    
    # Plotting spike trains untuk setiap neuron/layer
    for i, spike in enumerate(spike_data):
        plt.plot(time_steps, spike + (i * 1.2), label=f"Step {i+1}: Node")
        
    plt.xlabel("Waktu Simulasi (ms)", fontsize=11, fontweight='bold')
    plt.ylabel("Aktivasi / Blok Neuron", fontsize=11, fontweight='bold')
    plt.title(f"Neuromorphic Spike Train Output (\\pi_{{eff}} Modulated)\nEkspresi AST: ({expression_str})", fontsize=12, fontweight='bold')
    
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1.0))
    plt.tight_layout()
    
    # Simpan otomatis sebagai file gambar
    plt.savefig("spike_plot.png", dpi=300)
    plt.close()
    print("[INFO] Grafik spike_plot.png berhasil diperbarui secara otomatis dengan parameter lengkap.")

if __name__ == "__main__":
    # Contoh data dummy untuk pengujian mandiri visualizer
    t = np.linspace(0, 10, 100)
    dummy_spikes = [np.sin(t + i) > 0.5 for i in range(5)]
    plot_spike_train(dummy_spikes, t, "x + 5")
