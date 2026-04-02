import numpy as np
import matplotlib.pyplot as plt

def multi_plot():
    x = list(np.linspace(-4, 4, 20))
    
    y1 = []
    for i in x:
        y1.append(i**2)

    y2 = []
    for i in x:
        y2.append(i**3)

    fig = plt.figure()
    ax = fig.add_subplot()

    ax.plot(x, y1, color='green', marker='^', label='y1 = x**2')
    ax.plot(x, y2, color='red', marker='+', label='y2 = x**3')
    
    ax.set_facecolor('whitesmoke')
    ax.set_title("Dos funciones juntas")
    ax.set_ylabel("Y[amplitud]")
    ax.set_xlabel("X[rads]")
    ax.set_xlim([-4, 4])
    ax.set_ylim([-12, 12])
    ax.legend()
      
    plt.show()


if _name_ == '_main_':
    print("Bienvenidos a otra clase con Python")
    print("Line Plot")

    multi_plot()

    print("terminamos")