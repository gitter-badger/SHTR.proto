import sys
from PySide.QtGui import QLabel, QWidget, QPushButton, QDesktopServices, QVBoxLayout, QApplication, QPixmap
from datetime import datetime
from upload import *
from auth_server import *
from cherrypy import quickstart

#create a Qt App
date = datetime.now()
app = QApplication(sys.argv)
widget = QWidget()
# set up the QWidget...
widget.setLayout(QVBoxLayout())
label = QLabel()
auth_server = AuthVerificationServer()


def isTokenCollected():
    if(get_credentials() != None):
        return True
    else:
        return False

def receive_verification_code(sender):
    save_credentials(sender)
    auth_server.stop_server()


def redirect_to_permission_page():
    QDesktopServices.openUrl(get_permission_url())
    quickstart(auth_server)

def shoot():
    if( not isTokenCollected()):
        redirect_to_permission_page()

    #taking the screenshot
    filename = date.strftime('%Y-%m-%d_%H-%M-%S.jpg')
    p = QPixmap.grabWindow(QApplication.desktop().winId())
    p.save(filename, 'jpg')
    upload_file_to_drive(filename)

def upload_file_to_drive(fname):
    service = get_drive_service()
    insert_file(service, fname, 'SHTR SHOT', None, 'image/jpg', fname)

widget.layout().addWidget(QPushButton('Setup Google Drive', clicked=shoot))
dispatcher.connect(receive_verification_code)

widget.show()


#enter Qt App main loop
app.exec_()
sys.exit()