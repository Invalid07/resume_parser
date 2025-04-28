import os
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Use absolute paths for the model and vectorizer
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'rf_model.pkl')
VECTORIZER_PATH = os.path.join(BASE_DIR, 'models', 'tfidf.pkl')

# Load model and vectorizer
rf = pickle.load(open(MODEL_PATH, 'rb'))
tfidf = pickle.load(open(VECTORIZER_PATH, 'rb'))

@app.route('/')
def resume():
    return render_template('resume.html')

@app.route('/p', methods=["POST"])
def p():
    if 'resume' in request.files:
        file = request.files['resume']
        filename = file.filename
        if filename.endswith('.pdf'):
            text = pdf_to_text(file)  # You need to implement this function
        elif filename.endswith('.txt'):
            text = file.read().decode('utf-8')
        else:
            return render_template('resume.html', message="Invalid file format. Please upload a PDF or TXT file.")
        
        # Process the text and make predictions
        text_tfidf = tfidf.transform([text])
        prediction = rf.predict(text_tfidf)

        # Map the prediction to a meaningful result
        result = "Prediction result here"  # Update with actual result based on prediction

        return render_template('resume.html', message=result)

if __name__ == "__main__":
    app.run(debug=True)