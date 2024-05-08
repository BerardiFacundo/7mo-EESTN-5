const fs = require('fs');

function filtrarNumerosConPropiedad(numeros, resultado) {
    const numerosFiltrados = numeros.filter(numero => {
        const strNumero = numero.toString();
        return strNumero.charAt(0) === strNumero.charAt(strNumero.length - 1);
    });

    for (const num of numerosFiltrados) {
        resultado.push(num.toString());
    }

    return numerosFiltrados.length;
}
fs.readFile('entrada.txt', 'utf8', (err, data) => {
    if (err) {
        console.error('Error al leer el archivo:', err);
        return;
    }

    const lineas = data.split('\n');
    const N = parseInt(lineas[0]);
    const numeros = lineas[1].split(' ').map(num => parseInt(num));

    const resultado = [];
    const cantidadNumerosCumplen = filtrarNumerosConPropiedad(numeros, resultado);
    fs.writeFile('salida.txt', `${cantidadNumerosCumplen}\n${resultado.join(' ')}`, err => {
        if (err) {
            console.error('Error al escribir el archivo de salida:', err);
            return;
        }
        console.log('Archivo de salida generado exitosamente.');
    });
});
