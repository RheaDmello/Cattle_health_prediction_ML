import pandas as pd
from sklearn.preprocessing import StandardScaler
# Load the dataset
data = pd.read_csv("MilkQuality.csv")
X = data[['pH', 'Temperature', 'Taste', 'Odor', 'Fat ', 'Turbidity', 'Colour']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


from sklearn.cluster import KMeans


k = 3

# Initialize the KMeans model
kmeans = KMeans(n_clusters=k, random_state=0)

# Fit the model to the scaled data
kmeans.fit(X_scaled)

# Get the cluster labels
cluster_labels = kmeans.labels_

# Add cluster labels to the original dataset
data['Cluster'] = cluster_labels

# View the clustered dataset
print(data)