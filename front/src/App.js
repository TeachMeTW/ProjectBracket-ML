import './App.css';

import { useState } from "react";

function App() {

  const [imageSrc, setImageSrc] = useState("/NoImage.jpg");

  const updateImage = (event) => {
    console.log(event.target.files);
    setImageSrc(URL.createObjectURL(event.target.files[0]));
  };

  const whenSubmit = () => {
    alert("Thanks for submitting a response");
  };

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
