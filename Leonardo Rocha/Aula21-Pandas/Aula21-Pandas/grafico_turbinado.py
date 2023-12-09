import pandas as pd
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[100,200,300,400,500]

plt.title("Distância Percorrida x Energia Gasta")
plt.xlabel("Energia")
plt.ylabel("Distancia")
plt.scatter(x,y)
plt.show()