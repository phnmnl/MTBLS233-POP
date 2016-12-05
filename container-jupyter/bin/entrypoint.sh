#!/bin/bash

# Exit on first error
set -e

# Render Swift configuration

sed -i -e "s~OS_AUTH_URL~${OS_AUTH_URL%/}~g" /opt/hadoop/default/etc/hadoop/core-site.xml
sed -i -e "s~OS_USERNAME~$OS_USERNAME~g" /opt/hadoop/default/etc/hadoop/core-site.xml
sed -i -e "s~OS_PASSWORD~$OS_PASSWORD~g" /opt/hadoop/default/etc/hadoop/core-site.xml
sed -i -e "s~OS_TENANT_NAME~$OS_TENANT_NAME~g" /opt/hadoop/default/etc/hadoop/core-site.xml
sed -i -e "s~OS_DOMAIN_ID~$OS_DOMAIN_ID~g" /opt/hadoop/default/etc/hadoop/core-site.xml

# Start notebook
start-notebook.sh --NotebookApp.password=$SHA1_PASS
