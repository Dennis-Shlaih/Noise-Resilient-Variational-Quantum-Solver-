# Noise-Resilient-Variational-Quantum-Solver
A minimal implementation of a **Variational Quantum Algorithm** (VQA) using Qiskit, designed to study and demonstrate the **impact of noise on quantum optimization**. This project builds a simple ansatz circuit, simulates expectation values of a Pauli Hamiltonian, and compares convergence with and without noise.
--
## Project Objectives
- Build a parameterized quantum circuit (ansatz) using RY rotations and entanglement.
- Optimize the circuit parameters to minimize a quantum cost function.
- Introduce realistic quantum noise (decoherence, depolarization, readout error).
- Compare convergence behavior between ideal and noisy simulators.
- Understand the limitations of variational methods in the NISQ era.

---

## Installation

```bash
git clone https://github.com/Dennis-Shlaih/Noise-Resilient-Variational-Quantum-Solver-.git
cd Noise-Resilient-Variational-Quantum-Solver
pip install -r requirements.txt
Requirements include:
- `qiskit`
- `matplotlib`
- `numpy`
- `scipy`
```
---
## Usage

Run the full experiment using:

```bash
python main.py
```
