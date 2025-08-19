import {getInstructionByName, isPrivateKeyRequired} from "./InstructionFactory.tsx";
import React, {useState} from "react";

interface BrokerModalProps {
    brokerName: string;
    isOpen: boolean;
    onClose: () => void;
}

const BrokerModal: React.FC<BrokerModalProps> = ({ brokerName, isOpen, onClose }) => {
    let [apiKey, setApiKey] = useState("");
    let [privateKey, setPrivateKey] = useState("");

    /**
     * Handle verifying if the api key and optional private key are valid keys, then save to the database.
     *
     * @param brokerName The platform that provided the keys.
     * @param apiKey The main key allowing access to the platform's routes.
     * @param privateKey An optional private key.
     */
    function handleAPIKeySubmit(brokerName: string, apiKey: string, privateKey: string) {
        if (!isPrivateKeyRequired(brokerName)) {privateKey = "";}


    }


    if (!isOpen) return null;

    return (
        <dialog className="modal modal-open">
            <div className="modal-box">
                <form method="dialog">
                    <button onClick={onClose} className="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">✕</button>
                </form>
                {getInstructionByName(brokerName)}

                <div className="divider"></div>

                <fieldset className="fieldset">
                    <legend className="fieldset-legend">Enter API Key</legend>
                    <input
                        type="text"
                        className="input"
                        placeholder="Not Hidden"
                        onChange={(newApiKey) => setApiKey(newApiKey.target.value)}
                    />

                    {isPrivateKeyRequired(brokerName) ? (
                        <>
                            <legend className="fieldset-legend">Enter Private Key</legend>
                            <input
                                type="text"
                                className="input"
                                placeholder="Not Hidden"
                                onChange={
                                (newPrivateKey) => setPrivateKey(newPrivateKey.target.value)
                            }
                            />
                        </>
                    ) : ""}

                    <button onClick={() => handleAPIKeySubmit(brokerName, apiKey, privateKey)} type="submit" className="btn btn-wide mt-4">Submit</button>
                </fieldset>
            </div>
        </dialog>
    )
}

export default BrokerModal;