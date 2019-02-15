const ol = [18, 221, 45, 7646, 122, 311, 22]

const sortIntList = array => {
    const sortedArray = array.map((num, ind) => {
        if (!Number.isInteger(num)) {
            throw new Error(`Not integer in ${ind + 1}th element`)
        }
        return num
    })
    .sort((a, b) => {
        return a < b ? -1 : 1
    })
    return sortedArray
}

let x = sortIntList(ol)
console.log(x)