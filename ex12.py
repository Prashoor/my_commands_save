from sys import argv
file_nm=''

if len(argv) == 2:
	file_nm = argv[1]
else:
	print "Format : 'python ex12.py <filename>'"
	exit(0)
print 'Opening file %r' % file_nm
text_fl = open( file_nm )

print text_fl.read()
