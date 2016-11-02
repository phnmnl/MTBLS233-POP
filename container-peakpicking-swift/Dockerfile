# Add swiftclient to the base ubuntu image

# Run a docker registry backed by a Swift datastore.
#
# /usr/bin/docker run --rm \
#   -e infile=/name/of/infile/in/swift \
#   -e outfile=/name/of/outfile/in/swift \
#   -e swift_container_input=name-here \
#   -e swift_container_output=name-here \
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

FROM farmbio/phenomenal-swift
MAINTAINER anders larsson <anders.larsson@icm.uu.se>

COPY phenomenal /phenomenal

ENTRYPOINT ["/phenomenal/peak-picking.py"] 

