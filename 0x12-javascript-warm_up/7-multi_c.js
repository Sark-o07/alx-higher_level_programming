#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < Number(process.argv[2]); i++) {
    console.log('C is fun');
  }
}
