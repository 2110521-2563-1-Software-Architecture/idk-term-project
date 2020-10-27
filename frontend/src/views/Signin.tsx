import React from "react";
import { Button, Form } from "react-bootstrap";
import { Redirect } from "react-router-dom";

import signIn from "api/signIn";
import { isLoggedIn } from "helpers/Auth";
import "styles/Signin.scss";

interface State {
  signinData: {
    usernameEmail: string;
    password: string;
  };
  isLoggedIn: boolean;
}

class Signin extends React.Component {
  state: State = {
    signinData: {
      usernameEmail: "",
      password: "",
    },
    isLoggedIn: isLoggedIn(),
  };

  handleSignin = (e: React.MouseEvent<HTMLElement>) => {
    e.preventDefault();

    try {
      const result = signIn(this.state.signinData);
      if (result) {
        this.setState({ isLoggedIn: true });
      }
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
    if (this.state.isLoggedIn) {
      return <Redirect to="/" />;
    }

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
