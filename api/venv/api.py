import time
from flask import Flask, request, render_template, jsonify


app = Flask(__name__)

@app.route('/form', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        try:
            body = request.get_json()
            text = body['text']
            print(text)
        except:
            return jsonify(result='ERROR : 400, bad request')
        return jsonify(result=text)
    # handle get request
    return jsonify(result='ERROR : 404, only POST req allowed or service not available')
