import os
from io import BytesIO

from flask import Flask
from flask import send_file
from flask import request
from flask import abort
from subprocess import call

location = '/tmp/'
suffix = 'tempfile'
filename = location + suffix + '0001.png'

app = Flask(__name__)

@app.route('/')
def render():
    message = request.args.get('location', default = 'LOCATION', type = str)
    app.logger.info("Received message: %s" % message)

    scene = request.args.get('scene', default = 'next', type = str)
    blender_file = "models/%s.blend" % scene

    # This script changes the text, it is run inside Blender. 
    blender_expression = "import bpy; bpy.data.objects['Text'].data.body = '%s'" % message
    # Render 3D image
    call('blender -b %s --python-expr "%s" -o %s%s -f 1' % (blender_file, blender_expression, location, suffix), shell=True)
    
    return send_file(filename, mimetype='image/png')

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