#!/usr/bin/python
# coding: utf-8
import cv2
import numpy as np
import pickle
import bpy
from mathutils import Vector

bar = 2.2
depth = 0.2

bpy.ops.object.delete()
img = cv2.imread('test.png', -1)
for y in range(img.shape[0]):
	for x in range(img.shape[1]):
		if (x%2==0)&(y%2==0):
			if (img[y][x][3] == 0)|(img[y][x][0] == 255): # trans, white
				obj = bpy.ops.mesh.primitive_cube_add(location=(x*0.1, y*0.1, bar))
				bpy.ops.transform.resize(value=(0.1, 0.1, bar))
			else: # black
				obj = bpy.ops.mesh.primitive_cube_add(location=(x*0.1, y*0.1, depth + bar))
				bpy.ops.transform.resize(value=(0.1, 0.1, depth + bar))

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

bpy.ops.export_mesh.stl(filepath = 'stamp.stl')
