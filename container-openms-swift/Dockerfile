FROM ubuntu:14.04
MAINTAINER Anders Larsson, anders.larsson@icm.uu.se

# Install OpenMS & Swift-requirements
RUN apt-get update -y && apt-get upgrade -y && apt-get install -y openms libffi-dev libssl-dev python-dev python-pip

#Swift-pythonclient
RUN pip install pyopenssl ndg-httpsclient pyasn1 python-keystoneclient python-swiftclient
