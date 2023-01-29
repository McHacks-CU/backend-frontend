import time
from flask import Flask, request, render_template, jsonify
import re

# some_file.py
import sys

sys.path.insert(1, '../../ai')

from model import classify

app = Flask(__name__)

@app.route('/form', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        try:
            body = request.get_json()
            text = body['text']
            # print(text)
        except:
            return jsonify(result='ERROR : 400, bad request')
        # check code
        # print(text)
        keywords = ["query", "execute", "WHERE", "executeQuery", "statement", "prepare", "conn", "connection"] # keywords identifying sql
        sent_tokens = re.split(r'\n|;', text)
        need_to_check = ''
        for sentence in sent_tokens:
            tokenized_sent = [word.lower() for word in re.split(' ', sentence)]
            # print(tokenized_sent)
            # if any item in the tokenized sentence is a keyword, append the original sentence
            if any(keyw in tokenized_sent for keyw in keywords):
                need_to_check += str(sentence)

        print(need_to_check)
        if (not need_to_check):
            need_to_check = text

        resulting_info = classify(text, need_to_check)
                
        # fileinF = []
        # for sent in fileinE:
        #     # tokenize and lowercase tokens of the sentence
        #     tokenized_sent = [word.lower() for word in word_tokenize(sent)]
        #     # if any item in the tokenized sentence is a keyword, append the original sentence
        #     if any(keyw in tokenized_sent for keyw in keywords):
        #         fileinF.append(sent)

        return jsonify(result=resulting_info)

        # if (not classify(text)):
        #     return jsonify(result="WARNING : Your code is vulnerable to SQL Injection!")
        # else:
        #     return jsonify(result="Your code is safe!")
    # handle get request
    return jsonify(result='ERROR : 404, only POST req allowed or service not available')
