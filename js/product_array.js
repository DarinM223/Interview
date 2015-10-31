'use strict';

exports = module.exports = {};

/**
 * Given an array arr[] of n integers, construct a Product Array prod[] (of same size) 
 * such that prod[i] is equal to the product of all the elements of arr[] except arr[i]. 
 * Solve it without division operator and in O(n).
 *
 * @param {Array.<Integer>} arr the original array of numbers
 * @return {Array.<Integer>} a new array with the product of all the other numbers from arr
 */
exports.calcProductArray = function calcProductArray(arr) {
  var productArr = [];

  // Create a new array of all 1s
  for (var i = 0; i < arr.length; i++) {
    productArr.push(1);
  }

  var product = 1;
  // First multiply all of the previous multiplications to each element
  // So productArr[i] should be 1 * arr[1] * arr[2] * .... * arr[i - 1]
  for (var i = 0; i < arr.length; i++) {
    productArr[i] *= product;
    product *= arr[i];
  }

  product = 1;
  // Then multiply all of the multiplications after each element by going backward
  // So productArr[i] will be multiplied by 1 * arr[n-1] * arr[n-2] * ... * arr[i + 1]
  for (var i = arr.length - 1; i >= 0; i--) {
    productArr[i] *= product;
    product *= arr[i];
  }

  // The final result will be all of the previous multiplications * the next multiplications
  return productArr;
};

