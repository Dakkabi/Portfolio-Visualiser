import React, {useState} from "react";
import Alert from "../Alert.tsx";

interface AuthFormProps {
    titleText: string,
    btnText: string,
    redirectText: string,
    redirectPath: string,
    btnClickEvent: (email: string, password: string) => void;
    alertComponent: React.ReactNode;
}

const AuthForm: React.FC<AuthFormProps> = ({titleText, btnText, redirectText, redirectPath, btnClickEvent, alertComponent}) => {
    let [email, setEmail] = useState("");
    let [password, setPassword] = useState("");

    return (
        <div className="hero bg-base-200 min-h-screen">
            <div className="hero-content flex-col">
                <div className="text-center">
                    <h1 className="text-5xl font-bold">{titleText}</h1>
                    <p className="py-6">
                        Portfolio visualisation and analysis, free forever.
                    </p>
                    {alertComponent}
                </div>
                <div className="card bg-base-100 w-full max-w-sm shrink-0 shadow-2xl">
                    <div className="card-body">
                        <fieldset className="fieldset">
                            <label className="label">Email</label>
                            <input
                                type="email"
                                className="input"
                                placeholder="name@domain.com"
                                onChange={(newEmail) => setEmail(newEmail.target.value)}
                            />
                            <label className="label">Password</label>
                            <input
                                type="password"
                                className="input"
                                placeholder="Hidden"
                                onChange={(newPassword) => {setPassword(newPassword.target.value)}}
                            />
                            <button
                                className="btn btn-neutral mt-4"
                                type="submit"
                                onClick={() => btnClickEvent(email, password)}
                            >
                                {btnText}
                            </button>
                        </fieldset>

                        <div className="divider"></div>

                        <div className="text-center"><a className="link link-hover" href={redirectPath}>{redirectText}</a></div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default AuthForm;