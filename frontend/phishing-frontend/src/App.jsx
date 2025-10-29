import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeText = async () => {
    if (!text.trim()) return;
    setLoading(true);
    try {
      const res = await axios.post("http://localhost:8000/predict", { text });
      setResult(res.data);
    } catch (err) {
      console.error(err);
      alert("Error al analizar el texto");
    }
    setLoading(false);
  };

  return (
    <div className="app-container">
      <div className="card">
        <h1>Detector de Phishing</h1>
        <textarea
          placeholder="Pega aquí el contenido del email..."
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
        <button onClick={analyzeText} disabled={loading}>
          {loading ? "Analizando..." : "Analizar"}
        </button>

        {result && (
          <div className={`result ${result.label}`}>
            <h2>Resultado: {result.label.toUpperCase()}</h2>
            <p>Probabilidad: {Math.round(result.probability * 100)}%</p>
            <p>{result.explanation}</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
