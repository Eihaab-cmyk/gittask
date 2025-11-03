from flask import Blueprint, request, jsonify
from models import db, FriendRequest, User

friend_bp = Blueprint('friend_bp', __name__)

# send friend request
@friend_bp.route('/friends/request', methods=['POST'])
def send_friend_request():
    data = request.json
    fr = FriendRequest(from_user_id=data['from_user_id'], to_user_id=data['to_user_id'])
    db.session.add(fr)
    db.session.commit()
    return jsonify({"message": "Friend request sent"})

# accept friend request
@friend_bp.route('/friends/request/<int:id>/accept', methods=['PUT'])
def accept_friend_request(id):
    fr = FriendRequest.query.get_or_404(id)
    fr.status = 'accepted'
    db.session.commit()
    return jsonify({"message": "Friend request accepted"})

# show friends list
@friend_bp.route('/friends/<int:user_id>', methods=['GET'])
def get_friends(user_id):
    accepted1 = FriendRequest.query.filter_by(from_user_id=user_id, status='accepted').all()
    accepted2 = FriendRequest.query.filter_by(to_user_id=user_id, status='accepted').all()
    friends_ids = [fr.to_user_id for fr in accepted1] + [fr.from_user_id for fr in accepted2]
    friends = User.query.filter(User.id.in_(friends_ids)).all()
    return jsonify([{"id": f.id, "name": f.name, "email": f.email} for f in friends])

# unfriend
@friend_bp.route('/friends/unfriend', methods=['DELETE'])
def unfriend():
    data = request.json
    fr = FriendRequest.query.filter(
        (FriendRequest.from_user_id == data['user1_id']) & (FriendRequest.to_user_id == data['user2_id']) |
        (FriendRequest.from_user_id == data['user2_id']) & (FriendRequest.to_user_id == data['user1_id'])
    ).first_or_404()
    db.session.delete(fr)
    db.session.commit()
    return jsonify({"message": "Unfriended successfully"})