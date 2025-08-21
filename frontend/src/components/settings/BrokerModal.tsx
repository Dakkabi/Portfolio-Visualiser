import getInstructionByBrokerName from "./InstructionFactory.tsx";
import React, {useState} from "react";
import {protectedApi} from "../../config/axios.config.tsx";
import Alert from "../Alert.tsx";

interface BrokerModalProps {
    brokerName: string;
    isOpen: boolean;
    onClose: () => void;
    isPrivateKeyRequired: boolean;
}

const BrokerModal: React.FC<BrokerModalProps> = ({ brokerName, isOpen, onClose, isPrivateKeyRequired }) => {
    let [apiKey, setApiKey] = useState("");
    let [privateKey, setPrivateKey] = useState("");

    let [alertProps, setAlertProps] = useState<{message: string, type: string}>({message: "", type: ""})

    /**
     * Handle verifying if the api key and private key are valid, then save to the database.
     *
     * @param brokerName The platform that provided the keys.
     * @param apiKey The main key allowing access to the platform's routes.
     * @param privateKey A private key.
     */
    async function handleApiKeySubmit(brokerName: string, apiKey: string, privateKey: string | null) {
        if (!isPrivateKeyRequired) {privateKey = null;}

        const endpoint = "/keys/";
        const params = {
            api_key: apiKey,
            private_key: privateKey,
            brokers_name: brokerName,
        };

        try {
            await protectedApi.post(endpoint, params);
            setAlertProps({message: "Successfully added new API keys.", type: "alert-success"})

        } catch (postError: any) {
            if (postError.response && postError.response.status === 409) {
                // API Key may already exist
                try {
                    await protectedApi.put(endpoint, params);
                    setAlertProps({message: "Successfully updated API keys.", type: "alert-success"})

                } catch (putError: any) {
                    setAlertProps({message: `${putError.status}: ${putError.response.data.detail}`, type: "alert-error"})
                }
            } else {
                setAlertProps({message: `${postError.status}: ${postError.response.data.detail}`, type: "alert-error"})
            }
        }
    }

    if (!isOpen) return null;

    return (
        <div className="modal modal-open">
            <div className="modal-box" onClick={(e) => e.stopPropagation()}>
                <button onClick={onClose} className="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">✕</button>

                {getInstructionByBrokerName(brokerName)}

                <div className="divider"></div>

                <Alert
                    message={alertProps.message}
                    type={alertProps.type}
                />

                <fieldset className="fieldset">
                    <legend className="fieldset-legend">Enter API Key</legend>
                    <input
                        type="text"
                        className="input"
                        placeholder="Not Hidden"
                        value={apiKey}
                        onChange={(newApiKey) => setApiKey(newApiKey.target.value)}
                    />

                    {isPrivateKeyRequired ? (
                        <>
                            <legend className="fieldset-legend">Enter Private Key</legend>
                            <input
                                type="text"
                                className="input"
                                placeholder="Not Hidden"
                                value={privateKey}
                                onChange={
                                (newPrivateKey) => setPrivateKey(newPrivateKey.target.value)
                            }
                            />
                        </>
                    ) : ""}

                    <button onClick={() => handleApiKeySubmit(brokerName, apiKey, privateKey)} type="submit" className="btn btn-wide mt-4">Submit</button>
                </fieldset>
            </div>
        </div>
    )
}

export default BrokerModal;