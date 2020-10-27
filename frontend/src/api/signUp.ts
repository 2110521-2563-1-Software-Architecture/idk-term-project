import client from "./httpClient"

interface props {
    user_name: string;
    password: string;
    user_email: string;
}

export default signUp = (signupData: props) => {
    client.post("/api/signup/", signupData)
    .then((response) => {

    })
    .catch((error) => {

    })
};