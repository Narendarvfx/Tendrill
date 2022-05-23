import os
import sys

from PySide2 import QtCore, QtMultimedia

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

def mp3_play():

    filename = "D:/Iphone.mp3"
    app = QtCore.QCoreApplication(sys.argv)

    player = QtMultimedia.QMediaPlayer()

    def handle_state_changed(state):

        if state == QtMultimedia.QMediaPlayer.PlayingState:

            print("started")

        elif state == QtMultimedia.QMediaPlayer.StoppedState:

            print("finished")

            QtCore.QCoreApplication.quit()

    player.stateChanged.connect(handle_state_changed)

    url = QtCore.QUrl.fromLocalFile(filename)

    player.setMedia(QtMultimedia.QMediaContent(url))

    player.play()

    sys.exit(app.exec_())

if __name__ == "__main__":

    main()