import React, { useState, useEffect } from 'react'
import axios from 'axios'

export default function LeaveApplicationForm() {

    const [leaveType, setLeaveType] = useState([]);
    const [empId , setEmpId] = useState(null);

    useEffect(() => {
        const fetchLeaveType = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/leaveTypeDetail/');
                setLeaveType(response.data);
            } catch (error) {
                console.error('Error fetching leave type:', error);
            }
        }

        const getAllEmp = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/emp/');
                setEmpId(response.data);
                console.log(response.data)
            } catch (error) {
                console.error('Error fetching employee:', error);
            }
        }

        fetchLeaveType()
        getAllEmp()
    }, []);
    const [data, setData] = useState({
        employee: '',
        leave_type: '',
        start_date: '',
        end_date: '',
        status: 'pending',
    });

    const handleChange = (e) => {
        const { name, value } = e.target
        setData({
            ...data,
            [name]: value
        })
    }

const handleLeaveTypeChange = (e) => {
    const { value } = e.target;
    console.log('Selected leave type:', value);
    setData({
        ...data,
        leave_type: value
    });
}
    
    const handleSubmit = async (e) => {
        e.preventDefault();
        const selectedEmployee = empId.find(employee => employee.email=== data.employee);
        if (selectedEmployee) {
            data.employee = selectedEmployee.id;
        }
        console.log('Submitting form with employee ID:', data.employee);
        const res =  axios.post(`http://127.0.0.1:8000/leaveapplicationlist/${data.employee}/`, data)


        setData({
            employee: '',
            leave_type: '',
            start_date: '',
            end_date: '',
            status: 'pending',
        });
        
    }
    


    return (
        <>
            <div className='container'>

                <form onSubmit={handleSubmit} method="POST">
                    <div className="mb-3">
                        <label for="exampleInputEmail1" className="form-label">Employee Email</label>
                        <input type="email" className="form-control" name='employee' onChange={handleChange} value={data.emp_id} />

                    </div>
                    <div className="mb-3">
                        <label for="exampleInputType1" className="form-label">Leave Type</label>
                        <select className="form-select"  onChange={handleLeaveTypeChange}>
                        <option defaultChecked>Open this select menu</option>
                            {leaveType.map((i) => (
                                <option value={i.id}>{i.name}</option>
                            ))}
                        </select>
                    </div>
                    <div className="mb-3">
                        <label for="exampleInputDate1" className="form-label">Start Date</label>
                        <input type="date" className="form-control"  name="start_date" onChange={handleChange} value={data.start_date} />

                    </div>
                    <div className="mb-3">
                        <label for="exampleInputDate1" className="form-label">End Date</label>
                        <input type="date" className="form-control"  name="end_date" onChange={handleChange} value={data.end_date}/>

                    </div>
                    <div className="mb-3">
                        <label for="exampleInputText1" className="form-label">Leave Status</label>
                        <input type="text" className="form-control" name='status' onChange={handleChange}
                            value={data.status}
                        />

                    </div>
                    <button type="submit" className="btn btn-primary">Submit</button>
                </form>

            </div>

        </>
    )
}






