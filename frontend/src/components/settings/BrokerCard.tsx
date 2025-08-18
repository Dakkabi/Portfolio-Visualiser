import React, {useState} from "react";
import BrokerModal from "./BrokerModal.tsx";

interface BrokerCardProps {
    brokerName: string;
}

const BrokerCard: React.FC<BrokerCardProps> = ({ brokerName }) => {
    let [modalProps, setModalProps] = useState({brokerName: "", isOpen: false});

    /**
     * Close an opened Modal, and wipe the state.
     */
    function closeModal() {
        setModalProps({ brokerName: "", isOpen: false});
    }

    /**
     * Open's a BrokerModal component with the instructions loaded specific to the param inputted.
     *
     * @param brokerName The instruction manual to render inside the Modal.
     */
    function openModal(brokerName: string) {
        setModalProps({ brokerName: brokerName, isOpen: true });
    }

    return (
        <div>
            <a onClick={() => {openModal(brokerName)}} className="card w-87 cursor-pointer">
                <figure>
                    <img
                        src={`/logo/${brokerName}Billboard.webp`}
                        alt={brokerName + " Billboard"}
                    />
                </figure>
            </a>
            <BrokerModal
                brokerName={modalProps.brokerName}
                isOpen={modalProps.isOpen}
                onClose={closeModal}
            />
        </div>
    )
}

export default BrokerCard;