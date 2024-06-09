import matplotlib.pyplot as plt
import numpy as np

def create_plot():
    # Generate random data
    x = np.linspace(0, 10, 100)
    y = np.random.rand(100)

    # Create the plot
    plt.figure()
    plt.plot(x, y, label='Random Data')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Random Data Plot')
    plt.legend()

    # Save the plot to a file
    plt.savefig("/mnt/data/plot.png")

def update_content(*args, **kwargs):
    create_plot()
    output_div = Element('output')
    output_div.clear()
    output_div.write('<img src="/mnt/data/plot.png" alt="Random Data Plot">')
