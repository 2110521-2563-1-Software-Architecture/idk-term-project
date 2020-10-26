import React from "react";
import { Button, InputGroup, FormControl } from "react-bootstrap";

import "styles/Signup.scss";

class Home extends React.Component {
  render() {
    return (
      <div className="signup-container">
        <div className="card-container">
          <div className="main-card">
            <InputGroup className="mb-3">
              <FormControl
                placeholder="Shorten your link"
                aria-label="Shorten your link"
                aria-describedby="basic-addon2"
              />
              <InputGroup.Append>
                <Button variant="outline-primary">Shorten</Button>
              </InputGroup.Append>
            </InputGroup>
          </div>
        </div>
      </div>
    );
  }
}

export default Home;
