# Add swiftclient to the base ubuntu image

# Run a docker registry backed by a Swift datastore.
#
# /usr/bin/docker run --rm \
#   -e SETTINGS_FLAVOR=swift \
#   -e OS_CONTAINER=docker-registry \
#   -e OS_USERNAME=your-username \
#   -e OS_PASSWORD=your-password \
#   -e OS_AUTH_URL=https://endpoint-for-auth/v3.0/ \
#   -e OS_REGION_NAME=region-name \
#   -e OS_TENANT_NAME=your-tenant-name \
#   --name phenomenal-swift-ismyname \
#   farmbio/phenomenal-swift
#   swift upload my-swift-container myfile-in-container

FROM ubuntu:14.04
MAINTAINER anders larsson <anders.larsson@icm.uu.se>

# Install requirements for Ubuntu
RUN DEBIAN_FRONTEND=noninteractive apt-get update -y
RUN DEBIAN_FRONTEND=noninteractive apt-get upgrade -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y clang libicu-dev wget

#RUN wget -qO- http://dev.iachieved.it/iachievedit.gpg.key | sudo apt-key add -
#RUN echo "deb http://iachievedit-repos.s3.amazonaws.com/ trusty main" | tee --append /etc/apt/sources.list
#RUN export PATH="/opt/swift/swift-3.0/usr/bin:$PATH"
#RUN DEBIAN_FRONTEND=noninteractive apt-get update -y
#RUN apt-get install -y swift-3.0

# Add python swiftclient from ubuntu repos
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python-swiftclient

# Add python swiftclient - manual installation of speciffic swift-client version ubuntu 14.04
#RUN wget https://swift.org/builds/swift-3.0-release/ubuntu1404/swift-3.0-RELEASE/swift-3.0-RELEASE-ubuntu14.04.tar.gz
#RUN tar xzf swift-3.0-RELEASE-ubuntu14.04.tar.gz
#RUN mv swift-3.0-RELEASE-ubuntu14.04 swift
#ENV PATH="/swift/usr/bin/:${PATH}"

# Add python swiftclient - manual installation of speciffic swift-client version ubuntu 16.04
#RUN wget https://swift.org/builds/swift-3.0-release/ubuntu1604/swift-3.0-RELEASE/swift-3.0-RELEASE-ubuntu16.04.tar.gz
#RUN tar xzf swift-3.0-RELEASE-ubuntu16.04.tar.gz
#RUN mv swift-3.0-RELEASE-ubuntu16.04.tar.gz /usr/local/bin/swift

