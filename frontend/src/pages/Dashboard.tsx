import GlobalNavbar from "../components/global/GlobalNavbar.tsx";

function Dashboard() {
    return (
        <div>
            <GlobalNavbar currentPage="Dashboard" />
            <div className="min-h-screen bg-base-200">
                <div className="stats shadow bg-base-100">
                    <div className="stat">
                        <div className="stat-figure text-secondary"></div>
                        <div className="stat-title">Total Portfolio Value</div>
                        <div className="stat-value">$120,000</div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Dashboard;