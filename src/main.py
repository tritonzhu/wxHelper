# -*- coding: utf-8 -*-
import ctypes
import platform
import sys

from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QIcon
import tornado.ioloop

import config
from tornadoapp import application


class WebDaemon(QThread):
    def __init__(self, app):
        super().__init__()
        self.app = app

    def run(self):
        self.app.listen(config.HTTP_PORT)
        tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    # win vista and above
    if platform.system().lower() == "windows" and platform.version() >= '6.0':
        appid = 'me.muyan.wxhelper'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)

    web_daemon = WebDaemon(application)
    web_daemon.start()

    qtapp = QtWidgets.QApplication(sys.argv)

    webview = QtWebEngineWidgets.QWebEngineView()
    webview.resize(config.APP_WIDTH, config.APP_HEIGHT)
    webview.setUrl(QtCore.QUrl(config.BASE_URL))
    webview.setWindowTitle("微信助手")

    icon = QIcon('../icon/icon.ico')
    webview.setWindowIcon(icon)
    #webview.setContextMenuPolicy(False)

    def shut_down():
        web_daemon.quit()
    qtapp.aboutToQuit.connect(shut_down)

    webview.show()
    sys.exit(qtapp.exec())
