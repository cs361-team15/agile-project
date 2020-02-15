/** @jsx jsx */
import { css, jsx } from '@emotion/core'
import { useState } from 'react'

import {Button, Input} from '../components/FormComponents'
import { NavLink } from 'react-router-dom'

export default function LogIn() {
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")

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
        // Make 
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