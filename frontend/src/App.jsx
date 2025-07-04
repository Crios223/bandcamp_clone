// import { useState, useEffect } from 'react';
// import { useDispatch }       from 'react-redux';
// import {
//   createBrowserRouter,
//   RouterProvider,
//   Outlet,
// } from 'react-router-dom';


// import Navigation from './components/Navigation/Navigation';



// export default function App() {
//   return (
//     <>
//       <Navigation />
//       <Outlet />
//     </>
//   );
// }

// ------ CRUD OG CODE ------

// import { Routes, Route } from 'react-router-dom';
// import Navigation from './components/Navigation/Navigation';
// import AlbumForm from './components/AlbumForm/AlbumForm';
// import AlbumShow from './components/Albums/ShowAlbum';
// import LandingPage from './components/LandingPage/LandingPage';
// import ManageAlbums from './components/Albums/ManageAlbums';
// import UpdateAlbum from "./components/Albums/UpdateAlbum";

// export default function App() {
//   return (
//     <>
//       <Navigation />
//       <Routes>
//         <Route path="/" element={<LandingPage />} />
//         <Route path="/albums/new" element={<AlbumForm />} />
//         <Route path="/albums/:id" element={<AlbumShow />} />
//         <Route path="/albums/manage" element={<ManageAlbums />} />
//         <Route path="/albums/:id/edit" element={<UpdateAlbum />} />
//       </Routes>
//     </>
//   );
// }


import { useEffect, useState } from 'react';
import { useDispatch } from 'react-redux';
import { Routes, Route } from 'react-router-dom';

import Navigation from './components/Navigation/Navigation';
import AlbumForm from './components/AlbumForm/AlbumForm';
import AlbumShow from './components/Albums/ShowAlbum';
import LandingPage from './components/LandingPage/LandingPage';
import ManageAlbums from './components/Albums/ManageAlbums';
import UpdateAlbum from './components/Albums/UpdateAlbum';

import { restoreUser } from './store/session';

export default function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);

  useEffect(() => {
    dispatch(restoreUser()).then(() => setIsLoaded(true));
  }, [dispatch]);

  if (!isLoaded) return null; // or loading spinner

  return (
    <>
      <Navigation />
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/albums/new" element={<AlbumForm />} />
        <Route path="/albums/:id" element={<AlbumShow />} />
        <Route path="/albums/manage" element={<ManageAlbums />} />
        <Route path="/albums/:id/edit" element={<UpdateAlbum />} />
      </Routes>
    </>
  );
}