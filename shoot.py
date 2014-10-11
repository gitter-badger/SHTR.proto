import sys
from PySide.QtCore import *
from PySide.QtGui import *
from datetime import datetime
from upload import *


#create a Qt App
date = datetime.now()
app = QApplication(sys.argv)
widget = QWidget()
# set up the QWidget...
widget.setLayout(QVBoxLayout())

label = QLabel()
window = QMainWindow()
window.resize(800,600)
window.hide()

web = QWebView(window)
web.resize(800,600)

def shoot():
    #taking the screenshot
    filename = date.strftime('%Y-%m-%d_%H-%M-%S.jpg')
    p = QPixmap.grabWindow(QApplication.desktop().winId())
    p.save(filename, 'jpg')

    #building the web-service for uploading
    window.show()
    web.show()
    web.load(get_permission_url())
    web.loadFinished()
    #insert_file(service, filename, 'SHTR SHOT', None, 'image/jpg', filename)

widget.layout().addWidget(QPushButton('take screenshot', clicked=shoot))

widget.show()
app.exec_()

#enter Qt App main loop
app.exec_()
sys.exit()