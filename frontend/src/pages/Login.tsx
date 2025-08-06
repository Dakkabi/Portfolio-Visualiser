import React from "react";
import AuthForm from "../components/auth/AuthForm.tsx";

const Login: React.FC = () => {
    function handleLogin(email: string, password: string) {

    }

    return (
        <AuthForm
            title="Welcome Back!"
            buttonText="Login"
            onButtonClick={handleLogin}
            redirectText="Don't have an account? Click here to Sign up!"
            redirectPath="/signup"
        />
    );
}

export default Login;