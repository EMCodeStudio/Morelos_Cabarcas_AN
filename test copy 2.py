import tkinter as tk
from tkinter import ttk, messagebox
import math


# Funcion para calcular la raiz de una Ecuacion Cuadratica
def metodo_numerico(a, b, c):
    discriminante = b**2 - 4 * a * c
    if discriminante < 0:
        return None, None
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return x1, x2


# Funcion para calcular f con Formula de la Ecuacion
def calcular_f(a, b, c, x):
    return a * x**2 + b * x + c


# Funcion para cacular los resultados con Metodo de Biseccion
def metodo_biseccion(a, b, c, limite_a, limite_b, tol=1e-6):
    results = []
    contador_iteracion = limite_a
    maxima_iteracion = limite_b

    while contador_iteracion < maxima_iteracion:

        # =(a_limit+b_limit)/2
        pm = (limite_a + limite_b) / 2

        # =a*pm^2+b*pm+c
        f_pm = calcular_f(a, b, c, pm)

        results.append((a, b, pm, f_pm))

        if f_pm == 0 or (b - a) / 2 < tol:
            break

        # =SI(f_a*f_pm < 0;a_limit;pm)
        elif calcular_f(a, b, c, a) * f_pm < 0:
            limite_a = limite_a
        else:
            limite_a = pm
        # =SI(f_pm*f_b>0;pm;b_limit)
        if f_pm * calcular_f(a, b, c, a) > 0:
            limite_b = pm
        else:
            limite_b = limite_b
        contador_iteracion += 1
    return results


# Funcion para dar formato a los valores del metodo de biseccion en una tabla
def formato_tabla_biseccion(a, b, results):
    results_window = tk.Toplevel(root)
    results_window.title("Resultados de Metodo de Biseccion")
    tree = ttk.Treeview(results_window)
    tree["columns"] = (
        "i",
        "a",
        "f(a)",
        "pm",
        "f(pm)",
        "b",
        "f(b)",
        "Error %",
    )
    for column in tree["columns"]:
        tree.heading(column, text=column)
    for i, (a, b, c, limite_a, limite_b, pm, f_pm) in enumerate(results):

        # =a*a_limit^2+b*a_limit+c
        f_a = calcular_f(a, b, c, limite_a)
        # =a*b_limit^2+b*b_limit+c
        f_b = calcular_f(a, b, c, limite_b)

        # =ABS(pm2-pm)/pm2
        error_percent = abs((results[-2][2]) - pm / results[-2][2]) * 100
        tree.insert(
            "",
            "end",
            values=(i + 0, limite_a, f_a, pm, f_pm, limite_b, f_b, error_percent),
        )
    tree.pack(fill="both", expand=True)


# Funcion para dar formato a los valores del metodo numerico en un label
def formato_metodo_numerico():
    try:
        a = float(valor_a.get())
        b = float(valor_b.get())
        c = float(valor_c.get())
        x1, x2 = metodo_numerico(a, b, c)
        if x1 is None:
            messagebox.showerror("Error", "No hay solucion real!")
        else:
            resultado_numerico.config(text=f"x1 = {x1:.6f}, x2 = {x2:.6f}")
    except ValueError:
        messagebox.showerror("Error", "Ingrese numeros validos!")


# Funcion para dar formato a los valores del metodo de biseccion desde una tabla
def formato_metodo_biseccion():
    try:
        a = float(valor_a.get())
        b = float(valor_b.get())
        c = float(valor_c.get())

        limite_a = float(a_limite.get())
        limite_b = float(b_limite.get())

        results = metodo_biseccion(a, b, c, limite_a, limite_b)
        formato_tabla_biseccion(limite_a, limite_b, results)

    except ValueError:
        messagebox.showerror(
            "Error", " Coeficientes ingresados no son numeros validos!"
        )


# Crear la Interfaz
root = tk.Tk()
root.title("Ecuaciones Analisis Numerico")


# Campos de Entrada de Valores de los Coeficientes
valor_a = ttk.Entry(root)
valor_a.grid(row=0, column=1, padx=5, pady=5)
valor_b = ttk.Entry(root)
valor_b.grid(row=0, column=3, padx=5, pady=5)
valor_c = ttk.Entry(root)
valor_c.grid(row=0, column=5, padx=5, pady=5)

# Etiquetas de los Campos de Entrada de Valores
ttk.Label(root, text="   ").grid(row=0, column=0, padx=5, pady=5)
ttk.Label(root, text="x^2 +").grid(row=0, column=2, padx=5, pady=5)
ttk.Label(root, text="x +").grid(row=0, column=4, padx=5, pady=5)
ttk.Label(root, text="= 0").grid(row=0, column=6, padx=5, pady=5)


# Campos de Entrada de Valores de los Limites de la Iteracion
a_limite = ttk.Entry(root)
a_limite.grid(row=3, column=1, padx=5, pady=5)
b_limite = ttk.Entry(root)
b_limite.grid(row=3, column=3, padx=5, pady=5)

# Etiquetas de los Campos de Entrada de Limites de Iteracion
ttk.Label(root, text="   ").grid(row=3, column=0, padx=5, pady=5)
ttk.Label(root, text="xi").grid(row=3, column=2, padx=5, pady=5)
ttk.Label(root, text="xu").grid(row=3, column=4, padx=5, pady=5)


# Ejecutar Metodo Numerico
btnMetodoNumerico = ttk.Button(
    root, text="Metodo Numerico", command=formato_metodo_numerico
)
btnMetodoNumerico.grid(row=1, column=0, columnspan=2, pady=10)

# Ejecutar Metodo Biseccion
btnMetodoBiseccion = ttk.Button(
    root, text="Metodo Biseccion", command=formato_metodo_biseccion
)
btnMetodoBiseccion.grid(row=4, column=2, columnspan=2, pady=10)

# Mostrar resultado del metodo numerico al ejecutar btnMetodoNumerico
resultado_numerico = ttk.Label(root, text="", font=("Arial", 12, "bold"))
resultado_numerico.grid(row=2, column=0, columnspan=6)

# Mostrar Resultados
root.mainloop()