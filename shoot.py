import sys
from PySide.QtGui import QLabel, QWidget, QPushButton, QDesktopServices, QVBoxLayout, QApplication
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
#signal = Signal('First signal')

def receive_verification_code(sender):
    save_credentials(sender)

def redirect_to_permission_page():
    QDesktopServices.openUrl(get_permission_url())
    #threading.Thread(target=quickstart(AuthVerification))
    quickstart(AuthVerification())


def shoot():
    #taking the screenshot
    #filename = date.strftime('%Y-%m-%d_%H-%M-%S.jpg')
    #p = QPixmap.grabWindow(QApplication.desktop().winId())
    #p.save(filename, 'jpg')



    #insert_file(service, filename, 'SHTR SHOT', None, 'image/jpg', filename)

widget.layout().addWidget(QPushButton('Setup Google Drive', clicked=shoot))
dispatcher.connect(receive_verification_code)

widget.show()


#enter Qt App main loop
app.exec_()
sys.exit()