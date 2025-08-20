import React from "react";

interface BrokerCardProps {
    brokerName: string;
    cardClickEvent: (brokerName: string) => void;
}

const BrokerCard: React.FC<BrokerCardProps> = ({ brokerName, cardClickEvent }) => {

    return (
        <div>
            <a onClick={() => cardClickEvent(brokerName)} className="card w-87 cursor-pointer">
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