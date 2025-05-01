
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
from noise_models import build_combined_noise_model
from qiskit import transpile

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.save_statevector()

noise_model = build_combined_noise_model()
print("Noise Model Details:\n", noise_model)

sim = AerSimulator(noise_model=noise_model)
tqc = transpile(qc, sim)
result = sim.run(tqc).result()
state = result.get_statevector()
print("Noisy Statevector:\n", state)