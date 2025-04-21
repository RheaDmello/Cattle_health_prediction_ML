import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix


# Load the data
data = pd.read_csv('Supervised_data.csv')

# Split the data into features (X) and target variable (y)
X = data[['pH', 'Temperature', 'Taste', 'Odor', 'Fat ', 'Turbidity', 'Colour']]
y = data['New Grade']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Apply Decision Tree
dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)

# Make predictions
predictions = dt.predict(X_test)

# Calculate evaluation metrics
accuracy = accuracy_score(y_test, predictions)
conf_matrix =confusion_matrix(y_test, predictions)
specificity = conf_matrix[0, 0] / (conf_matrix[0, 0] + conf_matrix[0, 1])
precision = precision_score(y_test, predictions, average='weighted')
recall = recall_score(y_test, predictions, average='weighted')
sensitivity = recall
f1 = f1_score(y_test, predictions, average='weighted')
conf_matrix = confusion_matrix(y_test, predictions)

print("Decision Tree")
print("Accuracy:", accuracy)
print("Specificity:", specificity)
print("Precision:", precision)
print("Recall:", recall)
print("Sensitivity:", sensitivity)
print("F1 Score:", f1)
print("Confusion Matrix:", conf_matrix)