import {BrowserRouter, Navigate, Route, Routes} from "react-router-dom";
import "./App.css"
import Login from "./pages/auth/Login.tsx";
import SignUp from "./pages/auth/SignUp.tsx";
import Connections from "./pages/settings/Connections.tsx";

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Navigate to="/login" replace />} />

                {/* Auth Routes */}
                <Route path="/login" element={<Login />} />
                <Route path="/signup" element={<SignUp />} />

                {/* Settings Routes */}
                <Route path="/me/connections" element={<Connections />} />
            </Routes>
        </BrowserRouter>
    )
}

export default App;