import React from "react";

function InstructionTemplateBuilder({ brokerName, children }) {
    return (
        <div>
            <img
                src={`/logo/${brokerName}/${brokerName}Logo.webp`}
                alt={brokerName + " Logo"}
                className="w-100 h-auto"
            />
            {children}
        </div>
    )
}

function Trading212() {
    return (
        <InstructionTemplateBuilder brokerName="Trading212">
            <></>
        </InstructionTemplateBuilder>
    )
}

function Kraken() {
    return (
        <InstructionTemplateBuilder brokerName="Kraken">
            <></>
        </InstructionTemplateBuilder>
    )
}

const instructionsMap: Record<string, React.FC> = {
    Trading212,
    Kraken,
} satisfies Record<string, React.FC>

/**
 * Get an Instructions component for a Broker, via the Broker's name.
 *
 * @param brokerName The Broker's name to search for.
 */
export default function getInstructionByBrokerName(brokerName: string) {
    const Component = instructionsMap[brokerName];
    return Component ? <Component /> : <div>Unknown instructions for {brokerName}</div>
}