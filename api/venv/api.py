import time
from flask import Flask, request, render_template, jsonify
# import nltk

# some_file.py
import sys
<<<<<<< HEAD
# caution: path[0] is reserved for script path (or '' in REPL)
# sys.path.insert(1, '../ai')
=======

sys.path.insert(1, '../ai')
>>>>>>> main

# from model import classify

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
        # check code
        print(text)
        return jsonify(result="This is sent from the backend")

        # if (not classify(text)):
        #     return jsonify(result="WARNING : Your code is vulnerable to SQL Injection!")
        # else:
        #     return jsonify(result="Your code is safe!")
    # handle get request
    return jsonify(result='ERROR : 404, only POST req allowed or service not available')
