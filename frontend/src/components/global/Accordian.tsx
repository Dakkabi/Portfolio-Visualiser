import React, {type ReactNode} from "react";

interface AccordianProps {
    titleText: string
    children: ReactNode
}

const Accordian: React.FC<AccordianProps> = ({ titleText, children }) => {
    return (
        <div className="collapse collapse-open bg-base-100 border border-base-300 mt-2">
            <input type="radio" />
            <div className="collapse-title font-semibold">{titleText}</div>
            <div className="collapse-content text-sm">{children}</div>
        </div>
    )
}

export default Accordian;