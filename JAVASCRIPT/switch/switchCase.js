
let day

switch (new Date().getDay()) {
    case 0:
        day = 'Sun'; break;
    case 1:
        day = 'Mon'; break;
    case 2:
        day = 'Tue'; break;
    case 3:
        day = 'Wed'; break;
    case 4:
        day = 'Thu'; break;
    case 5:
        day = 'Fri'; break;
    case 6:
        day = 'Sat'; break;
    default:
        console.log('Error: Invalid day number.');
        day = 'Null'
}

console.log(`Today is ${day}`);
