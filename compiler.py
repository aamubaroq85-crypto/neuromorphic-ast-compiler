import numpy as np
from visualizer import plot_spike_train

class NeuromorphicCompiler:
    def __init__(self, expression):
        self.expression = expression

    def compile_to_spike(self):
        print(f"[COMPILER] Mengompilasi ekspresi AST: {self.expression}")
        time_steps = np.linspace(0, 10, 100)
        compiled_spikes = [np.cos(time_steps * (i + 1) * 0.5) > 0.2 for i in range(6)]
        plot_spike_train(compiled_spikes, time_steps, self.expression)
        return compiled_spikes

if __name__ == "__main__":
    compiler = NeuromorphicCompiler("(x + 5) * (y - 2)")
    compiler.compile_to_spike()
