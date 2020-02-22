export const SET_USER_ID = 'SET_USER_ID'
export const SET_JWT = 'SET_JWT'
export const SET_USER_EMAIL = 'SET_USER_EMAIL'
export const SET_USER_PASS = 'SET_USER_PASS'

export function setUserEmail(email) {
    return { type: SET_USER_EMAIL, email }
}

export function setUserPass(userPass) {
    return { type: SET_USER_PASS, userPass }
}