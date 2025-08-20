import React from "react";

import Trading212Logo from "../../assets/brokers/Trading212/Trading212Logo.webp"

function Trading212() {
    return (
        <div>
            <img
                src={Trading212Logo}
                alt="Trading212"
                className="w-100 h-auto"
            />
        </div>
    )
}

const instructionsMap: Record<string, React.FC> = {
    Trading212
} satisfies Record<string, React.FC>

/**
 * Get an Instructions component for a Broker, via the Broker's name.
 *
 * @param name The Broker's name to search for.
 */
export default function getInstructionByBrokerName(brokerName: string) {
    const Component = instructionsMap[brokerName];
    return Component ? <Component /> : <div>Unknown instructions for {brokerName}</div>
}