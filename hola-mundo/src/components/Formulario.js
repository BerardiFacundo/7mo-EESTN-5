import React, { useState } from 'react';
import './Formulario.css';

function Formulario() {
  const [nombre, setNombre] = useState('');
  const [mensaje, setMensaje] = useState('');

  const manejarCambio = (e) => {
    setNombre(e.target.value);
  };

  const manejarEnvio = (e) => {
    e.preventDefault();
    setMensaje(`¡Bienvenido, ${nombre}!`);
  };

  return (
    <div className="formulario-container">
      <form onSubmit={manejarEnvio} className="formulario">
        <label htmlFor="nombre">Nombre:</label>
        <input 
          type="text" 
          id="nombre" 
          value={nombre} 
          onChange={manejarCambio} 
          placeholder="Introduce tu nombre"
        />
        <button type="submit" className="boton-enviar">Enviar</button>
      </form>
      {mensaje && <p className="mensaje-bienvenida">{mensaje}</p>}
    </div>
  );
}

export default Formulario;
