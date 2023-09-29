def bisection(f, a, b, tol=1e-4, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("The function must have opposite signs at interval endpoints.")

    for index,i in enumerate(range(max_iter)):
        c = (a + b) / 2  # Calculate the midpoint of the interval
        if f(c) == 0 or (b - a) / 2 < tol:
            return c,index  # Found the root or the interval is small enough
        if f(c) * f(a) < 0:
            b = c  # Root is in the left half of the interval
        else:
            a = c  # Root is in the right half of the interval

    raise ValueError("Bisection method did not converge within the specified iterations.")

# Example usage:
# Define your function f(x) here
def f(x):
    return x**2 - 3

# Specify the interval [a, b] where you expect the root to be
a = 1
b = 2

# Call the bisection method to find the root
root,itreations = bisection(f, a, b)
print(f"Approximate root: {root}")
print(f"Number of itreations: {itreations}")
