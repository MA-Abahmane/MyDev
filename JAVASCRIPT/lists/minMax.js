

list = []

for (i = 0; i < 5; i++)
{
    n = Number(prompt('Enter your number ' + i))
    list.push(n)
}

console.log(max(list))