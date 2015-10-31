'use strict';

exports = module.exports = {};

exports.calcProductArray = function calcProductArray(arr) {
  var productArr = [];
  for (var i = 0; i < arr.length; i++) {
    productArr.push(1);
  }

  var product = 1;
  for (var i = 0; i < arr.length; i++) {
    productArr[i] *= product;
    product *= arr[i];
  }

  product = 1;
  for (var i = arr.length - 1; i >= 0; i--) {
    productArr[i] *= product;
    product *= arr[i];
  }

  return productArr;
};

