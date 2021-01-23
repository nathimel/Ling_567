import copy

path = "C:/Users/mypet/Documents/School/UW/Sr Qrt 2/LING 567/Ling_567/Lab3/lab_3_testsuite/lab_3_suite.txt"

file = open(path, 'r')
lines = file.readlines()

lines_copy = copy.deepcopy(lines)

counter = 0 # number of renumbered examples
example_counter = 0 # number of examples
line_counter = 0 # number of lines
for line in lines: # for each line
	if line[0:4] == "# XX":
		counter += 1
		lines_copy[line_counter] = "# " + str(example_counter) + line[4:]
	if line[0] == "#":
		example_counter += 1
	line_counter += 1
print(str(example_counter) + " examples found.")
print(str(counter) + " examples renumbered.")

with open("C:/Users/mypet/Documents/School/UW/Sr Qrt 2/LING 567/Ling_567/Lab3/lab_3_testsuite/lab_3_suite_processed.txt", 'w') as out_file:
	out_file.writelines(lines_copy)
	