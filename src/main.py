# -*- coding: utf-8 -*-
import ctypes
import platform
import sys

from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QIcon

import config
from webapp import webapp


class WebDaemon(QThread):
    def __init__(self, app):
        super().__init__()
        self.app = app

    def run(self):
        self.app.run(port=config.HTTP_PORT)


if __name__ == '__main__':
    # win vista and above
    if platform.system().lower() == "windows" and platform.version() >= '6.0':
        appid = 'me.muyan.wxhelper'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)

    web_daemon = WebDaemon(webapp)
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
