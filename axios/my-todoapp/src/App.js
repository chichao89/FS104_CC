
import React, { useEffect, useState, useCallback } from "react";
import './App.css';
import ToDo from './Component/ToDo'
import axios from "axios"

//const myToDoBaseURL = "http://127.0.0.1:8000/toDoLists/";

function App() {

  const [toDo, setToDo] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/toDoLists/')
            .then(response => setToDo(response.data));
  },[])

  return (
    <div className="App">
        <ToDo/>
    <div>
      <h1>To Do List</h1>
      {toDo.map((todo)=> (
         <div>
          <div style={{color:"red"}}>
            <hr/>
          {todo.title}
          <br/>
          {todo.priority}
          <br/>
          {todo.due_date}
          <br/>
          <hr/>
          </div>
          
        </div>
      ))}
    </div>
    </div>
  );
}

export default App;
