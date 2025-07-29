SERHOME = "/home/techzone"

# Create Web Server on a Managed Node
print "***Creating Web Server webserver1 on node2***"
AdminTask.createWebServer('node2', [
    '-name', 'webserver1',
    '-templateName', 'IHS',
    '-serverConfig', [
        '-webPort', '7777',
        '-serviceName', '',
        '-webInstallRoot', USERHOME + '/IBM/HTTPServer',
        '-webProtocol', 'HTTP',
        '-configurationFile', '',
        '-errorLogfile', '',
        '-accessLogfile', '',
        '-pluginInstallRoot', USERHOME + '/IBM/HTTPServer/plugin',
        '-webAppMapping', 'ALL'
    ],
    '-remoteServerConfig', [
        '-adminPort', '8008',
        '-adminUserID', '',
        '-adminPasswd', '',
        'HTTP'
    ]
])

print "***Creating the host alias***"
AdminConfig.create(
    'HostAlias',
    AdminConfig.getid('/Cell:MoREDemoCell/VirtualHost:default_host/'),
    '[[hostname "*"] [port "7777"]]'
)
AdminConfig.save()

print "***Syncing the nodes***"
AdminNodeManagement.syncActiveNodes()

# Start Web Server
print "***Starting Web Server***"
AdminTask.startMiddlewareServer('[-serverName webserver1 -nodeName node2 ]')
print "IHS is running at http://<hostname>:7777"
