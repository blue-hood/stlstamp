#!/usr/bin/python
# coding: utf-8
import numpy as np
import pickle
import bpy
from mathutils import Vector
import sys

filename = sys.argv[4]
bar = int(sys.argv[5])
depth = 3

bpy.ops.object.delete()
bpy.context.scene.unit_settings.system = 'METRIC';
bpy.context.scene.unit_settings.scale_length = 0.5;
with open(filename, 'rb') as f:
	img = pickle.load(f, encoding='latin-1');
print(img);
for y in range(img.shape[0]):
	for x in range(img.shape[1]):
		if (x%2==0)&(y%2==0):
		#if 1:
			if img.shape[2] == 4: # use a channel
				if (img[y][x][3] == 0)|(img[y][x][0] == 255): # trans, white
					obj = bpy.ops.mesh.primitive_cube_add(location=(x, y, bar))
					bpy.ops.transform.resize(value=(1.0, 1.0, bar))
				else: # black
					obj = bpy.ops.mesh.primitive_cube_add(location=(x, y, depth + bar))
					bpy.ops.transform.resize(value=(1.0, 1.0, depth + bar))
			else:
				if img[y][x][0] == 255: # white
					obj = bpy.ops.mesh.primitive_cube_add(location=(x, y, bar))
					bpy.ops.transform.resize(value=(1.0, 1.0, bar))
				else: # black
					obj = bpy.ops.mesh.primitive_cube_add(location=(x, y, depth + bar))
					bpy.ops.transform.resize(value=(1.0, 1.0, depth + bar))

scene = bpy.context.scene
obs = []
for ob in scene.objects:
	obs.append(ob)
ctx = bpy.context.copy()
# one of the objects to join
ctx['active_object'] = obs[0]
ctx['selected_objects'] = obs
# we need the scene bases as well for joining
ctx['selected_editable_bases'] = [scene.object_bases[ob.name] for ob in obs]
bpy.ops.object.join(ctx)

bpy.ops.export_mesh.stl(filepath = filename, ascii = False, use_scene_unit = True)
