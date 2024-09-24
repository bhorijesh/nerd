import numpy as np

def calculate_y(x):
    return x**2 + 6*x + 9


x_values = np.arange(-10, 5, 1)  
results = {}


for x in x_values:
    y = calculate_y(x)
    results[x] = y
    print(f"x: {x}, y: {y}")

for x in x_values:
    if results[x] == 0:
        print(f"y is zero at x = {x}")
        
    