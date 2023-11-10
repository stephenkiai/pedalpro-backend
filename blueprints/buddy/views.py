from flask import Blueprint
from flask import jsonify
from models import db, Users, Friendship

buddy_bp = Blueprint('buddy', __name__)


@buddy_bp.route('/send_friend_request/<string:friend_id>', methods=['POST'])
def send_friend_request(friend_id):
     # to implement
     pass
    

@buddy_bp.route('/accept_friend_request/<string:friend_id>', methods=['POST'])
def accept_friend_request(friend_id):
     # to implement
    pass

@buddy_bp.route('/get_user_buddies/<string:user_id>', methods=['GET'])
def get_user_buddies(user_id):
    user = Users.query.get(user_id)
    if user is None:
        return None

    buddies = [friendship.friend for friendship in user.buddies]
    return buddies
