#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

if __name__ == '__main__':
	for root, dirs, files in os.walk("."):
		if "Image.cue" in files:
			if not "cover.jpg" in files:
				print "cover not found: %s" % root
