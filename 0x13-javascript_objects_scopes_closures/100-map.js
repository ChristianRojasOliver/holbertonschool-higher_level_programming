#!/usr/bin/node
// Made by Christian Rojas to Holberton School 2021
const list = require('./100-data').list;
console.log(list);
const map1 = list.map((xd, i) => xd * i);
console.log(map1);
