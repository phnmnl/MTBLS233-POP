#!/bin/bash

#Exit immediately if a command exits with a non-zero status
set -e

echo "Creating Hadoop users..."
addgroup hadoop
adduser --disabled-password --gecos "" --ingroup hadoop hduser

echo "Disabling IPv6 (not supported by Hadoop)..."
echo "net.ipv6.conf.all.disable_ipv6 = 1" >> /etc/sysctl.conf
echo "net.ipv6.conf.default.disable_ipv6 = 1" >> /etc/sysctl.conf
echo "net.ipv6.conf.lo.disable_ipv6 = 1" >> /etc/sysctl.conf

echo "Fetching Hadoop..."
HADOOP_DOWNLOAD_URL=http://apache.mirrors.spacedump.net/hadoop/common/hadoop-2.7.2/hadoop-2.7.2.tar.gz
HADOOP_TGZ=${HADOOP_DOWNLOAD_URL##*/}
HADOOP_PACKAGE_NAME=${HADOOP_TGZ%.tar.gz}
wget -q $HADOOP_DOWNLOAD_URL -O /tmp/$HADOOP_TGZ

echo "Installing $HADOOP_PACKAGE_NAME..."
mkdir /opt/hadoop/
tar xzf /tmp/$HADOOP_TGZ -C /opt/hadoop/
ln -s /opt/hadoop/$HADOOP_PACKAGE_NAME /opt/hadoop/default
chown hduser:hadoop -R /opt/hadoop/

echo "$HADOOP_PACKAGE_NAME installation complete."
