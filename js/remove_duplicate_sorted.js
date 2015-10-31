'use strict';

exports = module.exports = {};

/**
 * Removes duplicates in a sorted array of numbers
 */
exports.removeDuplicates = function removeDuplicates(l) {
  if (l.length < 1) {
    return 0;
  }

  var currValue = l[0];
  var position = 1;
  var length = 1;

  for (var i = 1; i < l.length; i++) {
    if (currValue !== l[i]) {
      l[position] = l[i];
      currValue = l[i];
      position++;
      length++;
    }
  }

  return length;
};
