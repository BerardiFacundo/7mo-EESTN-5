import React from 'react';
import '../styles/ListaTareasPag.css';
import ListaTareas from '../components/ListaTareas';
import Title1 from '../components/Title1';

function ListaTareasPag() {
  return (
    <div>
      <Title1>Mi Lista de Tareas</Title1>
      <ListaTareas />
    </div>
  );
}

export default ListaTareasPag;
