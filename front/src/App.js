import logo from './logo.svg';
import './App.css';

import React, { useEffect, useRef, useState } from 'react';

function App() {

  const [num, setNum] = useState(0)

  const whenButtonClick = () => {
    setNum(num + 1)
  }

  const whenSubmit = () => {
    alert("Thanks for submitting a response")
  }

  useEffect(() => {
    document.title = `You clicked ${num} times`
  })



  return (

    <div>
      <div>Number: {num}</div>
      <button onClick={whenButtonClick}>button</button>
      <div>You clicked {num} times</div>

      <form onSubmit={whenSubmit}>
        <div>
          <label>
            Username:
            <input type="text" name="name" />
          </label>

        </div>
        <div>
          <label>
            Reported Problem:
            <input type="text" text="problem" />
          </label>
          <div><input type="submit" value="Submit" /></div>
        </div>

      </form>


    </div>

  );
}

export default App;
