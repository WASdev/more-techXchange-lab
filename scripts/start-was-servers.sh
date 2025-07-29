#!/bin/bash

cd /home/techzone/IBM/WebSphere/AppServer/bin

echo "Starting Deployment Manager..."
./startManager.sh

echo "Starting node agents..."
./startNode.sh -profileName AppSrv01
./startNode.sh -profileName AppSrv02

echo "Starting IHS..."
cd /home/techzone/IBM/HTTPServer/bin
./apachectl start

echo "All servers have been started!"
