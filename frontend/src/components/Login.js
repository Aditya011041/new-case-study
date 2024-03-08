import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

export default function Login() {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await axios.post('http://127.0.0.1:8000/login', {
                email
            }, {
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            const { emp_id, is_manager, manager_Id } = response.data;

            if (is_manager) {
                navigate('/manager-dashboard', { state: { manager_Id } });
            } else {
                navigate('/detail', { state: { emp_id } });
            }
        } catch (error) {
            console.error('Error:', error.message);
        }
    }

    return (
        <>
            <form onSubmit={handleSubmit}>
                <label>Name</label>
                <input type='text' placeholder='Your name' value={name}
                    onChange={(e) => {
                        setName(e.target.value)
                    }} />
                <label>Email</label>
                <input type='email' placeholder='Your email' value={email}
                    onChange={(e) => {
                        setEmail(e.target.value)
                    }} />
                   
                <button type="submit" className="btn btn-primary">Submit</button>
            </form>
        </>
    )
}
