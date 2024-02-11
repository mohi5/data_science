// HigherOrderFunction OR First-Class Function
// A function that returns a function or takes other functions as arguments is called higher-order function.
const powerTwo = (n) => {
    return n ** 2
}
function powerCube(powerTwo, n){
    return powerTwo(n) * n
}
console.log(powerCube(powerTwo, 3))