import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useLocation , useNavigate } from 'react-router-dom';

function EmpDetail() {

    const location = useLocation();
    const emp_id = location.state?.emp_id; 
    const [emp, setEmp] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchEmp = async () => {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/emp/${emp_id}`);
                setEmp(response.data);
            } catch (error) {
                console.error('Error fetching employee:', error);
            }
        };

        fetchEmp();
    }, [emp_id]);

    const leaveApply = () =>{
        navigate('/leave');
    }

    return (
        <>
            <h1>Employee Details</h1>
                {emp && (
                    <>
                        <p>Name: {emp.employee.name}</p>
                        <p>Email: {emp.employee.email}</p>
                        <h2>Project Details</h2>
                       <ul>
                       {emp.projects.map((i) => (
                            <div>
                           <li><p>Project Name - {i.title} </p></li> 
                           <li> <p>Project Desc - {i.description}</p></li> 
                            </div>
                        ))}
                        </ul> 
                        <h2>Manager Details</h2>
                        <ul>
                            {emp.managers.map((i)=>(
                                <div>
                                    <li><p>Project Man Name - {i.name}</p></li> 
                                </div>
                            ))}
                        </ul>
            <button onClick={leaveApply}>Apply For Leave</button>

                    </>
                )}
        </>
    );
}

export default EmpDetail;
