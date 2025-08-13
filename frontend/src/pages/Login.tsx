import AuthForm from "../components/auth/AuthForm.tsx"

function Login() {
    return (
        <AuthForm
            titleText="Welcome Back!"
            btnText="Login"
            redirectText="Don't have an account with us? Click me!"
            redirectPath="/signup"
        />
    )
}

export default Login;