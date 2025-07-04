import { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import './UpdateAlbum.css';



function UpdateAlbum() {
  const { id } = useParams();
  const navigate = useNavigate();

  const [album, setAlbum] = useState(null);
  const [title, setTitle] = useState('');
  const [releaseDate, setReleaseDate] = useState('');
  const [price, setPrice] = useState('');
  const [coverUrl, setCoverUrl] = useState('');
  const [artist, setArtist] = useState('');
  const [description, setDescription] = useState('');
  const [credits, setCredits] = useState('');
  const [errors, setErrors] = useState({});

  useEffect(() => {
    // Fetch album by ID when component mounts
    fetch(`http://localhost:5000/api/albums/${id}`, {
      credentials: 'include',
    })
      .then((res) => {
        if (!res.ok) throw new Error('Failed to fetch album');
        return res.json();
      })
      .then((data) => {
        setAlbum(data);
        setTitle(data.title || '');
        setReleaseDate(data.release_date || '');
        setPrice(data.price || '');
        setCoverUrl(data.cover_url || '');
        setArtist(data.artist || '');
        setDescription(data.description || '');
        setCredits(data.credits || '');
      })
      .catch((err) => console.error(err));
  }, [id]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrors({});

    const payload = {
      title,
      release_date: releaseDate,
      price,
      cover_url: coverUrl,
      artist,
      description,
      credits,
    };

    const res = await fetch(`http://localhost:5000/api/albums/${id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'include',
      body: JSON.stringify(payload),
    });

    if (res.ok) {
      const updated = await res.json();
      navigate(`/albums/${updated.id}`);
    } else {
      const errorData = await res.json();
      setErrors(errorData.errors || { general: 'Failed to update album' });
    }
  };

  if (!album) return <div>Loading...</div>;

  return (
    <div className="album-form">
      <h2>Update Album</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Album Title*
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="Album name"
          />
        </label>

        <label>
          Release Date
          <input
            type="date"
            value={releaseDate}
            onChange={(e) => setReleaseDate(e.target.value)}
          />
        </label>

        <label>
          Pricing (USD)
          <input
            type="number"
            step="0.01"
            value={price}
            onChange={(e) => setPrice(e.target.value)}
            placeholder="9.00"
          />
        </label>

        <label>
          Upload Album Cover
          <input
            type="text"
            value={coverUrl}
            onChange={(e) => setCoverUrl(e.target.value)}
            placeholder="Image URL"
          />
        </label>

        <label>
          Artist
          <input
            type="text"
            value={artist}
            onChange={(e) => setArtist(e.target.value)}
            placeholder="Leave blank to use username"
          />
        </label>

        <label>
          About This Album
          <textarea
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            placeholder="(optional)"
          />
        </label>

        <label>
          Album Credits
          <textarea
            value={credits}
            onChange={(e) => setCredits(e.target.value)}
            placeholder="(optional)"
          />
        </label>

        <button type="submit">Update Album</button>
      </form>
    </div>
  );
}

export default UpdateAlbum;