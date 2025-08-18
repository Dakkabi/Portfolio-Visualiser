import {getInstructionByName, isPrivateKeyRequired} from "./InstructionFactory.tsx";
import React from "react";

interface BrokerModalProps {
    brokerName: string;
    isOpen: boolean;
    onClose: () => void;
}

const BrokerModal: React.FC<BrokerModalProps> = ({ brokerName, isOpen, onClose }) => {

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
                    <input type="text" className="input" placeholder="Not Hidden" />

                    {!isPrivateKeyRequired(brokerName) ? (
                        <>
                            <legend className="fieldset-legend">Enter Private Key</legend>
                            <input type="text" className="input" placeholder="Not Hidden" />
                        </>
                    ) : ""}

                    <button type="submit" className="btn btn-wide mt-4">Submit</button>
                </fieldset>
            </div>
        </dialog>
    )
}

export default BrokerModal;