import time
from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/form', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        body = request.form
        print('body is : ' + str(body))
        return '''The code sent to the backend is: {}'''.format(body)
    # handle get request
    return '''ERROR : 404, only POST req allowed or service not available'''