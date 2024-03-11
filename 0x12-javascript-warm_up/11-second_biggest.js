#!/usr/bin/node
const args = process.argv;
let largest;
let first;

if (args.length < 4) {
  console.log(0);
} else {
  largest = parseInt(args[2]);
  for (let i = 2; i < args.length; i++) {
    if (parseInt(args[i]) > largest) {
      largest = parseInt(args[i]);
    }
  }
  first = largest;
  largest = Number.NEGATIVE_INFINITY;
  for (let i = 2; i < args.length; i++) {
    if (parseInt(args[i]) === first) {
      continue;
    }
    if (parseInt(args[i]) > largest) {
      largest = parseInt(args[i]);
    }
  }
  console.log(largest);
}
