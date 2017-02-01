#!/usr/local/bin/python
"""
  For loop
  while loop
"""
#for i in range(start,end,increment no)
for i in range(1,10,2):
   print i
   print "name"

for i in range(10,1,-1):
	print i
	print "name"


list=["a","b","c","d","e"]
i=0
listlength = len(list);

for i in range(listlength):
	print list[i]

i=0
while i <= 10:
	print "while loop example",i
	i =i +1
i=0
while i < (listlength):
   print list[i]
   i = i+1 
