data=('postgresql', 'semantic.amazonaws-prod.com', 5432, 'semantic', 'admin', '12345')
prod_config={
    'dialect':'postgresql',
    'user name':'admin',
    'password':'12345',
    'host':'semantic.amazonaws-prod.com',
    'port':'5432',
    'database name':'semantic'
    }
staging_config=prod_config.copy()
staging_config['host']='semantic.amazonaws-staging.com'
staging_config['password']='root'

print '{}://{}:{}@{}:{}/{}'.format(prod_config.get('dialect'),prod_config.get('user name'),prod_config.get('password'),
                                   prod_config.get('host'),prod_config.get('port'),prod_config.get('database name'))

print '{}://{}:{}@{}:{}/{}'.format(staging_config.get('dialect'),staging_config.get('user name'),staging_config.get('password'),
                                   staging_config.get('host'), staging_config.get('port'), staging_config.get('database name'))
