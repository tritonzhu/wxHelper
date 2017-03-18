import time
import re
import random
import io
import xml.dom.minidom
import requests
import itchat

from pyqrcode import QRCode

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Referer': 'https://wx.qq.com/'
}


class Bot:
    def __init__(self):
        self.session = requests.session()
        self.uuid = None
        self.isLogging = True

    def get_uuid(self):
        self.uuid = itchat.get_QRuuid()
        print(self.uuid)

    def get_qrcode(self):
        url = 'https://login.weixin.qq.com/l/%s' % self.uuid
        qr_code = QRCode(url)
        qr_bytes = io.BytesIO()
        qr_code.png(qr_bytes, scale=10)
        return qr_bytes.getvalue()

    def login(self):
        while self.isLogging:
            isLoggedIn = False
            while not isLoggedIn:
                status = itchat.check_login()
                print(status)
                if status == '200':
                    isLoggedIn = True
                elif status == '201':
                    if isLoggedIn is not None:
                        isLoggedIn = None
                elif status != '408':
                    break
            if isLoggedIn:
                break
        else:
            return # log in process is stopped by user
        print('logged in')
        itchat.web_init()
        itchat.show_mobile_login()
        itchat.get_contact(True)
        self.isLogging = False
        itchat.start_receiving()

    def friends(self):
        return itchat.get_friends()

    def groups(self):
        return itchat.get_chatrooms()

    def get_friend_avatar(self, username):
        return itchat.get_head_img(userName=username)

    def get_group_avatar(self, username):
        return itchat.get_head_img(chatroomUserName=username)

if __name__ == '__main__':
    bot = Bot()
    bot.get_uuid()
    bot.get_qrcode()

