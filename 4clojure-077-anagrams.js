#!/usr/bin/env node

const groupAnagram = (memo, word) => {
  const key = word.split('').sort().join('')
  memo[key] ? memo[key].add(word) : memo[key] = new Set([word])
  return memo
}

const values = (obj) =>
  Object.keys(obj).map(key => obj[key])


const anagrams = (words) =>
  values(words.reduce(groupAnagram, {}))


console.log(anagrams(['veer', 'lake', 'item', 'kale', 'mite', 'ever']))
