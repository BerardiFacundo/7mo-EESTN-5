import Calculadora from './calculadora.mjs'; // Importamos la clase Calculadora desde calculadora.js

const calculadora = new Calculadora();

const resultadoMultiplicacion = calculadora.multiplicar(5, 3);
const resultadoDivision = calculadora.dividir(10, 2);

console.log('Multiplicación:', resultadoMultiplicacion);
console.log('División:', resultadoDivision);