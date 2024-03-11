#!/usr/bin/node
function factorial (a) {
	if (a === 0) {
	  return 1;
	}
	return (a * factorial(a - 1));
  }
  const args = process.argv;
  const num = parseInt(args[2]);
  if (isNaN(num)) {
	console.log(1);
  } else {
	console.log(factorial(num));
  }
