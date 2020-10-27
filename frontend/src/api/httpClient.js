import axios from "axios";

const client = axios.create({
  baseURL: process.env.REACT_APP_BASE_URL || "",
  timeout: 1000,
  headers: {
    Authorization: localStorage.getItem("token") || "",
  },
});

client.interceptors.response.use((response) => {
  if (response.status === 401) {
    // redirect to login
  }
});

export default client;
