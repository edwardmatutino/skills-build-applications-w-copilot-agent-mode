

import logo from '../public/octofitapp-small.png';



function App() {
  return (
    <Router>
      <div className="container mt-4 App">
        <nav className="navbar navbar-expand-lg mb-4 rounded">
          <Link className="navbar-brand text-white d-flex align-items-center" to="/">
            <img src={logo} alt="Octofit Logo" className="App-logo" />
            Octofit Tracker
          </Link>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav mr-auto">
              <li className="nav-item"><Link className="nav-link text-white" to="/activities">Activities</Link></li>
              <li className="nav-item"><Link className="nav-link text-white" to="/leaderboard">Leaderboard</Link></li>
              <li className="nav-item"><Link className="nav-link text-white" to="/teams">Teams</Link></li>
              <li className="nav-item"><Link className="nav-link text-white" to="/users">Users</Link></li>
              <li className="nav-item"><Link className="nav-link text-white" to="/workouts">Workouts</Link></li>
            </ul>
          </div>
        </nav>
        <Routes>
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/users" element={<Users />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="/" element={<div className="text-center"><h2 className="display-4 mb-4">Welcome to Octofit Tracker</h2><p className="lead">Track your fitness, join teams, and compete on the leaderboard!</p></div>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
