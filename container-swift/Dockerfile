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
MAINTAINER Anders Larsson, anders.larsson@icm.uu.se

RUN apt-get update -y && apt-get upgrade -y && apt-get install -y libffi-dev libssl-dev python-dev python-pip
RUN pip install pyopenssl ndg-httpsclient pyasn1 python-keystoneclient python-swiftclient
