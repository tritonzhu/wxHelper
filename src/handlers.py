from tornado.web import RequestHandler
from bot import Bot

bot = Bot()


class RootHandler(RequestHandler):
    def get(self):
        self.render('index.html')


class QrcodeHandler(RequestHandler):
    def get(self):
        bot.get_uuid()
        png = bot.get_qrcode()
        self.add_header('Content-Type', 'image/png')
        self.write(png)


class LoginHandler(RequestHandler):
    def get(self):
        bot.login()
        self.write('ok')


class FriendsHandler(RequestHandler):
    def get(self):
        response = {
            'friends': bot.friends()
        }
        self.write(response)


class GroupHandler(RequestHandler):
    def get(self):
        response = {
            'groups': bot.groups()
        }
        self.write(response)


class FriendAvatarHandler(RequestHandler):
    def get(self, username):
        self.add_header('Content-Type', 'image/jpg')
        self.write(bot.get_friend_avatar(username))


class GroupAvatarHandler(RequestHandler):
    def get(self, username):
        self.add_header('Content-Type', 'image/jpg')
        self.write(bot.get_group_avatar(username))
