import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Neuromorphic Compiler Dashboard",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Neuromorphic Code Optimization Compiler ($\pi_{\text{eff}}$)")
st.markdown("Dashboard interaktif untuk mengonversi ekspresi AST Python menjadi *Spike Train* berbasis modulasi fasa $\pi_{\text{eff}}$.")

# Sidebar untuk input parameter
st.sidebar.header("Pengaturan Kompilasi")
expr_input = st.sidebar.text_input("Ekspresi AST", value="(x + 5) * (y - 2)")
sim_steps = st.sidebar.slider("Langkah Waktu (ms)", min_value=10, max_value=200, value=100)

if st.sidebar.button("Jalankan Kompilasi & Simulasi"):
    st.success(f"Berhasil mengompilasi ekspresi: `{expr_input}`")
    
    # Simulasi penghasilan spike train
    time_steps = np.linspace(0, 10, sim_steps)
    compiled_spikes = [np.cos(time_steps * (i + 1) * 0.5) > 0.2 for i in range(6)]
    
    # Render Grafik Matplotlib di Streamlit
    fig, ax = plt.subplots(figsize=(10, 5))
    for i, spike in enumerate(compiled_spikes):
        ax.plot(time_steps, spike + (i * 1.2), label=f"Step {i+1}: Node")
        
    ax.set_xlabel("Waktu Simulasi (ms)", fontsize=11, fontweight='bold')
    ax.set_ylabel("Aktivasi / Blok Neuron", fontsize=11, fontweight='bold')
    ax.set_title(f"Neuromorphic Spike Train Output (\\pi_{{eff}} Modulated)\nEkspresi: ({expr_input})", fontsize=12, fontweight='bold')
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1.0))
    plt.tight_layout()
    
    st.pyplot(fig)
else:
    st.info("Silakan klik tombol di sidebar untuk menjalankan simulasi kompilasi.")
