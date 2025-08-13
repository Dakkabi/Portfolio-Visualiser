import React from "react";

interface AuthFormProps {
    titleText: string,
    btnText: string,
    redirectText: string,
    redirectPath: string,
}

const AuthForm: React.FC<AuthFormProps> = ({titleText, btnText, redirectText, redirectPath}) => {
    return (
        <div className="hero bg-base-200 min-h-screen">
            <div className="hero-content flex-col">
                <div className="text-center">
                    <h1 className="text-5xl font-bold">{titleText}</h1>
                    <p className="py-6">
                        Portfolio visualisation and analysis, free forever.
                    </p>
                </div>
                <div className="card bg-base-100 w-full max-w-sm shrink-0 shadow-2xl">
                    <div className="card-body">
                        <fieldset className="fieldset">
                            <label className="label">Email</label>
                            <input type="email" className="input" placeholder="name@domain.com" />
                            <label className="label">Password</label>
                            <input type="password" className="input" placeholder="Hidden" />
                            <button className="btn btn-neutral mt-4" type="submit">{btnText}</button>
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