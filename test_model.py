
import joblib

import pandas as pd

 

# Load model

model = joblib.load("model.pkl")

 

# Test data

test_data = pd.DataFrame({"area": [7500], "bedrooms": [3], "bathrooms": [2]})

prediction = model.predict(test_data)

 

print(f"Predicted price: {prediction[0]}")

Add a commit message like:
Copy code

Added test_model.py script
