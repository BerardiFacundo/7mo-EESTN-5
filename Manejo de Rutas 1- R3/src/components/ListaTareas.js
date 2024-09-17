import { Link } from 'react-router-dom';

function ListaTareas({ tareas }) {
  return (
    <div className="row">
      {tareas.map((tarea) => (
        <div className="col-md-4" key={tarea.id}>
          <div className="card mb-4">
            <div className="card-body">
              <h5 className="card-title">{tarea.titulo}</h5>
              <p className="card-text">{tarea.descripcion}</p>
              <Link to={`/tarea/${tarea.id}`} className="btn btn-secondary">Ver detalles</Link>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}

export default ListaTareas;
