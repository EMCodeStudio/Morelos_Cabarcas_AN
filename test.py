import tkinter as tk
from tkinter import ttk, messagebox
import math


def solve_quadratic_equation(a, b, c):
    """Solve a quadratic equation."""
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        return None, None
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2


def calculate_f(a, b, c, x):
    """Calculate the value of the quadratic function."""
    return a * x**2 + b * x + c


def bisection_method(a, b, c, tol=1e-6):
    """Bisection method to find roots of a quadratic function."""
    results = []
    iter_count = a
    max_iter = b
    while iter_count < max_iter:

        pm = (a + b) / 2

        f_pm = calculate_f(a, b, c, pm)

        results.append((a, b, pm, f_pm))

        if f_pm == 0 or (b - a) / 2 < tol:
            break
        elif calculate_f(a, b, c, a) * f_pm < 0:
            b = pm
        else:
            a = pm
        iter_count += 1
    return results


def show_results(a, b, c, results):
    """Display the results in a new window."""
    results_window = tk.Toplevel(root)
    results_window.title("Bisection Method Results")

    tree = ttk.Treeview(results_window)
    tree["columns"] = (
        "Iteration",
        "a",
        "f(a)",
        "Midpoint",
        "f(Midpoint)",
        "b",
        "f(b)",
        "Error %",
    )
    for column in tree["columns"]:
        tree.heading(column, text=column)

    for i, (a_val, b_val, pm, f_pm) in enumerate(results):

        f_a = calculate_f(a, b, c, a_val)
        f_b = calculate_f(a, b, c, b_val)

        error_percent = (
            abs((pm - results[-2][2]) / results[-2][2]) * 100
            if len(results) > 1 and results[-2][2] != 0
            else 0
        )

        tree.insert(
            "", "end", values=(i + 0, a_val, f_a, pm, f_pm, b_val, f_b, error_percent)
        )

    tree.pack(fill="both", expand=True)


def calculate_and_show_results():
    """Calculate roots and show results."""
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        x1, x2 = solve_quadratic_equation(a, b, c)

        if x1 is None:
            messagebox.showerror("Error", "No real roots.")
        else:
            result_label.config(text=f"x1 = {x1:.6f}, x2 = {x2:.6f}")
            results = bisection_method(a, b, c)
            show_results(a, b, c, results)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric coefficients.")


root = tk.Tk()
root.title("Quadratic Equation Solver")

# Coefficient entries
entry_a = ttk.Entry(root)
entry_a.grid(row=0, column=1, padx=5, pady=5)
entry_b = ttk.Entry(root)
entry_b.grid(row=0, column=3, padx=5, pady=5)
entry_c = ttk.Entry(root)
entry_c.grid(row=0, column=5, padx=5, pady=5)

# Coefficient labels
ttk.Label(root, text="x^2 +").grid(row=0, column=0, padx=5, pady=5)
ttk.Label(root, text="x +").grid(row=0, column=2, padx=5, pady=5)
ttk.Label(root, text="= 0").grid(row=0, column=4, padx=5, pady=5)

# Solve button
solve_button = ttk.Button(root, text="Solve", command=calculate_and_show_results)
solve_button.grid(row=1, column=0, columnspan=6, pady=10)

# Result label
result_label = ttk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.grid(row=2, column=0, columnspan=6)

root.mainloop()
