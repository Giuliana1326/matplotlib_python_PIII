def grid():
    x = np.linspace(0, 10, 40)
    
    y1 = x**2
    y2 = x**3
    y3 = x**4
    y4 = np.sqrt(x)

    fig = plt.figure()
    fig.suptitle('Grilla con 4 funciones', fontsize=16)

    # ✅ Crear 4 gráficos (2x2)
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    ax4 = fig.add_subplot(2, 2, 4)

    # Gráfico 1
    ax1.plot(x, y1, color='darkred', label='y = x^2')
    ax1.set_facecolor('whitesmoke')
    ax1.grid(True)
    ax1.set_title("x^2")
    ax1.legend()

    # Gráfico 2
    ax2.plot(x, y2, color='green', label='y = x^3')
    ax2.set_facecolor('whitesmoke')
    ax2.grid(True)
    ax2.set_title("x^3")
    ax2.legend()

    # Gráfico 3
    ax3.plot(x, y3, color='orange', label='y = x^4')
    ax3.set_facecolor('whitesmoke')
    ax3.grid(True)
    ax3.set_title("x^4")
    ax3.legend()

    # Gráfico 4
    ax4.plot(x, y4, color='purple', label='y = sqrt(x)')
    ax4.set_facecolor('whitesmoke')
    ax4.grid(True)
    ax4.set_title("sqrt(x)")
    ax4.legend()

    plt.show()