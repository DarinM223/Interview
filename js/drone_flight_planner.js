'use strict';

exports = module.exports = {};

/**
 * Drone flight planner
 *
 * Drone can go left and right without using any fuel. To fly higher, the drone burns 1 liter of fuel. 
 * To fly lower, the drone gains 1 liter of fuel. Given an array of 3D coordinates, find the minimal 
 * amount of fuel the drone would need to fly through this route.
 *
 * @param {Array.<Object>} route the route to travel as a list of coordinate objects
 *
 * Example:
 * [{ x: 0, y: 2, z: 10 }, { x: 3, y: 5, z: 0 }, { x: 10, y: 20, z: 6 }, 
 * { x: 10, y: 12, z: 15 }, { x: 10, y: 10, z: 8 }]
 */
exports.calcFuel = function calcFuel(route) {
  var maxHeight = route[0].z;

  for (var i = 0; i < route.length; i++) {
    if (route[i].z > maxHeight) {
      maxHeight = route[i].z;
    }
  }

  return maxHeight - route[0].z;
}

