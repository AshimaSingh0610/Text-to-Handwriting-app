from flask import Flask, request, send_file, render_template
from pdf_generator.handwriting import generate_pdf

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    text = request.form['text']
    handwriting_style = request.form['style']
    pdf_path = generate_pdf(text, handwriting_style)
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
