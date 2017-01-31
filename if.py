#!/bin/python

age = int(raw_input("Please enter your age \n"));

if age  > 18:
	print "You are adult"
elif age > 12 and age < 18:
	print "You are in teenage"
else:
	print "you  are a kid"

