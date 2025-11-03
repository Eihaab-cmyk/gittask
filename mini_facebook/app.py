from flask import Flask
from config import Config
from models import db, ma
from routes.user_routes import user_bp
from routes.post_routes import post_bp
from routes.comment_routes import comment_bp
from routes.like_routes import like_bp
from routes.friend_routes import friend_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
ma.init_app(app)

app.register_blueprint(user_bp)
app.register_blueprint(post_bp)
app.register_blueprint(comment_bp)
app.register_blueprint(like_bp)
app.register_blueprint(friend_bp)

@app.before_request
def create_tables():
    app.before_request_funcs[None].remove(create_tables)
    db.create_all()

@app.route('/')
def home():
    return {"message": "Welcome to Mini-Facebook API"}

if __name__ == '__main__':
    app.run(debug=True)