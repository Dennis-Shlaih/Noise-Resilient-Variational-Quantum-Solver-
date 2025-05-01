from qiskit_aer.noise import NoiseModel, depolarizing_error, thermal_relaxation_error, ReadoutError

def add_readout_error(noise_model, p0=0.10, p1=0.10):
    error = ReadoutError([[1 - p0, p0], [p1, 1 - p1]])
    noise_model.add_all_qubit_readout_error(error)

def build_combined_noise_model():
    noise_model = NoiseModel(basis_gates=['cx', 'id', 'rz', 'sx', 'ry'])
    t1, t2 = 50, 30 
    gate_time_1q = 100 / 1000 
    gate_time_2q = 300 / 1000
    one_qubit_gates = ['ry', 'rz', 'sx']
    two_qubit_gates = ['cx']
    for gate in one_qubit_gates:
        dep_error = depolarizing_error(0.15, 1)
        thermal_error = thermal_relaxation_error(t1, t2, gate_time_1q)
        combined_error = dep_error.compose(thermal_error)
        noise_model.add_all_qubit_quantum_error(combined_error, [gate])
    dep_2q = depolarizing_error(0.25, 2)
    thermal_2q = thermal_relaxation_error(t1, t2, gate_time_2q).expand(
        thermal_relaxation_error(t1, t2, gate_time_2q)
    )
    combined_2q = dep_2q.compose(thermal_2q)
    noise_model.add_all_qubit_quantum_error(combined_2q, ['cx'])

    readout = ReadoutError([[0.9, 0.1], [0.1, 0.9]])
    noise_model.add_all_qubit_readout_error(readout)

    return noise_model
