import numpy as np
import collections

b0 = np.array([0, 0, 0 ,0])
b1 = np.array([1, 0, 0, 0])
b2 = np.array([0, 1, 0, 0])
b3 = np.array([0, 0, 1, 0])
b4 = np.array([0, 0, 0, 1])

Z = [b0, b1, b2, b3, b4, b1 + b2, b2 + b3, b3 + b4, b4 + b1, b1 + b3, b2 + b4, b1 + b2 + b3, b1 + b2 + b4, b1 + b3 + b4, b2 + b3 + b4, b1 + b2 + b3 + b4]

Z_value = [0 for i in range(16)]
for i in range(16):
    for j in range(4):
        Z_value[i] += Z[i][j] * (2 ** j)

indexes = np.zeros([16 ** 3, 7], dtype=int)

for i in range(16):
    for j in range(i + 1, 16):
        for k in range(j + 1, 16):
            W = [Z[i], Z[j], Z[k], Z[i] + Z[j], Z[j] + Z[k], Z[k] + Z[i], Z[i] + Z[j] + Z[k]]
            W_mod = []
            for l in range(7):
                W_mod.append(W[l] % 2)
            W_value = [0 for i in range(7)]
            for l in range(7):
                for m in range(4):
                    W_value[l] += W_mod[l][m] * (2 ** m)
            for l in range(7):
                indexes[16 ** 2 * i + 16 * j + k, l] = Z_value.index(W_value[l])

no_dup = []

for i in range(16 ** 3):
    if len(collections.Counter(indexes[i])) == 7:
        no_dup.append(i)

subgroups = []

for i in no_dup:
    subgroups.append(np.sort(indexes[i]))

subgroups_value = [0 for i in range(len(no_dup))]

for i in range(len(no_dup)):
    for j in range(7):
        subgroups_value[i] += subgroups[i][j] * (16 ** j)

unique_subgroup_num = len(collections.Counter(subgroups_value))

for i in range(unique_subgroup_num):
    unique_subgroups_value = collections.Counter(subgroups_value)

unique_subgroups_value = list(unique_subgroups_value.keys())

unique_subgroups_index = np.zeros([unique_subgroup_num, 7], dtype=int)

for i in range(unique_subgroup_num):
    VAL = unique_subgroups_value[i]
    for j in range(7):
        unique_subgroups_index[i, j] = VAL // 16 ** (6 - j)
        VAL = VAL % 16 ** (6 - j)

unique_subgroups = []
for i in range(unique_subgroup_num):
    subgroup = []
    for j in range(7):
        subgroup.append(list(Z[unique_subgroups_index[i, j]]))
    subgroup.append(list(b0))
    unique_subgroups.append(subgroup)


print("There are", unique_subgroup_num, "subgroups of (Z/2Z)^4 with index 2.")
for i in range(unique_subgroup_num):
    print("subgroup", i, ":", unique_subgroups[i])
