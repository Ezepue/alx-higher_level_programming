#!/usr/bin/node
const times = process.argv;
const intTimes = parseInt(times[2]);
if (isNaN(intTimes)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < intTimes; i++) {
    console.log('C is fun');
  }
}
