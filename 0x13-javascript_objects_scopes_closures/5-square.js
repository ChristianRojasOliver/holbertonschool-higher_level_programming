#!/usr/bin/node

const Rectangle = require('./4-rectangle');

// Made by Christian Rojas to Holberton School 2021
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
