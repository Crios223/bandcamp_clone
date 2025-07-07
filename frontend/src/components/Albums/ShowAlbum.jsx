// import { useParams } from 'react-router-dom';
// import { useEffect, useState } from 'react';
// import { useSelector } from 'react-redux';
// import ReviewForm from '../ReviewForm/ReviewForm';
// import './ShowAlbum.css';

// function ShowAlbum() {
//   const { id } = useParams();
//   const [album, setAlbum] = useState(null);
//   const [reviews, setReviews] = useState([]);
//   const [showForm, setShowForm] = useState(false);
//   const user = useSelector(state => state.session.user);

//   useEffect(() => {
//     fetch(`http://localhost:5000/api/albums/${id}`)
//       .then(res => res.json())
//       .then(data => setAlbum(data));

//     fetch(`http://localhost:5000/api/reviews`)
//       .then(res => res.json())
//       .then(data => {
//         const filtered = data.filter(r => r.album_id === Number(id));
//         setReviews(filtered);
//       });
//   }, [id, showForm]);

//   const avgRating = reviews.length
//     ? (reviews.reduce((sum, r) => sum + r.rating, 0) / reviews.length).toFixed(1)
//     : 'new';

//   const userReview = user ? reviews.find(r => r.user_id === user.id) : null;

//   const handleDelete = async (reviewId) => {
//     await fetch(`http://localhost:5000/api/reviews/${reviewId}`, {
//       method: 'DELETE'
//     });
//     setReviews(reviews.filter(r => r.id !== reviewId));
//   };

//   if (!album) return <div className="album-show loading">Loading...</div>;

//   return (
//     <div className="album-show">
//       <img className="album-cover" src={album.cover_url} alt={album.title} />
//       <h2 className="album-title">{album.title}</h2>
//       <p className="album-description">{album.description}</p>

//       <div className="review-header">
//         <h3>Reviews</h3>
//         <span className="rating-score">{avgRating} 🤘</span>
//       </div>

//       {user && (
//         <div className="review-actions">
//           {userReview ? (
//             <>
//               <button onClick={() => setShowForm(true)}>I changed my mind</button>
//               <button onClick={() => handleDelete(userReview.id)}>Delete</button>
//             </>
//           ) : (
//             <button onClick={() => setShowForm(true)}>
//               {reviews.length ? 'Everyone\'s a Critic' : 'Be the First'}
//             </button>
//           )}
//         </div>
//       )}

//       {showForm && (
//         <ReviewForm
//           albumId={album.id}
//           existingReview={userReview}
//           onClose={() => setShowForm(false)}
//         />
//       )}

//       <div className="review-list">
//         {reviews.map(r => (
//           <div key={r.id} className="review-item">
//             <div>
//               <strong>{r.rating} 🤘</strong>
//               <p>{r.comment}</p>
//             </div>
//           </div>
//         ))}
//       </div>
//     </div>
//   );
// }

// export default ShowAlbum;

// import { useParams } from 'react-router-dom';
// import { useEffect, useState } from 'react';
// import { useSelector } from 'react-redux';
// import ReviewForm from '../ReviewForm/ReviewForm';
// import './ShowAlbum.css';

// function ShowAlbum() {
//   const { id } = useParams();
//   const [album, setAlbum] = useState(null);
//   const [reviews, setReviews] = useState([]);
//   const [showForm, setShowForm] = useState(false);
//   const user = useSelector(state => state.session.user);

//   const fetchReviews = () => {
//     fetch(`http://localhost:5000/api/reviews/album/${id}`)
//       .then(res => res.json())
//       .then(data => setReviews(data));
//   };

//   useEffect(() => {
//     fetch(`http://localhost:5000/api/albums/${id}`)
//       .then(res => res.json())
//       .then(data => setAlbum(data));

//     fetchReviews();
//   }, [id]);

//   const avgRating = reviews.length
//     ? (reviews.reduce((sum, r) => sum + r.rating, 0) / reviews.length).toFixed(1)
//     : 'new';

//   const userReview = user ? reviews.find(r => r.user_id === user.id) : null;

//   const handleDelete = async (reviewId) => {
//     await fetch(`http://localhost:5000/api/reviews/${reviewId}`, {
//       method: 'DELETE',
//       credentials: 'include', // ✅ Ensure user is authenticated
//     });
//     setShowForm(false);
//     fetchReviews(); // ✅ Reload updated list
//   };

