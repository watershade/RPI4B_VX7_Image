# web_server.py - simple python web server
#
# Copyright (c) 2020-2021 Wind River Systems, Inc.
#
# The right to copy, distribute, modify or otherwise make use
# of this software may be licensed only pursuant to the terms
# of an applicable Wind River license agreement.
#
#
# DESCRIPTION
# This is an example of a python based web server to be run as a container.
# Creation of the container is enabled using CONTAINER_PYTHON_WEB_SERVER VSB
# configuration option, and requires the PYTHON layer (in addition to the
# container runtime layer). For example:
#
#  % vxprj vsb layer add PYTHON
#  % vxprj vsb config -s -add _WRS_CONFIG_CONTAINER_PYTHON_WEB_SERVER=y
#
# Note that Buildah container tool must to be installed on the build machine
# and added to the PATH environment.
#
# When the VSB is successfully built, the container is created in the VSB,
# as <VSB_DIR>/usr/containers/web_server/web_server.oci. Note that there is also a
# <VSB_DIR>/usr/containers/web_server/rootfs directory, provided for reference.
# The content of web_server.oci can be transferred to a target (e.g. in romfs)
# and used to run the container.
#
# Upon succesful execution, indicated by the "Starting server using port 8888"
# message on the target console, a web browser can connect using the
# <ip address>:8888 URL. This allows browsing the private IOS namespace
# of the container (directories and files visible by the container).
#

import os
import socketserver
from http.server import SimpleHTTPRequestHandler

PORTNO = 8888

os.chdir('/www')

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORTNO), SimpleHTTPRequestHandler) as server:
    print("Starting server using port", PORTNO)
    server.serve_forever()
