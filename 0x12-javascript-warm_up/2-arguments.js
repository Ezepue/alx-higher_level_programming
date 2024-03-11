#!/usr/bin/node
const args = process.argv;
const argLen = args.length - 2;
if (argLen === 0) {
  console.log('No argument');
} else if (argLen === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
