import {useEffect, useState} from "react";
import {api, protectedApi} from "../../config/axios.config.tsx";
import BrokerCard from "../../components/settings/BrokerCard.tsx";
import BrokerModal from "../../components/settings/BrokerModal.tsx";
import GlobalNavbar from "../../components/global/GlobalNavbar.tsx";

function Connections() {
    const [brokers, setBrokers] = useState<{ name: string, type: string[], private_key_required: boolean }[]>([]);
    const [connections, setConnections] = useState<{api_key: string, private_key: string, broker_name: string}[]>([]);
    const [modalProps, setModalProps] = useState<{ brokerName: string, isOpen: boolean }>(
        { brokerName: "", isOpen: false }
    );

    function openBrokerModal(brokerName: string) {
        setModalProps({ brokerName: brokerName, isOpen: true });
    }
    function closeBrokerModal() {
        setModalProps({ brokerName: "", isOpen: false });
    }

    /**
     * Check if the broker requires an additional private key field.
     *
     * @param brokerName The broker to search for.
     */
    function isPrivateKeyRequired(brokerName: string): boolean {
        for (let i = 0; i < brokers.length; i++) {
            if (brokers[i].name === brokerName) {
                return brokers[i].private_key_required;
            }
        }
        return false;
    }

    /**
     * Update the connectedBrokers array to update displays on the connected broker cards.
     */
    function refreshConnectedBrokers() {
        protectedApi.get("/keys/")
            .then(response => {
                setConnections(response.data);
            })
            .catch(error => {
                console.log(error);
            })
    }

    /**
     * Return a boolean on whether the user has provided valid keys for a broker.
     *
     * @param brokerName The broker to check for.
     */
    function isConnected(brokerName: string) {
        for (let i = 0; i < connections.length; i++) {
            if (connections[i].broker_name === brokerName) {
                return true;
            }
        }
        return false;
    }

    /**
     * Removes a broker connection from connections array.
     *
     * It would also be possible by calling `refreshConnectedBrokers()`,
     * but there is little concern for sync issues, as a page-refresh will fix that.
     * Therefore, this is a suitable optimisation.
     *
     * @param brokerName The broker to remove.
     */
    function removeConnection(brokerName: string) {
        const splicedConnections = connections.filter(
            (connection) => connection.broker_name !== brokerName
        );
        setConnections(splicedConnections);
    }

    function addConnection(params: {api_key: string, private_key: string | null, broker_name: string}) {
        setConnections(oldConnections => [...oldConnections, params]);
    }

    useEffect(() => {
        api.get("/brokers")
            .then(response => {
                setBrokers(response.data);
            })
            .catch(error => {
                console.log(error);
            })

        refreshConnectedBrokers();
    }, [])

    const stockBrokers = brokers.filter(broker => broker.type.includes("Stocks"));
    const cryptoExchanges = brokers.filter(exchange => exchange.type.includes("Crypto"));

    return (
        <div>
            <div>
                <BrokerModal
                    brokerName={modalProps.brokerName}
                    isOpen={modalProps.isOpen}
                    onClose={closeBrokerModal}
                    isPrivateKeyRequired={isPrivateKeyRequired(modalProps.brokerName)}
                    connected={isConnected(modalProps.brokerName)}
                    onDeleteApiKey={() => removeConnection(modalProps.brokerName)}
                    onAddApiKey={addConnection}
                />
            </div>
            <GlobalNavbar />
            <div className="text-center">
                <h1 className="text-5xl font-bold">Connections</h1>

                <div className="divider"></div>

                <h1 className="text-4xl font-bold">Stock Brokers</h1>
                <ul className="menu menu-horizontal">
                    {stockBrokers.map((broker) => (
                        <li key={broker.name}>
                            <BrokerCard
                                brokerName={broker.name}
                                cardClickEvent={openBrokerModal}
                                showStatus={isConnected(broker.name)}
                            />
                        </li>
                    ))}
                </ul>

                <div className="divider"></div>

                <h1 className="text-4xl font-bold">Crypto Exchanges</h1>
                <ul className="menu menu-horizontal">
                    {cryptoExchanges.map((exchange) => (
                        <li key={exchange.name}>
                            <BrokerCard
                                brokerName={exchange.name}
                                cardClickEvent={openBrokerModal}
                                showStatus={isConnected(exchange.name)}
                            />
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    )
}

export default Connections;