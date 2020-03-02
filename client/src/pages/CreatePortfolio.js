/** @jsx jsx */
import { css, jsx } from '@emotion/core'

import { useState } from 'react'

import {Button, Input} from '../components/FormComponents'
import { NavLink, useHistory } from 'react-router-dom'
import { useSelector } from 'react-redux'
import { getAuth } from '../redux/selectors'

const url = 'https://cors-anywhere.herokuapp.com/http://agile-trader.herokuapp.com/'

export default function CreatePortfolio() {
    const [name, setName] = useState("")

    const auth = useSelector(getAuth)
    
    const history = useHistory()
    return (
        <div css={css`
      display: flex;
      align-items: center;
      justify-content: center;
      flex-direction: column;
    `}>
      <h2>Create New Portfolio</h2>
      <form onSubmit={(e) => {
        e.preventDefault()

        fetch(url + 'insertPortfolio', {
          method: 'POST',
          mode: 'cors',
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            email: auth.email,
            portfolio: name
          })
        }).then((response)=>{
          console.log(response)

          history.push("/portfolios")
        })
    }
      }>
        <Input
          value={name}
          onChange={e => setName(e.target.value)}
          placeholder="Portfolio Name"
        />
        <Button type="submit">Enter</Button>
      </form>
      <NavLink to="/portfolios" css={css`text-decoration: none; color: #2b7bbe;`}>Back to your portfolios</NavLink>
    </div>
    )
}