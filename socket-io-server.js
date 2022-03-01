// var app = require('express')();
// var server = require('http').Server(app);
// var io = require('socket.io')(server);
// var cors = require('cors');

const app = require('express')();
const http = require('http').createServer(app);
const io = require('socket.io')(http, {
    cors: {
        origins: ['http://localhost:4200']
    }
});

io.on('connection', function (socket) {
    // app.use(cors());
    console.log("A user connected");
    socket.emit('test event', 'THIS is SOME NEW DATA!!!');
});

http.listen(3000, () => {
    // app.use(cors());
    console.log("Socket.io server is listening on port 3000");
});