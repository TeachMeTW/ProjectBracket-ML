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

  const [imageSrc, setImageSrc] = useState("/NoImage.jpg");

  const updateImage = (event) => {
    setImageSrc(URL.createObjectURL(event.target.files[0]));
  };

  return (

    <div className='App'>
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
              Upload an Image:
              <input type="file" accept="image/*" name="image upload" onChange={updateImage}/>
            </label>
          </div>

          <div>
            <label>
              Image Description:
              <input type="text" name="image description" />
            </label>
          </div>

          <div>
            <div>Image Preview:</div>
            <img src={imageSrc} alt="preview" />
          </div>
          
          <div><input type="submit" value="Submit" /></div>
        </form>
      </p>


    </div>

  );



}

export default App;