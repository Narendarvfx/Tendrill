import sys
from ldap3 import Server, Connection, ALL, NTLM, ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES, AUTO_BIND_NO_TLS, SUBTREE, \
    SAFE_SYNC
from ldap3.core.exceptions import LDAPCursorError

server_name = '192.168.5.2'
domain_name = 'oscarfx'
user_name = 'pipelineaccount'
password = 'Gunreddy^999'

format_string = '{:25}   {:>6}   {:19}   {:19}   {}'
# print(format_string.format('User', 'Logins', 'Last Login', 'Expires', 'Description'))

server = Server(server_name, get_info=ALL)
print("Connecting to Active Directory...")
conn = Connection(server, user='{}\\{}'.format(domain_name, user_name), password=password, authentication=NTLM,
                  auto_bind=True)
print("Connected")
conn.search('dc={},dc=com'.format(domain_name), '(objectclass=*)',
            attributes=['sAMAccountName', 'name', ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES])
print("Fetching data....")
for e in conn.entries:
    try:
        desc = e.description
    except LDAPCursorError:
        desc = ""
    print(e.name)
    # print(format_string.format(str(e.name)[:25], str(e.logonCount)[:6], str(e.lastLogon)[:19], str(e.accountExpires)[:19], desc))