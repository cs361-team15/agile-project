/** @jsx jsx */
import { css, jsx } from '@emotion/core'
import { BrowserRouter as Router, Switch, Route, NavLink } from "react-router-dom"

import {Button, Input} from './components/FormComponents'
import LogIn from './pages/Login'
import Landing from './pages/Landing'
import SignUp from './pages/SignUp'
import Portfolios from './pages/Portfolios'
import { useState } from 'react'

function TopNav() {
  const navLinks = css`
    list-style-type: none;
    margin: 0;
    padding: 0;
  `

  const navLink = css`
    padding: 8px;
    display: inline;
  `

  const [query, setQuery] = useState("")
  return (
    <div css={css`
      display: flex;
    `}>
      <div css={css`
        flex: 50%;
      `}>
        <NavLink to="/" css={css`text-decoration: none; color: black;`}><h2>Agile Trader</h2></NavLink>
      </div>
      <div css={css`
        flex: 25%;
      `}>
        <form onSubmit={(e) => {
          e.preventDefault()
          // Make 
        }}>
          <Input
            value={query}
            onChange={e => setQuery(e.target.value)}
            placeholder="Stock Search"
          />
          <Button type="submit">Enter</Button>
        </form>
      </div>
      <div css={css`
        flex: 25%;

      `}>
        <ul css={navLinks}>
          <li css={navLink}><NavLink to="/login" css={css`text-decoration: none; color: #2b7bbe;`}>Log In</NavLink></li>
          <li css={navLink}><NavLink to="/portfolios" css={css`text-decoration: none; color: #2b7bbe;`}>Portfolios</NavLink></li>
          <li css={navLink}><NavLink to="/news" css={css`text-decoration: none; color: #2b7bbe;`}>News</NavLink></li>
          <li css={navLink}><NavLink to="/account" css={css`text-decoration: none; color: #2b7bbe;`}>Account</NavLink></li>
        </ul>
      </div>
    </div>
  )
}

function App() {
  return (
    <Router>
      <div>
        <TopNav />
        <Switch>
          <Route path="/login">
            <LogIn />
          </Route>
          <Route path="/signup">
            <SignUp />
          </Route>
          <Route path="/portfolios">
            <Portfolios />
          </Route>
          <Route exact path="/">
            <Landing />
          </Route>
        </Switch>
      </div>
    </Router>
  )
}

export default App;
