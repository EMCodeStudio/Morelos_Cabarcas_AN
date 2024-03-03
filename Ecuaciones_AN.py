import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import math


# Funcion para calcular la raíz de una Ecuacion Cuadratica
def metodo_numerico(a, b, c):
    discriminante = b**2 - 4 * a * c
    if discriminante < 0:
        return None, None
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return x1, x2


# Funcion para calcular f con la formula de la Ecuacion
def calcular_f(a, b, c, x):
    return a * x**2 + b * x + c


# Funcion para calcular los resultados con el Metodo de Biseccion
def metodo_biseccion(a, b, c, limite_a, limite_b, total=1e-6):
    results = []
    contador_iteracion = limite_a
    maxima_iteracion = limite_b

    if calcular_f(a, b, c, limite_a) * calcular_f(a, b, c, limite_b) > 0:
        messagebox.showerror("Error", "No hay cambio de signo en el intervalo dado.")
        return []

    while contador_iteracion < maxima_iteracion and abs(limite_b - limite_a) > total:
        # =(a_limit+b_limit)/2
        pm = (limite_a + limite_b) / 2
        # =a*pm^2+b*pm+c
        f_pm = calcular_f(a, b, c, pm)
        results.append((a, b, c, limite_a, limite_b, pm, f_pm))

        if f_pm == 0:
            break
      
        elif calcular_f(a, b, c, limite_a) * f_pm < 0:
            limite_b = pm
        else:
            limite_a = pm
        contador_iteracion += 1
    return results

# Funcion para dar formato a los valores del metodo de biseccion en una tabla
def formato_tabla_biseccion(limite_a, limite_b, results):
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
        f_a = calcular_f(a, b, c, limite_a)
        f_b = calcular_f(a, b, c, limite_b)
        porcentaje_error = abs((pm - results[-1][5]) / pm) * 100
        tree.insert(
            "",
            "end",
            values=(i + 0, limite_a, f_a, pm, f_pm, limite_b, f_b, porcentaje_error),
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
        messagebox.showerror("Error", "Ingrese números validos!")


# Funcion para dar formato a los valores del metodo de biseccion desde una tabla
def formato_metodo_biseccion():
    try:
        a = float(valor_a.get())
        b = float(valor_b.get())
        c = float(valor_c.get())

        limite_a = float(a_limite.get())
        limite_b = float(b_limite.get())

        results = metodo_biseccion(a, b, c, limite_a, limite_b)
        if results:
            formato_tabla_biseccion(limite_a, limite_b, results)
    except ValueError:
        messagebox.showerror(
            "Error", "Los coeficientes ingresados no son números validos!"
        )

# Funcion para graficar la ecuacion
def formato_metodo_grafico():
    a = float(valor_a.get())
    b = float(valor_b.get())
    c = float(valor_c.get())
    x = range(-100, 100) # Rango de valores de X
    plt.plot(x, [calcular_f(a, b, c, i) for i in x])
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")
    plt.xlim(-60, 60)
    plt.ylim(-60, 60)
    plt.show()


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
ttk.Label(root, text="x^2 +").grid(row=0, column=2, padx=5, pady=5)
ttk.Label(root, text="x +").grid(row=0, column=4, padx=5, pady=5)
ttk.Label(root, text="= 0").grid(row=0, column=6, padx=5, pady=5)

# Campos de Entrada de Valores de los Limites de la Iteracion
a_limite = ttk.Entry(root)
a_limite.grid(row=3, column=1, padx=5, pady=5)
b_limite = ttk.Entry(root)
b_limite.grid(row=3, column=3, padx=5, pady=5)

# Etiquetas de los Campos de Entrada de Limites de Iteracion
ttk.Label(root, text="xi").grid(row=3, column=2, padx=5, pady=5)
ttk.Label(root, text="xu").grid(row=3, column=4, padx=5, pady=5)

# Ejecutar Metodo Numerico
btnMetodoNumerico = ttk.Button(
    root, text="Metodo Numerico", command=formato_metodo_numerico
)
btnMetodoNumerico.grid(row=1, column=0, columnspan=2, pady=10)

# Ejecutar Metodo Grafico
btnMetodoNumerico = ttk.Button(
    root, text="Metodo Grafico", command=formato_metodo_grafico
)
btnMetodoNumerico.grid(row=1, column=2, columnspan=2, pady=10)

# Ejecutar Metodo Biseccion
btnMetodoBiseccion = ttk.Button(
    root, text="Metodo Biseccion", command=formato_metodo_biseccion
)
btnMetodoBiseccion.grid(row=5, column=2, columnspan=2, pady=10)

# Mostrar resultado del metodo numerico al ejecutar btnMetodoNumerico
resultado_numerico = ttk.Label(root, text="", font=("Arial", 12, "bold"))
resultado_numerico.grid(row=2, column=0, columnspan=6)

# Mostrar Resultados
root.mainloop()
