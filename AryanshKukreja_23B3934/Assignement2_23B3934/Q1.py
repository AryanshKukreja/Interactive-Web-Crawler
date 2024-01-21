import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
y1 = np.array([300, 700, 1100, 1400, 1600, 1700, 1900, 1400, 1200, 1300, 2000, 3300])
y2 = np.array([100, 600, 800, 300, 400, 500, 3500, 3300, 2100, 1400, 2400, 2000])

plt.xlabel("Month Number")
plt.ylabel("Sales unit in Number")
plt.title("Facewash and facecream sales data")

plt.grid(linestyle="--")

mylabels = ["Face cream sales data", "Face creams wash data"]

plt.bar(x - 0.125, y1, label=mylabels[0], color="blue", width=0.25)
plt.bar(x + 0.125, y2, label=mylabels[1], color="orange", width=0.25)

plt.xticks(x)

plt.legend()
plt.show()

