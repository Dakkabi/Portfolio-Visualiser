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

protectedApi.interceptors.response.use(
    (response) => response,
    (error) => {
        if (error.response && error.response.status === 401) {
            sessionStorage.removeItem("accessToken");
            window.location.href = "/login";
        }
    }
)

export { api, protectedApi };