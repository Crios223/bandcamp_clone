# from flask import Flask
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

#     # Initialize extensions
#     db.init_app(app)
#     migrate.init_app(app, db)
#     CORS(app)
#     login_manager.init_app(app)

#     # Optional: Set the login view route name
#     login_manager.login_view = "auth.login"

#     # User loader callback for Flask-Login
#     @login_manager.user_loader
#     def load_user(user_id):
#         from app.models import User
#         return User.query.get(int(user_id))

#     # Import models early to ensure they're registered before routes use them
#     from app import models

#     # Register blueprints
#     from app.routes import main
#     from app.routes.albums_routes import albums_bp
#     from app.routes.auth_routes import auth_routes  # <-- added auth routes

#     app.register_blueprint(main)
#     app.register_blueprint(albums_bp)      # url_prefix already set in albums_bp
#     app.register_blueprint(auth_routes)    # url_prefix already set in auth_routes

#     return app



# from flask import Flask
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

#     # Initialize extensions
#     db.init_app(app)
#     migrate.init_app(app, db)
#     CORS(app)
#     login_manager.init_app(app)

#     # Optional: Set the login view route name
#     login_manager.login_view = "auth.login"

#     # User loader callback for Flask-Login
#     @login_manager.user_loader
#     def load_user(user_id):
#         from app.models import User
#         return User.query.get(int(user_id))


#     # Import models early to ensure they're registered before routes use them
#     from app import models

#     # Import models early to ensure they're registered before routes use them
#     # This avoids the 'no property reviews' error
#     from app.models.user import User
#     from app.models.album import Album
#     from app.models.review import Review
#     from app.models.track import Track
#     from app.models.image import Image

#     # Register blueprints
#     from app.routes import main
#     from app.routes.albums_routes import albums_bp
#     from app.routes.auth_routes import auth_routes  # <-- added auth routes

#     app.register_blueprint(main)
#     app.register_blueprint(albums_bp)      # url_prefix already set in albums_bp
#     app.register_blueprint(auth_routes)    # url_prefix already set in auth_routes

#     return app



from flask import Flask
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

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    login_manager.init_app(app)

    # Optional: Set the login view route name
    login_manager.login_view = "auth.login"

    # User loader callback for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User
        return User.query.get(int(user_id))

    # ✅ Import models explicitly and in safe order
    from app.models.user import User
    from app.models.album import Album
    from app.models.track import Track
    from app.models.image import Image
    from app.models.review import Review
    from app.models.cart_item import CartItem
    from app.models.wishlist_item import WishlistItem

    # Register blueprints
    from app.routes import main
    from app.routes.albums_routes import albums_bp
    from app.routes.auth_routes import auth_routes

    app.register_blueprint(main)
    app.register_blueprint(albums_bp)      # url_prefix already set in albums_bp
    app.register_blueprint(auth_routes)    # url_prefix already set in auth_routes

    return app