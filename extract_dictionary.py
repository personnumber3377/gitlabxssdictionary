#!/bin/python3

# the_stuff_1.txt
import re

def s():
	# Now do the stuff here...
	fh = open("the_stuff_2.txt", "r")
	data = fh.read()
	fh.close()
	# Now do the shit...
	
	# matches = re.findall(r'"(.*?)"', data) # Extract the stuff from the thing...
	# for s in matches:
	# 	print(f'"{s}"')

	matches = re.findall(r'\'(.*?)\'', data) # Extract the stuff from the thing...
	matches = list(set(matches))
	for s in matches:
		print(f'"{s}"')

	return

if __name__=="__main__":
	s()
	exit(0)

