import io
import requests
import itchat
from entity import Group, Friend

from pyqrcode import QRCode

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Referer': 'https://wx.qq.com/'
}


class Bot:
    def __init__(self):
        self.session = requests.session()
        self.uuid = None
        self.is_logging = True

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
        status = itchat.check_login()
        print(status)
        if status == '200':
            print('logged in')
            itchat.web_init()
            itchat.show_mobile_login()
            itchat.get_contact(True)
            self.is_logging = False
            itchat.start_receiving()
        return status

    def logout(self):
        itchat.logout()

    def friends(self):
        friends = itchat.get_friends()
        friend_list = [Friend(friend, self) for friend in friends]
        return friend_list

    def search_friend(self, user_name):
        friends = itchat.get_friends()
        friend_list = [Friend(friend, self) for friend in friends]
        for friend in friend_list:
            if friend.user_name == user_name:
                return friend
        return None

    def groups(self):
        groups = itchat.get_chatrooms()
        group_list = [Group(group, self) for group in groups]
        return group_list

    def search_group(self, user_name):
        groups = itchat.get_chatrooms()
        group_list = [Group(group, self) for group in groups]
        for group in group_list:
            if group.user_name == user_name:
                return group
        return None

    def get_friend_avatar(self, user_name):
        return itchat.get_head_img(userName=user_name)

    def get_group_avatar(self, user_name):
        return itchat.get_head_img(chatroomUserName=user_name)

    def get_group_member_avatar(self, group_user_name, user_name):
        return itchat.get_head_img(chatroomUserName=group_user_name, userName=user_name)

    def add_friend(self, user_name, verify_content=''):
        return itchat.add_friend(user_name, verifyContent=verify_content)

    def accept_friend(self, user_name, verify_content=''):
        return itchat.add_friend(user_name, status=3, verifyContent=verify_content)

    def set_alias(self, user_name, remark_name):
        return itchat.set_alias(user_name, remark_name)

    def update_chatroom(self, user_name, member_details=False):
        return itchat.update_chatroom(user_name, detailedMember=member_details)

if __name__ == '__main__':
    bot = Bot()
    bot.get_uuid()
    bot.get_qrcode()

