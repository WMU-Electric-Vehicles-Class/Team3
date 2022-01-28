import numpy as np
from matplotlib import pyplot as plt


year = [1882, 1888, 1896, 1921, 1967, 1968, 1972, 1988, 1996, 2008, 2020]
position = [10, 30, 35, 60, 40, 40, 45, 100, 125, 200, 373]

plt.title('Year vs Maximum EV Range')
plt.plot(year, position)
plt.xlabel('Year')
plt.ylabel('EV Maximum Range')
plt.show()