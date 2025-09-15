import React from "react";
import Accordian from "../global/Accordian.tsx";

function InstructionTemplateBuilder({ brokerName, children }) {
    return (
        <div>
            <img
                src={`/logo/${brokerName}/${brokerName}Logo.webp`}
                alt={brokerName + " Logo"}
                className="w-100 h-auto"
            />

            <div className="divider" />

            {children}
        </div>
    )
}

/**
 * Get the image path of a desired instruction image.
 *
 * @param brokerName The broker's name.
 * @param id The image identification.
 */
function getImageByBrokerName(brokerName: string, id: number) {
    return `/Brokers/${brokerName}/${brokerName}_${id}.webp`;
}

function Trading212() {
    return (
        <InstructionTemplateBuilder brokerName="Trading212">
            <Accordian titleText="How to create a Trading212 Account?">
                You can create a Trading212 Account on their website at: <br />
                <a href="https://www.trading212.com/" className="link link-primary">www.trading212.com/ </a>
            </Accordian>
            <Accordian titleText="How to create an API Key?">
                1. Navigate to:
                <div className="breadcrumbs text-sm">
                    <ul>
                        <li>
                            <svg width="16" height="16" viewBox="0 0 48 48" version="1" xmlns="http://www.w3.org/2000/svg"><path d="M6 22h36v4H6zm0-12h36v4H6zm0 24h36v4H6z"/></svg>
                            Menu
                        </li>
                        <li>
                            <svg width="16" height="16" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="m21.32 9.55-1.89-.63.89-1.78A1 1 0 0 0 20.13 6L18 3.87a1 1 0 0 0-1.15-.19l-1.78.89-.63-1.89A1 1 0 0 0 13.5 2h-3a1 1 0 0 0-.95.68l-.63 1.89-1.78-.89A1 1 0 0 0 6 3.87L3.87 6a1 1 0 0 0-.19 1.15l.89 1.78-1.89.63a1 1 0 0 0-.68.94v3a1 1 0 0 0 .68.95l1.89.63-.89 1.78A1 1 0 0 0 3.87 18L6 20.13a1 1 0 0 0 1.15.19l1.78-.89.63 1.89a1 1 0 0 0 .95.68h3a1 1 0 0 0 .95-.68l.63-1.89 1.78.89a1 1 0 0 0 1.13-.19L20.13 18a1 1 0 0 0 .19-1.15l-.89-1.78 1.89-.63a1 1 0 0 0 .68-.94v-3a1 1 0 0 0-.68-.95M20 12.78l-1.2.4A2 2 0 0 0 17.64 16l.57 1.14-1.1 1.1-1.11-.6a2 2 0 0 0-2.79 1.16l-.4 1.2h-1.59l-.4-1.2A2 2 0 0 0 8 17.64l-1.14.57-1.1-1.1.6-1.11a2 2 0 0 0-1.16-2.82l-1.2-.4v-1.56l1.2-.4A2 2 0 0 0 6.36 8l-.57-1.11 1.1-1.1L8 6.36a2 2 0 0 0 2.82-1.16l.4-1.2h1.56l.4 1.2A2 2 0 0 0 16 6.36l1.14-.57 1.1 1.1-.6 1.11a2 2 0 0 0 1.16 2.79l1.2.4ZM12 8a4 4 0 1 0 4 4 4 4 0 0 0-4-4m0 6a2 2 0 1 1 2-2 2 2 0 0 1-2 2"/></svg>
                            Settings
                        </li>
                        <li>API (Beta)</li>
                        <li>Generate API key</li>
                    </ul>
                    <br />
                    2. Please give all permissions, and give it a memorable name!
                    <img
                        src={getImageByBrokerName("Trading212", 1)}
                        alt="Trading212 API Creation"
                    />
                    <br />
                    <span className="inline-flex items-center">
                        3. Copy &nbsp; <svg width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" fill="none" stroke="#000" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"><path d="M11.25 4.25v-2.5h-9.5v9.5h2.5m.5-6.5v9.5h9.5v-9.5z"/></svg>
                         &nbsp; into the text field below and click Submit.
                    </span>
                </div>
            </Accordian>

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