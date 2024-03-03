

import tkinter as tk
from tkinter import ttk, messagebox
import math

# Función para calcular la raíz de una ecuación cuadrática
def metodo_numerico(coeficiente_a, coeficiente_b, coeficiente_c):
    discriminante = coeficiente_b ** 2 - 4 * coeficiente_a * coeficiente_c
    if discriminante < 0:
        return None, None
    else:
        x1 = (-coeficiente_b + math.sqrt(discriminante)) / (2 * coeficiente_a)
        x2 = (-coeficiente_b - math.sqrt(discriminante)) / (2 * coeficiente_a)
        return x1, x2

# Función para calcular f(x) con la fórmula de la ecuación
def calcular_f(coeficiente_a, coeficiente_b, coeficiente_c, x):
    return coeficiente_a * x ** 2 + coeficiente_b * x + coeficiente_c

# Funcion para calcular los resultados con el método de bisección
def metodo_biseccion(coeficiente_a, coeficiente_b, coeficiente_c, limite_a, limite_b, tol=1e-6):
    results = []
    contador_iteracion = limite_a
    maxima_iteracion = limite_b

    while contador_iteracion < maxima_iteracion:
        pm = (limite_a + limite_b) / 2
        f_pm = calcular_f(coeficiente_a, coeficiente_b, coeficiente_c, pm)
        results.append((coeficiente_a, coeficiente_b, coeficiente_c, limite_a, limite_b, pm, f_pm))

        if f_pm == 0 or (limite_b - limite_a) / 2 < tol:
            break
        elif calcular_f(coeficiente_a, coeficiente_b, coeficiente_c, limite_a) * f_pm < 0:
            limite_b = pm
        else:
            limite_a = pm
        contador_iteracion += 1
    return results

# Función para dar formato a los valores del método de bisección en una tabla
def formato_tabla_biseccion(coeficiente_a, coeficiente_b, results):
    results_window = tk.Toplevel(root)
    results_window.title("Resultados del Método de Bisección")
    tree = ttk.Treeview(results_window)
    tree["columns"] = ("i", "a", "f(a)", "pm", "f(pm)", "b", "f(b)", "Error %")
    for column in tree["columns"]:
        tree.heading(column, text=column)
    for i, (a, b, c, limite_a, limite_b, pm, f_pm) in enumerate(results):
        f_a = calcular_f(a, b, c, limite_a)
        f_b = calcular_f(a, b, c, limite_b)
        error_percent = abs(pm - results[-2][5]) / results[-2][5] * 100
        tree.insert("", "end", values=(i + 1, limite_a, f_a, pm, f_pm, limite_b, f_b, error_percent))
    tree.pack(fill="both", expand=True)

# Función para dar formato a los valores del método numérico en un label
def formato_metodo_numerico():
    try:
        coeficiente_a = float(valor_a.get())
        coeficiente_b = float(valor_b.get())
        coeficiente_c = float(valor_c.get())
        x1, x2 = metodo_numerico(coeficiente_a, coeficiente_b, coeficiente_c)
        if x1 is None:
            messagebox.showerror("Error", "No hay solución real!")
        else:
            resultado_numerico.config(text=f"x1 = {x1:.6f}, x2 = {x2:.6f}")
    except ValueError:
        messagebox.showerror("Error", "Ingrese coeficientes válidos!")

# Función para dar formato a los valores del método de bisección desde una tabla
def formato_metodo_biseccion():
    try:
        coeficiente_a = float(valor_a.get())
        coeficiente_b = float(valor_b.get())
        coeficiente_c = float(valor_c.get())
        limite_a = float(a_limite.get())
        limite_b = float(b_limite.get())
        results = metodo_biseccion(coeficiente_a, coeficiente_b, coeficiente_c, limite_a, limite_b)
        formato_tabla_biseccion(coeficiente_a, coeficiente_b, results)
    except ValueError:
        messagebox.showerror("Error", "Los coeficientes ingresados no son válidos!")

# Crear la Interfaz
root = tk.Tk()
root.title("Ecuaciones - Análisis Numérico")

# Campos de Entrada de Valores de los Coeficientes
valor_a = ttk.Entry(root)
valor_a.grid(row=0, column=1, padx=5, pady=5)
valor_b = ttk.Entry(root)
valor_b.grid(row=0, column=3, padx=5, pady=5)
valor_c = ttk.Entry(root)
valor_c.grid(row=0, column=5, padx=5, pady=5)

# Etiquetas de los Campos de Entrada de Valores
ttk.Label(root, text="x^2 +").grid(row=0, column=2, padx=5, pady=5)
ttk.Label(root, text="x +").grid(row=0, column=4, padx=5, pady=5)
ttk.Label(root, text="= 0").grid(row=0, column=6, padx=5, pady=5)

# Campos de Entrada de Valores de los Límites de la Iteración
a_limite = ttk.Entry(root)
a_limite.grid(row=3, column=1, padx=5, pady=5)
b_limite = ttk.Entry(root)
b_limite.grid(row=3, column=3, padx=5, pady=5)

# Etiquetas de los Campos de Entrada de Límites de Iteración
ttk.Label(root, text="xi").grid(row=3, column=2, padx=5, pady=5)
ttk.Label(root, text="xu").grid(row=3, column=4, padx=5, pady=5)

# Ejecutar Método Numérico
btnMetodoNumerico = ttk.Button(root, text="Método Numérico", command=formato_metodo_numerico)
btnMetodoNumerico.grid(row=1, column=0, columnspan=2, pady=10)

# Ejecutar Método Bisección
btnMetodoBiseccion = ttk.Button(root, text="Método Bisección", command=formato_metodo_biseccion)
btnMetodoBiseccion.grid(row=4, column=2, columnspan=2, pady=10)

# Mostrar resultado del método numérico al ejecutar btnMetodoNumerico
resultado_numerico = ttk.Label(root, text="", font=("Arial", 12, "bold"))
resultado_numerico.grid(row=2, column=0, columnspan=6)

# Mostrar Resultados
root.mainloop()
