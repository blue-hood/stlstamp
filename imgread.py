#!/usr/bin/python
# coding: utf-8
import cv2
import sys
import pickle

filename = sys.argv[1]
img = cv2.imread(filename, -1)
with open(filename, 'wb') as f:
	print(img);
	pickle.dump(img, f)
