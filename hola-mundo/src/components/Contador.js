import React, { useState } from 'react';
import './Contador.css';

function Contador() {
  const [valor, setValor] = useState(0);

  const incrementar = () => {
    setValor(valor + 1);
  };

  const decrementar = () => {
    setValor(valor - 1);
  };

  return (
    <div className="contador">
      <h2>Contador: {valor}</h2>
      <div className='botonesContador'>
      <button onClick={incrementar} className="botonSuma">Incrementar</button>
      <button onClick={decrementar} className="botonResta">Decrementar</button>
      </div>
    </div>
  );
}

export default Contador;