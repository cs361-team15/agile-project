/** @jsx jsx */
import { css, jsx } from '@emotion/core'

import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { getPortfolios, getAuth } from '../redux/selectors'
import { setPortfolios } from '../redux/actions'
import { NavLink, useHistory } from 'react-router-dom'

import Portfolio from '../components/Portfolio'

const url = 'https://cors-anywhere.herokuapp.com/http://agile-trader.herokuapp.com/'

export default function Portfolios() {
  const dispatch = useDispatch()
  const auth = useSelector(getAuth)
  const history = useHistory()

  useEffect(() => {
    if (auth.email === "") {
      history.push("/login")
    }
    // Make the request in here
    fetch(url + 'selectAllUserPortfolios', {
      method: 'POST',
      mode: 'cors',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        email: auth.email
      })
    }).then((res) => {
      return res.json()
    }).then((res) => {
      dispatch(setPortfolios(res))
    })
  }, [])

  const portfolios = useSelector(getPortfolios)

  console.log(portfolios)
  return (
    <div css={css`
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        `
      }
    >
      <h2>Portfolios</h2>
      <NavLink to="/portfolios/create" css={css`text-decoration: none; color: #2b7bbe;`}>Create new portfolio</NavLink>
      {portfolios.map(portfolio => <Portfolio key={portfolio.name} {...portfolio} />)}
    </div>
  )
}