import { NavLink, Outlet } from "react-router-dom";

function App() {
  return (
    <div className="App container">
      <header className="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
        <a href="/" className="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-dark text-decoration-none">
          <span className="fs-4"><b>League Scheduler</b></span>
        </a>
      <ul className="nav nav-pills">
        <li className="nav-item"><NavLink className="nav-link" to="/">Home</NavLink></li>
        <li className="nav-item"><NavLink className="nav-link" to="/teams">Teams</NavLink></li>
        <li className="nav-item"><NavLink className="nav-link" to="/locations">Locations</NavLink></li>
        <li className="nav-item"><NavLink className="nav-link" to="/schedules">Schedules</NavLink></li>
      </ul>
      </header>

      <Outlet />

    </div>
  );
}

export default App;
