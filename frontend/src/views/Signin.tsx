import React from "react";
import { Button, Form } from "react-bootstrap";

import signIn from "api/signIn";
import "styles/Signin.scss";

interface State {
  signinData: {
    usernameEmail: string;
    password: string;
  };
}

class Signin extends React.Component {
  state: State = {
    signinData: {
      usernameEmail: "",
      password: "",
    },
  };

  handleSignin = (e: React.MouseEvent<HTMLElement>) => {
    e.preventDefault;

    try {
      signIn(this.state.signinData);
    } catch (error) {
      console.log(error);
    }
  };

  handleSigninDataChange = ({
    target,
  }: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = target;
    const signinData = this.state.signinData;
    if (name === "usernameEmail" || name === "password") {
      signinData[name] = value;
    }
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
                <Button variant="primary" onClick={this.handleSignin}>
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
