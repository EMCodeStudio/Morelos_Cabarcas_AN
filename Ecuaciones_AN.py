import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import math


# Funcion para dar formato a los valores del metodo Cuadratico en un label
def formato_metodo_cuadratico():
    try:
        a = float(valor_a.get())
        b = float(valor_b.get())
        c = float(valor_c.get())

        x1, x2 = metodo_cuadratico(a, b, c)
        if x1 is None:
            messagebox.showerror("Error", "No hay solucion real!")
        else:
            resultado_cuadratico.config(text=f"x1 = {x1:.2f}, x2 = {x2:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Ingrese números validos!")


# Funcion para calcular la raíz de una Ecuacion Cuadratica
def metodo_cuadratico(a, b, c):
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
    print("Valores de x: " + x)


# Funcion para graficar la ecuacion
def formato_metodo_grafico():
    a = float(valor_a.get())
    b = float(valor_b.get())
    c = float(valor_c.get())
    x = range(-100, 100)  # Rango de valores de X
    plt.plot(x, [calcular_f(a, b, c, i) for i in x])

    plt.axhline(0, color="red")
    plt.axvline(0, color="red")

    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.show()


# Funcion para calcular los resultados con el Metodo de Biseccion
def valores_metodo_biseccion(a, b, c, limite_a, limite_b, maxima_iteracion):
    contador_iteracion = 0
    results = []
    if calcular_f(a, b, c, limite_a) * calcular_f(a, b, c, limite_b) > 0:
        messagebox.showerror("Error", "No hay cambio de signo en el intervalo dado.")
        return []

    while contador_iteracion < maxima_iteracion:
        pm = (limite_a + limite_b) / 2
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

        # Calcular el porcentaje de error usando el xr actual y el anterior
        if i > 0:
            porcentaje_error = abs((pm - results[i - 1][5]) / pm) * 100
        else:
            porcentaje_error = 0  # No hay error en la primera iteración
        tree.insert(
            "",
            "end",
            values=(
                i + 1,
                limite_a,
                f_a,
                pm,
                f_pm,
                limite_b,
                f_b,
                f"{porcentaje_error:.2f}",
            ),
        )
    tree.pack(fill="both", expand=True)


# Funcion para dar formato a los valores del metodo de biseccion desde una tabla
def metodo_biseccion():
    try:
        a = float(valor_a.get())
        b = float(valor_b.get())
        c = float(valor_c.get())

        limite_a = float(a_limite.get())
        limite_b = float(b_limite.get())

        maxima_iteracion = int(max_iteracion.get())

        results = valores_metodo_biseccion(
            a, b, c, limite_a, limite_b, maxima_iteracion
        )
        if results:
            formato_tabla_biseccion(limite_a, limite_b, results)
    except ValueError:
        messagebox.showerror(
            "Error", "Los coeficientes ingresados no son números validos!"
        )


# Funcion para calcular f con la formula de la Ecuacion
def calcular_f_falsa_posicion(x):
    return -25 + 82 * x - 90 * x**2 + 44 * x**3 - 8 * x**4 + 0.7 * x**5
    print("Valores de x: " + x)


# Funcion para calcular los resultados con el Metodo de Falsa Posicion
def valores_metodo_falsa_posicion(limite_xl, limite_xu, maxima_iteracion):
    contador_iteracion = 0
    results = []
    ##if calcular_f(a, b, c, limite_a) * calcular_f(a, b, c, limite_b) > 0:
    ##messagebox.showerror("Error", "No hay cambio de signo en el intervalo dado.")
    ##return []
    while contador_iteracion < maxima_iteracion:

        f_xl = calcular_f_falsa_posicion(limite_xl)
        f_xu = calcular_f_falsa_posicion(limite_xu)

        xr = limite_xu - (f_xu * (limite_xl - limite_xu)) / (f_xl - f_xu)

        f_xr = calcular_f_falsa_posicion(xr)

        results.append((limite_xl, limite_xu, f_xl, f_xu, xr, f_xr))

        if calcular_f_falsa_posicion(limite_xl) * f_xr > 0:
            limite_xl = xr
        else:
            limite_xl = limite_xl

        if calcular_f_falsa_posicion(xr) * f_xu < 0:
            limite_xu = limite_xu
        else:
            limite_xu = xr

        contador_iteracion += 1
    return results


