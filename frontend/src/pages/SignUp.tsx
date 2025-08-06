import React from "react";
import AuthForm from "../components/auth/AuthForm.tsx";

const SignUp: React.FC = () => {
    function handleSignUp(email: string, password: string) {

    }

    return (
        <AuthForm
            title="Welcome!"
            buttonText="Sign Up"
            onButtonClick={handleSignUp}
            redirectText="Already have an account with us? Click to Log back in!"
            redirectPath="/login"
        />
    );
}

export default SignUp;