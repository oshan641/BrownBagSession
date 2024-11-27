# from flask import Flask
# from flask_socketio import SocketIO
# from flask_cors import CORS
# from gevent import pywsgi
# from geventwebsocket.handler import WebSocketHandler

# app = Flask(__name__)
# CORS(app)

# # Simplified SocketIO configuration
# socketio = SocketIO(
#     app, 
#     cors_allowed_origins="*",
#     logger=True, engineio_logger=True
# )
# # socketio.init_app(app)


# @app.route('/')
# def index():
#     return "WebSocket Server Running"

# @socketio.on('connect')
# def handle_connect():
#     print('Client connected')
#     # socketio.emit('response', {'data':'success'})


# @socketio.on('disconnect')
# def handle_disconnect():
#     print('Client disconnected')
#     socketio.emit('response', {'data':'failure'})


# @socketio.on('message')
# def handle_message(data):
#     print('Received message:', data)
#     socketio.emit('response', {'data': data})

# if __name__ == '__main__':
#     pywsgi.WSGIServer(("", 5020), app, handler_class=WebSocketHandler).serve_forever()

# from geventwebsocket.handler import WebSocketHandler
# from gevent.pywsgi import WSGIServer
# from flask import Flask, request, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/api')
# def api():
#     if request.environ.get('wsgi.websocket'):
#         ws = request.environ['wsgi.websocket']
#         print(ws)
#         while True:
#             message = ws.receive()
#             print('received >> ', message)
#             ws.send(message)
#     return

# if __name__ == '__main__':
#     import logging
#     import sys
#     logging.basicConfig(format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
#     datefmt='%Y-%m-%d:%H:%M:%S',
#     level=logging.DEBUG)
#     logger = logging.getLogger()
#     h = logging.StreamHandler()
#     h.setLevel(logging.DEBUG)
#     logger.addHandler(h)
#     http_server = WSGIServer(('',5000), app, handler_class=WebSocketHandler)
#     http_server.serve_forever()

from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_sock import Sock

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
sock = Sock(app)


@sock.route('/echo')
def echo(ws):
    while True:
        data = ws.receive()
        ws.send({"status": "success"})

if __name__ == '__main__':
    # socketio.run(app,port=5500)
    app.run('localhost', 5030)