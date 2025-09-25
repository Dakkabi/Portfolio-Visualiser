import AuthForm from "../../components/auth/AuthForm.tsx"
import Alert from "../../components/global/Alert.tsx";
import {useState} from "react";
import {api} from "../../config/axios.config.tsx";
import handleLoginAuth from "../../utils/auth/loginForAccessToken.ts";

function Login() {
    let [responseAlertProps, setResponseAlertProps] = useState({message: "", type: ""})

    /**
     * Invoke an API endpoint to compare user's credentials, and return an access token if valid, before redirecting.
     *
     * @param email The user's email.
     * @param password The user's password.
     */
    function handleLogin(email: string, password: string) {
        const responseMessage = handleLoginAuth(email, password);
        setResponseAlertProps(responseMessage)
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