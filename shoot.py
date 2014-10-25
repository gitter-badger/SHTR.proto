import sys
from datetime import datetime

from PySide.QtGui import *
from PySide.QtWebKit import QWebView
from PySide.QtCore import QUrl
from PySide.QtCore import QRect, QSize

from oauth_verification import Authenticator


class TransWidget(QWidget):
    def __init__(self):
        super(TransWidget, self).__init__()
        self.setWindowOpacity(0.3)
        self.setFocus()
        self.showMaximized()
        self.band = QRubberBand(QRubberBand.Rectangle, self)

    def mousePressEvent(self, event):
        super(TransWidget, self).mousePressEvent(event)
        print "Mouse pressed"
        self.origin = event.pos()
        if not self.band:
            self.band = QRubberBand(QRubberBand.Rectangle, self)
        self.band.setGeometry(QRect(self.origin, QSize()))
        self.band.show()

    def mouseMoveEvent(self, event):
        super(TransWidget, self).mouseMoveEvent(event)
        self.band.setGeometry(QRect(self.origin, event.pos()).normalized())

    def mouseReleaseEvent(self, event):
        super(TransWidget, self).mouseReleaseEvent(event)
        self.band.hide()

class App:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.view = QWebView()
        self.filename = ''
        icon = QIcon("shutter.png")
        menu = QMenu()
        fullWindowShot = menu.addAction("Capture Full Window")
        regionShot = menu.addAction("Capture a region")
        settingAction = menu.addAction("Settings")
        exitAction = menu.addAction("Exit")
        fullWindowShot.triggered.connect(self.takeFullWindowShot)
        regionShot.triggered.connect(self.takeRegionShot)
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

    def takeFullWindowShot(self):
        self.filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S.jpg')
        p = QPixmap.grabWindow(QApplication.desktop().winId())
        p.save(self.filename, 'jpg')

    def takeRegionShot(self):
        self.transWidget = TransWidget()

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
    auth = Authenticator()
    app = App()

    if(auth._isAlreadyLoggedIn()):
        app.start()
    else:
        m = QMessageBox()
        m.setText("You are not logged into Google Drive")
        m.setInformativeText("We detected that you are not logged into google drive. So we are redirecting you to log in first.")
        m.setFocus()
        m.exec_()
        #app.redirect_to_permision_url(auth._get_permission_url())
        app.start()