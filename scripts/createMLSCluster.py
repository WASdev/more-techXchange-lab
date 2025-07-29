# Create MLS Cluster
print "***Creating cluster MLSCluster***"
AdminTask.createCluster(['-clusterConfig', ['-clusterName', 'MLSCluster', '-clusterType', 'MANAGED_LIBERTY_SERVER']])
print "***Creating createClusterMember for node1***"
AdminTask.createClusterMember(['-clusterName', 'MLSCluster', '-memberConfig', ['-memberNode', 'node1', '-memberName', 'libertyServer']])
print "***Creating createClusterMember for node2***"
AdminTask.createClusterMember(['-clusterName', 'MLSCluster', '-memberConfig', ['-memberNode', 'node2', '-memberName', 'libertyServer']])
AdminConfig.save()

print "***Syncing nodes***"
AdminNodeManagement.syncActiveNodes()

# Start the MLS Cluster
print "***Starting the cluster MLSCluster***"
cluster = AdminControl.queryNames('WebSphere:*,type=Cluster,name=MLSCluster')
AdminControl.invoke(cluster, 'start')
print "!!!Successfully started the cluster!!!"
