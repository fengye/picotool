#!/usr/bin/env python3

import argparse
import os

from pico8.tool import build

if __name__ == "__main__":
	parser = argparse.ArgumentParser("PICO-8 build script.")
	parser.add_argument('-s', '--source', dest='source', nargs='+', help="Lua source files", required=True)
	parser.add_argument('-r', '--resource', dest='resource', help="PICO-8 resource .p8 file", required=True)
	parser.add_argument('-o', '--output', dest='output', help="Output cartridge file", required=True)
	args = parser.parse_args()
	print("Source files: " + ', '.join(args.source))
	print("Resource file: " + args.resource)
	print("Output cartridge: " + args.output)

	temp_filename = "__build_source.lua"
	print("Creating temp file: " + temp_filename)
	build_source = ""
	for filename in args.source:
		with open(filename, 'r') as f:
			build_source = build_source + f.read() + '\n'

	with open(temp_filename, 'w') as f:
		f.write(build_source)

	class BuildArgs:
		def __init__(self, filename, lua, gfx):
			self.filename = filename
			self.lua = lua
			self.gfx = gfx

	build_args = BuildArgs(args.output, temp_filename, args.resource)
	build.do_build(build_args)
	
	print("Remove temp file: " + temp_filename)
	os.remove(temp_filename)

	print("Finished creating: " + args.output)