const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

// Función para calcular el número de Fibonacci
function fibonacci(n) {
    if (n <= 1) {
        return n;
    }
    let a = 0, b = 1, temp;
    for (let i = 2; i <= n; i++) {
        temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}

// Solicitar un número al usuario
readline.question('Ingresa un número para calcular Fibonacci: ', numero => {
    const n = parseInt(numero);

    if (isNaN(n) || n < 0) {
        console.log('Por favor, ingresa un número entero positivo.');
    } else {
        const resultado = fibonacci(n);
        console.log(`El número Fibonacci en la posición ${n} es ${resultado}.`);
    }
    
    readline.close();
});
