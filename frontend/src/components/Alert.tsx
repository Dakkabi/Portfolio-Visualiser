import React from "react";

type validAlertType = "alert-success" | "alert-info" | "alert-warning" | "alert-danger";

interface AlertProps {
    message: string
    type: string;
    properties?: validAlertType;
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