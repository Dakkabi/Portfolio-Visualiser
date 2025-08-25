import React from "react";

interface AlertProps {
    message: string
    type: string;
    properties?: string;
}

const Alert: React.FC<AlertProps> = ({message, type, properties}) => {
    if (message) {
        return (
            <div role="alert" className={`alert ${type} ${properties ? properties : ""}`}>
                {message}
            </div>
        )
    }
}

export default Alert;