import math

# Define the function whose root we want to find
def f(x):
    return 2 * math.cosh(x)*math.sin(x)
# Initial guesses for the roots
x0 = 0.4
x1 = 0.5

# Set a tolerance level for stopping the iterations
tolerance = 1e-4

# Maximum number of iterations (to prevent infinite looping)
max_iterations = 100
iterations = 0
# Start the secant iteration
for i in range(max_iterations):
    # Compute function values at the current guesses
    fx0 = f(x0)
    fx1 = f(x1)
    
    # Update the guess for the root using the secant formula
    x_new = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
    
    # Check if the absolute difference between the new and current guesses is below the tolerance
    if abs(x_new - x1) < tolerance:
        break
    
    # Update the guesses for the next iteration
    x0 = x1
    x1 = x_new
    iterations += 1

# Print the approximate root
print("Approximate Root:", x1)
print("Number of iterations:", iterations)