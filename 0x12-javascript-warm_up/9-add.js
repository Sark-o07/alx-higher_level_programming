#!/usr/bin/node
function add(a, b) {
  console.log(a + b);
}
let numA = Number(process.argv[2]);
let numB = Number(process.argv[3]);
add(numA, numB);
