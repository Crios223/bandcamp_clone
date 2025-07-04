import { useState } from 'react';
import { useDispatch } from 'react-redux';
import { useNavigate } from 'react-router-dom';

function AlbumForm() {
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const [title, setTitle] = useState('');
  const [releaseDate, setReleaseDate] = useState('');
  const [price, setPrice] = useState('');
  const [coverUrl, setCoverUrl] = useState('');
  const [artist, setArtist] = useState('');
  const [description, setDescription] = useState('');
  const [credits, setCredits] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const payload = {
      title,
      release_date: releaseDate,
      price,
      cover_url: coverUrl,
      artist,
      description,
      credits,
    };

    const res = await fetch('http://localhost:5000/api/albums/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'include',
      body: JSON.stringify(payload),
    });

    if (res.ok) {
      const album = await res.json();
      navigate(`/albums/${album.id}`);
    }
  };

  return (
    <form className="album-form" onSubmit={handleSubmit}>
      <h2>Create Album</h2>
      <label>Album Title*
        <input value={title} onChange={e => setTitle(e.target.value)} placeholder="Album name" required />
      </label>

      <label>Release Date
        <input value={releaseDate} onChange={e => setReleaseDate(e.target.value)} placeholder="mm/dd/yyyy (optional)" />
      </label>

      <label>Pricing*
        <input value={price} onChange={e => setPrice(e.target.value)} placeholder="9.00" required /> USD
      </label>

      <label>Upload Album Cover (URL)
        <input value={coverUrl} onChange={e => setCoverUrl(e.target.value)} placeholder="upload album art" />
      </label>

      <label>Artist
        <input value={artist} onChange={e => setArtist(e.target.value)} placeholder="leave blank to use username" />
      </label>

      <label>About this Album
        <textarea value={description} onChange={e => setDescription(e.target.value)} placeholder="(optional)" />
      </label>

      <label>Album Credits
        <textarea value={credits} onChange={e => setCredits(e.target.value)} placeholder="(optional)" />
      </label>

      <button type="submit">Add Album</button>
    </form>
  );
}

export default AlbumForm;
