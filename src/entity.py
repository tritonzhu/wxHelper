# most of the following codes are copied from wxpy


class Chat(object):
    """
    单个用户(:class:`User`)和群聊(:class:`Group`)的基础类
    """

    def __init__(self, raw, bot):

        self.raw = raw
        self.bot = bot

        self.alias = self.raw.get('Alias')
        self.uin = self.raw.get('Uin')

    @property
    def nick_name(self):
        """
        该聊天对象的昵称 (好友、群员的昵称，或群名称)
        """
        if self.user_name == 'filehelper':
            return '文件传输助手'
        elif self.user_name == 'fmessage':
            return '好友请求'
        else:
            return self.raw.get('NickName')

    @property
    def name(self):
        """
        | 该聊天对象的友好名称
        | 具体为: 从 备注名称、群聊显示名称、昵称(或群名称)，或微信号中，按序选取第一个可用的
        """
        for attr in 'remark_name', 'display_name', 'nick_name', 'wxid':
            _name = getattr(self, attr, None)
            if _name:
                return _name

    @property
    def wxid(self):
        """
        | 微信号
        | 有可能获取不到 (手机客户端也可能获取不到)
        """

        return self.alias or self.uin or None

    @property
    def user_name(self):
        """
        该聊天对象的内部 ID，通常不需要用到
        ..  attention::
            同个聊天对象在不同用户中，此 ID **不一致** ，且可能在新会话中 **被改变**！
        """
        return self.raw.get('UserName')

    def to_json(self):
        data = {
            'alias': self.alias,
            'uin': self.uin,
            'nick_name': self.nick_name,
            'name': self.name,
            'wxid': self.wxid,
            'user_name': self.user_name
        }
        return data

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.name)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash((Chat, self.user_name))


MALE = 1
FEMALE = 2


class User(Chat):
    """
    好友(:class:`Friend`)、群聊成员(:class:`Member`)，和公众号(:class:`MP`) 的基础类
    """

    def __init__(self, raw, bot):
        super(User, self).__init__(raw, bot)

    @property
    def remark_name(self):
        """
        备注名称
        """
        return self.raw.get('RemarkName')

    @property
    def sex(self):
        """
        性别
        """
        return self.raw.get('Sex')

    @property
    def province(self):
        """
        省份
        """
        return self.raw.get('Province')

    @property
    def city(self):
        """
        城市
        """
        return self.raw.get('City')

    @property
    def signature(self):
        """
        个性签名
        """
        return self.raw.get('Signature')

    @property
    def is_friend(self):
        """
        判断当前用户是否为好友关系
        :return: 若为好友关系则为 True，否则为 False
        """

        if self.bot:
            return self in self.bot.friends()

    def add(self, verify_content=''):
        """
        把当前用户加为好友
        :param verify_content: 验证信息(文本)
        """
        return self.bot.add_friend(self.user_name, verify_content=verify_content)

    def accept(self, verify_content=''):
        """
        接受当前用户为好友
        :param verify_content: 验证信息(文本)
        :return: 新的好友对象
        """
        return self.bot.accept_friend(user=self, verify_content=verify_content)

    def to_json(self):
        data = {
            'alias': self.alias,
            'uin': self.uin,
            'nick_name': self.nick_name,
            'name': self.name,
            'wxid': self.wxid,
            'user_name': self.user_name,
            'remark_name': self.remark_name,
            'sex': self.sex,
            'province': self.province,
            'city': self.city,
            'signature': self.signature
        }
        return data


class Group(Chat):
    """
    群聊对象
    """

    def __init__(self, raw, bot):
        super(Group, self).__init__(raw, bot)

    @property
    def members(self):
        """
        群聊的成员列表
        """
        def raw_member_list(update=False):
            if update:
                self.update_group(members_details=update)
            return self.raw.get('MemberList', list())

        ret = []
        for raw in raw_member_list(True):
            ret.append(Member(raw, self))
        return ret

    def __contains__(self, user):
        user_name = user.user_name
        for member in self.members:
            if member.user_name == user_name:
                return member

    def __iter__(self):
        for member in self.members:
            yield member

    def __len__(self):
        return len(self.members)

    def update_group(self, members_details=False):
        """
        更新群聊的信息
        :param members_details: 是否包括群聊成员的详细信息 (地区、性别、签名等)
        """

        def do():
            return self.bot.update_chatroom(self.user_name, members_details)

        super(Group, self).__init__(do(), self.bot)


class Friend(User):
    """
    好友对象
    """

    def set_remark_name(self, remark_name):
        """
        设置或修改好友的备注名称
        :param remark_name: 新的备注名称
        """

        return self.bot.set_alias(userName=self.user_name, alias=str(remark_name))


class Member(User):
    """
    群聊成员对象
    """

    def __init__(self, raw, group):
        super(Member, self).__init__(raw, group.bot)
        self.group = group

    @property
    def display_name(self):
        """
        在群聊中的显示昵称
        """
        return self.raw.get('DisplayName')
