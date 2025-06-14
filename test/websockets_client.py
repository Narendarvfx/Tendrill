import json
import sys

from PySide2 import QtCore, QtWebSockets, QtNetwork
from PySide2.QtCore import QUrl, QCoreApplication, QTimer
from PySide2.QtWidgets import QApplication


class Client(QtCore.QObject):
    def __init__(self, parent):
        super().__init__(parent)

        self.client =  QtWebSockets.QWebSocket("",QtWebSockets.QWebSocketProtocol.Version13,None)
        self.client.error.connect(self.error)

        self.client.open(QUrl("ws://127.0.0.1:8000/ws/emp/16/"))
        print(self.client.requestUrl())
        self.client.pong.connect(self.onPong)
        try:
            self.client.textMessageReceived.connect(self.processTextMessage)
        except Exception as e:
            print(e)

    def do_ping(self):
        print("client: do_ping")
        self.client.ping(b"foo")

    def send_message(self):
        print("client: send_message")
        data = {
            'name': "narendar",
            'message': "Hai"
        }
        self.client.sendTextMessage(json.dumps(data))

    def processTextMessage(self):
        print("hai")

    def onPong(self, elapsedTime, payload):
        print("onPong - time: {} ; payload: {}".format(elapsedTime, payload))

    def error(self, error_code):
        print("error code: {}".format(error_code))
        print(self.client.errorString())

    def close(self):
        self.client.close()

def quit_app():
    print("timer timeout - exiting")
    QCoreApplication.quit()

def ping():
    client.do_ping()

def send_message():
    client.send_message()

if __name__ == '__main__':
    global client
    app = QApplication(sys.argv)

    QTimer.singleShot(2000, ping)
    QTimer.singleShot(3000, send_message)
    # QTimer.singleShot(5000, quit_app)

    client = Client(app)

    app.exec_()