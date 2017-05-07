import time
from tornado.web import RequestHandler
from tornado.escape import json_decode
from bot import Bot


bot = Bot()


class RootHandler(RequestHandler):
    def get(self):
        self.redirect('http://127.0.0.1:8080/index')
        # self.write('hello')


class QrcodeHandler(RequestHandler):
    def get(self):
        bot.get_uuid()
        png = bot.get_qrcode()
        self.add_header('Content-Type', 'image/png')
        self.write(png)


class LoginHandler(RequestHandler):
    def get(self):
        self.write(bot.login())


class CheckLoginHandler(RequestHandler):
    def get(self):
        if bot.is_logged_in():
            self.write('true')
        else:
            self.write('false')


class LogoutHandler(RequestHandler):
    def get(self):
        bot.logout()
        self.write('logged out')
        # self.redirect('/login')


class FriendsHandler(RequestHandler):
    def get(self):
        response = {
            'friends': [friend.to_json() for friend in bot.friends()]
        }
        self.write(response)
    def post(self):
        data = json_decode(self.request.body)
        bot.add_friend(data['user_name'], data['verify_msg'])
        self.write('ok')


class GroupHandler(RequestHandler):
    def get(self):
        response = {
            'groups': [group.to_json() for group in bot.groups()]
        }
        self.write(response)


class GroupMemberHandler(RequestHandler):
    def get(self, user_name):
        group = bot.search_group(user_name)
        if group:
            members = group.members
            member_data_list = []
            for member in members:
                data = member.to_json()
                data['is_friend'] = member.is_friend
                member_data_list.append(data)

            response = {
                'members': member_data_list
            }
            self.write(response)
        else:
            self.set_status(404)


class FriendAvatarHandler(RequestHandler):
    def get(self, username):
        self.add_header('Content-Type', 'image/jpg')
        self.write(bot.get_friend_avatar(username))


class GroupAvatarHandler(RequestHandler):
    def get(self, username):
        self.add_header('Content-Type', 'image/jpg')
        self.write(bot.get_group_avatar(username))


class GroupMemberAvatarHandler(RequestHandler):
    def get(self, group_username, username):
        self.add_header('Content-Type', 'image/jpg')
        self.write(bot.get_group_member_avatar(group_username, username))


