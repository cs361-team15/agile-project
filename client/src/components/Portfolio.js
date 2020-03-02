import React from 'react'


export default function Portfolio({ name, activation_date, balance, total_value}) {
  return (
    <div>
      <h3>{name}</h3>
      <p>Date created: {activation_date}</p>
      <p>Current cash balance: {balance}</p>
      <p>Current total value: {total_value}</p>
    </div>
  )
}
