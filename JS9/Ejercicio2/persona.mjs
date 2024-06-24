class Persona { // Creamos la clase Persona con propiedades y método
    constructor(nombre, edad) {
      this.nombre = nombre;
      this.edad = edad;
    }
  
    mostrarInformacion() {
      console.log(`Nombre: ${this.nombre}, Edad: ${this.edad}`);
    }
  }
  
  export default Persona; //se exporta la clase 