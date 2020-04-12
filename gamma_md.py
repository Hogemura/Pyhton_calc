#!/usr/bin/env python
import numpy as np

zero = np.zeros([2, 2])
identity = np.identity(2)

sigma_1 = np.array([[0, 1], [1, 0]])
sigma_2 = np.array([[0, -1j], [1j, 0]])
sigma_3 = np.array([[1, 0], [0, -1]])

gamma_0 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]], dtype=np.complex128)
gamma_1 = np.concatenate([np.concatenate([zero, -sigma_1]), np.concatenate([sigma_1, zero])], axis=1)
gamma_2 = np.concatenate([np.concatenate([zero, -sigma_2]), np.concatenate([sigma_2, zero])], axis=1)
gamma_3 = np.concatenate([np.concatenate([zero, -sigma_3]), np.concatenate([sigma_3, zero])], axis=1)

gammaM_0 = np.concatenate([np.concatenate([zero, sigma_2]), np.concatenate([sigma_2, zero])], axis=1)
gammaM_1 = np.concatenate([np.concatenate([1j * sigma_3, zero]), np.concatenate([zero, 1j * sigma_3])], axis=1)
gammaM_2 = np.concatenate([np.concatenate([zero, sigma_2]), np.concatenate([-sigma_2, zero])], axis=1)
gammaM_3 = np.concatenate([np.concatenate([-1j * sigma_1, zero]), np.concatenate([zero, -1j * sigma_1])], axis=1)

gammaM_5 = 1j * gammaM_0 @ gammaM_1 @ gammaM_2 @ gammaM_3

print(gammaM_5 == np.concatenate([np.concatenate([sigma_2, zero]), np.concatenate([zero, -sigma_2])], axis=1))

Unit = np.concatenate([np.concatenate([identity, sigma_2]), np.concatenate([sigma_2, -identity])], axis=1)

gammas_D = [gamma_0, gamma_1, gamma_2, gamma_3]
gammas_M = [gammaM_0, gammaM_1, gammaM_2, gammaM_3]

for i in range(4):
    print(gammas_M[i] == Unit @ gammas_D[i] @ Unit * 1 / 2)
