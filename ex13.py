# -*- coding : utf-8 -*-
from sys import argv
from os.path import exists

file_nm=''
if len(argv) == 2:
	file_nm = argv[1]
else:
	file_nm = raw_input("Enter a file name to write: ")

out_file = open(file_nm , 'w')

if len(out_file): #exists(file_nm)
	print "Emptying the file"
	out_file.truncate()

out_file.write(raw_input("Line 1: "))
out_file.write('\n')
out_file.write(raw_input("Line 2: "))
out_file.write('\n')
out_file.write(raw_input("Line 3: "))

print "Now closing the file"
out_file.close()