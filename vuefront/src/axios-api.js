import axios from "axios";

const AxiosWithoutToken = axios.create({
  baseURL: "http://localhost:8000/",
});

const createAxiosInstance = (token) => {
  return axios.create({
    baseURL: "http://localhost:8000/",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
  });
};

export { createAxiosInstance, AxiosWithoutToken };
