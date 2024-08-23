import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Navbar from "./components/Navbar.js";
import "./App.css";
import Home from "./pages/Home.js";
import Presentacion from "./pages/Presentacion.js"
import Contador from "./components/Contador.js";
import ListaTareasPag from './pages/ListaTareasPag.js';
import FormularioPag from "./pages/FormularioPag.js";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Navbar />
        <Router>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/presentacion" element={<Presentacion />} /> 
            <Route path="/contador" element={<Contador />} /> 
            <Route path="/tareas" element={<ListaTareasPag />} />
            <Route path="/formulario" element={<FormularioPag />} />
          </Routes>
        </Router>
      </header>
    </div>
  );
}

export default App;
