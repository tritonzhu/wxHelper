import tornado.ioloop
import handlers
import tornado.web

routers = [
    (r'/', handlers.RootHandler),
    (r'/api/qrcode.png', handlers.QrcodeHandler),
    (r'/api/login', handlers.LoginHandler),
    (r'/api/friends', handlers.FriendsHandler),
    (r'/api/groups', handlers.GroupHandler),
    (r'/api/friends/(@[a-z0-9]+)/avatar', handlers.FriendAvatarHandler),
    (r'/api/groups/(@@[a-z0-9]+)/avatar', handlers.GroupAvatarHandler),
    (r'/api/groups/(@@[a-z0-9]+)/members', handlers.GroupMemberHandler),
]

application = tornado.web.Application(handlers=routers, template_path='../templates', static_path='../static')

if __name__ == "__main__":
    application.listen(11235)
    tornado.ioloop.IOLoop.current().start()
