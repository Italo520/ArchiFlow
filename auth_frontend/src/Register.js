import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Register = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [nome_completo, setNomeCompleto] = useState('');
    const [telefone, setTelefone] = useState('');
    const [tipo_usuario, setTipoUsuario] = useState('cliente');
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.post('http://127.0.0.1:8000/api/register/', {
                email,
                password,
                profile: {
                    nome_completo,
                    telefone,
                    tipo_usuario
                }
            });
            navigate('/login');
        } catch (error) {
            console.error('Registration failed!', error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>Register</h2>
            <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" required />
            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" required />
            <input type="text" value={nome_completo} onChange={(e) => setNomeCompleto(e.target.value)} placeholder="Full Name" required />
            <input type="text" value={telefone} onChange={(e) => setTelefone(e.target.value)} placeholder="Phone" required />
            <select value={tipo_usuario} onChange={(e) => setTipoUsuario(e.target.value)}>
                <option value="cliente">Cliente</option>
                <option value="arquiteto">Arquiteto</option>
                <option value="administrador">Administrador</option>
            </select>
            <button type="submit">Register</button>
        </form>
    );
};

export default Register;