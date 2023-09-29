# Define the function whose root we want to find
def f(x):
    return x**2 +3*x +1

# Define the derivative of the function
def df(x):
    return 2 * x+3

# Initial guess for the root
x0 = 0

# Set a tolerance level for stopping the iterations
tolerance = 1e-4

# Maximum number of iterations (to prevent infinite looping)
max_iterations = 100

# Initialize the current guess
x_current = x0
iterations = 0
# Start the Newton-Raphson iteration
for i in (range(max_iterations)):
    # Compute the function value and its derivative at the current guess
    fx = f(x_current)
    dfx = df(x_current)
    
    # Update the guess for the root
    x_new = x_current - fx / dfx
    
    # Check if the absolute difference between the new and current guesses is below the tolerance
    if abs(x_new - x_current) < tolerance:
        break
    
    # Update the current guess
    x_current = x_new
    iterations += 1

# Print the approximate root
print("Approximate Root:", x_current)
print("iterations:", iterations)
