#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

if __name__ == '__main__':
	cnt =0
	
	for root, dirs, files in os.walk("."):
		if "Image.cue" in files:
			cnt+=1
			if not "cover.jpg" in files:
				print "cover not found: %s" % root
	
	print "Cuesheet Total: %d" % cnt
