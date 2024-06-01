/**
 * map() =>
 *   iterating trough each elements
 *   of a copy of the original list
 */

// convert a list of Fahrenheit values to Celsius

F = [0, 32, 40, 65, 45, 70, 88]

// for each enement subtract 32 to convert to Celsius
C = F.map(x => x - 32)

// print modified list
console.log('Fer: ', F);
console.log('Cel: ', C);