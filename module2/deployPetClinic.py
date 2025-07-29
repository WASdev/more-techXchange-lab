USERHOME = "/home/techzone"
DEMOPATH = USERHOME + "/Student/tx-more-lab"
DMGRCONFIGPATH = USERHOME + "/IBM/WebSphere/AppServer/profiles/Dmgr01/config"

# Install Application PetClinic
print "***Now installing Application PetClinic***"
AdminApp.install(
    DEMOPATH + "/module2/spring-petclinic/target/spring-petclinic-3.5.0-SNAPSHOT.war",
    "[ -distributeApp -useMetaDataFromBinary -appname spring-petclinic-3_4_0-SNAPSHOT_war -validateinstall warn "
    "-noallowDispatchRemoteInclude -noallowServiceRemoteInclude -novalidateSchema -contextroot /spring-petclinic "
    "-MapModulesToServers [[ spring-petclinic-3.5.0-SNAPSHOT.war spring-petclinic-3.5.0-SNAPSHOT.war,WEB-INF/web.xml "
    "WebSphere:cell=MoREDemoCell,cluster=MLSCluster+WebSphere:cell=MoREDemoCell,node=node2,server=webserver1 ]] "
    "-MapWebModToVH [[ spring-petclinic-3.5.0-SNAPSHOT.war spring-petclinic-3.5.0-SNAPSHOT.war,WEB-INF/web.xml default_host ]]"
)
AdminConfig.save()

# Generate and Propogate Plugin
print "***Generating Plugin for PetClinic***"
AdminControl.invoke(
    'WebSphere:name=PluginCfgGenerator,process=dmgr,platform=common,node=CellManager,version=9.0.5.24,type=PluginCfgGenerator,mbeanIdentifier=PluginCfgGenerator,cell=MoREDemoCell,spec=1.0',
    'generate',
    [DMGRCONFIGPATH, "MoREDemoCell", "node2", "webserver1", "false"]
)

print "***Propogating Plugin for PetClinic***"
AdminControl.invoke(
    'WebSphere:name=PluginCfgGenerator,process=dmgr,platform=common,node=CellManager,version=9.0.5.24,type=PluginCfgGenerator,mbeanIdentifier=PluginCfgGenerator,cell=MoREDemoCell,spec=1.0',
    'propagate',
    [DMGRCONFIGPATH, "MoREDemoCell", "node2", "webserver1"]
)

print("PetClinic successfully deployed! Access the application at:")
print("- SSL: https://localhost:8888/spring-petclinic/")
print("- Non-SSL: http://localhost:7777/spring-petclinic/")
