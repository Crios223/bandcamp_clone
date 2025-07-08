import { useEffect, useState } from 'react';
import { useSelector } from 'react-redux';

function ShopWishManage() {
  const user = useSelector(state => state.session.user);
  const [cartItems, setCartItems] = useState([]);

  useEffect(() => {
    if (user) fetchCart();
  }, [user]);

  const fetchCart = async () => {
    const res = await fetch('/api/cart/', { credentials: 'include' });
    if (res.ok) {
      const data = await res.json();
      const userCart = data.filter(item => item.user_id === user.id);
      setCartItems(userCart);
    }
  };

  const handleDelete = async (itemId) => {
    await fetch(`/api/cart/${itemId}`, { method: 'DELETE', credentials: 'include' });
    fetchCart();
  };

  return (
    <div className="shop-cart-container">
      <h2>Your Shopping Cart</h2>
      {cartItems.length ? (
        <ul className="cart-list">
          {cartItems.map(item => (
            <li key={item.id} className="cart-item">
              Album ID: {item.album_id}
              <button onClick={() => handleDelete(item.id)}>Remove</button>
            </li>
          ))}
        </ul>
      ) : (
        <p>Your cart is empty.</p>
      )}
    </div>
  );
}

export default ShopWishManage;