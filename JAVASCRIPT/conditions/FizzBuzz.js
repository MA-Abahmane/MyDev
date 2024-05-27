/// FizzBuzz Challenge


min = Number(prompt('[FizzBuzz] Enter The starting number: '))
max = Number(prompt('[FizzBuzz] Enter the ending number: '))

while (max < min) 
    max = Number(prompt('Enter the ending number: '))



for (let i = min; i <= max; i++){
    if (i % 3 == 0 && i % 5 == 0)
        console.log('FizzBuzz');
    else if (i % 3 == 0)
        console.log('Fizz');
    else if (i % 5 == 0)
        console.log('Buzz');
    else 
        console.log(i);
}
