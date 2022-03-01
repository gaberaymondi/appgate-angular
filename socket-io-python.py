import eventlet
import socketio
import logging

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})


# @sio.on('connect')
# def connect(sid, environ):
#     print('connect ', sid)

# @sio.on('event')
# def message(sid, data):
#     print('msg ', data)

@sio.on('LEAK')
def process_message(data):
    print("function is working")
    logging.warning("Leak received: "+data)
    

# @sio.event
# def connect(sid, environ):
#     print('connect ', sid)
    


# @sio.event
# def my_message(sid, data):
#     print('message ', data)
#     sio.emit('test event', {'test event':'THIS is SOME NEW DATA!!!'})



# @sio.event
# def disconnect(sid):
#     print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 3001)), app)