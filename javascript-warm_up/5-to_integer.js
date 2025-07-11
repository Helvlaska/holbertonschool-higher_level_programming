#!/usr/bin/node

const arg = process.argv[2];
// Transforme une value en entier
const number = parseInt(arg);

// isNaN = is Not a Number
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${number}`);
}
