from scipy.integrate import solve_ivp #for solving ODE's 
import numpy as np 
import matplotlib.pyplot as plt
import math

e = math.e

def first_order_ode(x, y):
    return e**(x+y)
# initial conditions
x0 = 0  
y0 = 1  

# Define the range of x values for the solution
x_range = (0, 5)  

# Solve the ODE using scipy's solve_ivp function
solution = solve_ivp(first_order_ode, x_range, [y0], t_eval=np.linspace(x_range[0], x_range[1], 100))

for i, (x, y) in enumerate(zip(solution.t, solution.y[0])):
    print(f"Step {i + 1}: x = {x}, y(x) = {y}")

# Plotting the solution
plt.figure(figsize=(8, 6))
plt.plot(solution.t, solution.y[0], label='y(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solution of First Order ODE')
plt.legend()
plt.grid(True)
plt.show()
