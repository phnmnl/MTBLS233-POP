FROM ubuntu:14.04
MAINTAINER Marco Capuccini, marco.capuccini@farmbio.uu.se

# Install apt deps
RUN apt-get update && apt-get install --yes \
  openms \
  openjdk-7-jre-headless \
  wget

# Install Hadoop
ADD bin/install-hadoop.sh tmp/install-hadoop.sh
RUN tmp/install-hadoop.sh && rm tmp/install-hadoop.sh

# Set evnironment
ENV HADOOP_HOME=/opt/hadoop/default
ENV PATH=$PATH:$HADOOP_HOME/bin
ENV PATH=$PATH:$HADOOP_HOME/sbin
ENV HADOOP_MAPRED_HOME=$HADOOP_HOME
ENV HADOOP_COMMON_HOME=$HADOOP_HOME
ENV HADOOP_HDFS_HOME=$HADOOP_HOME
ENV YARN_HOME=$HADOOP_HOME
ENV HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
ENV HADOOP_OPTS=-Djava.library.path=$HADOOP_HOME/lib
ENV JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64

# Add MTBLS233 parameters and scripts
ADD params_MTBLS233 /params_MTBLS233
