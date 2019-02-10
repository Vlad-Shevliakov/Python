const arr = [1, 'a', 2, 'b', 3, 'c']
arr.forEach((el, ind) => {
    if (typeof el !== 'number') arr.splice(ind, 1)
})

console.log(arr)