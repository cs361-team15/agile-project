import { combineReducers } from 'redux'

import {
    SET_JWT,
    SET_USER_ID,
    SET_USER_EMAIL,
    SET_USER_PASS
} from './actions'

function authReducer(state = {}, action) {
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
        case SET_USER_ID:
            return {
                ...state,
                uID: action.uID
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

function portfolioReducer(state = [], action) {
    switch(action.type) {
        default:
            return state
    }
}

const rootReducer = combineReducers({
    auth: authReducer,
    portfolio: portfolioReducer
})

export default rootReducer