#!/usr/bin/node
const times = process.argv;
const intTimes = parseInt(times[2]);
if (isNaN(intTimes)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < intTimes; i++) {
    let row = '';
    for (let j = 0; j < intTimes; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
