#!/bin/python
"""
   case statement in python

"""

def checknum(val):
	try:
	        if 5/val > 0:
		    print  "invalid division"
	except Exception:
		print "Number cannot be divided by zero"
	finally:
	  	val = int(raw_input("Enter the postive number"))
		if 5/val > 0:
			print "Number was divisible"



checknum(0)
