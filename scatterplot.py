
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt 
from matplotlib import pyplot as plt, font_manager as fm

data = pd.read_csv("MilkQuality.csv")


plt.plot(data['pH'])
plt.plot(data['New Grade'])
 
# Adding Title to the Plot
plt.title("Scatter Plot")
 
# Setting the X and Y labels
plt.xlabel('pH')
plt.ylabel('New Grade')
 
plt.show()