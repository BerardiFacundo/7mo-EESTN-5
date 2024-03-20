function traducirDelIdiomaP(frase) {
    let resultado = '';
    let i = 0;

    while (i < frase.length) {
        let letra = frase[i];
        if (letra === 'p' && i < frase.length - 2 && frase[i + 2] === letra.toLowerCase()) {
            resultado += frase[i + 1].toUpperCase();
            i += 3;
        } else {
            resultado += letra;
            i++;
        }
    }

    return resultado;
}