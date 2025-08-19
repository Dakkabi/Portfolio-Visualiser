import {useEffect, useState} from "react";
import {api} from "../../config/axios.config.tsx";
import BrokerCard from "../../components/settings/BrokerCard.tsx";

function Connections() {
    const [brokers, setBrokers] = useState<{ name: string, type: string[] }[]>([]);

    useEffect(() => {
        api.get("/brokers")
            .then(response => {
                setBrokers(response.data);
            })
            .catch(error => {
                console.log(error);
            })
    }, [])

    const stockBrokers = brokers.filter(broker => broker.type.includes("Stocks"));
    const cryptoExchanges = brokers.filter(exchange => exchange.type.includes("Crypto"));

    return (
        <div className="text-center">
            <h1 className="text-5xl font-bold">Connections</h1>

            <div className="divider"></div>

            <h1 className="text-4xl font-bold">Brokers</h1>
            <ul className="menu menu-horizontal">
                {stockBrokers.map((broker) => (
                    <li key={broker.name}>
                        <BrokerCard brokerName={broker.name} />
                    </li>
                ))}
            </ul>

            <div className="divider"></div>

            <h1 className="text-4xl font-bold">Crypto Exchanges</h1>
            <ul className="menu menu-horizontal">
                {cryptoExchanges.map((exchange) => (
                    <li key={exchange.name}>
                        <BrokerCard brokerName={exchange.name} />
                    </li>
                ))}
            </ul>
        </div>
    )
}

export default Connections;