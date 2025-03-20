import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

def f(x):
    return x**2

def grad_f(x):
    return 2*x

def track_trajectory(xk, trajectory):
    trajectory.append(xk[0])

x0 = np.array([10.0])

methods = ["CG", "Newton-CG", "BFGS"]

trajectories = {}

results = {}
for method in methods:
    trajectory = [x0[0]]  
    if method == "Newton-CG":
        res = opt.minimize(f, x0, jac=grad_f, hess=lambda x: np.array([[2]]), 
                           method=method, callback=lambda xk: track_trajectory(xk, trajectory))
    else:
        res = opt.minimize(f, x0, jac=grad_f, method=method, 
                           callback=lambda xk: track_trajectory(xk, trajectory))
    results[method] = res
    trajectories[method] = trajectory

for method, res in results.items():
    print(f"{method}: {res.nit} iteraciones, mínimo en {res.x[0]:.6f}")

x_vals = np.linspace(-10, 10, 100)
y_vals = f(x_vals)

plt.figure(figsize=(6, 4))
plt.plot(x_vals, y_vals, label=r"$f(x) = x^2$", color="black")

for method, traj in trajectories.items():
    plt.plot(traj, f(np.array(traj)), marker="o", linestyle="dashed", markersize=8, label=method)

plt.legend()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Iteraciones de Optimización en $x^2$")
plt.grid(True)
plt.show()

