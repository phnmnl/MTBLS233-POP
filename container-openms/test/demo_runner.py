#!/usr/bin/python
import os
import sys
import subprocess
import glob

swift_container_input = "anders-test"
swift_container_output = "anders-test"
os_password = os.environ["OS_PASSWORD"]
os_username = os.environ["OS_USERNAME"]

try:

   # This command is example of providing all parameters as one environment variable named "envparams"
   dockerCommand1 = 'docker run -e "envparams=infile={0},outfile={1},swift_container_input={2},swift_container_output={3},OS_AUTH_URL=https://identity1.citycloud.com:5000/v3/,OS_AUTH_VERSION=3,OS_TENANT_NAME=UU_KTH_PhenoMeNal,OS_TENANT_ID=17bcdf88f1fd40de85f53b5038722681,OS_REGION_NAME=Lon1,OS_DOMAIN_ID=08ba9f88ca5647b0ad4d651698eef3d0,OS_USER_DOMAIN_ID=08ba9f88ca5647b0ad4d651698eef3d0,OS_USERNAME={4},OS_PASSWORD={5}" farmbio/mtbls233-openms /bin/OpenMS.py PeakPickerHiRes -in {{infile}} -out {{outfile}} -ini /params_MTBLS233/PPparam.ini'
   
   # first list all files in container (to be processed one by one in loop)
   swiftlist = subprocess.check_output(["swift", "list", "anders-test", "-p", "testdata"])
   for aFile in swiftlist.splitlines():
      print aFile
      inputfile = aFile
      outputfile = "/MTBLS233-POP/pp_out/" + os.path.basename(aFile)
      command = dockerCommand1.format(inputfile, outputfile, swift_container_input, swift_container_output, os_username, os_password)
      stdout = subprocess.check_output( command, shell=True )
      print "stdout: " + stdout
     
   # This command is example of providing parameters as separate environment variables
   dockerCommand2 = 'docker run -e "infile={0}" -e "outfile={1}" -e "swift_container_input={2}" -e "swift_container_output={3}" -e "OS_AUTH_URL=https://identity1.citycloud.com:5000/v3/" -e "OS_AUTH_VERSION=3" -e "OS_TENANT_NAME=UU_KTH_PhenoMeNal" -e "OS_TENANT_ID=17bcdf88f1fd40de85f53b5038722681" -e "OS_REGION_NAME=Lon1" -e "OS_DOMAIN_ID=08ba9f88ca5647b0ad4d651698eef3d0" -e "OS_USER_DOMAIN_ID=08ba9f88ca5647b0ad4d651698eef3d0" -e "OS_USERNAME={4}" -e "OS_PASSWORD={5}" farmbio/mtbls233-openms /bin/OpenMS.py FeatureFinderMetabo -in {{infile}} -out {{outfile}} -ini /params_MTBLS233/FFparam.ini'
   
   swiftlist = subprocess.check_output(["swift", "list", "anders-test", "-p", "MTBLS233-POP/pp_out/"])
   for aFile in swiftlist.splitlines():
      print aFile
      inputfile = aFile
      outputfile = "/MTBLS233-POP/ff_out/" + os.path.basename(aFile) + ".featureXML"
      command = dockerCommand2.format(inputfile, outputfile, swift_container_input, swift_container_output, os_username, os_password)
      stdout = subprocess.check_output( command, shell=True )
      print "stdout: " + stdout
   
   
   dockerCommand3 = 'docker run -e "infile={0}" -e "outfile={1}" -e "swift_container_input={2}" -e "swift_container_output={3}" -e "OS_AUTH_URL=https://identity1.citycloud.com:5000/v3/" -e "OS_AUTH_VERSION=3" -e "OS_TENANT_NAME=UU_KTH_PhenoMeNal" -e "OS_TENANT_ID=17bcdf88f1fd40de85f53b5038722681" -e "OS_REGION_NAME=Lon1" -e "OS_DOMAIN_ID=08ba9f88ca5647b0ad4d651698eef3d0" -e "OS_USER_DOMAIN_ID=08ba9f88ca5647b0ad4d651698eef3d0" -e "OS_USERNAME={4}" -e "OS_PASSWORD={5}" farmbio/mtbls233-openms /bin/OpenMS.py FeatureLinkerUnlabeledQT -in {{infile}} -out {{outfile}} -ini /params_MTBLS233/FLparam.ini'
      
   inputfile = "MTBLS233-POP/ff_out/"
   outputfile = "/MTBLS233-POP/fl_out/" + "MTBLS233-POP.consensusXML"
   command = dockerCommand3.format(inputfile, outputfile, swift_container_input, swift_container_output, os_username, os_password)
   stdout = subprocess.check_output( command, shell=True )
   print "stdout: " + stdout
   
   
   dockerCommand4 = 'docker run -e "infile={0}" -e "outfile={1}" -e "swift_container_input={2}" -e "swift_container_output={3}" -e "OS_AUTH_URL=https://identity1.citycloud.com:5000/v3/" -e "OS_AUTH_VERSION=3" -e "OS_TENANT_NAME=UU_KTH_PhenoMeNal" -e "OS_TENANT_ID=17bcdf88f1fd40de85f53b5038722681" -e "OS_REGION_NAME=Lon1" -e "OS_DOMAIN_ID=08ba9f88ca5647b0ad4d651698eef3d0" -e "OS_USER_DOMAIN_ID=08ba9f88ca5647b0ad4d651698eef3d0" -e "OS_USERNAME={4}" -e "OS_PASSWORD={5}" farmbio/mtbls233-openms /bin/OpenMS.py FileFilter -in {{infile}} -out {{outfile}} -ini /params_MTBLS233/FileFparam.ini'
   
   swiftlist = subprocess.check_output(["swift", "list", "anders-test", "-p", "MTBLS233-POP/fl_out/"])
   for aFile in swiftlist.splitlines():
      print aFile
      inputfile = aFile
      outputfile = "/MTBLS233-POP/filef_out/" + "MTBLS233-POP.consensusXML"
      command = dockerCommand4.format(inputfile, outputfile, swift_container_input, swift_container_output, os_username, os_password)
      stdout = subprocess.check_output( command, shell=True )
      print "stdout: " + stdout
   
   
   dockerCommand5 = 'docker run -e "infile={0}" -e "outfile={1}" -e "swift_container_input={2}" -e "swift_container_output={3}" -e "OS_AUTH_URL=https://identity1.citycloud.com:5000/v3/" -e "OS_AUTH_VERSION=3" -e "OS_TENANT_NAME=UU_KTH_PhenoMeNal" -e "OS_TENANT_ID=17bcdf88f1fd40de85f53b5038722681" -e "OS_REGION_NAME=Lon1" -e "OS_DOMAIN_ID=08ba9f88ca5647b0ad4d651698eef3d0" -e "OS_USER_DOMAIN_ID=08ba9f88ca5647b0ad4d651698eef3d0" -e "OS_USERNAME={4}" -e "OS_PASSWORD={5}" farmbio/mtbls233-openms /bin/OpenMS.py TextExporter -in {{infile}} -out {{outfile}} -ini /params_MTBLS233/TEparam.ini'
   
   swiftlist = subprocess.check_output(["swift", "list", "anders-test", "-p", "MTBLS233-POP/filef_out/"])
   for aFile in swiftlist.splitlines():
      print aFile
      inputfile = aFile
      outputfile = "/MTBLS233-POP/te_out/" + "Result.csv"
      command = dockerCommand5.format(inputfile, outputfile, swift_container_input, swift_container_output, os_username, os_password)
      stdout = subprocess.check_output( command, shell=True )
      print "stdout: " + stdout

except Exception as err:
   print "Exception formated:" + format(err)
	
      
