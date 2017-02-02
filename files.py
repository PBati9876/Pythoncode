#!/bin/python
"""
   Program to read and write to the text file
   a = append
   w = write
   r = read
   wr = read,write
"""

out = open("filename.txt","w")
out.write("hello world\n")
out.write("I am Bikram\n")
out.write("I am pawan\n")
out.write("This is linux\n")
out.close()


read = open("filename.txt","r")

line = read.readline();
while line:
	print line,
	line = read.readline()
	

#print read.readline();
#print read.readline();

out = open("filename.txt","a")
out.write("This is python")
out.close()

#readwrite = open("filename.txt","rw")

