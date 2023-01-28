import time
from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/form', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        language = request.form.get('code')
        print(code)
        return '''The code sent to the backend is: {}'''.format(code)
        # return '''Your code is vulerable to sql injection {}'''.format(code)

    # handle get request
    return '''ERROR : 404, only POST req allowed or service not available'''