import numpy as np

matrix_3x3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
diag_sum_3x3 = np.trace(matrix_3x3)
print(diag_sum_3x3)  # Output: 15

matrix_4x4 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
diag_sum_4x4 = np.trace(matrix_4x4)
print(diag_sum_4x4)  # Output: 34
