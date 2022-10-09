import logo from './logo.svg';
import './App.css';

import React, { useEffect, useRef, useState } from 'react';

function App() {

  const whenSubmit = () => {
    alert("Thanks for submitting a response")
  }

  return (

    <div>
      <p>
        <form onSubmit={whenSubmit}>
          <div>
            <label>
              Username:
              <input type="text" name="name" />
            </label>
          </div>
          <div>
            <label>
              Image Description:
              <input type="text" name="image description" />
            </label>
            <div><input type="submit" value="Submit" /></div>
          </div>
        </form>
      </p>

      <p>
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
      </p>
    </div>

  );
}

export default App;
