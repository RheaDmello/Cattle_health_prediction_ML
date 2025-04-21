import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('Supervised_data.csv')

# Bar Chart for New Grade distribution
plt.figure(figsize=(8, 6))
data['New Grade'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Distribution of New Grade')
plt.xlabel('New Grade')
plt.ylabel('Count')
plt.show()

# Pie Chart for 'Taste', 'Odor', and 'Fat' parameters
plt.figure(figsize=(10, 8))
data[['Taste', 'Odor', 'Fat ']].sum().plot(kind='pie', autopct='%1.1f%%', colors=['lightcoral', 'lightskyblue', 'lightgreen'])
plt.title('Distribution of Taste, Odor, and Fat Parameters')
plt.show()

# Histogram for Temperature
plt.figure(figsize=(10, 6))
plt.hist(data['Temperature'], bins=10, color='lightgreen', edgecolor='black')
plt.title('Temperature Distribution')
plt.xlabel('Temperature')
plt.ylabel('')
plt.show()