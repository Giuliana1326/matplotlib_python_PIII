import matplotlib.pyplot as plt

def line_plot():
    fig = plt.figure()  # crear figura
    ax = fig.add_subplot(111)  # crear eje

    ax.plot(x, y, color='blue', label='y = x^2')  # gráfico de línea

    ax.set_xlabel('x')  # nombre eje x
    ax.set_ylabel('y')  # nombre eje y
    ax.set_title('Gráfico de y = x^2')  # título

    ax.legend()  # mostrar leyenda

    plt.show()  # mostrar gráfico