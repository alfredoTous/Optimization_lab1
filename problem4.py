import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

def f1(x):
    return x**2

def grad_f1(x):
    return 2*x

def f2(x):
    return (x - 3)**2 + 2

def grad_f2(x):
    return 2*(x - 3)

def track_trajectory(xk, trajectory):
    trajectory.append(xk[0])

methods = ["CG", "Newton-CG", "BFGS"]

trajectories = {}

results = {}

def optimization_methods(f,grad_f,x0,tol):
    print("\n")
    for method in methods:
        trajectory = [x0[0]]  
        if method == "Newton-CG":
            res = opt.minimize(f, x0, jac=grad_f, hess=lambda x: np.array([[2]]), 
                               method=method, callback=lambda xk: track_trajectory(xk, trajectory), tol=tol)
        else:
            res = opt.minimize(f, x0, jac=grad_f, method=method, 
                               callback=lambda xk: track_trajectory(xk, trajectory), tol=tol)
        results[method] = res
        trajectories[method] = trajectory

    for method, res in results.items():
        print(f"{method}: {res.nit} iterations, minimum: {res.x[0]:.2f}")

    x_vals = np.linspace(-10, 10, 100)
    y_vals = f(x_vals)

    plt.figure(figsize=(6, 4))
    plt.plot(x_vals, y_vals, label=r"f(x)", color="black")

    for method, traj in trajectories.items():
        plt.plot(traj, f(np.array(traj)), marker="o", linestyle="dashed", markersize=8, label=method)

    plt.legend()
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(f"Optimization on f(x)$")
    plt.grid(True)  

    img_path = "actual_plot.png"
    plt.savefig(img_path)
    plt.close()  

    return img_path


def calculate_optimization_methods(f,tol,x0):

    x0 = np.array([x0])
    if f == "x**2":
        img_path = optimization_methods(f1,grad_f1,x0,tol)
    else:
        img_path = optimization_methods(f2,grad_f2,x0,tol)
    
    return img_path

        




