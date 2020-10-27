import React from "react";
import { Form, Button } from "react-bootstrap";

import "styles/Signup.scss";

class Signup extends React.Component {
  state = {
    signupData: {
      user_name: "",
      password: "",
      user_email: "",
    },
  };

  handleSignupDataChange = ({ target: { name, value } }) => {
    const signupData = this.state.signupData;
    signupData[name] = value;
    this.setState({ signupData });
  };

  handleSubmit = (e) => {
    e.prevenDefault();

    axios
      .post(process.env.REACT_APP_BACKEND_URL + "/auth/register", this.state.signupData)
      .then( (response) => {
        console.log(response);
        console.log(response.data);
      })
      .catch((error) => {
        if (error.response && error.response.status === 400) {
          
        } else {

        }
      });
  };

  render() {
    return (
      <div className="signup-container">
        <div className="form-container">
          <div className="form-card">
            <Form onSubmit={this.handleSubmit}>
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
