#!/usr/bin/node
const arg = process.argv;
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

function add(a, b) {
  console.log(a + b)
}

add(a, b);
