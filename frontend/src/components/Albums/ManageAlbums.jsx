import { useEffect, useState } from 'react';
import { useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom';
// yeah man, this is the ManageAlbums component
function ManageAlbums() {
  const user = useSelector(state => state.session.user);
  const [albums, setAlbums] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchAlbums = async () => {
      const res = await fetch('http://localhost:5000/api/albums/current', {
        credentials: 'include'
      });
      if (res.ok) {
        const data = await res.json();
        setAlbums(data);
      }
    };
    fetchAlbums();
  }, []);

  const handleDelete = async (albumId) => {
    const confirmed = window.confirm("Are you sure you want to delete this album?");
    if (!confirmed) return;

    const res = await fetch(`http://localhost:5000/api/albums/${albumId}`, {
      method: 'DELETE',
      credentials: 'include'
    });

    if (res.ok) {
      setAlbums(prev => prev.filter(album => album.id !== albumId));
    }
  };

  const handleEdit = (albumId) => {
    navigate(`/albums/${albumId}/edit`);
  };

  return (
    <div className="manage-albums-page">
      <h2>Your Albums</h2>
      {albums.length === 0 ? (
        <p>No albums yet.</p>
      ) : (
        <div className="album-list">
          {albums.map(album => (
            <div key={album.id} className="album-card">
              <h3>{album.title}</h3>
              <p className="artist">By: {user.username}</p>
              <button onClick={() => handleEdit(album.id)}>Update</button>
              <button onClick={() => handleDelete(album.id)}>Delete</button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default ManageAlbums;