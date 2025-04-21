import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
df = pd.read_csv(r"algos.csv")

# Plotting the accuracy graph
plt.figure(figsize=(8, 6))
plt.bar(df['Algorithm'], df['Accuracy'], color='skyblue')
plt.xlabel('Algorithm')
plt.ylabel('Accuracy')
plt.title('Accuracy of Different Machine Learning Algorithms')
plt.ylim(0, 1)  # Set the y-axis limit from 0 to 1 for accuracy range
plt.show()