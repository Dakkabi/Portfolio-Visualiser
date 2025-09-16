import GlobalNavbar from "../components/global/GlobalNavbar.tsx";
import {useEffect, useState} from "react";
import {protectedApi} from "../config/axios.config.tsx";
import {Link} from "react-router-dom";

interface PortfolioInterface {
    Cash: {
        total: number;
    }
}

function Dashboard() {
    const [portfolio, setPortfolio] = useState<PortfolioInterface | null>(null);

    /**
     *
     */
    function fetchPortfolio() {
        protectedApi.get("/portfolio/total")
            .then((response) => {
                const portfolio = response.data.portfolio;
                setPortfolio(portfolio);
            })
            .catch((error) => {
                console.log(error);
            })
    }

    useEffect(() => {
        fetchPortfolio();
    }, []);

    return (
        <div>
            <GlobalNavbar currentPage="Dashboard" />
            <div className="min-h-screen bg-base-200">
                {portfolio ? (
                    <>
                        <div className="p-4">
                            <span className="font-bold text-2xl p-4">Total Dashboard</span>
                        </div>

                        <div className="ms-10 mt-5 mr-10">
                            <div className="stats shadow bg-base-100 w-full">
                                <div className="stat">
                                    <div className="stat-title text-black">Total Portfolio Value</div>
                                    <div className="stat-value">£{portfolio.Cash.total}</div>
                                </div>
                                <div className="stat">
                                    <div className="stat-title text-black">Day Change</div>
                                    <div className="stat-value text-success">+£2300.00 (1.95%)</div>
                                </div>
                                <div className="stat">
                                    <div className="stat-title text-black">Unrealised Gain/Loss</div>
                                    <div className="stat-value text-error">-£20,000.00 (-14.29%)</div>
                                </div>
                                <div className="stat">
                                    <div className="stat-title text-black">Total Dividend Earnings</div>
                                    <div className="stat-value text-info">£728.24</div>
                                </div>
                            </div>
                        </div>
                    </>
                ) : (
                    <div className="hero min-h-screen">
                        <div className="hero-content text-center">
                            <div className="">
                                <h1 className="text-5xl font-bold">You don't seem to have any connections.</h1>
                                <h2 className="text-4xl font-bold mt-4">Add some at <Link to="/me/connections" className="text-primary link link-hover">Connections</Link></h2>
                            </div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    )
}

export default Dashboard;