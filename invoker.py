import function

import os

from flask import Flask
from flask import request
from flask import abort
from subprocess import call

location = '/tmp/'
suffix = 'tempfile'
filename = location + suffix + '0001.png'

app = Flask(__name__)

@app.route('/')
def invoke():
	return function.render(request)

@app.route('/favicon.ico')
def favicon():
    abort(404)

@app.after_request
def cleanup(response):
    if os.path.isfile(filename):
        os.remove(filename)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)