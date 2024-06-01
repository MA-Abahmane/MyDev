

/**
 * My Kitchen
 */


const p = new Promise((resolve, reject) => {
    
    setTimeout(() => {
        let x = 1

        if (x === 1)
            resolve('Data Loaded')
        else if (x === 0)
            reject('Loading Failed')
    }, 3000)
})

p
.then((message) => console.log('[Success]', message))
.catch((message) => console.log('[Failure]', message))
