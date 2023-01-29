import time
from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/form', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        try:
            body = request.get_json()
            print(body['text'])
        except:
            print("JSON is broken")
        return '''The code was sent'''
    # handle get request
    return '''ERROR : 404, only POST req allowed or service not available'''