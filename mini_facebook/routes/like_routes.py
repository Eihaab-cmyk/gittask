# routes/like_routes.py
from flask import Blueprint, request, jsonify
from models import db, Like, LikeSchema

like_bp = Blueprint('like_bp', __name__)
like_schema = LikeSchema()
likes_schema = LikeSchema(many=True)

# Like a post
@like_bp.route('/likes', methods=['POST'])
def like_post():
    data = request.json
    like = Like(user_id=data['user_id'], post_id=data['post_id'])
    try:
        db.session.add(like)
        db.session.commit()
    except:
        return jsonify({"message": "Already liked"}), 400
    return like_schema.jsonify(like)

# Unlike a post
@like_bp.route('/likes', methods=['DELETE'])
def unlike_post():
    data = request.json
    like = Like.query.filter_by(user_id=data['user_id'], post_id=data['post_id']).first_or_404()
    db.session.delete(like)
    db.session.commit()
    return jsonify({"message": "Post unliked"})

# Get like count for a post
@like_bp.route('/likes/post/<int:post_id>', methods=['GET'])
def get_like_count(post_id):
    count = Like.query.filter_by(post_id=post_id).count()
    return jsonify({"post_id": post_id, "likes_count": count})
