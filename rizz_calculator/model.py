import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pickle

class RizzModel:
    def __init__(self):
        self.model = RandomForestClassifier()
        self.is_trained = False

    def load_data(self, file_path):
        """Load data from a CSV file."""
        data = pd.read_csv(file_path)
        return data

    def preprocess_data(self, data):
        """Preprocess the input data."""
        # Here you would handle any necessary preprocessing steps.
        # For example, converting categorical features to numerical ones, etc.
        # For this demo, let's assume we have already cleaned and structured data.
        features = data[['skibidy_rizz', 'sigma_wolf', 'chaos_level']]
        labels = data['rizz_category']  # Assuming you have a column for rizz categories
        return features, labels

    def train_model(self, file_path):
        """Train the Random Forest model using the provided data file."""
        data = self.load_data(file_path)
        features, labels = self.preprocess_data(data)
        
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

        # Train the model
        self.model.fit(X_train, y_train)
        self.is_trained = True

        # Evaluate the model
        predictions = self.model.predict(X_test)
        report = classification_report(y_test, predictions)
        print("Model Training and Evaluation Report:\n", report)

    def predict_rizz(self, user_data):
        """Predict rizz category based on user input."""
        if not self.is_trained:
            raise Exception("Model is not trained yet. Please train the model first.")

        # Prepare the user data for prediction
        user_features = [[user_data['skibidy_rizz'], user_data['sigma_wolf'], user_data['chaos_level']]]
        
        # Make a prediction
        prediction = self.model.predict(user_features)
        return prediction[0]

    def save_model(self, filename):
        """Save the trained model to a file."""
        with open(filename, 'wb') as file:
            pickle.dump(self.model, file)

    def load_model(self, filename):
        """Load a trained model from a file."""
        with open(filename, 'rb') as file:
            self.model = pickle.load(file)
        self.is_trained = True


