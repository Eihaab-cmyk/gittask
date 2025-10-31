from flask import Blueprint, request, jsonify
from models import db, Post, PostSchema

post_bp = Blueprint('post_bp', __name__)
post_schema = PostSchema()
posts_schema = PostSchema(many=True)

@post_bp.route('/posts', methods=['POST'])
def create_post():
    data = request.json
    new_post = Post(title=data['title'], content=data['content'], user_id=data['user_id'])
    db.session.add(new_post)
    db.session.commit()
    return post_schema.jsonify(new_post)

@post_bp.route('/posts/<int:id>', methods=['PUT'])
def edit_post(id):
    post = Post.query.get_or_404(id)
    data = request.json
    post.title = data.get('title', post.title)
    post.content = data.get('content', post.content)
    db.session.commit()
    return post_schema.jsonify(post)

@post_bp.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({"message": "Post deleted successfully"})

@post_bp.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return posts_schema.jsonify(posts)

# get post by id
@post_bp.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    post = Post.query.get_or_404(id)
    return post_schema.jsonify(post)

# get post by user id
@post_bp.route('/posts/user/<int:user_id>', methods=['GET'])
def get_posts_by_user(user_id):
    posts = Post.query.filter_by(user_id=user_id).all()
    return posts_schema.jsonify(posts)