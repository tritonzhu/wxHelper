import tornado.ioloop
import tornado.web
from . import handlers

routers = [
    (r'/', handlers.RootHandler),
    (r'/api/qrcode.png', handlers.QrcodeHandler),
    (r'/api/login', handlers.LoginHandler),
    (r'/api/checklogin', handlers.CheckLoginHandler),
    (r'/api/logout', handlers.LogoutHandler),
    (r'/api/friends', handlers.FriendsHandler),
    (r'/api/groups', handlers.GroupHandler),
    (r'/api/friends/(@[a-z0-9]+)/avatar', handlers.FriendAvatarHandler),
    (r'/api/groups/(@@[a-z0-9]+)/avatar', handlers.GroupAvatarHandler),
    (r'/api/groups/(@@[a-z0-9]+)/members', handlers.GroupMemberHandler),
    (r'/api/groups/(@@[a-z0-9]+)/(@[a-z0-9]+)/avatar', handlers.GroupMemberAvatarHandler),
]

application = tornado.web.Application(handlers=routers, template_path='templates', static_path='static')

if __name__ == "__main__":
    application.listen(11235)
    tornado.ioloop.IOLoop.current().start()
