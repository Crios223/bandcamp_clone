//?   ------ GET all Albums --------------

import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

function LandingPage() {
  const [albums, setAlbums] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    fetch('http://localhost:5000/api/albums')
      .then(res => res.json())
      .then(data => setAlbums(data));
  }, []);

  return (
    <div className="landing-page">
      <h1>All Albums</h1>
      <div className="album-grid">
        {albums.map(album => (
          <div
            key={album.id}
            className="album-card"
            onClick={() => navigate(`/albums/${album.id}`)}
          >
            <img src={album.cover_url} alt={album.title} style={{ width: '200px' }} />
            <h3>{album.title}</h3>
          </div>
        ))}
      </div>
    </div>
  );
}

export default LandingPage;