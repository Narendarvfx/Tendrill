import os
import sys

from PySide2 import QtCore, QtMultimedia, QtGui, QtWidgets

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

def mp3_play():

    filename = "D:/Iphone.mp3"
    if not QtCore.QCoreApplication.instance():
        app = QtCore.QCoreApplication(sys.argv)
    else:
        app = QtCore.QCoreApplication.instance()
        print(app)

    player = QtMultimedia.QMediaPlayer()

    def handle_state_changed(state):

        if state == QtMultimedia.QMediaPlayer.PlayingState:

            print("started")

        elif state == QtMultimedia.QMediaPlayer.StoppedState:

            print("finished")

            # QtCore.QCoreApplication.quit()

    player.stateChanged.connect(handle_state_changed)

    url = QtCore.QUrl.fromLocalFile(filename)

    player.setMedia(QtMultimedia.QMediaContent(url))

    player.play()
    # app.exec_()
    sys.exit(app.exec_())

if __name__ == "__main__":

    mp3_play()