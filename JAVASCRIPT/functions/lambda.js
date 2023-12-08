

a = Number(prompt('Enter Number a'))
b = Number(prompt('Enter Number b'))


// function add(a, b)
// {
//     return (a + b)
// }


add = (a, b) => a + b
sub = (a, b) => a - b
mul = (a, b) => a * b
div = (a, b) => a / b

console.log(a + ' + ' + b + ' = ' + add(a, b))
console.log(a + ' - ' + b + ' = ' + sub(a, b))
console.log(a + ' * ' + b + ' = ' + mul(a, b))
console.log(a + ' / ' + b + ' = ' + div(a, b))