#!/usr/bin/env python
import numpy as np

zero = np.zeros([2, 2])

# Pauli
sigma_1 = np.array([[0, 1], [1, 0]])
sigma_2 = np.array([[0, -1j], [1j, 0]])
sigma_3 = np.array([[1, 0], [0, -1]])

# Dirac
gamma_0 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]], dtype=np.complex128)
gamma_1 = np.concatenate([np.concatenate([zero, -sigma_1]), np.concatenate([sigma_1, zero])], axis=1)
gamma_2 = np.concatenate([np.concatenate([zero, -sigma_2]), np.concatenate([sigma_2, zero])], axis=1)
gamma_3 = np.concatenate([np.concatenate([zero, -sigma_3]), np.concatenate([sigma_3, zero])], axis=1)
gammas = [gamma_0, gamma_1, gamma_2, gamma_3]

zero4 = np.zeros([4, 4], dtype=np.complex128)

metric = np.array([
[1, 0, 0, 0],
[0, -1, 0, 0],
[0, 0, -1, 0],
[0, 0, 0, -1]
], dtype=np.complex128)

J_v_01 = np.array([
[0, 1j, 0, 0],
[1j, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0]
])

J_v_02 = np.array([
[0, 0, 1j, 0],
[0, 0, 0, 0],
[1j, 0, 0, 0],
[0, 0, 0, 0]
])

J_v_03 = np.array([
[0, 0, 0, 1j],
[0, 0, 0, 0],
[0, 0, 0, 0],
[1j, 0, 0, 0]
])

J_v_12 = np.array([
[0, 0, 0, 0],
[0, 0, -1j, 0],
[0, 1j, 0, 0],
[0, 0, 0, 0]
])

J_v_23 = np.array([
[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, -1j],
[0, 0, 1j, 0]
])

J_v_31 = np.array([
[0, 0, 0, 0],
[0, 0, 0, 1j],
[0, 0, 0, 0],
[0, -1j, 0, 0]
])

# J_v anticommute
J_v = [
[zero4, J_v_01, J_v_02, J_v_03],
[-J_v_01, zero4, J_v_12, -J_v_31],
[-J_v_02, -J_v_12, zero4, J_v_23],
[-J_v_03, J_v_31, -J_v_23, zero4]
]

# m: mu, n: nu, r: rho, l: lambda
check = 0
for m in range(4):
    for n in range(4):
        for r in range(4):
            for l in range(4):
                LHS = J_v[m][n] @ J_v[r][l] - J_v[r][l] @ J_v[m][n]
                RHS = metric[m][r] * J_v[n][l] - metric[n][r] * J_v[m][l] + metric[m][l] * J_v[r][n] - metric[n][l] * J_v[r][m]
                RHS = -1j * RHS
                bool = LHS == RHS
                if bool.all() == False:
                    check += 1

if check == 0:
    print("eq(5.48) is true for V!")
else:
    print("eq(5.48) is false for V!")

# J_s anticommute
J_s = [
[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0]
]
for m in range(4):
    for n in range(4):
        J_s[m][n] = 1j * (gammas[m] @ gammas[n] - gammas[n] @ gammas[m])

# m: mu, n: nu, r: rho, l: lambda
check = 0
for m in range(4):
    for n in range(4):
        for r in range(4):
            for l in range(4):
                LHS = J_s[m][n] @ J_s[r][l] - J_s[r][l] @ J_s[m][n]
                RHS = metric[m][r] * J_s[n][l] - metric[n][r] * J_s[m][l] + metric[m][l] * J_s[r][n] - metric[n][l] * J_s[r][m]
                RHS = -1j * RHS
                bool = LHS == RHS
                if bool.all() == False:
                    check += 1

if check == 0:
    print("eq(5.48) is true for S!")
else:
    print("eq(5.48) is false for S!")
