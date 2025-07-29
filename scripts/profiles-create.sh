#!/bin/bash

cd /home/techzone/IBM/WebSphere/AppServer/bin

echo "Creating Deployment Manager Profile..."

./manageprofiles.sh -create -profileName Dmgr01 -profilePath /home/techzone/IBM/WebSphere/AppServer/profiles/Dmgr01 -templatePath /home/techzone/IBM/WebSphere/AppServer/profileTemplates/management -serverType DEPLOYMENT_MANAGER -enableAdminSecurity true -adminUserName techzone -adminPassword IBMDem0s! -nodeName CellManager -cellName MoREDemoCell

echo "Starting Deployment Manager"

./startServer.sh dmgr

echo "Creating the First Node"

./manageprofiles.sh -create -profileName AppSrv01 -profilePath /home/techzone/IBM/WebSphere/AppServer/profiles/AppSrv01 -templatePath /home/techzone/IBM/WebSphere/AppServer/profileTemplates/managed -nodeName node1 -dmgrAdminUserName techzone -dmgrAdminPassword IBMDem0s! -dmgrHost $HOSTNAME -dmgrPort 8879

echo "Creating the Second Node"

./manageprofiles.sh -create -profileName AppSrv02 -profilePath /home/techzone/IBM/WebSphere/AppServer/profiles/AppSrv02 -templatePath /home/techzone/IBM/WebSphere/AppServer/profileTemplates/managed -nodeName node2 -dmgrAdminUserName techzone -dmgrAdminPassword IBMDem0s! -dmgrHost $HOSTNAME -dmgrPort 8879