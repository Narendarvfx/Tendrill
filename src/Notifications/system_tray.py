from PySide2 import QtWidgets, QtGui, QtCore


class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    """
    CREATE A SYSTEM TRAY ICON CLASS AND ADD MENU
    """

    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.application_version = 0.5
        self.setToolTip('OscarFX Pipeline Application Build - %s' % self.application_version)
        menu = QtWidgets.QMenu(parent)

        open_app = menu.addAction("Open Desktop App")
        exitAction = menu.addAction("Exit")
        open_app.triggered.connect(self.open_app)
        open_app.setIcon(QtGui.QIcon("D:/Native Design/Shot-Buzz/icons/oscarfx/png.png"))
        menu.addSeparator()

        self.setContextMenu(menu)
        self.activated.connect(self.onTrayIconActivated)
        # QtCore.QObject.connect(exitAction,QtCore.SIGNAL('triggered()'), self.exit)

    def exit(self):
      QtCore.QCoreApplication.exit()

    def onTrayIconActivated(self, reason):
        if reason == self.DoubleClick:
            print("Do something on double click")
        if reason == self.Trigger:
            self.open_app()

    def open_app(self):
        """
        this function will open application
        :return:
        """
        print("Open Desktop App Here .....")

if __name__ == "__main__":
    icon = QtGui.QIcon('D:/Native Design/Shot-Buzz/icons/oscarfx/png.png')
    SystemTrayIcon(icon)