import React, { useState } from 'react';
import './ListaTareas.css'; // Asegúrate de que esta ruta sea correcta

function ListaTareas() {
  const [tareas, setTareas] = useState([]);
  const [nuevaTarea, setNuevaTarea] = useState('');

  const agregarTarea = () => {
    if (nuevaTarea.trim() === '') return;

    setTareas([...tareas, { texto: nuevaTarea, completada: false }]);
    setNuevaTarea('');
  };

  const handleKeyDown = (event) => {
    if (event.key === 'Enter') {
      agregarTarea();
    }
  };

  const toggleCompletada = (index) => {
    const nuevasTareas = tareas.map((tarea, i) => 
      i === index ? { ...tarea, completada: !tarea.completada } : tarea
    );
    setTareas(nuevasTareas);
  };

  const eliminarTarea = (index) => {
    const nuevasTareas = tareas.filter((_, i) => i !== index);
    setTareas(nuevasTareas);
  };

  return (
    <div className="lista-tareas">
      <h2>Lista de Tareas</h2>
      <input 
        type="text" 
        value={nuevaTarea} 
        onChange={(e) => setNuevaTarea(e.target.value)} 
        onKeyDown={handleKeyDown} 
        placeholder="Añadir nueva tarea" 
        className="input-tarea"
      />
      <button onClick={agregarTarea} className="boton-agregar">Agregar</button>
      <ul>
        {tareas.map((tarea, index) => (
          <li 
            key={index} 
            className={`tarea ${tarea.completada ? 'completada' : 'no-completada'}`}
          >
            <span onClick={() => toggleCompletada(index)}>{tarea.texto}</span>
            <button onClick={() => eliminarTarea(index)} className="boton-eliminar">Eliminar</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ListaTareas;
