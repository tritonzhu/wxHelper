import tornado.ioloop
import handlers
import tornado.web

routers = [
    (r'/', handlers.RootHandler),
    (r'/qrcode.png', handlers.QrcodeHandler),
    (r'/login', handlers.LoginHandler),
    (r'/friends', handlers.FriendsHandler),
    (r'/groups', handlers.GroupHandler),
    (r'/friends/(@[a-z0-9]+)/avatar', handlers.FriendAvatarHandler),
    (r'/groups/(@@[a-z0-9]+)/avatar', handlers.GroupAvatarHandler),
    (r'/groups/(@@[a-z0-9]+)/members', handlers.GroupMemberHandler),
]

application = tornado.web.Application(handlers=routers, template_path='../templates', static_path='../static')

if __name__ == "__main__":
    application.listen(11235)
    tornado.ioloop.IOLoop.current().start()
