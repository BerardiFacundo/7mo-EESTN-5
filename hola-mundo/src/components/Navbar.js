import React, { useState } from 'react';
import './Navbar.css';

function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  const toggleNavbar = () => {
    setIsOpen(!isOpen);
  };

  return (
    <>
      <button className="toggle-button" onClick={toggleNavbar}>
        ☰
      </button>
      <div className={`navbar ${isOpen ? 'open' : ''}`}>
        <ul>
          <li><a href="/">Home</a></li>
          <li><a href="/presentacion">Presentacion</a></li>
          <li><a href="/contador">Contador</a></li>
          <li><a href="/tareas">Lista de tareas</a></li>
          <li><a href="/formulario">Formulario</a></li>
        </ul>
      </div>
    </>
  );
}

export default Navbar;
