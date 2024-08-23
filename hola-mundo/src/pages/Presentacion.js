import React from 'react';
import '../styles/Presentacion.css';
import FotoPresentacion from '../assets/FotoPresentacion.jpg'
import TarjetaPresentacion from '../components/TarjetaPresentacion'; 

function Presentacion() {
  return (
    <div className="container">
      <h1>Mí Tarjeta De Presentación</h1>
      <TarjetaPresentacion
        nombre="Facundo"
        apellido="Berardi"
        profesion="Desarrollador Web - Front-end Developer - Tecnico en Informatica"
        imagen={FotoPresentacion} 
      />
    </div>
  );
}

export default Presentacion;