const f = (() => {
    let x = 0
    return () => {
        ++x
        console.log(x)
    }
})

const x = f()

console.log(x())
console.log(x())
console.log(x())
console.log(x())