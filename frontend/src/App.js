import React from "react";
import { Routes, Route } from "react-router-dom";
import Login from "./components/Login";

// Componente temporário para a página principal após o login
function Dashboard() {
  return (
    <div style={{ textAlign: 'center', color: 'white', backgroundColor: '#282c34', height: '100vh', paddingTop: '50px' }}>
      <h1>Painel Financeiro</h1>
      <p>Bem-vindo ao sistema!</p>
    </div>
  );
}

function App() {
  return (
    <Routes>
      <Route path="/" element={<Login />} />
      <Route path="/dashboard" element={<Dashboard />} />
    </Routes>
  );
}

export default App;