import React from "react";

function Trading212() {
    return (
        <h1 className="text-5xl">Trading212</h1>
    )
}

const instructionsMap: Record<string, React.FC> = {
    Trading212
} satisfies Record<string, React.FC>

function getInstructionByName(name: string) {
    const Component = instructionsMap[name];
    return Component ? <Component /> : <div>Unknown instructions for {name}</div>
}

export default getInstructionByName;