/*
    for OF: return Object Values
    for IN: return Object Indexes

    Break; break out of loop
    Continue; move on to next iteration
*/

l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

console.log('Length: ' , l.length) // 10

for (i in l)
    console.log(i);  // Indexes:  0 1 2...9


for (i of l)
    console.log(i);  // Values:  a b c...j



d = {
 "a": 1, "b": 2,
 "c": 3, "d": 4,
 "e": 5, "f": 6,
 "g": 7, "h": 8,
 "i": 9, "j": 10
}

 for (key in d) console.log(`"${key}" <|> ${d[key]}`);


/// forEach()
// l.forEach((x) => console.log('=>', x));
