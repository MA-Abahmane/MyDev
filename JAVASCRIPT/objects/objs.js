/// Constructor object creation

function Car(name, model, prise, stock) {
    this.name = name;
    this.model = model;
    this.prise = prise;
    this.stock = stock;

    this.verifyStock = () => {
        if (this.stock > 0)
            console.log('Stock available');
        else 
            console.log('Stock unavailable');
    }

    this.display = () => {
        console.log(`Car name: ${this.name}\n
        Model: ${this.model}\n
        Prise: ${this.prise}\n
        Stock: ${this.stock}`);
    }
}

c1 = new Car('Abahmane', '2025', 50000, 500)
c2 = new Car('Abahmane', '2027', 70000, 800)

c1.verifyStock()

c1.stock += 700
delete c1.stock

c1.display()




// Regular Object Creation

const car = {
    name: 'Abahmane',
    model: '2025',
    prise: 50000,
    stock: 500,

    verifyStock: function () {
        if (this.stock > 0)
            console.log('Stock available');
        else 
            console.log('Stock unavailable');
    },

    display: function () {
        console.log(`Car name: ${this.name}\n
        Model: ${this.model}\n
        Prise: ${this.prise}\n
        Stock: ${this.stock}`);
    }
}

car.stock += 700

console.log(`${car.stock} cars in stock`); 

car.display()


for (let key in car) {
    if (typeof(car[key]) == 'function')
        console.log(`${key}`);
    else
        console.log(`${key}: ${car[key]}`);
}


/// Arrays \\\

l1 = [1, 2, 3, 4, 5]

l1 = new Array(1, 2, 3, 4, 5)

l1 = new Array(5)
l1[0] = 1
l1[1] = 2
l1[2] = 3
l1[3] = 4
l1[4] = 5


// Array Methods

l1.length // list length => 5

l1.indexOf(3)  // index of 3 => 2

l1[1] // => element at index 1 => 2

l1 = 'amine'
l1.charAt(4)

console.log(l1.substring(1, 2))
