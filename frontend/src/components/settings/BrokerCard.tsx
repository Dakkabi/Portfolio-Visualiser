import React from "react";

interface BrokerCardProps {
    brokerName: string;
    cardClickEvent: (brokerName: string) => void;
    showStatus: boolean;
}

const BrokerCard: React.FC<BrokerCardProps> = ({ brokerName, cardClickEvent, showStatus }) => {

    return (
        <div>
            <a onClick={() => cardClickEvent(brokerName)} className="card w-87 cursor-pointer">
                {showStatus ?
                    <div aria-label="status" className="status status-xl status-success absolute top-2 right-2" />
                    :
                    ""
                }
                <figure>
                    <img
                        src={`/Brokers/${brokerName}/${brokerName}Billboard.webp`}
                        alt={brokerName + " Billboard"}
                    />
                </figure>
            </a>
        </div>
    )
}

export default BrokerCard;