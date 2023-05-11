import numpy as np
import matplotlib.pyplot as plt
#X Y cordinate graph with players ranks and points in the 2022 NBA draft.
#X is rank
#Y is points

x = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
y = [1437, 1010, 976, 1204, 1302, 789, 227, 614, 163, 193, 1056, 612, 467, 387, 639, 760, 85, 105, 673, 360, 679, 466, 266, 184, 42, 82, 122, 145, 75]

median_points = np.median(y)
plt.axhline(y = median_points, color = "r", linestyle = "--", label = "Median Points")


plt.plot(x, y)
plt.xlabel("Rank (X)")
plt.ylabel("Points (Y)")
plt.title("Rank vs. Points")
plt.show()

