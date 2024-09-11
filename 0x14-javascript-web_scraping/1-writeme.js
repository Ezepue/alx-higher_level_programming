#!/usr/bin/node
// script that writes a string to a file.
// The first argument is the file path
// The second argument is the string to write
// The content of the file must be written in utf-8
const fs = require('fs');
const filename = process.argv[2];
const content = process.argv[3];
fs.writeFile(filename, content, (err) => {
  if (err) {
    console.log(err);
  }
});
