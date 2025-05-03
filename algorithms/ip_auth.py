from flask import Flask, request, abort

app = Flask(__name__)
ALLOWED_IPS = ['127.0.0.1', '192.168.0.2']

@app.before_request
def limit_remote_addr():
    if request.remote_addr not in ALLOWED_IPS:
        abort(403)

@app.route('/')
def index():
    return 'Welcome, authorized client!'

if __name__ == '__main__':
    app.run()
