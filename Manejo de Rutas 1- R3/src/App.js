import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import PaginaInicio from './pages/PaginaInicio';
import PaginaDetalleTarea from './pages/PaginaDetalleTarea';
import PaginaCrearTarea from './pages/PaginaCrearTarea';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<PaginaInicio />} />
        <Route path="/tarea/:id" element={<PaginaDetalleTarea />} />
        <Route path="/crear" element={<PaginaCrearTarea />} />
      </Routes>
    </Router>
  );
}

export default App;
