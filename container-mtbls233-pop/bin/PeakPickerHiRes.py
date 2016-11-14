#!/usr/bin/python
import os
import sys
import subprocess
import time
import glob

#
# Currently using command line client instead of direct python bindings
#

print "Inside " + __file__

# read input vars from environment
try:
   infilename = os.environ["infile"]
   outfilename = os.environ["outfile"]
   incontainer = os.environ["swift_container_input"]
   outcontainer = os.environ["swift_container_output"]
except Exception as err: 
   print "Missing mandatory environment variable:" + format(err)
   raise

try:
   # swift local download directory
   swift_download_dir = "/swift_download"
   local_infile = os.path.join(swift_download_dir, infilename)
   
   # make sure local download directory exists (inclusive subdirs)
   local_inpath = os.path.dirname(local_infile)
   if not os.path.exists(local_inpath):
       os.makedirs(local_inpath)
   
   # different swift command depending on file or directory to download 
   if os.path.isdir(local_infile):
	   cmd_swift_download = "swift download {0} -p {1} -D {2}".format(incontainer, infilename, swift_download_dir)
   else:
       cmd_swift_download = "swift download {0} {1} --output {2}".format(incontainer, infilename, local_infile)
   
   print "Start downloading file " + local_infile + " from container " + incontainer
   starttime_download = time.time()
   stdout = subprocess.check_output(cmd_swift_download, shell=True)
   downloadtime = time.time() - starttime_download;
   print "stdout: " + stdout

   
   # if local infile is a dir then expand it to all files
   if os.path.isdir(local_infile):
      allFilesPath = os.path.join(local_infile, "*")
      allFiles = ""
      print "allFilesPath=" + allFilesPath
      for aFile in glob.glob(allFilesPath):
   	   allFiles += aFile + " "
   	   
      local_infile = allFiles
   
   # make sure local output directory exists (inclusive subdirs)
   local_outpath = os.path.dirname(outfilename)
   if not os.path.exists(local_outpath):
       os.makedirs(local_outpath)
   
   # Run the openMS command
   paramfile = "/params_MTBLS233/PPparam.ini"
   command = "PeakPickerHiRes -in {0} -out {1} -ini {2}".format(local_infile, outfilename, paramfile)
   starttime_mscommand = time.time()
   stdout = subprocess.check_output(command, shell=True)
   mscommandtime = time.time() - starttime_mscommand;
   print "stdout: " + stdout
   # end run openMS command
      
   print "Start uploading file " + outfilename
   starttime_upload = time.time()
   stdout = subprocess.check_output(["swift", "upload", outcontainer, outfilename])
   uploadtime = time.time() - starttime_upload;
   print "stdout: " + stdout
   
   print "downloadtime=" + "{0:.2f}".format(downloadtime)
   print "uploadtime=" + "{0:.2f}".format(uploadtime)
   print "mscommandtime=" + "{0:.2f}".format(mscommandtime)

except Exception as e:
   print "Errormessage:" + e.output
   raise

print "Done " + __file__


