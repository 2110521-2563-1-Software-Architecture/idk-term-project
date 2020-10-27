import React from "react";
import { Form, Button } from "react-bootstrap";

import "styles/Signup.scss";
import "api/signUp.ts";
import { signUp } from "api/signUp";
import { Redirect } from "react-router-dom";

class Signup extends React.Component {
  state = {
    signupData: {
      user_name: "",
      password: "",
      user_email: "",
    },
    isSignup: false,
  };

  handleSignupDataChange = ({ 
    target,
  }: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = target;
    const signupData = this.state.signupData;
    if (name === "user_name" || name === "password" || name === "user_email"){
      signupData[name] = value;
    }
    this.setState({ signupData });
  };

  handleSignup = (e: React.MouseEvent<HTMLElement>) => {
    e.preventDefault();
    
    try {
      signUp(this.state.signupData); 
      this.setState({ shouldRedirect: true });
    } catch (error) {
      console.log(error);
    }
  };

  render() {
    if (this.state.isSignup) {
      return <Redirect to="/" />
    }
    return (
      <div className="signup-container">
        <div className="form-container">
          <div className="form-card">
            {/* {
              this.state.shouldRedirect ?
              <Redirect to="/" push/> : */}
              <Form>
                <Form.Group controlId="formBasicUsername">
                  <Form.Label>Username</Form.Label>
                  <Form.Control
                    type="username"
                    placeholder="Enter username"
                    name="user_name"
                    onChange={this.handleSignupDataChange}
                  />
                </Form.Group>

                <Form.Group controlId="formBasicEmail">
                  <Form.Label>Email address</Form.Label>
                  <Form.Control
                    type="email"
                    placeholder="Enter email"
                    name="user_email"
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
                  <Button variant="primary" onClick={this.handleSignup}>
                    Sign up
                  </Button>
                </div>
              </Form>
            {/* } */}
          </div>
        </div>
      </div>
    );
  }
}

export default Signup;
