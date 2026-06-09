import numpy as np

marks = np.array([
    [78, 85, 90],
    [88, 79, 92],
    [65, 70, 72],
    [90, 95, 93]
])

print("Per student average:", marks.mean(axis=1))
print("Per subject average:", marks.mean(axis=0))
print("Top score in each subject:", marks.max(axis=0))

# axis 0 = “go down the rows” (operate column‑wise).
# axis 1 = “go across the columns” (operate row‑wise)

passed = marks >= 75
print("Pass/fail matrix:\n", passed)