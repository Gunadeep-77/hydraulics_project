import numpy as np
import math

# Define the coefficients matrix (A) and the constants vector (b)
A = np.array([
    [1, 0, 0, 0, 0, 1, 0],   # q1 + q6 = 2.5
    [1, -1, 0, 0, 0, 0, -1], # q1 - q2 - q7 = 0
    [0, 1, -1, 0, 0, 0, 0],  # q2 - q3 = 0.5
    [0, 0, 1, 1, 0, 0, 0],   # q3 + q4 = 1
    [0, 0, 0, -1, 1, 0, 0],  # q5 - q4 = 1
    [0, 0, 0, 0, -1, 1, 0]   # q6 - q5 = 0
])

b = np.array([2.5, 0, 0.5, 1, 1, 0])

# Solve the system of equations
solution, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)

# Print the flow rates
for i, v in enumerate(solution):
    print(f'Q{i+1} = {v:.2f}')

# Verification
Q = [None]
Q.extend(list(solution))

print('\nVerification:')
loop1 = 0.00006144 * (Q[1]**2) + 0.002 * (Q[7]**2) - 0.00079 * (Q[5]**2) - 0.0000625 * (Q[6]**2)
print(f'loop 1: {loop1:.6f}')

# Head loss calculation
def get_hf(l, d, q, friction_factor=0.2, g=9.81):
    num = 8 * friction_factor * l * (q**2)
    den = (math.pi ** 2) * g * (d**5)
    return num / den

# Order L and D's according to Q's
L = [600, 600, 200, 600, 600, 200, 200]  # Lengths in meters
D = [250, 150, 100, 150, 150, 200, 100]  # Diameters in mm (will be converted to meters)
Q = Q[1:]  # Remove the first None value

# Convert diameters from mm to meters
D = [d * 1e-3 for d in D]

print('\nHeads at nodes in meters:')
h1 = 15
h2 = h1 - get_hf(L[0], D[0], Q[0])
h3 = h2 - get_hf(L[1], D[1], Q[1])
h4 = h3 - get_hf(L[2], D[2], Q[2])
h5 = h4 - get_hf(L[3], D[3], Q[3])
h6 = h5 - get_hf(L[4], D[4], Q[4])

print(f"h1 : {h1:.2f}")
print(f"h2 : {h2:.2f}")
print(f"h3 : {h3:.2f}")
print(f"h4 : {h4:.2f}")
print(f"h5 : {h5:.2f}")
print(f"h6 : {h6:.2f}")
