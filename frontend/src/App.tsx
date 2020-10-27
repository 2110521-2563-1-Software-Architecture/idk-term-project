import * as React from "react";
import { Navbar } from "react-bootstrap";

import { Home } from "views";

function App() {
  return (
    <div className="App">
      <Navbar bg="dark" variant="dark" sticky="top">
        <Navbar.Brand href="#home">
          idk.ly
        </Navbar.Brand>
      </Navbar>
      <Home />
    </div>
  );
}

export default App;
