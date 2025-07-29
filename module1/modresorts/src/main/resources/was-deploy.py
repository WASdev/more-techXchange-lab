#
# Deploy and start an application to WAS
# Will uninstall first if application is already installed
#
print('[INFO] Entering deploy for ModResorts...')
AdminConfig.reset()

print('[INFO] Check if ModResorts is already installed')
installedAppList = AdminApp.list()

serverName='server1'
appPath='./modresorts-2.0.0.war'
appName='ModResorts'

if appName in installedAppList:
    print('[INFO] Application ' + appName + ' is installed. Uninstalling now.')
    AdminApp.uninstall(appName)
    AdminConfig.save()
else:
    print('[INFO] Application ' + appName + ' is not installed.')

print('[INFO] Installing ' + appName)
AdminApp.install(appPath, ['-appname', appName, '-server', serverName])
AdminConfig.save()

print('[INFO] Begin check if App is ready...')
AdminApp.isAppReady(appName)
print('[INFO] End check if App is ready.')

print('[INFO] Begin check deployment status... ')
print AdminApp.getDeployStatus(appName)
print('[INFO] End check deployment status.')

print('[INFO] Begin map all users to the users role')
AdminApp.edit(appName, '[-MapRolesToUsers [["users" "no" "no" "professor|fry|zoidberg|hermes|leela|bender|amy" "" "no" "" ""]]]')
AdminConfig.save()
print('[INFO] Finished map all users to the users role')

print('[INFO] Begin start application... ')
# For more complex WAS installations use other csv params in the queryNames, e.g.: cell=mycell,node=mynode,
appManager = AdminControl.queryNames('type=ApplicationManager,process=server1,*')
AdminControl.invoke(appManager, 'startApplication', appName)
print('[INFO] End start application... ')

print('[INFO] Leaving deploy for ModResorts.')
