#!/usr/bin/node

// Made by Christian Rojas to Holberton School 2021
let i = 0;

exports.logMe = function (item) {
  console.log(i + ': ' + item);
  i++;
};
