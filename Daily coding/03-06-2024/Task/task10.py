import numpy as np
arr = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
unique, counts = np.unique(arr, return_counts=True)
frequency = dict(zip(unique, counts))
print(frequency)  # Output: {1: 1, 2: 2, 3: 3, 4: 4}
