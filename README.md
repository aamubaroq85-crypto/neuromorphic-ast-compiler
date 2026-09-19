# Neuromorphic Code Optimization Compiler ($\pi_{\text{eff}}$)

Kompiler eksperimental untuk mengonversi kode program tingkat tinggi (Python AST) menjadi *Spike Train* berbasis modulasi fasa $\pi_{\text{eff}}$ untuk arsitektur *Neuromorphic Computing* (Spiking Neural Network).

## Fitur Utama
- **AST Parsing**: Menerjemahkan ekspresi matematika langsung menjadi rantai instruksi.
- **$\pi_{\text{eff}}$ Phase Modulation**: Mengodekan fasa gelombang sinyal untuk efisiensi energi dan eliminasi spike redundan.
- **Zero-Middleware Target**: Menghasilkan sinyal yang dapat dipetakan langsung ke unit neuron buatan.

## Cara Menjalankan

1. **Jalankan Kompiler Utama:**
   <code>python compiler.py</code>

2. **Jalankan Pengujian & Simulasi Nengo SNN:**
   <code>python test_parser.py && python nengo_adapter.py</code>

## Visualisasi Output Spike Train

<img src="[https://raw.githubusercontent.com/aamubaroq85-crypto/neuromorphic-ast-compiler/main/spike_plot.png](https://raw.githubusercontent.com/aamubaroq85-crypto/neuromorphic-ast-compiler/main/spike_plot.png)" alt="Spike Train Output" width="100%" />
