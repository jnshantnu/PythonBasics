import numpy as np

sales = np.array([1200, 1350, 1280, 1500, 1700, 1600, 1800])

print("Total:", sales.sum())
print("Average:", sales.mean())
print("Max:", sales.max())
print("Min:", sales.min())

growth = (sales[1:] - sales[:-1]) / sales[:-1] * 100

## Each entry is “current week – previous week” for weeks 1, 2, 3, … in order.
# Conceptually:
# 
# sales[1:] → all “current” values starting from week 1.
# 
# sales[:-1] → all “previous” values aligned with those.
# 
# Subtraction → all week‑over‑week deltas in one vectorized operation, no loop.
# 
# Why this pattern is powerful
# This “shift two slices and subtract” trick is extremely common whenever you want:
# 
# Differences between consecutive time periods (week‑over‑week, month‑over‑month, day‑over‑day).
# 
# Returns in a time series (price differences, log returns).
# 
# First differences in any numeric series.


print("Week-over-week growth %:", growth)

moving_avg = np.convolve(sales, np.ones(3)/3, mode='valid')
print("3-week moving average:", moving_avg)