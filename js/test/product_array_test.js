'use strict';

var expect = require('chai').expect
  , mod = require('../product_array.js'); 

describe('Testing product array', function() {
  it('should work with a bunch of numbers', function() {
    var input = [1, 5, 3, 7, 8];
    var result = mod.calcProductArray(input);

    console.log(result);

    expect(result.length).to.eql(5);
    expect(result[0]).to.eql(5 * 3 * 7 * 8);
    expect(result[1]).to.eql(1 * 3 * 7 * 8);
    expect(result[2]).to.eql(1 * 5 * 7 * 8);
    expect(result[3]).to.eql(1 * 5 * 3 * 8);
    expect(result[4]).to.eql(1 * 5 * 3 * 7);
  });
});

