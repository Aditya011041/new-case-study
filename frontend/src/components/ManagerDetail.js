import React, { useState , useEffect } from 'react'
import {useLocation} from 'react-router-dom'
import axios from 'axios';
export default function ManagerDetail() {

    const [managers , setManagers] = useState(null);
    const location = useLocation();
    const manager_Id = location.state?.manager_Id;

    useEffect(() => {

        const fetchManager = async () => {
            const response = await axios.get(`http://127.0.0.1:8000/manager/${manager_Id}`)
            setManagers(response.data);
            console.log(response.data);

        }
        fetchManager()
    } , [manager_Id])

  return (
   <>
   <h1>Manager ka Ilaka</h1>
   {
    managers && 
        managers.map((i) => (
            <>
            <p key={i.manager.id}>Name: {i.manager.name}</p>
            <p >Email: {i.manager.email}</p>
            <p className='fw-bold'>Employees {i.employees.map(emp => (
                <>
                <li key={emp.id}>{emp.name}</li>
                <li>{emp.email}</li>
                </>
            ))}</p>
            <p><span className='fw-bold'> Projects:</span> {i.projects.map(proj => (
                <>
                <li  key={proj.id}>{proj.title}</li>
                <li>{proj.description}</li>
                <li>{proj.created_at}</li>
                </>
            ))}</p>
            </>
        ))
    

   }

   
   </>
  )
}
