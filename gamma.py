#!/usr/bin/env python
import numpy as np

zero = np.zeros([2, 2])

sigma_1 = np.array([[0, 1], [1, 0]])
sigma_2 = np.array([[0, -1j], [1j, 0]])
sigma_3 = np.array([[1, 0], [0, -1]])

gamma_0 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]], dtype=np.complex128)
gamma_1 = np.concatenate([np.concatenate([zero, -sigma_1]), np.concatenate([sigma_1, zero])], axis=1)
gamma_2 = np.concatenate([np.concatenate([zero, -sigma_2]), np.concatenate([sigma_2, zero])], axis=1)
gamma_3 = np.concatenate([np.concatenate([zero, -sigma_3]), np.concatenate([sigma_3, zero])], axis=1)

Gamma_1 = np.identity(4, dtype=np.complex128)
Gamma_2 = gamma_0

Gamma_3 = 1j * gamma_1
Gamma_4 = 1j * gamma_2
Gamma_5 = 1j * gamma_3

Gamma_6 = -np.dot(gamma_0, gamma_1)
Gamma_7 = -np.dot(gamma_0, gamma_2)
Gamma_8 = -np.dot(gamma_0, gamma_3)

Gamma_9 = 1j * np.dot(gamma_1, gamma_2)
Gamma_10 = 1j * np.dot(gamma_2, gamma_3)
Gamma_11 = 1j * np.dot(gamma_3, gamma_1)

Gamma_12 = 1j * gamma_0 @ gamma_1 @ gamma_2 @ gamma_3

Gamma_13 = gamma_1 @ gamma_2 @ gamma_3

Gamma_14 = -1j * gamma_0 @ gamma_2 @ gamma_3
Gamma_15 = -1j * gamma_0 @ gamma_1 @ gamma_3
Gamma_16 = -1j * gamma_0 @ gamma_1 @ gamma_2

Gammas = [Gamma_1, Gamma_2, Gamma_3, Gamma_4, Gamma_5, Gamma_6, Gamma_7, Gamma_8,
Gamma_9, Gamma_10, Gamma_11, Gamma_12, Gamma_13, Gamma_14, Gamma_15, Gamma_16]

xi = np.zeros([16, 16], dtype=np.complex128)
co = np.zeros([16, 16])

cond1 = 0
cond2 = 0

for a in range(16):
    for b in range(16):
        if a == b:
            prod = Gammas[a] @ Gammas[b]
            if (prod == Gamma_1).all() == False:
                cond1 += 1
            else:
                xi[a, b] = 1
                co[a, b] = 1
        if a != b:
            prod = Gammas[a] @ Gammas[b]
            for k in range(16):
                bool = prod == Gammas[k]
                if bool.all() == True:
                    xi[a, b] = 1
                    co[a, b] = k + 1
                    break
                bool = prod == -Gammas[k]
                if bool.all() == True:
                    xi[a, b] = -1
                    co[a, b] = k + 1
                    break
                bool = prod == 1j * Gammas[k]
                if bool.all() == True:
                    xi[a, b] = 1j
                    co[a, b] = k + 1
                    break
                bool = prod == -1j * Gammas[k]
                if bool.all() == True:
                    xi[a, b] = -1j
                    co[a, b] = k + 1
                    break
            if xi[a, b] == 0:
                print('wrong!', a + 1, b + 1)

if cond1 == 0:
    print('proposition 1 is correct !')

for i in range(16):
    for j in range(16):
        if i != j:
            if co[i, j] == 1:
                cond2 += 1
    cond2 += 16 - len(np.unique(co[i]))

if cond2 == 0:
    print('proposition 2 is correct !')

com = np.zeros([16, 16])
for i in range(16):
    for j in range(16):
        bool = Gammas[i] @ Gammas[j] == Gammas[j] @ Gammas[i]
        if bool.all() == True:
            com[i, j] = 1
        else:
            bool = Gammas[i] @ Gammas[j] == -Gammas[j] @ Gammas[i]
            if bool.all() == True:
                com[i, j] = -1

cond3 = 0
cond4 =0

for i in range(16):
    for j in range(16):
        if i != j:
            if com[i, j] == 0:
                cond3 += 1

if cond3 == 0:
    print('proposition 3 is correct !')

for i in range(1, 16):
    if -1 not in com[i]:
        cond4 += 1

if cond4 == 0:
    print('proposition 4 is correct !')

cond5 = 0
for i in range(1, 16):
    if np.trace(Gammas[i]) != 0:
        cond5 += 1

if cond5 == 0:
    print('proposition 5 is correct !')
