# -*- coding: utf-8 -*-

u = """
I want to type a paragraph here %r
where I could see what I am typing.

For this I am gonna pay you some money %c %d
""" % ('"Prashoor"' , unichr(0x20B9) , 2000)

print u.encode('utf-8')


print "Now here goes the code",

print "How old are you?"
age = raw_input("AGE?")
print "How much do you weight?"
weight = raw_input("Your Real Weight")

print """
So you are %r years old, with %r weight
""" % ( age , weight )
