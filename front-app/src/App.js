import React from "react";
import "./App.css";
import axios from "axios";
import { useState } from "react";

const callApiBluFilter = async (urlLinkImage, setData, setHasImage) => {
  const data = {
    url: urlLinkImage,
  };
  const response = await axios.post("http://localhost:8888/filter", data);
  setData(response.data);
  setHasImage(true);
  return response.data;
};

function UrlButton() {
  const [url, setUrl] = useState("");
  const [hasImage, setHasImage] = useState(false);
  const [dataImage, setData] = useState("");

  return hasImage ? (
    <div>
      <p>Your image with blur filter</p>
      <img src={`data:image/jpeg;base64,${dataImage}`} />
    </div>
  ) : (
    <div>
      <p>Insert your image url to apply blur filter</p>
      <input type="text" onChange={(e) => setUrl(e.target.value)} />
      <input
        type="button"
        value="Apply filter"
        onClick={async () => callApiBluFilter(url, setData, setHasImage)}
      />
    </div>
  );
}

function App() {
  return (
    <div className="App">
      <div className="App-header">
        <UrlButton />
      </div>
    </div>
  );
}

export default App;
