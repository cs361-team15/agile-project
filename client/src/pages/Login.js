/** @jsx jsx */
import { css, jsx } from '@emotion/core'
import { useState } from 'react'
import { NavLink, useHistory } from 'react-router-dom'
import { useDispatch, useSelector } from 'react-redux'
import fetch from 'isomorphic-fetch'

import {Button, Input} from '../components/FormComponents'
import { setUserEmail} from '../redux/actions'
import { getAuth } from '../redux/selectors'

const url = 'https://cors-anywhere.herokuapp.com/http://agile-trader.herokuapp.com/'

export default function LogIn() {
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const [error, setError] = useState(false)

  const dispatch = useDispatch()
  const history = useHistory()

  const sendData = () => {
    console.log('Sending request')
    fetch(url + 'authentication' ,{
      method: 'POST',
      mode: 'cors',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        email: email,
        password: password
      })
    }).then((response) => {
      console.log(response.status)
      if (response.status === 200) {
        // Redirect to portfolios, and store the user in the store
        setError(false)
        dispatch(setUserEmail(email))
        history.push("/portfolios")
      }
      else {
        setError(true)
      }
    })
  }

  return (
    <div css={css`
      display: flex;
      align-items: center;
      justify-content: center;
      flex-direction: column;
    `}>
      <h2>Log In</h2>
      <form onSubmit={(e) => {
        e.preventDefault()

        sendData()
      }}>
        <Input
          value={email}
          onChange={e => setEmail(e.target.value)}
          placeholder="Email"
        />
        <Input
          type="password"
          value={password}
          onChange={e => setPassword(e.target.value)}
          placeholder="Password"
        />
        <Button type="submit">Enter</Button>
      </form>
      {error && <p>Invalid email or password</p>}
      <NavLink to="/login" css={css`text-decoration: none; color: #2b7bbe;`}>Forgot your password?</NavLink>
      <NavLink to="/signup" css={css`text-decoration: none; color: #2b7bbe;`}>Sign Up</NavLink>
    </div>
  )
}