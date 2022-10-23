# import PySide2
#
# def finished(reply):
#     print("finished: ", reply.readAll())
#
# url = "https://172.168.1.197/api/production/shots/"
# req = PySide2.QtNetwork.QNetworkRequest(url)
# req.setRawHeader("Authorization" ,'Token 8f1192dfa465d1f566c38e53ed199d8da7090a55')
# req.setHeader( PySide2.QtNetwork.QNetworkRequest.ContentTypeHeader, "application/json" )
# nam = PySide2.QtNetwork.QNetworkAccessManager()
# nam.finished.connect(finished)
# nam.get(req)
#
# try:
#     print(req)
# except Exception as e:
#     print(e)
import subprocess, os
shot_dir =r'C:\jfx\KIS\BOO_GKB\BOO_GKB_0080_fg01_v002\paint\scripts\nuke\BOO_GKB_0080_fg01_v002_paint_v001_01.nk'
nuke = r"C:\Program Files\Nuke13.0v2\Nuke13.0.exe"
cmd = '"{}" {}'.format(nuke, shot_dir)
# os.system(cmd)

default_folder_structure = r'P:\Tendrill\folder_structure\{}'.format('paint')
base_dir = r'C:\KIS\BOO_GKB\BOO_GKB_0080_fg01_v002\paint'


cmd = f"robocopy /e  {default_folder_structure} {base_dir} /MIR"

try:
    a = os.system(cmd)
    print (a)

except Exception as e:
    print (e)
    print("Failed to create folder structure")
#
# try:
#     call(['robocopy', row_data['Input Path'], os.path.join(self.base_dir, 'scans', 'plates'), "/S", "/MIR"])
# except Exception as e:
#     print(e)
#     pass

# subprocess.Popen(r'explorer /select,"{}"'.format(shot_dir))