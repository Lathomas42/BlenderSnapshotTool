import bpy
import time
import os

fn = os.getenv('fn')

bpy.ops.render.opengl()
#time.sleep(3)
img = bpy.data.images[0]
img.reload()
filepath = r'images/'+fn+'.tif'

settings = bpy.context.scene.render.image_settings
form = settings.file_format

settings.file_format = 'TIFF'

img.save_render(filepath)

settings.file_format = form
bpy.ops.wm.quit_blender()
