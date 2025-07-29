#!/bin/bash

echo "Uninstalling application modresorts..."
/home/techzone/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/wsadmin.sh \
  -lang jython -user techzone -password IBMDem0s! \
  -c "AdminApp.uninstall('modresorts-2_0_0_war'); AdminConfig.save()"

echo "Uninstalling applications spring-petclinic..."
/home/techzone/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/wsadmin.sh \
  -lang jython -user techzone -password IBMDem0s! \
  -c "AdminApp.uninstall('spring-petclinic-3_4_0-SNAPSHOT_war'); AdminConfig.save()"

/home/techzone/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/wsadmin.sh \
  -lang jython -user techzone -password IBMDem0s! \
  -f /home/techzone/Student/tx-more-lab/scripts/deleteMLSCluster.py

echo "Stopping IHS..."
cd /home/techzone/IBM/HTTPServer/bin
./apachectl stop

cd /home/techzone/IBM/WebSphere/AppServer/bin

echo "Stopping node agents..."
./stopNode.sh -profileName AppSrv01 -username techzone -password IBMDem0s!
./stopNode.sh -profileName AppSrv02 -username techzone -password IBMDem0s!

echo "Stopping Deployment Manager..."
./stopManager.sh -username techzone -password IBMDem0s!

echo "All servers have been stopped!"
