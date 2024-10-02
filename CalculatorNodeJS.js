const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  });
  
  // Funciones para cada operación
  function add(a, b) {
    return a + b;
  }
  
  function subtract(a, b) {
    return a - b;
  }
  
  function multiply(a, b) {
    return a * b;
  }
  
  function divide(a, b) {
    if (b === 0) {
      return "Error: Division by zero is not allowed";
    }
    return a / b;
  }
  
  // Objeto que asocia las operaciones con las funciones
  const operations = {
    add: add,
    subtract: subtract,
    multiply: multiply,
    divide: divide
  };
  
  // Solicitar entrada del usuario
  readline.question('Enter the first number: ', num1 => {
    readline.question('Enter the second number: ', num2 => {
      readline.question('Enter the operation (add, subtract, multiply, divide): ', operation => {
        
        num1 = parseFloat(num1);
        num2 = parseFloat(num2);
  
        // Verificar si la operación es válida
        if (operations[operation]) {
          const result = operations[operation](num1, num2);
          console.log(`The result is: ${result}`);
        } else {
          console.log("Error: Invalid operation");
        }
        
        readline.close();
      });
    });
  });