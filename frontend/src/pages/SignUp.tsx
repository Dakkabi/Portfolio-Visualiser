import AuthForm from "../components/auth/AuthForm.tsx";

function SignUp() {
    return (
        <AuthForm
            titleText="Welcome!"
            btnText="Sign Up"
            redirectText="Already have an account with us? Click me!"
            redirectPath="/login"
        />
    )
}

export default SignUp;