from flask import Flask,request,render_template
import pickle
import sklearn

# ------------------------------------------------------------------------------------------------------------
# load model
# rf=pickle.load(open('resume_parser/models/rf_model.pkl','rb'))
# tfidf=pickle.load(open('resume_parser/models/tfidf.pkl','rb'))


# -----------------------------------------------------------------------------------------------------------------
app = Flask(__name__)


# ---------------------------------------------------------------------------------------------------------
# routing
@app.route('/')    # fro routing 
def resume():
    return render_template('resume.html')
@app.route('/p', methods=["POST"])
def p():
    def pred():
        # Process the PDF or TXT file and make prediction
        if 'resume' in request.files:
            file = request.files['resume']
            filename = file.filename
            if filename.endswith('.pdf'):
                text = pdf_to_text(file)
            elif filename.endswith('.txt'):
                text = file.read().decode('utf-8')
            else:
                return render_template('resume.html', message="Invalid file format. Please upload a PDF or TXT file.")
# --------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------
# python main 
if __name__=="__main__":
    app.run(debug=True)