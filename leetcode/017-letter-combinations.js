'use strict';

/*
Given a digit string, return all possible letter combinations that
the number could represent.
*/

var lettersForDigit = {
  '1': [],
  '2': ['a', 'b', 'c'],
  '3': ['d', 'e', 'f'],
  '4': ['g', 'h', 'i'],
  '5': ['j', 'k', 'l'],
  '6': ['m', 'n', 'o'],
  '7': ['p', 'q', 'r', 's'],
  '8': ['t', 'u', 'v'],
  '9': ['w', 'x', 'y', 'z'],
  '0': []
}

var stringProduct = function stringProduct(xs, ys) {
  if (xs.length === 0) xs = [''];
  if (ys.length === 0) ys = [''];
  var uniqueCombinations = [];
  for (var i = 0; i < xs.length; i++) {
    var x = xs[i];
    for (var j = 0; j < ys.length; j++) {
      var y = ys[j];
      var combination = x.concat(y);
      uniqueCombinations.push(combination);
    }
  }
  return uniqueCombinations;
};

var letterCombinations = function letterCombinations(digits) {
  if (digits === '') return [];
  var first = digits[0];
  var rest = digits.substr(1);
  return stringProduct(lettersForDigit[first], letterCombinations(rest));
};
