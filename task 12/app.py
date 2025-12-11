from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# Load dataset
DATA_PATH = "crop_yield.csv"
df = pd.read_csv(DATA_PATH)

# Prepare features and target
FEATURE_COLS = ["Crop", "Crop_Year", "Season", "State", "Area", "Annual_Rainfall", "Fertilizer", "Pesticide"]
TARGET_COL = "Yield"

# Basic preprocessing: one-hot encode categorical features
X = df[FEATURE_COLS].copy()
y = df[TARGET_COL].values
X = pd.get_dummies(X, columns=["Crop", "Season", "State"], drop_first=False)

# Keep the columns to align incoming requests
MODEL_COLUMNS = X.columns.tolist()

# Train a simple model
model = RandomForestRegressor(n_estimators=50, random_state=42)
model.fit(X, y)


@app.route("/")
def index():
    # Send distinct options for the form
    crops = sorted(df['Crop'].unique().tolist())
    seasons = sorted(df['Season'].unique().tolist())
    states = sorted(df['State'].unique().tolist())
    return render_template('index.html', crops=crops, seasons=seasons, states=states)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Build DataFrame for single sample
    sample = pd.DataFrame([{
        'Crop': data.get('Crop'),
        'Crop_Year': int(data.get('Crop_Year')),
        'Season': data.get('Season'),
        'State': int(data.get('State')),
        'Area': float(data.get('Area')),
        'Annual_Rainfall': float(data.get('Annual_Rainfall')),
        'Fertilizer': float(data.get('Fertilizer')),
        'Pesticide': float(data.get('Pesticide')),
    }])

    sample = pd.get_dummies(sample, columns=["Crop", "Season", "State"], drop_first=False)
    # Align columns
    for col in MODEL_COLUMNS:
        if col not in sample.columns:
            sample[col] = 0
    sample = sample[MODEL_COLUMNS]

    pred = model.predict(sample.values)[0]
    return jsonify({'predicted_yield': float(pred)})


if __name__ == '__main__':
    app.run(debug=True)
