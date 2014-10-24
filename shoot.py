import sys
from PySide.QtGui import *
from PySide.QtWebKit import QWebView
from oauth_verification import Authenticator
from PySide.QtCore import QUrl

class App:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.view = QWebView()
        icon = QIcon("shutter.png")
        menu = QMenu()
        settingAction = menu.addAction("Settings")
        exitAction = menu.addAction("Exit")
        settingAction.triggered.connect(self.setting)
        exitAction.triggered.connect(sys.exit)

        self.tray = QSystemTrayIcon()
        self.tray.setIcon(icon)
        self.tray.setContextMenu(menu)
        self.tray.show()

    def redirect_to_permision_url(self, url):
        self.view = QWebView()
        self.view.load(QUrl(url))
        self.view.show()
        self.view.loadFinished.connect(self.load1)

    def load1(self):
       self.view.urlChanged.connect(self.onUrlChange)

    def onUrlChange(self, url):
        print url

    def start(self):
        self.app.exec_()
        sys.exit()

    def setting(self):
        self.dialog = QDialog()
        self.dialog.setWindowTitle("The Setting Dialog")
        self.dialog.show()

if __name__ == "__main__":
    app = App()
    auth = Authenticator()
    app.redirect_to_permision_url(auth._get_permission_url())
    app.start()