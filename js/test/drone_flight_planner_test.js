'use strict';

var expect = require('chai').expect
  , mod = require('../drone_flight_planner.js');

describe('Testing drone flight planner', function() {
  it('should work with example flight plan', function() {
    var exampleFlightPlan = [{ x: 0, y: 2, z: 10 }, { x: 3, y: 5, z: 0 }, { x: 9, y: 20, z: 6 }, 
      { x: 10, y: 12, z: 15 }, { x: 10, y: 10, z: 8 } ];

    var result = mod.calcFuel(exampleFlightPlan);
    expect(result).to.eql(5);
  });
});

