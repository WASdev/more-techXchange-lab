#!/bin/bash

#
# Install the application and any prerequisites
# Ensure password-less ssh to the demo data server is setup before running this script. (run ssh-copy-id -i ~/.ssh/id_rsa.pub username@server.dreamhost.com)
#

#
# ARGS:
#
# The remote server to deploy to
remote_server=$1
user=$2
password=$3

#
# MAIN ENTRY
#

# Create dir on remote server for artifacts
ssh -o StrictHostKeyChecking=no root@${remote_server} "rm -rf /root/appinstall/modresorts; mkdir -p /root/appinstall/modresorts;"

# Copy artifacts to remote server
scp modresorts-2.0.0.war root@${remote_server}:/root/appinstall/modresorts
scp was-datasource-create.py root@${remote_server}:/root/appinstall/modresorts
scp was-deploy.py root@${remote_server}:/root/appinstall/modresorts

creds=""
if [[ -n $user ]]; then
  creds=" -user $user -password $password "
fi

# Install the app using wsadmin over ssh
ssh -o StrictHostKeyChecking=no root@${remote_server} > install.log << EOF

  cd /root/appinstall/modresorts

  /opt/IBM/WebSphere/AppServer/bin/wsadmin.sh $creds -f was-datasource-create.py

  /opt/IBM/WebSphere/AppServer/bin/wsadmin.sh $creds -f was-deploy.py

EOF

cat install.log
