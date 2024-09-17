import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { tareas } from '../data/Tareas.js';
import '../styles/PaginaCrearTarea.css';

function PaginaCrearTarea() {
  const [titulo, setTitulo] = useState('');
  const [descripcion, setDescripcion] = useState('');
  const [completada, setCompletada] = useState(false);
  const navegar = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    const nuevaTarea = {
      id: tareas.length + 1,
      titulo,
      descripcion,
      fecha: new Date().toISOString().split('T')[0],
      completada,
    };
    tareas.push(nuevaTarea);  // Simulación
    navegar('/');
  };

  return (
    <div className="container">
      <h1>Crear nueva tarea</h1>
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label className="form-label">Título</label>
          <input
            type="text"
            className="form-control"
            value={titulo}
            onChange={(e) => setTitulo(e.target.value)}
            required
          />
        </div>
        <div className="mb-3">
          <label className="form-label">Descripción</label>
          <textarea
            className="form-control"
            value={descripcion}
            onChange={(e) => setDescripcion(e.target.value)}
            required
          />
        </div>
        <div className="form-check mb-3">
          <input
            type="checkbox"
            className="form-check-input"
            checked={completada}
            onChange={(e) => setCompletada(e.target.checked)}
          />
          <label className="form-check-label">Completada</label>
        </div>
        <button type="submit" className="btn btn-primary">Guardar tarea</button>
      </form>
    </div>
  );
}

export default PaginaCrearTarea;
