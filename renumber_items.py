# This program will re-number examples entries in a test suite in text
#   format (before being processed by make_item)
# All lines that start with "# XX" where X is a digit have the "XX" replaced with the number of "# XX"'s encountered so far. 

import sys, copy

# if the wrong number of arguments were supplied
if len(sys.argv) < 2:
	print("Usage: renumber_items.py <input_file> <ouuput_file>")
	print("   input_file  : name of the file to renumber")
	print("   ouuput_file : name of the file to output to")
	sys.exit()

# the two program arguments
in_path = sys.argv[1]
out_path = sys.argv[2]

# open the input file and read its lines
file = open(in_path, 'r')
lines = file.readlines()

# make a copy of the input file
# (so we don't edit a table while iterating over it
lines_copy = copy.deepcopy(lines)

# some variables for the loop
line_counter = 0 # number of lines
example_counter = 0 # number of examples sentences

# for each line
for line in lines:
	for i in range(3,7): # check for "# X:", "# XX:", "# XXX:", etc.
		if line[0] == "#" and line[i]==":": # re-number this example
			example_counter += 1
			print(example_counter)
			lines_copy[line_counter] = "# " + str(example_counter) + line[i:]
	line_counter += 1 # track the lines so far

# print some useful info
print(str(example_counter) + " examples found and renumbered.")

# write to the output file
with open(out_path, 'w') as out_file:
	out_file.writelines(lines_copy)