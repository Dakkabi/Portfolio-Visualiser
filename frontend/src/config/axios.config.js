import axios from "axios";
import { goto } from '$app/navigation';

const api = axios.create(
    {baseURL: '/api'}
);

api.interceptors.response.use(
    /*
     * Intercept responses with 401 Unauthorized status codes.
     */
    (response) => {
        return response
    },
    async (error) => {
        if (error.response && error.response.status === 401) {
            sessionStorage.clear();

            goto('/');
        }

        return Promise.reject(error);
    }
);

api.interceptors.request.use(
    /*
     * Automatically inject 'access_token' in sessionStorage in all requests.
     */
    (config) => {
        const token = sessionStorage.getItem('access_token');

        if (token) config.headers['Authorization'] = `Bearer ${token}`;

        return config;
    }
);

export default api;

