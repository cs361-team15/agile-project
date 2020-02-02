import React from 'react'
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom"
import './App.css'

function TopNav() {

  return (
    <div className="Top-Nav row debug">
      <div className="column-50">
        <h2>LOGO</h2>
      </div>
      <div className="column-25">
        <h2>SEARCH BAR</h2>
      </div>
      <div className="column-25">
        <ul className="nav-links">
          <li className="inline nav-link"><Link to="/login">Log In</Link></li>
          <li className="inline nav-link"><Link>Portfolios</Link></li>
          <li className="inline nav-link"><Link>News</Link></li>
          <li className="inline nav-link"><Link>Account</Link></li>
        </ul>
      </div>
    </div>
  )
}

function App() {
  return (
    <Router>
      <div className="App">
        <TopNav />
        <Switch>
          <Route path="/login">
            <p>placeholder login</p>
          </Route>
          <Route exact path="/">
            <p>placeholder index</p>
          </Route>
        </Switch>
      </div>
    </Router>
  )
}

export default App;
