const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

// Función para contar las vocales en una palabra
function contarVocales(palabra) {
    const vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
    let contador = 0;

    // Recorremos cada letra de la palabra
    for (let letra of palabra) {
        if (vocales.includes(letra)) {
            contador++;
        }
    }

    return contador;
}

// Solicitar la palabra al usuario
readline.question('Ingresa una palabra: ', palabra => {
    const numeroDeVocales = contarVocales(palabra);
    console.log(`La palabra "${palabra}" tiene ${numeroDeVocales} vocal(es).`);
    readline.close();
});
