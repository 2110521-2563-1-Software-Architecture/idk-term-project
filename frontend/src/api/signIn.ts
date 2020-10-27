import client from "./httpClient";

export const signIn = () => {
  client.get("token/").then().catch();
};
