process.stdin.resume();
process.stdin.setEncoding('utf8');
const util = require('util');

const arDrone = require('ar-drone');
const client = arDrone.createClient();
client.createRepl();
client.config('control:altitude_max', 1000);
client.ftrim();
client.takeoff(function(){
  this.calibrate(0)
})
client.stop();

const commandMapper = {"0": client.stop, "1": client.up, "2": client.down, "3": client.left, "4": client.right, "5": client.front, "6": client.back, "7": client.clockwise, "8": client.counterClockwise}

const speed = 0.2;
process.stdin.on('data', function (command) {
  let droneCommand = command.replace('\n', '');
  // do something with the command here, command is string : "1", "2", "3" etc
  //let commandCallback = null;
  switch(droneCommand){
    case "1":
      client.up(speed);

      break;
    case "2":
      client.down(speed);

      break;
    case "3":
      client.left(speed);

      break;
    case "4":
      client.right(speed);

      break;
    case "5":
      client.front(speed);

      break;
    case "6":
      client.back(speed);

      break;
    case "7":
      client.clockwise(speed);

      break;
    case "8":
      client.counterClockwise(speed);

      break;
    default:
      break;
  }
  //commandMapper[droneCommand](speed);
  client.after(500, function(){
    this.stop();
    console.log('done');
  })
  // quit is to stop connecting to the drone. This should land the drone safely.
  if (droneCommand === 'quit'){
    done();
  }
});

function done() {
  client.land();
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
