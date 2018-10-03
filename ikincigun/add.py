#apt install python-ldap

import ldap
import ldap.modlist as modlist

l = ldap.open("192.168.59.4")
l.protocol_version = ldap.VERSION3	
username = "cn=alorak,dc=pardus,dc=lab"
password  = "secret"
l.simple_bind(username, password)

dn="ou=altdal,ou=iki,dc=pardus,dc=lab" 
attrs = {}
attrs['objectclass'] = ['top','organizationalUnit']
attrs['ou'] = 'altdal'
ldif = modlist.addModlist(attrs)

l.add_s(dn,ldif)

l.unbind_s()
