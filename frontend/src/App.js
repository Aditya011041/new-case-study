import './App.css';
import EmpDetail from './components/EmpDetail';
import LeaveApplicationForm from './components/LeaveApplicationForm';
import Login from './components/Login';
import {BrowserRouter, Routes, Route} from "react-router-dom";
import ManagerDetail from './components/ManagerDetail';

function App() {
  return (
    <div className="App">

<BrowserRouter>
<Routes>
  <Route path="/detail" element={<EmpDetail />} />
  <Route path="/" element={<Login/>} />
  <Route path="/leave" element={<LeaveApplicationForm/>} />
  <Route path = "/manager-dashboard" element={<ManagerDetail/>}/>
</Routes>
</BrowserRouter>
     
    </div>
  );
}

export default App;
