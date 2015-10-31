'use strict';

var expect = require('chai').expect
  , mod = require('../remove_duplicate_sorted.js');

describe('Testing remove duplicates from sorted array', function() {
  it('should remove duplicates from sorted array', function() {
    var arr = [1, 1, 1, 2, 2, 3, 3, 3];
    var result = mod.removeDuplicates(arr);

    expect(arr).to.eql([1, 2, 3, 2, 2, 3, 3, 3]);
    expect(result).to.eql(3);
  });

  it('should return 0 length if array length is 0', function() {
    var arr = [];
    var result = mod.removeDuplicates(arr);

    expect(arr).to.eql([]);
    expect(result).to.eql(0);
  });

  it('should return 1 length if array length is 1', function() {
    var arr = [1];
    var result = mod.removeDuplicates(arr);

    expect(arr).to.eql([1]);
    expect(result).to.eql(1);
  });

  it('should return 1 length if all elements are the same', function() {
    var arr = [1, 1, 1, 1, 1, 1];
    var result = mod.removeDuplicates(arr);

    expect(arr).to.eql([1, 1, 1, 1, 1, 1]);
    expect(result).to.eql(1);
  });
});
