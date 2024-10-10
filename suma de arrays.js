// Función para sumar los números en una matriz de 3x2
function sumarMatriz(matriz) {
    let sumaTotal = 0;

    // Recorremos la matriz
    for (let i = 0; i < matriz.length; i++) {
        for (let j = 0; j < matriz[i].length; j++) {
            sumaTotal += matriz[i][j]; // Sumar el valor actual al total
        }
    }

    return sumaTotal;
}

// Definir el array de 3x2
const matriz = [
    [15, 22],
    [32, 34],
    [25, 61]
];

// Llamar a la función y mostrar el resultado
const suma = sumarMatriz(matriz);
console.log(`La suma de los números en la matriz es: ${suma}`);
