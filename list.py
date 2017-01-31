#!/bin/python
"""
  Example of  list
"""
bill = 5;
name = "bikram"

list = [ "a","b",1,2]
print "size of the list is ",len(list)
print list

print list[0]
print list[1]
print list[2]
print list[3]

del list[0]

print list[0]

list[2]="d"

list.append("c")

print list
