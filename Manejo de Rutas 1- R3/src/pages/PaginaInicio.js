import React from 'react';
import { Link } from 'react-router-dom';
import { tareas } from '../data/Tareas';
import ListaTareas from '../components/ListaTareas';
import '../styles/PaginaInicio.css';

function PaginaInicio() {
  return (
    <div className="container">
      <h1>Lista de Tareas</h1>
      <ListaTareas tareas={tareas} />
      <div className="text-center">
        <Link to="/crear">Crear nueva tarea</Link>
      </div>
    </div>
  );
}

export default PaginaInicio;
