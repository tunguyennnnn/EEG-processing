const arDrone = require('ar-drone');
const client = arDrone.createClient();
client.createRepl();
client.config('control:altitude_max', 1000);
client.ftrim();
client.takeoff(function(){
  this.calibrate(0)
})
client.stop();
