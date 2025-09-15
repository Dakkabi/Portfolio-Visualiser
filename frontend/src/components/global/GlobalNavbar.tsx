import {Link} from "react-router-dom";
import React from "react";

interface GlobalNavbarProps {
    currentPage: string;
}

/**
 * If `currentPage` matches the dropdown menu page name, highlight it to show that it is currently selected.
 *
 * @param currentPage The current page name.
 * @param dropdownPageName The component list name.
 * @return TailwindCSS string class names on how to decorate the list name.
 */
function highlightCurrentPage(currentPage: string, dropdownPageName: string) {
    if (currentPage === dropdownPageName) {
        return "font-bold bg-base-300";
    }
    return "";
}

const GlobalNavbar: React.FC<GlobalNavbarProps> = ({ currentPage }) => {
    return (
        <div className="navbar shadow-sm">
            <div className="navbar-start">
                <div className="dropdown">
                    <div tabIndex={0} role="button" className="btn btn-ghost btn-circle">
                        <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h7" /> </svg>
                    </div>
                    <ul tabIndex={0} className="menu menu-sm dropdown-content rounded-box z-1 mt-3 w-52 p-2 shadow">
                        <li><Link to={"/"} className={`${highlightCurrentPage(currentPage, "Dashboard")}`}>Dashboard</Link></li>
                    </ul>
                </div>
            </div>
            <div className="navbar-center">
                <span className="text-2xl font-bold">Portfolio Visualiser</span>
            </div>
            <div className="navbar-end">
                <div className="dropdown dropdown-end">
                    <button tabIndex={1} className="btn btn-ghost btn-circle">
                        <svg className="h-7 w-7" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 4a4 4 0 1 0 0 8 4 4 0 0 0 0-8M6 8a6 6 0 1 1 12 0A6 6 0 0 1 6 8m2 10a3 3 0 0 0-3 3 1 1 0 1 1-2 0 5 5 0 0 1 5-5h8a5 5 0 0 1 5 5 1 1 0 1 1-2 0 3 3 0 0 0-3-3z" fill="#0D0D0D"/></svg>
                    </button>
                    <ul
                        tabIndex={1}
                        className="menu menu-sm dropdown-content rounded-box z-1 mt-3 w-52 p-2 shadow">
                        <li><Link
                            to={"/me/connections"}
                            className={`${highlightCurrentPage(currentPage, "Connections")}`}>
                            Connections
                        </Link></li>
                    </ul>
                </div>
            </div>
        </div>
    );
};

export default GlobalNavbar;