import React from "react";
import { Form, Button } from "react-bootstrap";

import "styles/Signup.scss";

class Signup extends React.Component {
  state = {
    signupData: {
      username: "",
      email: "",
      password: "",
    },
  };

  handleSignupDataChange = ({ target: { name, value } }) => {
    const signupData = this.state.signupData;
    signupData[name] = value;
    this.setState({ signupData });
  };

  render() {
    return (
      <div className="signup-container">
        <div className="form-container">
          <div className="form-card">
            <Form>
              <Form.Group controlId="formBasicUsername">
                <Form.Label>Username</Form.Label>
                <Form.Control
                  type="username"
                  placeholder="Enter username"
                  name="username"
                  onChange={this.handleSignupDataChange}
                />
              </Form.Group>

              <Form.Group controlId="formBasicEmail">
                <Form.Label>Email address</Form.Label>
                <Form.Control
                  type="email"
                  placeholder="Enter email"
                  name="email"
                  onChange={this.handleSignupDataChange}
                />
              </Form.Group>

              <Form.Group controlId="formBasicPassword">
                <Form.Label>Password</Form.Label>
                <Form.Control
                  type="password"
                  placeholder="Password"
                  name="password"
                  onChange={this.handleSignupDataChange}
                />
              </Form.Group>

              <div className="content-right">
                <Button variant="primary" type="submit">
                  Sign up
                </Button>
              </div>
            </Form>
          </div>
        </div>
      </div>
    );
  }
}

export default Signup;
