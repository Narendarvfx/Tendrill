from PySide2.QtWebEngineWidgets import QWebEngineView


class Browser(object):
    def __init__(self, obj):
        super(Browser, self).__init__()
        self.main_window = obj
        self.browser = QWebEngineView()
        self.browser.setUrl('https://www.google.com')
        self.main_window.ui.browser_layout.addWidget(self.browser)