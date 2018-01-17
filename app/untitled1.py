from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/<user1>')
def vote_to_user(user1):
    return '给 %s 投票' % user1





if __name__ == '__main__':
    app.run(host='0.0.0.0')
