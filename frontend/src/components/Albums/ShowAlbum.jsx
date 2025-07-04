import { useParams } from 'react-router-dom';
import { useEffect, useState } from 'react';
import './ShowAlbum.css';

function ShowAlbum() {
  const { id } = useParams();
  const [album, setAlbum] = useState(null);

  useEffect(() => {
    fetch(`http://localhost:5000/api/albums/${id}`)
      .then(res => res.json())
      .then(data => setAlbum(data));
  }, [id]);

  if (!album) return <div className="album-show loading">Loading...</div>;

  return (
    <div className="album-show">
      <img className="album-cover" src={album.cover_url} alt={album.title} />
      <h2 className="album-title">{album.title}</h2>
      <p className="album-description">{album.description}</p>
    </div>
  );
}

export default ShowAlbum;