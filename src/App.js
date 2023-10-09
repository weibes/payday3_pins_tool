import React from 'react';

export default function App() {
    return(
        <h1>hello nerd</h1>
    )

}


function findFourDigitPins(numbers) {
    let retList = []
    if (numbers.length == 4) {
        let allPerms = perm(numbers)
        for (const elem of allPerms) {
            retList.push(elem)
        }
    } else if (numbers.length == 1) {
        let oneItem = []
        for (i = 0; i < 4; i++) {
            oneItem.push(numbers[0])
        }
        retList = oneItem
    } else { // need to add more, add recursive call
        for (const num of numbers) {
            let currNumbers = numbers.slice()
            currNumbers.push(num)
            retList.concat(findFourDigitsPins(currNumbers))
        }
    }
    // check for dupes in a dumb stupid way
    let retListCheck = []
    for (const item of retList) {
        if (!retListCheck.includes(item)) {
            retListCheck.push(item)
        }
    }
    retList = retListCheck
    return retList
}


function perm(xs) {
    let ret = [];
  
    for (let i = 0; i < xs.length; i = i + 1) {
      let rest = perm(xs.slice(0, i).concat(xs.slice(i + 1)));
  
      if(!rest.length) {
        ret.push([xs[i]])
      } else {
        for(let j = 0; j < rest.length; j = j + 1) {
          ret.push([xs[i]].concat(rest[j]))
        }
      }
    }
    return ret;
  }
