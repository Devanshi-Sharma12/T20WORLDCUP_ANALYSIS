import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def train_model(csv_file):
    # Load the CSV file
    df = pd.read_csv(csv_file)
    print("Columns in the CSV file:", df.columns)

    # Use 'Average' as a feature and 'Wickets' as the target
    features = ['Average']
    target = 'Wickets'

    # Check if required columns are present
    missing_features = [col for col in features if col not in df.columns]
    if missing_features:
        raise KeyError(f"Missing columns in the CSV: {missing_features}")
    if target not in df.columns:
        raise KeyError(f"Target column '{target}' is missing in the CSV file.")

    # Extract features and target
    X = df[features]
    y = df[target]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate the model
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"Model Mean Squared Error: {mse}")
    return model

if __name__ == "__main__":
    try:
        model = train_model('most_wickets_t20_world_cup_2024.csv')
    except Exception as e:
        print("Error:", e)
