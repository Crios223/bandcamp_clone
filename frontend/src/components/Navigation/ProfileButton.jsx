// import { useDispatch } from 'react-redux';
// import { useNavigate } from 'react-router-dom';
// import { login } from '../../store/session';

// function ProfileButton({ user }) {
//   const dispatch = useDispatch();
//   const navigate = useNavigate();

//   const handleDemoLogin = async () => {
//     try {
//       await dispatch(login({ email: 'demo@demo.com', password: 'password' }));
//       navigate('/');
//     } catch (err) {
//       console.error('Demo login failed:', err);
//     }
//   };

//   if (user) {
//     return <p>Hello, {user.username}</p>; // replace with a real dropdown later
//   }

//   return (
//     <div className="profile-dropdown">
//       <button onClick={() => navigate('/login')}>Log In</button>
//       <button onClick={() => navigate('/signup')}>Sign Up</button>
//       <button onClick={handleDemoLogin}>Log in as Demo User</button>
//     </div>
//   );
// }

// export default ProfileButton;



















// import { useDispatch } from 'react-redux';
// import { useNavigate } from 'react-router-dom';
// import { login, logout } from '../../store/session';

// function ProfileButton({ user }) {
//   const dispatch = useDispatch();
//   const navigate = useNavigate();

//   const handleDemoLogin = async () => {
//     try {
//       await dispatch(login({ email: 'demo@demo.com', password: 'password' }));
//       navigate('/');
//     } catch (err) {
//       console.error('Demo login failed:', err);
//     }
//   };

//   const handleLogout = async () => {
//     try {
//       await dispatch(logout());
//       navigate('/');
//     } catch (err) {
//       console.error('Logout failed:', err);
//     }
//   };

//   if (user) {
//     return (
//       <div className="profile-logged-in">
//         <span>Hello, {user.username}</span>
//         <button onClick={handleLogout}>Log out</button>
//       </div>
//     );
//   }

//   return (
//     <div className="profile-dropdown">
//       <button onClick={() => navigate('/login')}>Log In</button>
//       <button onClick={() => navigate('/signup')}>Sign Up</button>
//       <button onClick={handleDemoLogin}>Log in as Demo User</button>
//     </div>
//   );
// }

// export default ProfileButton;








import { useDispatch } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import { login, logout } from '../../store/session';

function ProfileButton({ user }) {
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const handleDemoLogin = async () => {
    try {
      await dispatch(login({ email: 'demo@demo.com', password: 'password' }));
      navigate('/');
    } catch (err) {
      console.error('Demo login failed:', err);
    }
  };

  const handleLogout = async () => {
    try {
      await dispatch(logout());
      navigate('/');
    } catch (err) {
      console.error('Logout failed:', err);
    }
  };

  if (user) {
    return (
      <div className="profile-logged-in">
        <button onClick={handleLogout}>Log out</button>
      </div>
    );
  }

  return (
    <div className="profile-dropdown">
      <button onClick={() => navigate('/login')}>Log In</button>
      <button onClick={() => navigate('/signup')}>Sign Up</button>
      <button onClick={handleDemoLogin}>Log in as Demo User</button>
    </div>
  );
}

export default ProfileButton;