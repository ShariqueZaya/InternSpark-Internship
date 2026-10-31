# Import required libraries
import joblib

# Load the trained model and vectorizer
model = joblib.load("notebooks/spam_model.pkl")
tfidf = joblib.load("notebooks/tfidf_vectorizer.pkl")

# Function to predict spam or ham
def predict_spam(message):

    # Convert message into numerical features
    message_tfidf = tfidf.transform([message])

    # Predict the message
    prediction = model.predict(message_tfidf)

    # Display the result
    if prediction[0] == 1:
        return "Spam Message"
    else:
        return "Ham Message (Not Spam)"


# Take input from the user
message = input("Enter your SMS message: ")

# Display prediction
result = predict_spam(message)

print("Prediction:", result)