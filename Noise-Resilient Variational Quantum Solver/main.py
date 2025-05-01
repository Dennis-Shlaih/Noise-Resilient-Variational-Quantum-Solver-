import matplotlib.pyplot as plt
from ansatz import create_ansatz
from cost_function import compute_expectation
from optimizer import optimize_vqa
from noise_models import build_combined_noise_model
from qiskit import transpile
from qiskit.quantum_info import Pauli, DensityMatrix
from qiskit_aer import AerSimulator
NUM_QUBITS = 2
DEPTH = 1
INITIAL_PARAMS = [0.1] * (NUM_QUBITS * DEPTH) 
print("\nRunning Ideal Simulation")
ideal_cost_fn = lambda p: -compute_expectation(p, create_ansatz)
ideal_result, ideal_history = optimize_vqa(ideal_cost_fn, INITIAL_PARAMS)
print("\n Running Noisy Simulation")
noise_model = build_combined_noise_model()
print(noise_model)
def compute_noisy_expectation(params):
    qc = create_ansatz(params, num_qubits=NUM_QUBITS)
    qc.save_density_matrix()
    sim = AerSimulator(method='density_matrix', noise_model=noise_model) 
    tqc = transpile(qc, sim)
    result = sim.run(tqc).result()
    final_dm = result.data(0)['density_matrix']
    dm = DensityMatrix(final_dm)
    return dm.expectation_value(Pauli('ZZ')).real * -1
noisy_result, noisy_history = optimize_vqa(compute_noisy_expectation, INITIAL_PARAMS)
plt.figure(figsize=(8, 5))
plt.plot(ideal_history, label='Ideal Simulation')
plt.plot(noisy_history, label='Noisy Simulation', linestyle='--')
plt.xlabel("Iteration")
plt.ylabel("Cost (Negative Energy)")
plt.title("Cost Function Convergence (Ideal vs Noisy)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
print("\n Final Results")
print("Ideal Params:", ideal_result.x)
print("Ideal Final Cost:", ideal_result.fun)
print("\nNoisy Params:", noisy_result.x)
print("Noisy Final Cost:", noisy_result.fun)
