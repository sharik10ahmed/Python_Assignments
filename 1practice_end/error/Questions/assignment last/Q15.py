import matplotlib.pyplot as plt
import numpy as np

# a) Plot Sine and Cosine
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), label="Sine")
plt.plot(x, np.cos(x), label="Cosine")
plt.legend()
plt.title("Sine and Cosine Waves")
plt.show()

# b) Plot Histogram
data = [10, 15, 15, 20, 25, 25, 25, 30]
plt.hist(data, bins=4, edgecolor='black')
plt.title("Histogram Example")
plt.show()
