/** @jsx jsx */
import { css, jsx } from '@emotion/core'

import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { getPortfolios } from '../redux/selectors'
import { setPortfolios } from '../redux/actions'
import { NavLink } from 'react-router-dom'

import Portfolio from '../components/Portfolio'

const url = 'https://cors-anywhere.herokuapp.com/http://agile-trader.herokuapp.com/'

export default function Portfolios() {
  const dispatch = useDispatch()

  useEffect(() => {
    // Make the request in here
    fetch(url + 'selectAllUserPortfolios', {
      method: 'GET',
      mode: 'cors',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      }
    })
    dispatch(setPortfolios([{name:'Port1', id: 0},{name:'Port2', id: 1},{name:'Port3', id: 2}]))
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
      {portfolios.map(portfolio => <Portfolio key={portfolio.id} {...portfolio} />)}
    </div>
  )
}