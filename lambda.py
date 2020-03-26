#!/usr/bin/env python
import numpy as np

lambda_1 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
lambda_2 = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]])
lambda_3 = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]])
lambda_4 = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]])
lambda_5 = np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]])
lambda_6 = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]])
lambda_7 = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]])
lambda_8 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]]) * 3 ** (-0.5)

lambdas = [lambda_1, lambda_2, lambda_3, lambda_4, lambda_5, lambda_6, lambda_7, lambda_8]
traces = np.zeros([8, 8], dtype=np.complex128)

cond = 0

for a in range(8):
    for b in range(8):
        traces[a, b] = np.trace(lambdas[a] @ lambdas[b])

for a in range(8):
    for b in range(8):
        if a == b:
            if traces[a, b] != 2:
                cond += 1
        else:
            if traces[a, b] != 0:
                cond += 1

if cond == 0:
    print('lambda_a lambda_b is delta_ab')
