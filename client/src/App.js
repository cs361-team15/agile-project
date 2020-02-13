/** @jsx jsx */
import { css, jsx } from '@emotion/core'
import { BrowserRouter as Router, Switch, Route, NavLink } from "react-router-dom"

import {Button, Input} from './components/FormComponents'
import LogIn from './pages/Login'
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
        <h2>LOGO</h2>
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
            placeholder="Search"
          />
          <Button type="submit">Enter</Button>
        </form>
      </div>
      <div css={css`
        flex: 25%;

      `}>
        <ul css={navLinks}>
          <li css={navLink}><NavLink to="/login">Log In</NavLink></li>
          <li css={navLink}><NavLink to="/portfolios">Portfolios</NavLink></li>
          <li css={navLink}><NavLink to="/news">News</NavLink></li>
          <li css={navLink}><NavLink to="/account">Account</NavLink></li>
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
          <Route exact path="/">
            <p>placeholder index</p>
          </Route>
        </Switch>
      </div>
    </Router>
  )
}

export default App;