# Funcion para dar formato a los valores del metodo de Falsa Posicion en una tabla
def formato_tabla_falsa_posicion(limite_a, limite_b, results):
    results_window = tk.Toplevel(root)
    results_window.title("Resultados de Metodo de Falsa Posicion")
    tree = ttk.Treeview(results_window)
    tree["columns"] = (
        "iteracion",
        "xl",
        "f(xl)",
        "xu",
        "f(xu)",
        "xr",
        "f(xr)",
        "Error a%",
    )
    for column in tree["columns"]:
        tree.heading(column, text=column)
    for i, (limite_xl, limite_xu, f_xl, f_xu, xr, f_xr) in enumerate(results):
        print("ORIGINAL XU", limite_xu)
        # Calcular el porcentaje de error usando el punto medio actual y el anterior
        if i > 0:
            porcentaje_error_aproximado = (
                abs((limite_xu - results[i - 1][4]) / limite_xu) * 100
            )
            print("XU", limite_xu)
            print("POSICIONES", results[i - 1][4])
        else:
            porcentaje_error_aproximado = 0  # No hay error en la primera iteración
        tree.insert(
            "",
            "end",
            values=(
                i + 0,
                limite_xl,  # XL
                f_xl,
                limite_xu,  # XU
                f_xu,
                xr,
                f_xr,
                f"{porcentaje_error_aproximado:.2f}",
            ),
        )
    tree.pack(fill="both", expand=True)


def metodo_falsa_posicion():
    try:

        limite_a = float(a_limite.get())
        limite_b = float(b_limite.get())
        maxima_iteracion = int(max_iteracion.get())

        results = valores_metodo_falsa_posicion(limite_a, limite_b, maxima_iteracion)
        if results:
            formato_tabla_falsa_posicion(limite_a, limite_b, results)
    except ValueError:
        messagebox.showerror("Error", "Los datos ingresados no son números validos!")


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
ttk.Label(root, text="X^2 +").grid(row=0, column=2, padx=5, pady=5)
ttk.Label(root, text="X +").grid(row=0, column=4, padx=5, pady=5)
ttk.Label(root, text="= 0").grid(row=0, column=6, padx=5, pady=5)

# Campos de Entrada de Valores de los Limites de la Iteracion
a_limite = ttk.Entry(root)
a_limite.grid(row=3, column=1, padx=5, pady=5)

b_limite = ttk.Entry(root)
b_limite.grid(row=3, column=3, padx=5, pady=5)

max_iteracion = ttk.Entry(root)
max_iteracion.grid(row=3, column=5, padx=5, pady=5)


# Etiquetas de los Campos de Entrada de Limites de Iteracion
ttk.Label(root, text="Xi").grid(row=3, column=2, padx=5, pady=5)
ttk.Label(root, text="Xu").grid(row=3, column=4, padx=5, pady=5)
ttk.Label(root, text="Max Iteraciones").grid(row=3, column=6, padx=5, pady=5)


# Ejecutar Metodo Cuadratico
btnMetodoCuadratico = ttk.Button(
    root, text="Metodo Cuadratico", command=formato_metodo_cuadratico
)
btnMetodoCuadratico.grid(row=1, column=0, columnspan=2, pady=10)

# Ejecutar Metodo Grafico
btnMetodoGrafico = ttk.Button(
    root, text="Metodo Grafico", command=formato_metodo_grafico
)
btnMetodoGrafico.grid(row=1, column=2, columnspan=2, pady=10)

# Ejecutar Metodo Biseccion
btnMetodoBiseccion = ttk.Button(root, text="Metodo Biseccion", command=metodo_biseccion)
btnMetodoBiseccion.grid(row=5, column=2, columnspan=2, pady=10)

# Ejecutar Metodo Falsa Posicion
btnMetodoFalsaPosicion = ttk.Button(
    root, text="Metodo Falsa Posicion", command=metodo_falsa_posicion
)
btnMetodoFalsaPosicion.grid(row=5, column=4, columnspan=2, pady=10)

# Mostrar resultado del metodo Cuadratico al ejecutar btnMetodoCuadratico
resultado_cuadratico = ttk.Label(root, text="", font=("Arial", 12, "bold"))
resultado_cuadratico.grid(row=2, column=0, columnspan=6)

# Mostrar Resultados
root.mainloop()
