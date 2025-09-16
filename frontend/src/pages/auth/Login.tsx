import AuthForm from "../../components/auth/AuthForm.tsx"
import Alert from "../../components/global/Alert.tsx";
import {useState} from "react";
import {api} from "../../config/axios.config.tsx";

function Login() {
    let [responseAlertProps, setResponseAlertProps] = useState({message: "", type: ""})

    /**
     * Invoke an API endpoint to compare user's credentials, and return an access token if valid, before redirecting.
     *
     * @param email The user's email.
     * @param password The user's password.
     */
    function handleLogin(email: string, password: string) {
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
                setResponseAlertProps({message: "Success, you will be redirected shortly.", type: "alert-success"})

                sessionStorage.setItem("accessToken", response.data.access_token);
            })
            .catch(error => {
                setResponseAlertProps({message: `${error.status}: ${error.response.data.detail}`, type: "alert-error"})
            })
    }

    return (
        <AuthForm
            titleText="Welcome Back!"
            btnText="Login"
            redirectText="Don't have an account with us? Click me!"
            redirectPath="/signup"
            btnClickEvent={handleLogin}
            alertComponent={<Alert message={responseAlertProps.message} type={responseAlertProps.type} />}
        />
    )
}

export default Login;