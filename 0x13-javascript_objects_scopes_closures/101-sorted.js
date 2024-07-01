#!/bin/usr/node
const dict = require('./101-data.js').dict;
const allList = Object.entries(dict);
const vals = Object.values(dict);
const uniqueVals = [...new Set(vals)];
const newDict = {};
for (const j in uniqueVals) {
  const list = [];
  for (const k in allList) {
    if (allList[k][1] === uniqueVals[j]) {
      list.unshift(allList[k][0]);
    }
  }
  newDict[uniqueVals[j]] = list;
}
console.log(newDict);
