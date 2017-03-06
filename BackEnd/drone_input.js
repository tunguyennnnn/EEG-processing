process.stdin.resume();
process.stdin.setEncoding('utf8');
const util = require('util');

process.stdin.on('data', function (command) {
  let command = command.replace('\n', '');
  // do something with the command here, command is string : "1", "2", "3" etc


  // quit is to stop connecting to the drone. This should land the drone safely.
  if (command === 'quit') {
    done();
  }
});

function done() {

  process.exit();
}

// const net = require('net');
//
//
// net.createServer(function(socket){
//   let command = ''
//   socket.on('data', function(data){
//     command = 'XXX' + data;
//   });
// }).listen(5000);
