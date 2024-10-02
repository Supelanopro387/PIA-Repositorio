<?php
// Solicitar la palabra al usuario
echo "Ingresa una palabra: ";
$palabra = trim(fgets(STDIN));

// Convertir la palabra a minúsculas y eliminar espacios
$palabraLimpia = strtolower(str_replace(' ', '', $palabra));

// Invertir la palabra
$palabraInvertida = strrev($palabraLimpia);

// Verificar si es un palíndromo
if ($palabraLimpia === $palabraInvertida) {
    echo "La palabra '{$palabra}' es un palíndromo.\n";
} else {
    echo "La palabra '{$palabra}' no es un palíndromo.\n";
}
?>
