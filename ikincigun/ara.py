#apt install python-ldap

import ldap
import ldap.modlist as modlist

l = ldap.open("192.168.59.4")
l.protocol_version = ldap.VERSION3	
username = "cn=alorak,dc=pardus,dc=lab"
password  = "secret"
l.simple_bind(username, password)

baseDN = "ou=iki,dc=pardus,dc=lab"
searchScope = ldap.SCOPE_SUBTREE
retrieveAttributes = None 
searchFilter = "cn=*"

ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
result_set = []
while 1:
	result_type, result_data = l.result(ldap_result_id, 0)
	if (result_data == []):
		break
	else:
		if result_type == ldap.RES_SEARCH_ENTRY:
			result_set.append(result_data)
print result_set
