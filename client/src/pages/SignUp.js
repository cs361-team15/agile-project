/** @jsx jsx */
import { css, jsx } from '@emotion/core'
import { useState } from 'react'

import {Button, Input} from '../components/FormComponents'
import { NavLink, useHistory } from 'react-router-dom'


const url = 'https://cors-anywhere.herokuapp.com/http://agile-trader.herokuapp.com/'

export default function LogIn() {
  const [email, setEmail] = useState("")
  const [firstName, setFirstName] = useState("")
  const [lastName, setLastName] = useState("")
  const [password, setPassword] = useState("")
  const [passwordConfirm, setPasswordConfirm] = useState("")
  const [perror, setPerror] = useState(false)
  const [eerror, setEerror] = useState(false)

  const history = useHistory()

  return (
    <div css={css`
      display: flex;
      align-items: center;
      justify-content: center;
      flex-direction: column;
    `}>
      <h2>Sign Up</h2>
      <form onSubmit={(e) => {
        e.preventDefault()
        if (password != passwordConfirm) {
          setPerror(true)
        }
        else {
          fetch(url + 'insertUser', {
            method: 'POST',
            mode: 'cors',
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              email: email,
              password: password,
              first_name: firstName,
              last_name: lastName
            })
          }).then(()=>{
            history.push("/login")
          })
        }
      }}>
        <Input
          value={firstName}
          onChange={e => setFirstName(e.target.value)}
          placeholder="First Name"
        />
        <Input
          value={lastName}
          onChange={e => setLastName(e.target.value)}
          placeholder="Last Name"
        />
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
        <Input
          type="password"
          value={passwordConfirm}
          onChange={e => setPasswordConfirm(e.target.value)}
          placeholder="Confirm Password"
        />
        <Button type="submit">Enter</Button>
      </form>
      <NavLink to="/login" css={css`text-decoration: none; color: #2b7bbe;`}>Log In</NavLink>
    </div>
  )
}