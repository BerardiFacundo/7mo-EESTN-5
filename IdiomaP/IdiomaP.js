function traducirIdiomaP(frase) {
    const vocales = ['a', 'e', 'i', 'o', 'u'];
    let resultado = '';

    for (let i = 0; i < frase.length; i++) {
        const letra = frase[i];
        
        if (vocales.includes(letra.toLowerCase())) {
            resultado += letra + 'p' + letra.toLowerCase();
        } else {
            resultado += letra;
        }
    }

    return resultado;
}