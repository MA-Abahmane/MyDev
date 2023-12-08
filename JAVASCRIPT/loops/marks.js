

i = 1
mSum = 0
while (i <= 20)
{
    n = Number(prompt('Enter -1 to quit\nEnter mark number ' + i))
    if (n != -1)
        mSum += n;
    else
        break;
    i++
}


myn = mSum / (i - 1);
if (myn)
{
    console.log(myn);
}
else
    console.log('No marks entered');