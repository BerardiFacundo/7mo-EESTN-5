import logo from "../logo.svg";
import logo2 from "../github.png";
import "../styles/Home.css";
import Title1 from "../components/Title1";

function Home() {
  return (
    <div>
    
      <Title1>Hola mundo!!</Title1>
      <h3>Bienvenido a la página principal</h3>
      <img src={logo} className="App-logo" alt="logo" />
      <a
        className="Link"
        href="https://github.com/BerardiFacundo"
        target="_blank"
        rel="noopener noreferrer"
      >
        <img src={logo2} className="github" alt="logo" />
        <p>Te presento mi github BerardiFacundo.</p>
      </a>
    </div>
  );
}

export default Home;
