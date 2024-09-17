import React from 'react';
import { useParams } from 'react-router-dom';
import { tareas } from '../data/Tareas.js';
import '../styles/PaginaDetalleTareas.css';

function PaginaDetalleTarea() {
  const { id } = useParams();
  const tarea = tareas.find((tarea) => tarea.id === parseInt(id));

  return (
    <div className="container">
      {tarea ? (
        <div className="card">
          <h1>{tarea.titulo}</h1>
          <p>{tarea.descripcion}</p>
          <p><strong>Fecha de creación:</strong> {tarea.fecha}</p>
          <p><strong>Estado:</strong> {tarea.completada ? 'Completada' : 'Incompleta'}</p>
        </div>
      ) : (
        <p>Tarea no encontrada</p>
      )}
    </div>
  );
}

export default PaginaDetalleTarea;
