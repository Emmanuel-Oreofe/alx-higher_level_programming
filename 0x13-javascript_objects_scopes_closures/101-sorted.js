#!/usr/bin/node
const dict = require('./101-data.js').dict;
let const = {};
for (let const in dict) {
  if (newDict[dict[key]] === undefined) {
    newDict[dict[key]] = [key];
  } else {
    newDict[dict[key]].push(key);
  }
}
console.log(newDict);
