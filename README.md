# Emotion Detection Website

This is a simple command-line emotion detection project using Python, scikit-learn, and a Naive Bayes classifier. The model predicts the user's emotion based on their text input and provides feedback with an accuracy score.

## Features
- Reads emotion data from a CSV file (`datasets.csv`).
- Trains a Multinomial Naive Bayes model to classify emotions.
- Accepts user input and predicts the emotion in real-time.
- Displays a friendly message and the prediction confidence.

## Getting Started

### Prerequisites
- Python 3.x
- Required packages:
  - pandas
  - scikit-learn

Install dependencies with:
```bash
pip install pandas scikit-learn
```

### Running the App
1. Make sure `datasets.csv` is in the same directory as `app.py`.
2. Run the script:
   ```bash
   python app.py
   ```
3. Enter your emotion as text when prompted, or type `q` to quit.

## How to Add Data and Improve Accuracy

1. **Open `datasets.csv`:**
   - The file should have two columns: the first for emotion text, the second for the label (e.g., 0 for negative, 1 for positive).
   - Example row: `I am so happy today,1`

2. **Add More Data:**
   - Add more rows with diverse and representative emotion texts and their correct labels.
   - The more varied and accurate your data, the better the model will perform.

3. **Save the File:**
   - After adding new data, save `datasets.csv`.

4. **Retrain the Model:**
   - Simply rerun `app.py`. The script will automatically retrain the model using the updated data.

5. **Tips for Better Accuracy:**
   - Add more examples for each emotion/label.
   - Avoid duplicate or ambiguous entries.
   - Ensure the labels are correct and consistent.

## Example `datasets.csv`
```
I am sad,0
I feel great,1
Not feeling well,0
Excited for the trip,1
```

## License
This project is for educational purposes.
