import axios from 'axios';

/**
 * For general unrestricted API endpoints.
 */
export const api = axios.create({
    baseURL: "/api"
});

/**
 * For use with API endpoints that require an access_token bearer.
 */
export const protectedApi = axios.create({
    baseURL: "/api",
});