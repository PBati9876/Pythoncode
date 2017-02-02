#!/bin/python
"""
  Linux command in python
"""
import os
import commands
import subprocess

os.system("touch testfile")
os.system('echo "This is the content" >> testfile')
os.system('cat testfile')
files = os.popen("ls").read()

#subprocess = subprocess.check_output("ls")
#print subprocess

commands = commands.getoutput("ls")
print commands

#print files
