from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_q = QuantumRegister(133, 'q')
creg_meas = ClassicalRegister(2, 'meas')
circuit = QuantumCircuit(qreg_q, creg_meas)

circuit.rz(pi / 2, qreg_q[0])
circuit.sx(qreg_q[0])
circuit.rz(pi / 2, qreg_q[0])
circuit.rz(pi / 2, qreg_q[1])
circuit.sx(qreg_q[1])
circuit.rz(pi / 2, qreg_q[1])
circuit.cz(qreg_q[0], qreg_q[1])
circuit.rz(pi / 2, qreg_q[1])
circuit.sx(qreg_q[1])
circuit.rz(pi / 2, qreg_q[1])
circuit.barrier(qreg_q[0], qreg_q[1])
circuit.measure(qreg_q[0], creg_meas[0])
circuit.measure(qreg_q[1], creg_meas[1])
