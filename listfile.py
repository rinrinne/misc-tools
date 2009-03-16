#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, os.path, re
import optparse

VERSION = '1.0'

if __name__ == '__main__':
	parser = optparse.OptionParser(
		usage="%prog [options] <directory> [<directory> ...]\n"
		"List files under specified directory.",
		version="%s" % VERSION
		)
	parser.add_option(
		"-e", "--excludefile",
		action="store", type="string", dest="exclude",
		default=None,
		help="Specify file written exclude files. The default value for this option is '%default'."
		)
	parser.add_option(
		"-a", "--absdisp",
		action="store_true", dest="abstruct",
		default=False,
		help="When this option specified, output file with abspath. The default value for this option is '%default'."
		)
	parser.add_option(
		"-p", "--pattern",
		action="store", type="string", dest="pattern",
		default="\.cue$",
		help="Specify pattern for filename. pattern is regexp. The default value for this option is '%default'."
		)
	
	
	# Parse command-line arguments.
	(options, args) = parser.parse_args()
	
	# file check
	if(options.exclude is not None and not os.path.isfile(options.exclude)):
		sys.stderr.write("exclude file not found.")
		sys.exit(1)
	
	flist = []
	
	for arg in args:
		for current, dirs, files in os.walk(arg):
			for file in files:
				if re.search(options.pattern, file) is not None:
					path = ""
					if options.abstruct:
						path = os.path.join(os.path.abspath(current), file)
					else:
						path = os.path.join(current, file)
					flist.append(path)
	
	excludes = []
	
	if options.exclude is not None:
		f = open(options.exclude, 'r')
		for line in f:
			line = line.rstrip()
			if line.startswith("#"):
				continue
			if options.abstruct:
				excludes.append(os.path.abspath(line))
			else:
				excludes.append(line)
		f.close()
	
	set_file = set(flist)
	set_file.difference_update(set(excludes))
	
	for file in set_file:
		print file
	
