from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import os

# File Directory
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'datasets.csv')

# Read Data from the csv File
data = pd.read_csv(file_path)
data.columns = ["emotion", "labels"]

# Assign an variable
emotion = data["emotion"]
label = data["labels"]

# Convert Text to numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emotion)

# ML model
model = MultinomialNB()
model.fit(X, label)

# Prediction
while True :
    user_input = input("What you feel today ? or press q to 'Quit' : ")
    user_input = user_input.lower()
    
    # Check if the user press q
    if user_input == "q" :
        break
    
    # Transfom text to int, and Predict user input
    vector = vectorizer.transform([user_input])
    prediction = model.predict(vector)
    proba = model.predict_proba(vector)
        
    # Check the result and give some condition
    if prediction[0] == 0 :
        print("Cheer up! | Accuracy : {:.2f}%".format(proba[0][0] * 100))
    else :
        print("HAHA Glad you have a wonderful day! | Accuracy : {:.2f}%".format(proba[0][0] * 100))
    
# Print when user leaves the loop
print("\nThank you and Goodbye!")

