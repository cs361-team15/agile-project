/** @jsx jsx */
import { css, jsx } from '@emotion/core'
import { useState } from 'react'
import { NavLink } from 'react-router-dom'
import { useDispatch, useSelector } from 'react-redux'
import fetch from 'isomorphic-fetch'

import {Button, Input} from '../components/FormComponents'
import { setUserEmail, setUserPass } from '../redux/actions'
import { getAuth } from '../redux/selectors'

const url = 'https://cors-anywhere.herokuapp.com/http://agile-trader.herokuapp.com/'

export default function LogIn() {
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")

  const dispatch = useDispatch()

  const sendData = () => {
    console.log('Sending request')
    fetch(url + 'authenticate' ,{
      method: 'POST',
      mode: 'cors',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        username: email,
        password: password
      })
    }).then((response) => {
      console.log(response.status)
    })
  }

  const auth = useSelector(getAuth)
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
        
        dispatch(setUserEmail(email))
        dispatch(setUserPass(password))

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
      <NavLink to="/login" css={css`text-decoration: none; color: #2b7bbe;`}>Forgot your password?</NavLink>
      <NavLink to="/signup" css={css`text-decoration: none; color: #2b7bbe;`}>Sign Up</NavLink>
    </div>
  )
}