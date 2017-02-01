#!/bin/python
"""
   Example of function
"""

def functionexample(val):
	print val


functionexample(5)
functionexample(6)
functionexample(7)


def checkage(val):
	if val > 18:
		return "adult"
	elif val >12 and val < 18:
		return "tenage"
	else:
		return "child"


print checkage(5)
print checkage(14)
print checkage(20)
inputage = int(raw_input("Please enter your age \n"));

print "you are", checkage(inputage)