//   const handleReviewSuccess = () => {
//     fetchReviews();       // ✅ Reload clean data
//     setShowForm(false);   // ✅ Close form
//   };

//   if (!album) return <div className="album-show loading">Loading...</div>;

//   return (
//     <div className="album-show">
//       <img className="album-cover" src={album.cover_url} alt={album.title} />
//       <h2 className="album-title">{album.title}</h2>
//       <p className="album-description">{album.description}</p>

//       <div className="review-header">
//         <h3>Reviews</h3>
//         <span className="rating-score">{avgRating} 🤘</span>
//       </div>

//       {user && (
//         <div className="review-actions">
//           {userReview ? (
//             <>
//               <button onClick={() => setShowForm(true)}>I changed my mind</button>
//               <button onClick={() => handleDelete(userReview.id)}>Delete</button>
//             </>
//           ) : (
//             <button onClick={() => setShowForm(true)}>
//               {reviews.length ? "Everyone's a Critic" : 'Be the First'}
//             </button>
//           )}
//         </div>
//       )}

//       {showForm && (
//         <ReviewForm
//           albumId={album.id}
//           existingReview={userReview}
//           onSuccess={handleReviewSuccess}
//         />
//       )}

//       <div className="review-list">
//         {reviews.map(r => (
//           <div key={r.id} className="review-item">
//             <div>
//               <strong>{r.rating} 🤘</strong>
//               <p>{r.comment}</p>
//             </div>
//           </div>
//         ))}
//       </div>
//     </div>
//   );
// }

// export default ShowAlbum;





import { useParams } from 'react-router-dom';
import { useEffect, useState } from 'react';
import { useSelector } from 'react-redux';
import ReviewForm from '../ReviewForm/ReviewForm';
import './ShowAlbum.css';

function ShowAlbum() {
  const { id } = useParams();
  const [album, setAlbum] = useState(null);
  const [reviews, setReviews] = useState([]);
  const [showForm, setShowForm] = useState(false);
  const user = useSelector(state => state.session.user);

  const fetchReviews = () => {
    fetch(`http://localhost:5000/api/reviews/album/${id}`)
      .then(res => res.json())
      .then(data => setReviews(data));
  };

  useEffect(() => {
    fetch(`http://localhost:5000/api/albums/${id}`)
      .then(res => res.json())
      .then(data => setAlbum(data));

    fetchReviews();
  }, [id]);

  const avgRating = reviews.length
    ? (reviews.reduce((sum, r) => sum + r.rating, 0) / reviews.length).toFixed(1)
    : 'new';

  const userReview = user ? reviews.find(r => r.user_id === user.id) : null;

  const handleDelete = async (reviewId) => {
    await fetch(`http://localhost:5000/api/reviews/${reviewId}`, {
      method: 'DELETE',
      credentials: 'include',
    });
    setShowForm(false);
    fetchReviews();
  };

  const handleReviewSuccess = () => {
    fetchReviews();
    setShowForm(false);
  };

  if (!album) return <div className="album-show loading">Loading...</div>;

  return (
    <div className="album-show">
      <img className="album-cover" src={album.cover_url} alt={album.title} />
      <h2 className="album-title">{album.title}</h2>
      <p className="album-description">{album.description}</p>

      <div className="review-header">
        <h3>Reviews</h3>
        <span className="rating-score">{avgRating} 🤘</span>
      </div>

      {showForm && (
        <ReviewForm
          albumId={album.id}
          existingReview={userReview}
          onSuccess={handleReviewSuccess}
        />
      )}

      <div className="review-list">
        {reviews.map(r => (
          <div key={r.id} className="review-item">
            <div>
              <strong>{r.rating} 🤘</strong>
              <p>{r.comment}</p>
            </div>

            {user && r.user_id === user.id && (
              <div className="review-buttons">
                <button onClick={() => setShowForm(true)}>I changed my mind</button>
                <button onClick={() => handleDelete(r.id)}>Delete</button>
              </div>
            )}
          </div>
        ))}
      </div>

      {user && !userReview && !showForm && (
        <div className="review-actions">
          <button onClick={() => setShowForm(true)}>
            {reviews.length ? "Everyone's a Critic" : 'Be the First'}
          </button>
        </div>
      )}
    </div>
  );
}

export default ShowAlbum;