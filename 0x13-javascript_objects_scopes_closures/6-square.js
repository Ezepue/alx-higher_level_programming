#!/usr/bin/node
class Square extends require('./5-square.js') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
