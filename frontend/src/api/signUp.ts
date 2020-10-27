import client from "./httpClient"

interface props {
  user_name: string;
  password: string;
  user_email: string;
}

export const signUp = (signupData: props) => {
  const body = signupData;
  client.post("api/signup/", body)
  .then((response) => {
    console.log(response);
    alert("Sign up success!!!");
  })
  .catch((error) => {
    console.log(error);
    alert("Sign up fail!!!")
  })
};