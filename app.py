from flask import Flask, request, render_template
from flask_cors import CORS
from chatbot import handle_prompt 

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_data(as_text=True)
    return handle_prompt(data)

if __name__ == '__main__':
    app.run()