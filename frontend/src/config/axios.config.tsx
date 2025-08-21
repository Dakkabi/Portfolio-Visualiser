import Axios from "axios";

/**
 * General axios instance, for use with api endpoints that require no user authentication.
 */
const api = Axios.create({
    baseURL: "/api",
})

/**
 * Protected axios instance, for use with api endpoints that require an access token.
 */
const protectedApi = Axios.create({
    baseURL: "/api",
})

protectedApi.interceptors.request.use(
    (config) => {
        const accessToken = sessionStorage.getItem("accessToken");
        if (accessToken) {
            config.headers.Authorization = `Bearer ${accessToken}`;
        }
        return config;
    },
    (error) => Promise.reject(error)
)

export { api, protectedApi };