#!/usr/bin/python
import os
import sys
import subprocess

#
# Currently this script is hardcoded peak-picking for swift and openstack
# in future this could be changed to more generic implementation
# Currently using command line client instead of direct python bindings
#

print "Start script"

# read input vars from environment
try:
   infilename = os.environ["infile"]
   outfilename = os.environ["outfile"]
   incontainer = os.environ["swift_container_input"]
   outcontainer = os.environ["swift_container_output"]
except Exception as err: 
   print "Missing mandatory environment variable:" + format(err)
   sys.exit(1)


print "Start downloading file " + infilename + " from container " + incontainer
stdout = subprocess.check_output(["swift", "download", incontainer, infilename])
print "stdout: " + stdout


print "Do openMS peak-picking here...:)"
# create dummy resultfile
outfile = open(outfilename, "w+")
outfile .write("A line in the resultfile")
print "Done openMS peak-picking"


print "Start uploading file " + outfile.name
stdout = subprocess.check_output(["swift", "upload", outcontainer, outfilename])
print "stdout: " + stdout


print "Done script"
