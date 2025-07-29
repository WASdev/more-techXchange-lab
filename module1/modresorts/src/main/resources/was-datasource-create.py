#
# Create a datasource for the application
# Assumes a node scoped JDBC provider (/Node:<insert node here>/JDBCProvider:DB2JDBC01/) is already configured in the WAS installation
# Assumes a node scoped the auth alias (<insert node here>/prod01AuthAlias) is already configured in the WAS installation
#
#
print('[INFO] Creating data source for ModResorts')

node_name = AdminControl.getNode()

ds = AdminConfig.getid('/DataSource:ModResortsDs/')
if not ds:
	print '[INFO] Datasource does not already exist. Will create now.'
else:
	print '[INFO] Datasource already exists. Delete and recreate'
	AdminTask.deleteDatasource(ds)

db2JdbcProvider = AdminConfig.getid('/Node:' + node_name + '/JDBCProvider:DB2JDBC01/')

AdminTask.createDatasource(db2JdbcProvider, '[-name "ModResortsDs" -jndiName jdbc/ModResortsJndi -componentManagedAuthenticationAlias ' + node_name + '/prod01AuthAlias -dataStoreHelperClassName com.ibm.websphere.rsadapter.DB2UniversalDataStoreHelper -configureResourceProperties [[databaseName java.lang.String PROD01] [driverType java.lang.Integer 4] [serverName java.lang.String localhost] [portNumber java.lang.Integer 50000]]]')

print('[INFO] Saving config')
AdminConfig.save()

print('[INFO] Testing connection...')
newDs = AdminConfig.getid('/DataSource:ModResortsDs/')
AdminControl.testConnection(newDs)
print('[INFO] Finished testing connection.')

print('[INFO] Finished creating data source for ModResorts')
