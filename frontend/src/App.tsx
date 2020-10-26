import React from "react";
import { Navbar } from "react-bootstrap";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import { Home, Signin } from "views";

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar bg="dark" variant="dark" sticky="top">
          <Navbar.Brand href="#home">idk.ly</Navbar.Brand>
        </Navbar>

        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route exact path="/signin">
            <Signin />
          </Route>
          <Route exact path="/signup">
            <Home />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;
