SMS Spam Detection using Machine Learning

Project Overview

This project uses Machine Learning to classify SMS messages as either Spam or Ham (Not Spam). It analyzes the text of a message and predicts whether it is unwanted spam.

Objective

To build and evaluate machine learning models that can detect spam messages with good accuracy.

Dataset

The project uses the SMS Spam Collection dataset, which contains SMS messages labeled as:

- Ham: Legitimate messages
- Spam: Unwanted or promotional messages

Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

Machine Learning Models

The following models were trained and evaluated:

1. Multinomial Naive Bayes
2. Logistic Regression

Methodology

1. Loaded and explored the dataset.
2. Cleaned and preprocessed the messages.
3. Converted text into numerical features using TF-IDF.
4. Split the dataset into training and testing sets.
5. Trained and evaluated both machine learning models.
6. Compared model performance using accuracy, precision, recall, F1-score, and ROC-AUC.
7. Developed a simple Python application to predict whether a message is spam.

Results

Multinomial Naive Bayes achieved approximately 98.26% accuracy, while Logistic Regression achieved approximately 96.71% accuracy on the test dataset.

How to Run the Project

1. Install dependencies

pip install -r requirements.txt

2. Run the application

From the project root folder, run:

python src/app.py

3. Enter a message

Type an SMS message when prompted. The application will display whether it is Spam or Ham.

Project Structure

SMS_Spam_Detection/
├── dataset/
├── notebooks/
├── results/
│   └── plots/
├── report/
├── src/
│   └── app.py
├── .gitignore
├── README.md
└── requirements.txt

Author

Md Sharique Zaya

Artificial Intelligence Intern
InternSpark