import numpy as np

rolls = np.random.randint(1, 7, size=10000)


# np.random.randint(low, high, size=...) returns random integers from low (inclusive) up to high (exclusive).
# low = 1: smallest possible value is 1.
# high = 7: upper bound is exclusive, so the largest possible value is 6 (7 is not included).
# This means the values are in [1, 7) → possible values: 1, 2, 3, 4, 5, 6.
# What size=10000 means
# size=10000 tells NumPy to generate 10,000 such random integers and put them into a 1D array.
# So rolls is an array like: [3, 6, 2, 1, 4, 5, ...] with length 10,000 (the actual numbers vary every run).


print("Average roll:", rolls.mean())

counts = np.bincount(rolls)[1:]
print("Counts for 1-6:", counts)

probabilities = counts / len(rolls)
print("Estimated probabilities:", probabilities)