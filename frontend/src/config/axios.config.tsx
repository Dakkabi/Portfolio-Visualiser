import axios from "axios";

let baseUrl = "/api"

const api = axios.create({
    baseURL: baseUrl,
});

const protectedApi = axios.create({
    baseURL: baseUrl,
});

