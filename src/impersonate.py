import win32security, win32con, win32.win32api , win32 ,win32.win32security

class Impersonate:
    def __init__(self, login, password):
        self.domain = 'domain'
        self.login = login
        self.password = password

    def logon(self):
        self.handle = win32.win32security.LogonUser(self.login, self.domain,self.password,win32con.LOGON32_LOGON_INTERACTIVE,win32con.LOGON32_PROVIDER_DEFAULT)
        win32.win32security.ImpersonateLoggedOnUser(self.handle)

    def logoff(self):
        win32security.RevertToSelf() # terminates impersonation
        self.handle.Close() # guarantees cleanup

if __name__=='__main__':
    a = Impersonate('user_name','user_password')

    # Logging in
    a.logon()

    # Do whatever
    print(f"\n\t\tImpersonating: {win32.win32api.GetUserName()}")

    #Another way to call an Object
    Impersonate.logoff(a) # Logoff and Clean up