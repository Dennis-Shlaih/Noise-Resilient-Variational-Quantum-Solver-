from qiskit_aer import Aer
from qiskit.quantum_info import Pauli, Statevector
from ansatz import create_ansatz

def compute_expectation(params, ansatz_fn, num_qubits=2):
    qc = ansatz_fn(params, num_qubits=num_qubits)
    
    backend = Aer.get_backend('statevector_simulator')
    state = Statevector.from_instruction(qc)
    
    zz_op = Pauli('ZZ')
    expectation = state.expectation_value(zz_op).real
    return expectation

if __name__ == "__main__":
    params = [0.1, 0.2]
    exp_val = compute_expectation(params, create_ansatz)
    print(f"Expectation Value: {exp_val:.4f}")
