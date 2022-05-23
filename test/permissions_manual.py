import os
import win32security
import ntsecuritycon as con
def permissions_manual():
    # s_list = ['srinivas.r','Ganeshbabu.G','chandu.g'] ##ForSubmission
    # list = ['srinivas.r','Ganeshbabu.G','chandu.g','AchutKumarReddy.S']
    list = ['waseemakram.shaik','akhil.p','praveen.g','gangadhar.v']
    # list = ['KiranKumar.ch']
    base_dir = r"\\172.168.1.250\ofxstorage\jobs\TTP\GS\101"
    shot_dir = os.listdir(base_dir)
    for dir in shot_dir:
        # p = os.path.join(base_dir,dir,'_forsubmission', '_paint')
        p = os.path.join(base_dir, dir, '_roto')
        for user in list:
            try:
                FILENAME = p

                artist, domain, type = win32security.LookupAccountName("", str(user))

                sd = win32security.GetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION)

                dacl = sd.GetSecurityDescriptorDacl()

                dacl.AddAccessAllowedAceEx(win32security.ACL_REVISION_DS,
                                           win32security.SUB_CONTAINERS_AND_OBJECTS_INHERIT, con.GENERIC_ALL,
                                           artist)

                sd.SetSecurityDescriptorDacl(1, dacl, 0)
                win32security.SetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION, sd)
            except Exception as e:
                print(e)
        s = os.path.join(base_dir, dir, '_forsubmission', '_roto')
        for user in list:
            try:
                FILENAME = s

                artist, domain, type = win32security.LookupAccountName("", str(user))

                sd = win32security.GetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION)

                dacl = sd.GetSecurityDescriptorDacl()

                dacl.AddAccessAllowedAceEx(win32security.ACL_REVISION_DS,
                                           win32security.SUB_CONTAINERS_AND_OBJECTS_INHERIT, con.GENERIC_ALL,
                                           artist)

                sd.SetSecurityDescriptorDacl(1, dacl, 0)
                win32security.SetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION, sd)
            except Exception as e:
                print(e)

permissions_manual()
