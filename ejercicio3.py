def scatter_plot():
    sample_size = 20

    x = np.arange(-np.pi, np.pi, 0.1)
    y = np.tanh(x)

    fig = plt.figure()
    fig.suptitle('Scatter', fontsize=16)
    ax2 = fig.add_subplot(1, 1, 1)

    ax2.scatter(x, y, c='darkcyan', marker='o', label='y = tanh(x)')
    
    ax2.set_facecolor('whitesmoke')
    ax2.set_xlabel("X")
    ax2.set_ylabel("Y")
    ax2.grid(True)

    ax2.legend()

    plt.show()