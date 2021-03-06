#!/usr/bin/node
// Made by Christian Rojas to Holberton School 2021
class Rectangle {
  constructor (h, w) {
    if (h > 0 && w > 0) {
      this.width = h;
      this.height = w;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const auxiliar = this.width;
    this.width = this.height;
    this.height = auxiliar;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
