var http = require("http");
var url = require('url');
var fs = require('fs');
var io = require('socket.io');
var Redis = require('ioredis');
var redis = new Redis();

var server = http.createServer(function(request, response){
    var path = url.parse(request.url).pathname;
    switch(path){
        case '/':
            response.writeHead(200, {'Content-Type': 'text/html'});
            response.write('hello world');
            response.end();
            break;
        case '/index.html':
            fs.readFile(__dirname + path, function(error, data){
                if (error){
                    response.writeHead(404);
                    response.write("opps this doesn't exist - 404");
                    response.end();
                }
                else{
                    response.writeHead(200, {"Content-Type": "text/html"});
                    response.write(data, "utf8");
                    response.end();
                }
            });
            break;
        default:
            response.writeHead(404);
            response.write("opps this doesn't exist - 404");
            response.end();
            break;
    }
});

server.listen(8001);
var listener = io.listen(server);

listener.sockets.on('connection', function(socket) {
    // Send data to client
    setInterval(function() {
        redis.lrange('myList', 0, 9, function(err, data) {
            socket.emit('data', {'data': data})
        });
    }, 1000);
});
