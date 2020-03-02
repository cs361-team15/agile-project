import { combineReducers } from 'redux'

import {
    SET_JWT,
    SET_USER_EMAIL,
    SET_USER_PASS,
    // Portfolio actions
    SET_PORTFOLIOS
} from './actions'

const initialState = {
    jwt: "",
    email: "",
    userPass: ""
}

function authReducer(state = initialState, action) {
    switch (action.type) {
        case SET_JWT:
            return {
                ...state,
                jwt: action.jwt
            }
        case SET_USER_EMAIL:
            return {
                ...state,
                email: action.email
            }
        case SET_USER_PASS:
            return {
                ...state,
                userPass: action.userPass
            }
        default:
            return state
    }
}

function portfolioReducer(state = [{}], action) {
    switch(action.type) {
        case SET_PORTFOLIOS:
            return action.portfolios
        default:
            return state
    }
}

const rootReducer = combineReducers({
    auth: authReducer,
    portfolios: portfolioReducer
})

export default rootReducer