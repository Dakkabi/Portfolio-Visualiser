import Axios from "axios";

/**
 * General axios instance, for use with api endpoints that require no user authentication.
 */
export const api = Axios.create({
    baseURL: "/api",
})

/**
 * Protected axios instance, for use with api endpoints that require an access token.
 */
export const protectedApi = Axios.create({
    baseURL: "/api",
})