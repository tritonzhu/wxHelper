from flask import Flask, jsonify, request, render_template, make_response
from bot import Bot

webapp = Flask(__name__, template_folder='../templates', static_folder='../static')

bot = Bot()


@webapp.route('/')
def root():
    return render_template('index.html')


@webapp.route('/qrcode.png')
def get_qr():
    bot.get_uuid()
    response = make_response(bot.get_qrcode())
    response.headers['Content-Type'] = 'image/png'
    return response


@webapp.route('/login')
def login():
    bot.login()
    return make_response('ok')


@webapp.route('/friends')
def friends():
    return jsonify(bot.friends())


@webapp.route('/groups')
def groups():
    return jsonify(bot.groups())


@webapp.route('/friends/<username>/avatar')
def friend_avatar(username):
    response = make_response(bot.get_friend_avatar(username))
    response.headers['Content-Type'] = 'image/jpg'
    return response


@webapp.route('/groups/<username>/avatar')
def group_avatar(username):
    response = make_response(bot.get_group_avatar(username))
    response.headers['Content-Type'] = 'image/jpg'
    return response


if __name__ == '__main__':
    webapp.run(port=11235)
