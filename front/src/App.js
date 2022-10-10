import logo from './logo.svg';
import './App.css';
import './CssSyleSheets/PopUpCss.css';

import React, { useEffect, useRef, useState } from 'react';

function App() {

  const whenSubmit = () => {
    alert("Thanks for submitting a response")
  }

  //problem pop up 
  const Popup = props => {
    return (
      <div className="popup-box">
        <div className="box">
          <span className="close-icon" onClick={props.handleClose}>x</span>
          {props.content}
        </div>
      </div>
    );
  };

  const [isOpen, setIsOpen] = useState(false);
 
  const togglePopup = () => {
    setIsOpen(!isOpen);
  }

  return (

    <div>
      <h1 className='center'>Machine learning Image Upload!</h1> 
      <input
          type="button"
          value="You got Bugs to Report?"
          onClick={togglePopup}
        />
        {isOpen && <Popup
          content={<>
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
          </>}
          handleClose={togglePopup}
        />}


    </div>

  );
}

export default App;