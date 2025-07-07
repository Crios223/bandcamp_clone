import { createSlice } from '@reduxjs/toolkit';

const reviewsSlice = createSlice({
  name: 'reviews',
  initialState: {},
  reducers: {
    setReviews(state, action) {
      const reviews = action.payload;
      for (let review of reviews) {
        state[review.id] = review;
      }
    },
    addReview(state, action) {
      state[action.payload.id] = action.payload;
    },
    editReview(state, action) {
      state[action.payload.id] = action.payload;
    },
    removeReview(state, action) {
      delete state[action.payload];
    },
  },
});

export const { setReviews, addReview, editReview, removeReview } = reviewsSlice.actions;

export const fetchReviews = (albumId) => async dispatch => {
  const res = await fetch(`/api/reviews/album/${albumId}`);
  if (res.ok) {
    const data = await res.json();
    dispatch(setReviews(data));
  }
};

export const createReview = (review) => async dispatch => {
  const res = await fetch(`/api/reviews/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    credentials: 'include',
    body: JSON.stringify(review)
  });
  if (res.ok) {
    const data = await res.json();
    dispatch(addReview(data));
  }
};

export const updateReview = (id, review) => async dispatch => {
  const res = await fetch(`/api/reviews/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    credentials: 'include',
    body: JSON.stringify(review)
  });
  if (res.ok) {
    const data = await res.json();
    dispatch(editReview(data));
  }
};

export const deleteReview = (id) => async dispatch => {
  const res = await fetch(`/api/reviews/${id}`, {
    method: 'DELETE',
    credentials: 'include'
  });
  if (res.ok) {
    dispatch(removeReview(id));
  }
};

export default reviewsSlice.reducer;