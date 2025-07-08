import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useDispatch } from 'react-redux'; 
import { setUser } from '../../store/session'; 
import './SignupForm.css';

function SignupForm() {
  const navigate = useNavigate();
  const dispatch = useDispatch(); 
  const [step, setStep] = useState(1);

  const [formData, setFormData] = useState({
    artist_name: '',
    username: '',
    email: '',
    password: '',
    genre: '',
    genre_tags: '',
    location: '',
    bandcamp_url: ''
  });

  const handleChange = e => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const next = () => setStep(step + 1);
  const back = () => setStep(step - 1);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await fetch('http://localhost:5000/api/auth/signup', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify(formData)
      });

      if (res.ok) {
        const user = await res.json();
        dispatch(setUser(user));
        console.log("✅ Signed up & logged in:", user);
        navigate('/');
      } else {
        const error = await res.json();
        console.error("❌ Signup error:", error);
        alert(error.message);
      }
    } catch (err) {
      console.error("❌ Unexpected error during signup:", err);
      alert("Something went wrong. Please try again.");
    }
  };

  return (
    <div className="signup-form-container">
      <form onSubmit={handleSubmit} className="signup-form">
        {step === 1 && (
          <>
            <h2>Signup Page 1</h2>
            <input
              name="artist_name"
              placeholder="Artist/Band name"
              value={formData.artist_name}
              onChange={handleChange}
              required
            />
            <input
              name="username"
              placeholder="Username"
              value={formData.username}
              onChange={handleChange}
              required
            />
            <input
              name="email"
              placeholder="Email"
              type="email"
              value={formData.email}
              onChange={handleChange}
              required
            />
            <input
              name="password"
              placeholder="Password"
              type="password"
              value={formData.password}
              onChange={handleChange}
              required
            />
            <button type="button" onClick={next}>Next</button>
          </>
        )}

        {step === 2 && (
          <>
            <h2>Signup Page 2</h2>
            <select name="genre" value={formData.genre} onChange={handleChange} required>
              <option value="">Select genre</option>
              <option>Rock</option>
              <option>Hip-Hop</option>
              <option>Electronic</option>
              <option>Jazz</option>
              <option>Other</option>
            </select>
            <input
              name="genre_tags"
              placeholder="Genre tag(s) (optional)"
              value={formData.genre_tags}
              onChange={handleChange}
            />
            <input
              name="location"
              placeholder="Location (e.g. NYC, Berlin)"
              value={formData.location}
              onChange={handleChange}
            />
            <button type="button" onClick={back}>Back</button>
            <button type="button" onClick={next}>Next</button>
          </>
        )}

        {step === 3 && (
          <>
            <h2>Signup Page 3</h2>
            <label>Your Bandcamp URL</label>
            <div className="url-input">
              <input
                name="bandcamp_url"
                value={formData.bandcamp_url}
                onChange={handleChange}
                required
              />
              <span>.bandcamp.com</span>
            </div>
            <button type="button" onClick={back}>Back</button>
            <button type="submit">Done</button>
          </>
        )}
      </form>
    </div>
  );
}

export default SignupForm;