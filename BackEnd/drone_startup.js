const arDrone = require('ar-drone');
const client = arDrone.createClient();
client.createRepl();

client.takeoff(function(){
  this.calibrate(0)
})
