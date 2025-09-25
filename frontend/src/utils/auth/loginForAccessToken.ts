import {api} from "../../config/axios.config.tsx";

function handleLoginAuth(email: string, password: string): {message: string, type: string} {
    let params = new URLSearchParams();
    params.append("username", email);
    params.append("password", password);

    let headers = {headers: {"Content-Type": "application/x-www-form-urlencoded"}}

    api.post(
            "/auth/login",
            params,
            headers
    )
    .then(response => {
        sessionStorage.setItem("accessToken", response.data.access_token);

        window.location.href = "/"

        return {message: "", type: ""};
    })
    .catch(error => {
        return {message: `${error.status}: ${error.response.data.detail}`, type: "alert-error"}
    })
}

export default handleLoginAuth;