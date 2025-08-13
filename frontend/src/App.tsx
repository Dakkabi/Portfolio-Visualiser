import {BrowserRouter, Navigate, Route, Routes} from "react-router-dom";
import "./App.css"
import Login from "./pages/Login.tsx";
import SignUp from "./pages/SignUp.tsx";

export default function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Navigate to="/login" replace />} />

                <Route path="/login" element={<Login />} />
                <Route path="/signup" element={<SignUp />} />
            </Routes>
        </BrowserRouter>
    )
}