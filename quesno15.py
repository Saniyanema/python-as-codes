def print_pascal_triangle(N):
    for i in range(N):
        # Print leading spaces
        print(' ' * (N - i - 1), end='')
        # Print binomial coefficients
        for j in range(i + 1):
            # Calculate binomial coefficient using math.comb
            print(math.comb(i, j), end=' ')
        print()

import math
N = int(input())
print_pascal_triangle(N)
