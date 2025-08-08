import axios from "axios";

let baseUrl = "/api"

export const api = axios.create({
    baseURL: baseUrl,
});

export const protectedApi = axios.create({
    baseURL: baseUrl,
});