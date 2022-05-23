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
