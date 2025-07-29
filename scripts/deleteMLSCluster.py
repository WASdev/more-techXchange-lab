print "***Stopping MLSCluster***"
cluster = AdminControl.queryNames('WebSphere:*,type=Cluster,name=MLSCluster')
if cluster:
    AdminControl.invoke(cluster, 'stop')
    print "Cluster stopped successfully"
else:
    print "Cluster not found or already stopped"

print "***Deleting MLSCluster***"
AdminTask.deleteCluster(['-clusterName', 'MLSCluster'])
AdminConfig.save()
print "!!!Cluster MLSCluster deleted!!!"