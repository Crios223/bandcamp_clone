import { createSlice } from '@reduxjs/toolkit';

// Initial state
const initialState = { user: null };

// Slice
const sessionSlice = createSlice({
  name: 'session',
  initialState,
  reducers: {
    setUser(state, action) {
      state.user = action.payload;
    },
    removeUser(state) {
      state.user = null;
    }
  }
});

export const { setUser, removeUser } = sessionSlice.actions;

//
// --------------------- THUNKS ---------------------
//

// Login
export const login = (credentials) => async dispatch => {
  const res = await fetch('http://localhost:5000/api/auth/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    credentials: 'include', // required for Flask session cookies
    body: JSON.stringify(credentials)
  });

  if (res.ok) {
    const user = await res.json();
    dispatch(setUser(user));
    return user;
  } else {
    const error = await res.json();
    throw error;
  }
};

// Restore session
export const restoreUser = () => async dispatch => {
  const res = await fetch('http://localhost:5000/api/auth/', {
    credentials: 'include'
  });

  if (res.ok) {
    const user = await res.json();
    dispatch(setUser(user));
    return user;
  }
};

// Logout
export const logout = () => async dispatch => {
  const res = await fetch('http://localhost:5000/api/auth/logout', {
    method: 'DELETE',
    credentials: 'include'
  });

  if (res.ok) {
    dispatch(removeUser());
  }
};

export default sessionSlice.reducer;
