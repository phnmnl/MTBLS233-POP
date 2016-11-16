## OpenMS - Swift container - MTBLS233

This container adds script folder ``bin/``  that demonstrates downloading and uploading with Swift obect storage and executing openMS commands

OpenMS.py is handling the down and uploading of files from Swift object storage. OpenMS.py is also running the openMS command specified as argument, and replacing the tags {infile} {outfile} with the local files checked out by the from swift storage. The files to be downloaded and uploaded with swift are specified as environment variables, ``-e "infile=testfile.txt" -e "outfile=result.txt" -e "swift_container_input=anders-test" -e "swift_container_output=anders-test"``

This container also adds OpenMS parameters for analysis MTBLS233 in directory ``/params_MTBLS233``
  
The container builds on container: ``farmbio/phenomenal-openms-swift``

### Build container 
```bash
docker build -t farmbio/phenomenal-mtbls233-pop .
```

### Run container 

PeakPickerHiRes
```bash
docker run --rm -e "infile=testfile.txt" -e "outfile=result.txt" -e "swift_container_input=anders-test" -e "swift_container_output=anders-test" -e "OS_AUTH_URL=https://identity1.citycloud.com:5000/v3/" -e "OS_AUTH_VERSION=3" -e "OS_TENANT_NAME=your-tenant-name" -e "OS_TENANT_ID=17bcdf88f1fd40de85f53b5038722681" -e "OS_REGION_NAME=Lon1" -e "OS_DOMAIN_ID=08ba9f88ca5647b0ad4d651698eef3d0" -e "OS_USER_DOMAIN_ID=08ba9f88ca5647b0ad4d651698eef3d0" -e "OS_USERNAME=your-username" -e "OS_PASSWORD=your-password" farmbio/phenomenal-mtbls233-pop /bin/OpenMS.py PeakPickerHiRes -in {infile} -out {outfile} -ini /params_MTBLS233/PPparam.ini
```

FeatureFinderMetabo
```bash
docker run --rm -e "infile=testfile.txt" -e "outfile=result.txt" -e "swift_container_input=anders-test" -e "swift_container_output=anders-test" -e "OS_AUTH_URL=https://identity1.citycloud.com:5000/v3/" -e "OS_AUTH_VERSION=3" -e "OS_TENANT_NAME=your-tenant-name" -e "OS_TENANT_ID=17bcdf88f1fd40de85f53b5038722681" -e "OS_REGION_NAME=Lon1" -e "OS_DOMAIN_ID=08ba9f88ca5647b0ad4d651698eef3d0" -e "OS_USER_DOMAIN_ID=08ba9f88ca5647b0ad4d651698eef3d0" -e "OS_USERNAME=your-username" -e "OS_PASSWORD=your-password" farmbio/phenomenal-mtbls233-pop /bin/OpenMS.py FeatureFinderMetabo -in {infile} -out {outfile} -ini /params_MTBLS233/FFparam.ini
```

FeatureLinkerUnlabeledQT
```bash
docker run --rm -e "infile=testfile.txt" -e "outfile=result.txt" -e "swift_container_input=anders-test" -e "swift_container_output=anders-test" -e "OS_AUTH_URL=https://identity1.citycloud.com:5000/v3/" -e "OS_AUTH_VERSION=3" -e "OS_TENANT_NAME=your-tenant-name" -e "OS_TENANT_ID=17bcdf88f1fd40de85f53b5038722681" -e "OS_REGION_NAME=Lon1" -e "OS_DOMAIN_ID=08ba9f88ca5647b0ad4d651698eef3d0" -e "OS_USER_DOMAIN_ID=08ba9f88ca5647b0ad4d651698eef3d0" -e "OS_USERNAME=your-username" -e "OS_PASSWORD=your-password" farmbio/phenomenal-mtbls233-pop /bin/OpenMS.py FeatureLinkerUnlabeledQT -in {infile} -out {outfile} -ini /params_MTBLS233/FLparam.ini
```

FileFinder
```bash
docker run --rm -e "infile=testfile.txt" -e "outfile=result.txt" -e "swift_container_input=anders-test" -e "swift_container_output=anders-test" -e "OS_AUTH_URL=https://identity1.citycloud.com:5000/v3/" -e "OS_AUTH_VERSION=3" -e "OS_TENANT_NAME=your-tenant-name" -e "OS_TENANT_ID=17bcdf88f1fd40de85f53b5038722681" -e "OS_REGION_NAME=Lon1" -e "OS_DOMAIN_ID=08ba9f88ca5647b0ad4d651698eef3d0" -e "OS_USER_DOMAIN_ID=08ba9f88ca5647b0ad4d651698eef3d0" -e "OS_USERNAME=your-username" -e "OS_PASSWORD=your-password" farmbio/phenomenal-mtbls233-pop /bin/OpenMS.py FileFinder -in {infile} -out {outfile} -ini /params_MTBLS233/FileFparam.ini
```

TextExporter
```bash
docker run --rm -e "infile=testfile.txt" -e "outfile=result.txt" -e "swift_container_input=anders-test" -e "swift_container_output=anders-test" -e "OS_AUTH_URL=https://identity1.citycloud.com:5000/v3/" -e "OS_AUTH_VERSION=3" -e "OS_TENANT_NAME=your-tenant-name" -e "OS_TENANT_ID=17bcdf88f1fd40de85f53b5038722681" -e "OS_REGION_NAME=Lon1" -e "OS_DOMAIN_ID=08ba9f88ca5647b0ad4d651698eef3d0" -e "OS_USER_DOMAIN_ID=08ba9f88ca5647b0ad4d651698eef3d0" -e "OS_USERNAME=your-username" -e "OS_PASSWORD=your-password" farmbio/phenomenal-mtbls233-pop /bin/OpenMS.py TextExporter -in {infile} -out {outfile} -ini /params_MTBLS233/TEparam.ini
```

### Run interactive for testing
```bash
docker run -it farmbio/phenomenal-mtbls233-pop /bin/bash
