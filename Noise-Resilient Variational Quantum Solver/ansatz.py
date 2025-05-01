from qiskit import QuantumCircuit

def create_ansatz(params, num_qubits=2, reps=1):
    qc = QuantumCircuit(num_qubits)
    param_index = 0
    for _ in range(reps):
        for qubit in range(num_qubits):
            qc.ry(params[param_index], qubit)
            param_index += 1
        for qubit in range(num_qubits - 1):
            qc.cx(qubit, qubit + 1)
    return qc

if __name__ == "__main__":
    params = [0.1, 0.2]  
    qc = create_ansatz(params, num_qubits=2, reps=1)
    qc.draw('mpl')
