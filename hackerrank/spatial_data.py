import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import LeaveOneOut
from sklearn.metrics import c_index

# Step 1: Z-score Standardization
# Load the predictor features from input.csv
input_data = pd.read_csv('input.csv')
scaler = StandardScaler()
standardized_input = scaler.fit_transform(input_data)

# Load the output (water permeability values) from output.csv
output_data = pd.read_csv('output.csv')

# Load the geographical coordinate locations from coordinates.csv
coordinates = pd.read_csv('coordinates.csv')

# Step 2: Spatial Leave-One-Out Cross-Validation (SKCV)
c_index_values = []
for d in range(0, 251, 10):
    loo = LeaveOneOut()
    predictions = []
    true_values = []
    for train_index, test_index in loo.split(coordinates):
        # Calculate Euclidean distances
        distances = np.linalg.norm(coordinates.values - coordinates.values[test_index], axis=1)
        neighbors = np.where(distances <= d)[0]

        # Use the 15NN model to make predictions
        knn_model = KNeighborsRegressor(n_neighbors=15)
        knn_model.fit(standardized_input[train_index][:, neighbors], output_data.values[train_index])
        prediction = knn_model.predict(standardized_input[test_index][:, neighbors])

        predictions.append(prediction[0])
        true_values.append(output_data.values[test_index][0])

    # Step 3: Estimate Prediction Performance
    c_index_value = c_index(true_values, predictions)
    c_index_values.append(c_index_value)

# Step 4: Visualize Results
import matplotlib.pyplot as plt

distance_values = range(0, 251, 10)
plt.plot(distance_values, c_index_values, marker='o')
plt.xlabel('Distance (m)')
plt.ylabel('C-Index')
plt.title('C-Index as a Function of Distance')
plt.show()
