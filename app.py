import os
from io import BytesIO

from flask import Flask
from flask import send_file
from flask import request
from subprocess import call

blender_file = 'outrun.blend'
location = '/tmp/'
suffix = 'tempfile'
filename = location + suffix + '0001.png'

app = Flask(__name__)

@app.route('/')
def render():
    name = request.args.get('name', default = 'Your name', type = str)
    app.logger.info("Received name: %s" % name)

    # This script changes the text, it is run inside Blender. 
    blender_expression = "import bpy; bpy.data.objects['Text'].data.body = '%s'" % name
    # Render 3D image
    call('blender -b %s --python-expr "%s" -o %s%s -f 1' % (blender_file, blender_expression, location, suffix), shell=True)
    
    return send_file(filename, mimetype='image/png')

@app.after_request
def cleanup(response):
    os.remove(filename)
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)