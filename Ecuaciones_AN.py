from tkinter import *
from tkinter.ttk import *
import matplotlib.pyplot as plt
import math

root = Tk()

root.title("Ecuaciones")
root.geometry("400x400")

value1 = StringVar()
value2 = StringVar()
value3 = StringVar()  

variable = StringVar() 

def quadraticEquation():
    a = float(value1.get())
    b = float(value2.get())
    c = float(value3.get())  

    d = (b ** 2) - (4 * a * c)  # Formula

    if d < 0:
        label = Label(root, text="No tiene solucion en los Reales", background="red")
        label.place(x=100, y=100)
        label.config(font=("Ink Free", 12))
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        r = "({:.6f}".format(x1) + ") - (" + "{:.6f}".format(x2) + ")" # Formato de los resultados
        print("X1: ", "{:.6f}".format(x1)) 
        print("X2: ", "{:.6f}".format(x2))
        variable.set(r)

def f(a, b, c, x):
    return a * x**2 + b * x + c

def openWindow():
    
    a = float(value1.get())
    b = float(value2.get())
    c = float(value3.get())

    x = range(-100, 100) # Rango de valores de X

    plt.plot(x, [f(a, b, c, i) for i in x])
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")
    plt.xlim(-60, 60)
    plt.ylim(-60, 60)
    plt.show()

# Entradas

field1 = Entry(root, textvariable=value1)  # Changed to textvariable=value1
field1.place(x=30, y=30, width=40, height=30)
field1.config(font=("Ink Free", 12))

field2 = Entry(root, textvariable=value2)  # Changed to textvariable=value2
field2.place(x=130, y=30, width=40, height=30)
field2.config(font=("Ink Free", 12))

field3 = Entry(root, textvariable=value3)  # Changed to textvariable=value3
field3.place(x=230, y=30, width=40, height=30)
field3.config(font=("Ink Free", 12))

# Etiquetas

label1 = Label(root, text="X^2 +", background="blue")
label1.place(x=75, y=30, width=50, height=30)
label1.config(font=("Ink Free", 12))

label2 = Label(root, text="X +", background="blue")
label2.place(x=175, y=30, width=50, height=30)
label2.config(font=("Ink Free", 12))

label3 = Label(root, text="= 0", background="blue")
label3.place(x=275, y=30, width=50, height=30)
label3.config(font=("Ink Free", 12))

# Botones

button1 = Button(root, text="Grafico", command=openWindow) # Llama a la funcion openWindow
button1.place(x=50, y=80, width=100, height=30)

button2 = Button(root, text="Calcular", command=quadraticEquation) # Llama a la funcion quadraticEquation
button2.place(x=200, y=80, width=100, height=30)

# Resultado

result1 = Label(root, text="X1", background="blue", textvariable=variable)  # Changed to textvariable=variable
result1.place(x=50, y=120, width=230, height=30)
result1.config(font=("Ink Free", 12))

# Window
root.resizable(False, False)
root.config(bg="blue", cursor="hand2")

root.mainloop()
