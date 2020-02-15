/** @jsx jsx */
import { css, jsx } from '@emotion/core'

import { NavLink } from 'react-router-dom'

export default function Landing() {
    return (
        <div css={css`
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        `}>
        <h2>Welcome to Agile Trader!</h2>
        <p>The best stock trading site out there!</p>
        <NavLink to="/signup" css={css`text-decoration: none; color: #2b7bbe;`}><h3>Sign Up</h3></NavLink>
        <NavLink to="/login" css={css`text-decoration: none; color: #2b7bbe;`}><h3>Log In</h3></NavLink>
        </div>
    )
}