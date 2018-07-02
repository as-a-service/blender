import os

from flask import Flask
from flask import send_file
from flask import request
from subprocess import call


app = Flask(__name__)

@app.route('/')
def render():
    name = request.args.get('name', default = 'Your name', type = str)
    app.logger.info("Received name: %s" % name)

    expression = "import bpy; bpy.data.objects['Text'].data.body = '%s'" % name

    location = '/tmp/'
    suffix = 'tempfile'
    blend_file = 'script.blend'
    filename = location + suffix + '0001.png'
    call('blender -b %s --python-expr "%s" -o %s%s -f 1' % (blend_file, expression, location, suffix), shell=True)
    return send_file(filename, mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8080)