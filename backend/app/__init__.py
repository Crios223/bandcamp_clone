# from flask import Flask, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_cors import CORS
# from flask_login import LoginManager
# import os

# # Initialize extensions
# db = SQLAlchemy()
# migrate = Migrate()
# login_manager = LoginManager()

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object("app.config.Config")

#     db.init_app(app)
#     migrate.init_app(app, db)

#     CORS(app, supports_credentials=True, origins=[
#         "http://localhost:5173", "http://127.0.0.1:5173"
#     ])

#     login_manager.init_app(app)

#     # REMOVE this line to stop redirects:
#     # login_manager.login_view = "auth.login"

#     @login_manager.unauthorized_handler
#     def unauthorized():
#         return jsonify({"message": "Unauthorized"}), 401

#     @login_manager.user_loader
#     def load_user(user_id):
#         from app.models import User
#         return User.query.get(int(user_id))

#     # Import models
#     from app.models.user import User
#     from app.models.album import Album
#     from app.models.track import Track
#     from app.models.image import Image
#     from app.models.review import Review
#     from app.models.cart_item import CartItem
#     from app.models.wishlist_item import WishlistItem

#     # Register routes
#     from app.routes import main
#     from app.routes.albums_routes import albums_bp
#     from app.routes.auth_routes import auth_routes
#     from app.routes.track_routes import track_routes
#     from app.routes.image_routes import image_routes
#     from app.routes.review_routes import review_routes
#     from app.routes.wishlist_routes import wishlist_routes
#     from app.routes.cart_routes import cart_routes

#     app.register_blueprint(main)
#     app.register_blueprint(albums_bp)
#     app.register_blueprint(auth_routes)
#     app.register_blueprint(track_routes, url_prefix="/api/tracks")
#     app.register_blueprint(image_routes, url_prefix="/api/images")
#     app.register_blueprint(review_routes, url_prefix="/api/reviews")
#     app.register_blueprint(wishlist_routes)
#     app.register_blueprint(cart_routes)

#     return app


# Above work AlbumCRUD


from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_login import LoginManager
import os

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    # Session Cookie Settings (🔐 persist login)
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
    app.config['SESSION_COOKIE_SECURE'] = False  # Set to True in production w/ HTTPS

    db.init_app(app)
    migrate.init_app(app, db)

    CORS(app, supports_credentials=True, origins=[
        "http://localhost:5173", "http://127.0.0.1:5173"
    ])

    login_manager.init_app(app)

    # Custom unauthorized handler to avoid redirects
    @login_manager.unauthorized_handler
    def unauthorized():
        return jsonify({"message": "Unauthorized"}), 401

    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User
        return User.query.get(int(user_id))

    # Import models
    from app.models.user import User
    from app.models.album import Album
    from app.models.track import Track
    from app.models.image import Image
    from app.models.review import Review
    from app.models.cart_item import CartItem
    from app.models.wishlist_item import WishlistItem

    # Register routes
    from app.routes import main
    from app.routes.albums_routes import albums_bp
    from app.routes.auth_routes import auth_routes
    from app.routes.track_routes import track_routes
    from app.routes.image_routes import image_routes
    from app.routes.review_routes import review_routes
    from app.routes.wishlist_routes import wishlist_routes
    from app.routes.cart_routes import cart_routes

    app.register_blueprint(main)
    app.register_blueprint(albums_bp)
    app.register_blueprint(auth_routes)
    app.register_blueprint(track_routes, url_prefix="/api/tracks")
    app.register_blueprint(image_routes, url_prefix="/api/images")
    app.register_blueprint(review_routes, url_prefix="/api/reviews")
    app.register_blueprint(wishlist_routes)
    app.register_blueprint(cart_routes)

    return app