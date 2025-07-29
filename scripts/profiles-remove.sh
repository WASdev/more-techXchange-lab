#!/bin/bash

/home/techzone/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/wsadmin.sh \
  -lang jython -user techzone -password IBMDem0s! \
  -f /home/techzone/Student/tx-more-lab/scripts/deleteMLSCluster.py

echo "Stopping IHS..."
cd /home/techzone/IBM/HTTPServer/bin
./adminctl stop

cd /home/techzone/IBM/WebSphere/AppServer/bin

echo "Stopping all node agents..."
./stopNode.sh -profileName AppSrv01 -username techzone -password IBMDem0s!
./stopNode.sh -profileName AppSrv02 -username techzone -password IBMDem0s!

echo "Stopping Deployment Manager..."
./stopManager.sh -username techzone -password IBMDem0s!

echo "Removing all profiles..."
./manageprofiles.sh -deleteAll
rm -rf ../profiles/AppSrv01
rm -rf ../profiles/AppSrv02
rm -rf ../profiles/Dmgr01

echo "Cleanup complete."
