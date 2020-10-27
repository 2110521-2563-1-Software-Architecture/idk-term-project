import client from "./httpClient";

export interface Props {
  usernameEmail: string;
  password: string;
}

const signIn = (props: Props): boolean => {
  const body = {
    user_name: props.usernameEmail,
    password: props.password,
  };
  client
    .post("signin/", body)
    .then((response) => {
      if (response.status === 200) {
        const token = `Bearer ${response.data.access}`;
        localStorage.setItem("token", token);

        return true;
      }
    })
    .catch((error) => {
      console.log(error);
    });

  return false;
};

export default signIn;
