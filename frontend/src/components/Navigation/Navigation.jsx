// import { useSelector, useDispatch } from 'react-redux';
// import { useNavigate } from 'react-router-dom';
// import ProfileButton from './ProfileButton';
// import './Navigation.css';

// function Navigation() {
//   const user = useSelector(state => state.session.user);
//   const navigate = useNavigate();

//   const goHome = () => navigate('/');

//   return (
//     <nav className="navbar">
//       <div className="navbar-left" onClick={goHome}>
//         <img src="/favicon.ico" alt="Bcamp" className="logo" />
//         <span className="brand-name">Bcamp</span>
//       </div>
//       <div className="navbar-right">
//         <ProfileButton user={user} />
//       </div>
//     </nav>
//   );
// }

// export default Navigation;














// import { useSelector } from 'react-redux';
// import { useNavigate } from 'react-router-dom';
// import ProfileButton from './ProfileButton';
// import './Navigation.css';

// function Navigation() {
//   const user = useSelector(state => state.session.user);
//   const navigate = useNavigate();

//   const goHome = () => navigate('/');

//   return (
//     <nav className="navbar">
//       <div className="navbar-left" onClick={goHome}>
//         <img src="/favicon.ico" alt="Bcamp" className="logo" />
//         <span className="brand-name">Bcamp</span>
//       </div>

//       <div className="navbar-right">
//         {user && (
//           <>
//             <div className="dropdown">
//               <button className="dropdown-btn">Add Product</button>
//               <div className="dropdown-content">
//                 <button onClick={() => navigate('/albums/new')}>Add Album</button>
//               </div>
//             </div>

//             <span className="hello-user">Hello, {user.username}</span>

//             <ProfileButton user={user} />

//             <div className="dropdown">
//               <button className="dropdown-btn">Manage Products</button>
//               <div className="dropdown-content">
//                 <button onClick={() => navigate('/albums/manage')}>Manage Albums</button>
//               </div>
//             </div>
//           </>
//         )}
//       </div>
//     </nav>
//   );
// }

// export default Navigation;







import { useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import ProfileButton from './ProfileButton';
import './Navigation.css';

function Navigation() {
  const user = useSelector(state => state.session.user);
  const navigate = useNavigate();

  const goHome = () => navigate('/');

  return (
    <nav className="navbar">
      <div className="navbar-left" onClick={goHome}>
        <img src="/favicon.ico" alt="Bcamp" className="logo" />
        <span className="brand-name">Bcamp</span>
      </div>

      <div className="navbar-right">
        {user ? (
          <>
            <div className="dropdown">
              <button className="dropdown-btn">Add Product</button>
              <div className="dropdown-content">
                <button onClick={() => navigate('/albums/new')}>Add Album</button>
              </div>
            </div>

            <span className="hello-user">Hello, {user.username}</span>

            <ProfileButton user={user} />

            <div className="dropdown">
              <button className="dropdown-btn">Manage Products</button>
              <div className="dropdown-content">
                <button onClick={() => navigate('/albums/manage')}>Manage Albums</button>
              </div>
            </div>
          </>
        ) : (
          <ProfileButton user={null} />
        )}
      </div>
    </nav>
  );
}

export default Navigation;