import matplotlib.pyplot as plt
import numpy as np

def ScatterPlot(xArr, yArr, colorArr):
    # Unit area ellipse
    rx, ry = 1., 1.
    area = rx * ry * np.pi
    theta = np.arange(0, 2 * np.pi + 0.01, 1)
    verts = np.column_stack([rx / area * np.cos(theta), ry / area * np.sin(theta)])

    # Convert colorArr boolean value to right/wrong colors (green, red)
    colorArrColors = [] # This will hold the colors of the converted boolean values
    for x in range(len(colorArr)):
        if colorArr[x]:
            colorArrColors.append('green')
        else:
            colorArrColors.append('red')

    # Plot with the passed data
    fig, ax = plt.subplots()
    ax.scatter(xArr, yArr, 100, colorArrColors, marker=verts)
    plt.show()