// process.stdin.resume();
// process.stdin.setEncoding('utf8');
// var util = require('util');
//
// process.stdin.on('data', function (text) {
//   console.log('received data:' + text);
//   if (text === 'quit\n') {
//     done();
//   }
// });
//
// function done() {
//
//   process.exit();
// }

const net = require('net');


net.createServer(function(socket){
  let command = ''
  socket.on('data', function(data){
    command = 'XXX' + data;
  });
}).listen(5000);
