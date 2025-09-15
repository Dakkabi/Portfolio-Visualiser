import GlobalNavbar from "../components/global/GlobalNavbar.tsx";

function Dashboard() {
    return (
        <div>
            <GlobalNavbar currentPage="Dashboard" />
            <div className="min-h-screen bg-base-200">
                <div className="p-4">
                    <span className="font-bold text-2xl p-4">Total Dashboard</span>
                </div>

                <div className="ms-10 mt-5 mr-10">
                    <div className="stats shadow bg-base-100 w-full">
                        <div className="stat">
                            <div className="stat-title">Total Portfolio Value</div>
                            <div className="stat-value">£120,000.00</div>
                        </div>
                        <div className="stat">
                            <div className="stat-title">Day Change</div>
                            <div className="stat-value text-success">+£2300.00 (1.95%)</div>
                        </div>
                        <div className="stat">
                            <div className="stat-title">Unrealised Gain/Loss</div>
                            <div className="stat-value text-error">-£20,000.00 (-14.29%)</div>
                        </div>
                        <div className="stat">
                            <div className="stat-title">Total Dividend Earnings Year To Date</div>
                            <div className="stat-value text-info">£728.24</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Dashboard;