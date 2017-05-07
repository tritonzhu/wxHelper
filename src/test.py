import itchat
from itchat.content import *

@itchat.msg_register([SYSTEM])
def get_msg(msg):
    print(msg.user)


friends = itchat.get_friends()

itchat.auto_login(True)
itchat.run(True)