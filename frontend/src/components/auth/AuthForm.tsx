import React, {useState} from "react";
import { Link } from "react-router-dom";

type AuthFormProps = {
    title: string;
    buttonText: string;
    onButtonClick: (email: string, password: string) => void;
    redirectText: string;
    redirectPath: string;
};

const AuthForm: React.FC<AuthFormProps> = ({title, buttonText, onButtonClick, redirectText, redirectPath}) => {
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")

    return (
        <div className="hero bg-base-200 min-h-screen">
            <div className="hero-content flex-col">
                <div className="text-center">
                    <h1 className="text-5xl font-bold">{title}</h1>
                </div>
                <div className="card bg-base-100 w-full max-w-sm shrink-0">
                    <div className="card-body">
                        <fieldset className="fieldset">
                            <label className="label">Email</label>
                            <input
                                type="email"
                                className="input"
                                onChange={(newEmail) => setEmail(newEmail.target.value)}
                                placeholder="name@domain.com"
                            />
                            <label className="label">Password</label>
                            <input
                                type="password"
                                className="input"
                                placeholder="Hidden"
                                onChange={(newPassword) => setPassword(newPassword.target.value)}
                            />

                            <button className="btn btn-neutral mt-4" onClick={() => onButtonClick(email, password)}>{buttonText}</button>
                        </fieldset>

                        <div className="divider"></div>

                        <Link to={redirectPath}>
                            <p className="link link-hover text-center">{redirectText}</p>
                        </Link>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default AuthForm;