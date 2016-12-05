FROM jupyter/all-spark-notebook
MAINTAINER Marco Capuccini, marco.capuccini@farmbio.uu.se

# Install Hadoop
USER root
ADD bin/install-hadoop.sh tmp/install-hadoop.sh
RUN tmp/install-hadoop.sh && rm -Rf tmp/
ADD core-site.xml /opt/hadoop/default/etc/hadoop
RUN chown hduser:hadoop /opt/hadoop/default/etc/hadoop/core-site.xml
RUN chmod -R g+w /opt/hadoop/default/etc/hadoop
RUN usermod -a -G hadoop $NB_USER
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
ENV HADOOP_CLASSPATH=/opt/hadoop-openstack/jars/hadoop-openstack-2.7.1.jar
USER $NB_USER

# Install PIP deps
RUN pip install \
  git+https://github.com/mcapuccini/luigi.git@feature/k8s-task \
  pykube

# Add notebooks
RUN git clone https://github.com/phnmnl/MTBLS233-notebooks.git /home/jovyan/work
VOLUME /home/jovyan/work

# Set entrypoint
ADD bin/entrypoint.sh /entrypoint.sh
CMD ["/entrypoint.sh"]
