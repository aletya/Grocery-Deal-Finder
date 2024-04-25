import Logo from "@/assets/logo.png";
import Home from "@/components/Home/Home";
import Results from "@/components/Results/Results";

import styles from "./App.module.css";

import { BrowserRouter as Router, Route, Routes} from 'react-router-dom';

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/result/:data" element={<Results />} />
      </Routes>
    </Router>
  );
}
