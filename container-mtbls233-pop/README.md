## OpenMS - Swift container - peak-picking example

This container adds script folder ``bin/``  that demonstrates downloading and uploading with Swift obectstorage and executing openMS commands

This container also adds OpenMS parameters for analysis MTBLS233 in directory ``/params_MTBLS233``
  
The container builds on container: ``farmbio/phenomenal-openms-swift``

### Build container 
```bash
docker build -t farmbio/phenomenal-mtbls233-pop .
```

### Run container 

```bash
docker run --rm -e "infile=testfile.txt" -e "outfile=result.txt" -e "swift_container_input=anders-test" -e "swift_container_output=anders-test" -e "OS_AUTH_URL=https://identity1.citycloud.com:5000/v3/" -e "OS_AUTH_VERSION=3" -e "OS_TENANT_NAME=your-tenant-name" -e "OS_TENANT_ID=17bcdf88f1fd40de85f53b5038722681" -e "OS_REGION_NAME=Lon1" -e "OS_DOMAIN_ID=08ba9f88ca5647b0ad4d651698eef3d0" -e "OS_USER_DOMAIN_ID=08ba9f88ca5647b0ad4d651698eef3d0" -e "OS_USERNAME=your-username" -e "OS_PASSWORD=your-password" bin/PeakPickerHiRes.py
```

### Run interactive for testing
```bash
docker run -it farmbio/phenomenal-mtbls233-pop /bin/bash
