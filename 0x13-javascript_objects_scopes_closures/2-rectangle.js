#!/usr/bin/node
// Made by Christian Rojas to Holberton School 2021
class Rectangle {
  constructor (h, w) {
    if (h > 0 && w > 0) {
      this.width = h;
      this.height = w;
    }
  }
}
module.exports = Rectangle;
