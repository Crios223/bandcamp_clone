// import { useState } from 'react';
// import { useDispatch, useSelector } from 'react-redux';

// function ReviewForm({ albumId, onSuccess, existingReview }) {
//   const dispatch = useDispatch();
//   const user = useSelector(state => state.session.user);

//   const [rating, setRating] = useState(existingReview?.rating || 0);
//   const [comment, setComment] = useState(existingReview?.comment || '');
//   const [errors, setErrors] = useState([]);

//   const handleSubmit = async e => {
//     e.preventDefault();
//     if (!user) {
//       setErrors(["You must be logged in to leave a review."]);
//       return;
//     }

//     const payload = {
//       rating,
//       comment,
//       album_id: albumId,
//       user_id: user.id,
//     };

//     try {
//       const res = await fetch(`/api/reviews${existingReview ? `/${existingReview.id}` : ''}`, {
//         method: existingReview ? 'PUT' : 'POST',
//         headers: { 'Content-Type': 'application/json' },
//         credentials: 'include',
//         body: JSON.stringify(payload),
//       });

//       const data = await res.json();
//       if (res.ok) {
//         onSuccess?.(data);
//       } else {
//         setErrors(data.errors || [data.message || "Something went wrong."]);
//       }
//     } catch (err) {
//       console.error(err);
//       setErrors(["Something went wrong."]);
//     }
//   };

//   const renderHands = () => {
//     return Array.from({ length: 5 }, (_, i) => (
//       <span
//         key={i}
//         style={{ cursor: 'pointer', fontSize: '24px', marginRight: 4 }}
//         onClick={() => setRating(i + 1)}
//       >
//         {i < rating ? '🤘' : '🖐️'}
//       </span>
//     ));
//   };

//   return (
//     <form onSubmit={handleSubmit} className="review-form">
//       <h2>{existingReview ? 'Edit Your Review' : 'Leave a Review'}</h2>

//       {errors.length > 0 && (
//         <ul className="review-errors">
//           {errors.map((err, i) => <li key={i}>{err}</li>)}
//         </ul>
//       )}

//       <div className="rating-input">
//         <label>Rating:</label>
//         <div>{renderHands()}</div>
//       </div>

//       <div>
//         <label>Comment:</label>
//         <textarea
//           value={comment}
//           onChange={e => setComment(e.target.value)}
//           rows={4}
//           placeholder="Share your thoughts..."
//         />
//       </div>

//       <button type="submit">
//         {existingReview ? 'Update Review' : 'Submit Review'}
//       </button>
//     </form>
//   );
// }

// export default ReviewForm;



import { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import './ReviewForm.css';

function ReviewForm({ albumId, onSuccess, existingReview }) {
  const dispatch = useDispatch();
  const user = useSelector(state => state.session.user);

  const [rating, setRating] = useState(existingReview?.rating || 0);
  const [hover, setHover] = useState(0);
  const [comment, setComment] = useState(existingReview?.comment || '');
  const [errors, setErrors] = useState([]);

  const handleSubmit = async e => {
    e.preventDefault();
    if (!user) {
      setErrors(["You must be logged in to leave a review."]);
      return;
    }

    const payload = {
      rating,
      comment,
      album_id: albumId,
      user_id: user.id,
    };

    try {
      const res = await fetch(`http://localhost:5000/api/reviews${existingReview ? `/${existingReview.id}` : ''}`, {
        method: existingReview ? 'PUT' : 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify(payload),
      });

      if (res.ok) {
        const data = await res.json();
        onSuccess?.(data);
      } else {
        const errorText = await res.text();
        try {
          const errorData = JSON.parse(errorText);
          setErrors(errorData.errors || [errorData.message || "Something went wrong."]);
        } catch {
          setErrors(["Unexpected server response."]);
        }
      }
    } catch (err) {
      console.error(err);
      setErrors(["Something went wrong."]);
    }
  };

  const renderHands = () => {
    return Array.from({ length: 5 }, (_, i) => (
      <span
        key={i}
        className={`rating-icon ${i < rating ? 'selected' : ''} ${hover > i ? 'hovered' : ''}`}
        onClick={() => setRating(i + 1)}
        onMouseEnter={() => setHover(i + 1)}
        onMouseLeave={() => setHover(0)}
      >
        🤘
        {rating === i + 1 && <span className="checkmark">✅</span>}
      </span>
    ));
  };

  return (
    <form onSubmit={handleSubmit} className="review-form">
      <h2>{existingReview ? 'Edit Your Review' : 'Leave a Review'}</h2>

      {errors.length > 0 && (
        <ul className="review-errors">
          {errors.map((err, i) => <li key={i}>{err}</li>)}
        </ul>
      )}

      <div className="rating-input">
        <label>Rating:</label>
        <div className="rating-icons">{renderHands()}</div>
      </div>

      <div className="comment-area">
        <label>Comment:</label>
        <textarea
          value={comment}
          onChange={e => setComment(e.target.value)}
          rows={4}
          placeholder="Share your thoughts..."
        />
      </div>

      <button type="submit">
        {existingReview ? 'Update Review' : 'Submit Review'}
      </button>
    </form>
  );
}

export default ReviewForm;