import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
y1 = np.array([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])

y2 = np.array([13635, 9591, 12227, 6907, 14045, 11752, 16212, 16545, 8831, 7993, 776, 12163])
y3 = np.array([15652, 16943, 14150, 12201, 10903, 12552, 13889, 15017, 11421, 14642, 13731, 13814])
y4 = np.array([13845, 17457, 15512, 14350, 11069, 16918, 16608, 12413, 13533, 12427, 2168, 16013])
y5 = np.array([13292, 15732, 17280, 10446, 14579, 11764, 13577, 12995, 16684, 656, 12554, 12216])
y6 = np.array([12089, 17641, 14184, 11801, 12489, 12540, 15644, 14691, 571, 10940, 11286, 15706])
y7 = np.array([14484, 11685, 10942, 15134, 16223, 14737, 16642, 12514, 13540, 10725, 13449, 14307])

plt.xticks(x)
plt.yticks(y1)

mylabels = ["Face cream sales data", "Face wash sales data", "Toothpaste sales data",
            "Toothpaste sales data", "Toothpaste sales data", "Toothpaste sales data"]

plt.plot(x,y2, color='red', marker='o', label=mylabels[2])
plt.plot(x,y3, color='green', marker='o', label=mylabels[3])
plt.plot(x,y4, color='blue', marker='o', label=mylabels[0])
plt.plot(x,y5, color='purple', marker='o', label=mylabels[4])
plt.plot(x,y6, color='brown', marker='o', label=mylabels[5])
plt.plot(x,y7, color='orange', marker='o', label=mylabels[1])

plt.xlabel("Month Number")
plt.ylabel("Sales unit in number")
plt.title("Sales data")

plt.legend()
plt.show()

