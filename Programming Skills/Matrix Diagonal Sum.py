# Without using numpy
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # Gets matrix length (ex: length = 3 -> matrix[3][3])
        n = len(mat)
        # Gets matrix middle
        middle = n // 2
        sum_ = 0

        # Example: diagonal mat[3][3] = [0, 0], [1, 1], ... + [3, 3], [2,2], ...
        for i in range(n):
            sum_ += mat[i][i] + mat[n-1-i][i]

        # Return sum if matrix is even,
        # Else subtracts the element in the middle or it will be summed twice
        return sum_ if n % 2 == 0 else sum_ - mat[middle][middle]

# Using numpy
import numpy as np
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # Gets mat length
        length = np.size(mat)
        # Takes element in the middle of the matrix
        center = np.take(mat, length // 2)
        # Trace gets the diagonal's sum, so the total = normal diagonal + inversed matrix diagonal
        sum_total = np.trace(mat) + np.trace(np.fliplr(mat))

        # If matrix is even, return just the sum_total,
        # Else, subtract the element in the center so it is not added twice
        return sum_total if length % 2 == 0 else sum_total - center
    