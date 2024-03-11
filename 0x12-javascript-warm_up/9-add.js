#!/usr/bin/node
function add (a, b) {
	console.log(a + b);
  }
  const args = process.argv;
  const first = parseInt(args[2]);
  const second = parseInt(args[3]);
  if (isNaN(first) || isNaN(second)) {
	console.log(NaN);
  } else {
	add(first, second);
  }
