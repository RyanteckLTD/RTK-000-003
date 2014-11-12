/*
 * RTK-000-003 Node.js an Cylon Basis
 * Licensed under the GNU GPL V3 License
 * (C) Seravo Oy 2014
 * Contributors: Otto Kekäläinen
 *
 * This Node.js code is designed to be compatible with the JavaScript
 * pseudo-code that the Blockly visual programming environment produces.
 * You can for example code a figure that the Artist at code.org can draw,
 * and then run that exact code with this Node.js module so that
 * it is executed by the Ryantek robot.
 *
 * Async queue is used to force the code run in sequense as it does in Blockly
 */

var async = require('async');

/*
 * This code is build using Cylon, so in theory it could run on multiple
 * different hardware platforms.
 *
 * GPIO pin configuration:
 * 11 = right wheel forwards (BCM 17)
 * 12 = right wheel backwards (BCM 18)
 * 15 = left wheel forwards (BCM 22)
 * 16 = left wheel backwards (BCM 23)
 *
 * See also http://cylonjs.com/documentation/platforms/raspberry-pi/
 *
 * On the Ryantek robot on full 360 degrees turn is about 1.52 seconds
 * of power for the electric motors:
 */

var circleTime = 1.52;

/*
 * 100 pixels equal 2 seconds of power for forward or backward movement
 * 1 pixel is 0.02 seconds
 */
var pixelTime = 2/100;


/*
 * Make a short 0.5 second pause between each step
 */
var pauseTime = 0.5;

var Cylon = require('cylon');

Cylon.robot({
  connection: {
    name: 'raspi',
    adaptor: 'raspi'
  },
  devices: [
    {
      name: 'rwheelf',
      driver: 'led',
      pin: 11
    },
    {
      name: 'rwheelb',
      driver: 'led',
      pin: 12
    },
    {
      name: 'lwheelf',
      driver: 'led',
      pin: 15
    },
    {
      name: 'lwheelb',
      driver: 'led',
      pin: 16
    },
  ],
  work: function(my) {

    function runStep(stepName, stepParameter, callback) {

      switch (stepName) {
        case 'moveForward':
          my.rwheelf.turnOn();
          my.lwheelf.turnOn();
          // 100 pixels equal 1 second
          after((stepParameter*pixelTime).seconds(), function () {
            my.rwheelf.turnOff();
            my.lwheelf.turnOff();
            after(pauseTime.seconds(), function () {
              callback();
            });
          });
          break;

        case 'moveBackward':
          my.rwheelb.turnOn();
          my.lwheelb.turnOn();
          // 100 pixels equal 1 second
          after((stepParameter*pixelTime).seconds(), function () {
            my.rwheelb.turnOff();
            my.lwheelb.turnOff();
            after(pauseTime.seconds(), function () {
              callback();
            });
          });
          break;

        case 'turnLeft':
          my.rwheelf.turnOn();
          my.lwheelb.turnOn();
          // 90 degrees equal 0.38 seconds
          // 360 degrees equal 1.52 seconds
          after((stepParameter/360*circleTime).seconds(), function () {
            my.rwheelf.turnOff();
            my.lwheelb.turnOff();
            after(pauseTime.seconds(), function () {
              callback();
            });
          });
          break;

        case 'turnRight':
          my.rwheelb.turnOn();
          my.lwheelf.turnOn();
          // 90 degrees equal 0.38 seconds
          // 360 degrees equal 1.52 seconds
          after((stepParameter/360*circleTime).seconds(), function () {
            my.rwheelb.turnOff();
            my.lwheelf.turnOff();
            after(pauseTime.seconds(), function () {
              callback();
            });
          });
          break;

       }
    }

    function moveForward(pixels) {
      if (pixels === undefined) {
        pixels = 100; // default 100 pixels
      }
      q.push({name: 'moveForward', parameter: pixels});
    }

    function moveBackward(pixels) {
      if (pixels === undefined) {
        pixels = 100; // default 100 pixels
      }
      q.push({name: 'moveBackward', parameter: pixels});
    }

    function turnLeft(degrees) {
      if (degrees === undefined) {
        degrees = 90; // default 90 degrees
      }
      q.push({name: 'turnLeft', parameter: degrees});
    }

    function turnRight(degrees) {
      if (degrees === undefined) {
        degrees = 90; // default 90 degrees
      }
      q.push({name: 'turnRight', parameter: degrees});
    }

    // dummy functions that might be called but will not do anything
    function colour_random() {}
    function penColour() {}
    function penWidth() {}

    // Create queue that processes one task at the time
    var q = async.queue(function (task, callback) {
      console.log(task.name + '(' + task.parameter + ');');
      runStep(task.name, task.parameter, callback);
    }, 1);


    // assign a callbacks
    q.saturated = function() {
      console.log('Queue max concurrency.');
    }
    q.drain = function() {
      console.log('Program completed.');
    }

    // Use same syntax for movement as in code.org tutorials and Blockly
    // ** EDIT BELOW TO MAKE YOUR OWN MOVEMENT PATTERN **

    for (x = 0; x < 10; x++) {
      turnRight(30);
      moveForward(10);
      turnLeft(30);
      moveForward(10);
    }

      moveBackward(300);
      moveForward(50);

    // ** EDIT ABOVE TO MAKE YOUR OWN MOVEMENT PATTERN **
    // Remember to run this as sudo!

    // Reset all pins, just to be sure
    my.rwheelf.turnOff();
    my.lwheelf.turnOff();
    my.rwheelb.turnOff();
    my.lwheelb.turnOff();

    process.on('SIGINT', function() {
      console.log("Caught interrupt signal");
      my.rwheelf.turnOff();
      my.lwheelf.turnOff();
      my.rwheelb.turnOff();
      my.lwheelb.turnOff();
      process.exit();
    });

    process.on('exit', function() {
      console.log("Program exiting");
      my.rwheelf.turnOff();
      my.lwheelf.turnOff();
      my.rwheelb.turnOff();
      my.lwheelb.turnOff();
      process.exit();
    });

  }
}).start();

