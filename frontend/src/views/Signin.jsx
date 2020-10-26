import React from "react";
import { Button, Form } from "react-bootstrap";

import "styles/Signin.scss";

class Signin extends React.Component {
  state = {
    signinData: {
      usernameEmail: "",
      password: "",
    },
  };

  handleSigninDataChange = ({ target: { name, value } }) => {
    const signinData = this.state.signinData;
    signinData[name] = value;
    this.setState({ signinData });
  };

  render() {
    return (
      <div className="signin-container">
        <div className="form-container">
          <div className="form-card">
            <Form>
              <Form.Group controlId="usernameOrEmail">
                <Form.Label>Username or Email</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="Enter username or email"
                  name="usernameEmail"
                  value={this.state.signinData.usernameEmail}
                  onChange={this.handleSigninDataChange}
                />
              </Form.Group>

              <Form.Group controlId="password">
                <Form.Label>Password</Form.Label>
                <Form.Control
                  type="password"
                  placeholder="Password"
                  name="password"
                  value={this.state.signinData.password}
                  onChange={this.handleSigninDataChange}
                />
              </Form.Group>
              <div className="content-right">
                <Button variant="primary" type="submit">
                  Sign in
                </Button>
              </div>
            </Form>
          </div>
        </div>
      </div>
    );
  }
}

export default Signin;
