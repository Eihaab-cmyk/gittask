from flask import Blueprint, request, jsonify
from models import db, Comment, CommentSchema, Post, User

comment_bp = Blueprint('comment_bp', __name__)
comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)

# add comment
@comment_bp.route('/comments', methods=['POST'])
def add_comment():
    data = request.json
    new_comment = Comment(content=data['content'], user_id=data['user_id'], post_id=data['post_id'])
    db.session.add(new_comment)
    db.session.commit()
    return comment_schema.jsonify(new_comment)

# edit comment
@comment_bp.route('/comments/<int:id>', methods=['PUT'])
def edit_comment(id):
    comment = Comment.query.get_or_404(id)
    data = request.json
    comment.content = data.get('content', comment.content)
    db.session.commit()
    return comment_schema.jsonify(comment)

# delete comment
@comment_bp.route('/comments/<int:id>', methods=['DELETE'])
def delete_comment(id):
    comment = Comment.query.get_or_404(id)
    db.session.delete(comment)
    db.session.commit()
    return jsonify({"message": "Comment deleted successfully"})

# get comments for a post
@comment_bp.route('/comments/post/<int:post_id>', methods=['GET'])
def get_comments_by_post(post_id):
    comments = Comment.query.filter_by(post_id=post_id).all()
    return comments_schema.jsonify(comments)