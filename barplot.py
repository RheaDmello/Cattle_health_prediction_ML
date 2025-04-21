#Barplot to visualize pH with New Grade

import matplotlib.pyplot as plt
import pandas as pd

# Load data from CSV file
data = pd.read_csv('MilkQuality.csv')

# pH vs New Grade
x_values = data['New Grade']
y_values = data['pH']

# Plotting the bar plot
plt.bar(x_values, y_values)

# Adding labels and title
plt.xlabel('New Grade')
plt.ylabel('pH')
plt.title('Bar Plot')

# Show plot
plt.show()


#Temperature vs New Grade
x_values = data['New Grade']
y_values = data['Temperature']
plt.bar(x_values, y_values)
plt.xlabel('New Grade')
plt.ylabel('Temperature')
plt.title('Bar Plot')
plt.show()

#Taste vs New Grade
x_values = data['New Grade']
y_values = data['Taste']
plt.bar(x_values, y_values)
plt.xlabel('New Grade')
plt.ylabel('Taste')
plt.title('Bar Plot')
plt.show()

#Odor vs New Grade
x_values = data['New Grade']
y_values = data['Odor']
plt.bar(x_values, y_values)
plt.xlabel('New Grade')
plt.ylabel('Odor')
plt.title('Bar Plot')
plt.show()

#Fat vs New Grade
x_values = data['New Grade']
y_values = data['Fat ']
plt.bar(x_values, y_values)
plt.xlabel('New Grade')
plt.ylabel('Fat')
plt.title('Bar Plot')
plt.show()

#Turbidity vs New Grade
x_values = data['New Grade']
y_values = data['Turbidity']
plt.bar(x_values, y_values)
plt.xlabel('New Grade')
plt.ylabel('Turbididty')
plt.title('Bar Plot')
plt.show()

#Colour vs New Grade
x_values = data['New Grade']
y_values = data['Colour']
plt.bar(x_values, y_values)
plt.xlabel('New Grade')
plt.ylabel('Colour')
plt.title('Bar Plot')
plt.show()

