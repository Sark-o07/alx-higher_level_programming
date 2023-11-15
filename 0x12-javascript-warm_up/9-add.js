#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}
const numA = Number(process.argv[2]);
const numB = Number(process.argv[3]);
add(numA, numB);
