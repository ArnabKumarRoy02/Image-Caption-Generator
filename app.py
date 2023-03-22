from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def after():
    file = request.files['file1']

    file.save('static/file.jpg')
    return render_template('predict.html')

if __name__ == "__main__":
    app.debug=True
    app.run()