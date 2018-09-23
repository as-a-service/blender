from flask import send_file
from subprocess import call

def render(request):
    location = '/tmp/renders/'
    suffix = 'tempfile'
    filename = location + suffix + '0001.png'
    
    message = request.args.get('text', default = 'HELLO', type = str)
    
    scene = request.args.get('scene', default = 'basic', type = str)
    blender_file = "models/%s.blend" % scene

    # This script changes the text, it is run inside our 3D software. 
    blender_expression = "import bpy; bpy.data.objects['Text'].data.body = '%s'" % message
    # Render 3D image
    call('blender -b %s --python-expr "%s" -o %s%s -f 1' % (blender_file, blender_expression, location, suffix), shell=True)
    
    return send_file(filename, mimetype='image/png')