function esNombreElegante(nombre) {
    return nombre.charAt(0) === 'a' && nombre.charAt(nombre.length - 1) === 'a';
}

function procesarNombre(nombre) {
    const elegante = esNombreElegante(nombre);
    console.log(`${nombre} es elegante: ${elegante}`);
}

const nombres = process.argv.slice(2);

for (let nombre of nombres) {
    procesarNombre(nombre.toLowerCase());
}