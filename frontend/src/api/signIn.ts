import client from "./httpClient";

export interface props {
  usernameEmail: string;
  password: string;
}

export const signIn = (props: props) => {
  const body = {
    user_name: props.usernameEmail,
    password: props.password,
  };
  client
    .post("token/", body)
    .then((response) => {
      if (response.status === 200) {
        const token = `Bearer ${response.data.access}`;
        localStorage.setItem("token", token);
      }
    })
    .catch((error) => {
      console.log(error);
    });
};
