import AuthForm from "../components/auth/AuthForm.tsx";
import {api} from "../config/axios.config.tsx";
import Alert from "../components/Alert.tsx";
import {useState} from "react";

function SignUp() {
    let [responseAlertProps, setResponseAlertProps] = useState({message: "", type: ""})

    /**
     * Invoke an API endpoint to create a new user into the database, then return an access token, before redirecting.
     *
     * @param email The user's email.
     * @param password The user's password
     */
    function handleSignUp(email: string, password: string) {
        api.post(
            "/users",
            { email: email, password: password }
        )
            .then(() => {
                setResponseAlertProps({message: "Success, you will be shortly redirected.", type: "alert-success"})
            })
            .catch(error => {
                setResponseAlertProps({message: `${error.status}: ${error.response.data.detail}`, type: "alert-error"})
            })
    }

    return (
        <AuthForm
            titleText="Welcome!"
            btnText="Sign Up"
            redirectText="Already have an account with us? Click me!"
            redirectPath="/login"
            btnClickEvent={handleSignUp}
            alertComponent={<Alert message={responseAlertProps.message} type={responseAlertProps.type} />}
        />
    )
}

export default SignUp;