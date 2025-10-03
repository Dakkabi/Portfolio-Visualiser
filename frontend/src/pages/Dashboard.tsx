import GlobalNavbar from "../components/global/GlobalNavbar.tsx";
import {useEffect, useState} from "react";
import {protectedApi} from "../config/axios.config.tsx";
import {Link} from "react-router-dom";
import {percentageChange} from "../utils/mathUtils.ts";
import {
    CartesianGrid,
    Line,
    LineChart,
    Pie,
    PieChart,
    Tooltip,
    XAxis,
    YAxis
} from "recharts";
import renderActiveShape from "../components/global/ActiveShapePieChart.tsx";

interface PortfolioInterface {
    Cash: {
        free: number;
        total: number;
        total_dividends: number;
        unrealised_gain_loss: number;
        invested: number;
    },
    Stock: {
        assets: {
                ticker: string;
                average_price: number;
                quantity: number;
        }[],
        order_history: {
            ticker: string;
            execution_date: string;
            quantity: number;
            execution_type: string;
        }[]
    }
}

interface ChartDataInterface {
    name: string;
    value: number;
}

function Dashboard() {
    const [portfolio, setPortfolio] = useState<PortfolioInterface | null>(null);
    const [pieChartData, setPieChartData] = useState<ChartDataInterface[]>([]);

    /**
     * Fetch the user's portfolio data from the database.
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

    /**
     * Populate the Pie Chart with data pairs.
     */
    function populatePieChartData() {
        const assets = portfolio?.Stock?.assets;

        if (!assets || !Array.isArray(assets)) return;

        const assetChartInfo: ChartDataInterface[] = assets.map(asset => ({
          name: asset.ticker,
          value: Math.round(asset.quantity * asset.average_price * 100) / 100,
        }))

        assetChartInfo.push({name: "Cash", value: portfolio?.Cash.free})

        setPieChartData(assetChartInfo);
    }

    /**
     * Return a DaisyUI text-colour string depending on if the value is negative or positive.
     *
     * @param value - The stat value.
     * @return string - A TailwindCSS string.
     */
    function colourStatTextOnValue(value: number) {
        if (value > 0) {
            return "text-success";
        } else if (value < 0) {
            return "text-error";
        }
        return "";
    }

    useEffect(() => {
        fetchPortfolio();
    }, []);

    useEffect(() => {
        if (!portfolio) return;

        populatePieChartData();

    }, [portfolio]);

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
                                    <div className="stat-title text-black">Total Invested</div>
                                    <div className="stat-value">£{portfolio.Cash.invested}</div>
                                </div>
                                <div className="stat">
                                    <div className="stat-title text-black">Unrealised Gain/Loss</div>
                                    <div className={`stat-value ${colourStatTextOnValue(portfolio.Cash.unrealised_gain_loss)}`}>
                                        £{portfolio.Cash.unrealised_gain_loss} ({percentageChange(portfolio.Cash.invested, portfolio.Cash.total)}%)
                                    </div>
                                </div>
                                <div className="stat">
                                    <div className="stat-title text-black">Total Dividend Earnings</div>
                                    <div className="stat-value text-info">£{portfolio.Cash.total_dividends}</div>
                                </div>
                            </div>
                        </div>

                        <div className="w-full flex gap-x-10 ms-10 mt-5 mr-10">
                            {/* Pie Chart */}
                            <div className="card bg-base-100 shadow-sm">
                                <div className="card-body">
                                    <PieChart width={400} height={400}>
                                        <Pie
                                            activeShape={renderActiveShape}
                                            dataKey="value"
                                            isAnimationActive={true}
                                            data={pieChartData}
                                            innerRadius={100}
                                            fill="#242124"
                                        />
                                    </PieChart>
                                </div>
                            </div>

                            {/* Asset Table */}
                            <div className="card w-full bg-base-100 mr-20 shadow-sm">
                                <div className="card-body">
                                    <div className="overflow-x-auto">
                                        <table className="table">
                                            <thead>
                                                <tr>
                                                    <th>Ticker</th>
                                                    <th>Average Price</th>
                                                    <th>Quantity</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                {portfolio.Stock.assets.map((asset, index) => (
                                                    <tr key={index}>
                                                        <th>{asset.ticker}</th>
                                                        <td>£{asset.average_price.toFixed(2)}</td>
                                                        <td>{asset.quantity}</td>
                                                    </tr>
                                                ))}
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>
                        </div>

                        {/* Line Graph */}
                        <div className="w-full flex gap-x-10 ms-10 mt-5 mr-10">
                            <div className="card bg-base-100 shadow-sm w-full mr-20">
                                <div className="card-body ">
                                        <LineChart
                                            width={1750}
                                            height={500}
                                            data={}
                                        >
                                            <CartesianGrid strokeDasharray="3 3" />
                                            <XAxis dataKey="name" />
                                            <YAxis />
                                            <Tooltip />
                                            <Line type="monotone" dataKey="pv" stroke="#8884d8" activeDot={{ r: 8 }} />
                                            <Line type="monotone" dataKey="uv" stroke="#82ca9d" />
                                        </LineChart>
                                    <h1></h1>
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