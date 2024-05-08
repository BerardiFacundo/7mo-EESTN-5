function generarSecuencia() {
    const entradaSemilla = document.getElementById('semilla');
    const resultadoParrafo = document.getElementById('resultado');
    const semilla = parseInt(entradaSemilla.value);

    if (isNaN(semilla) || semilla < 1 || semilla >= 10000) {
        resultadoParrafo.textContent = "Ingrese una semilla válida (1 ≤ S < 10000).";
        return;
    }

    const secuencia = [];
    let actual = semilla;

    while (actual !== 1) {
        secuencia.push(actual);
        if (actual % 2 === 0) {
            actual = actual / 2;
        } else {
            actual = actual * 3 + 1;
        }
    }
    secuencia.push(1);
    const longitud = secuencia.length;
    const maximoNumero = Math.max(...secuencia);

    resultadoParrafo.textContent = `\n Longitud de la secuencia: ${longitud}`;
    resultadoParrafo.textContent += `\n Número más grande en la secuencia: ${maximoNumero}`;
}
