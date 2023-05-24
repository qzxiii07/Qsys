# app/auth/wechat.py

from flask import request, jsonify, session
from app.models import User

@auth_bp.route('/wechat')
def wechat_auth():
    code = request.args.get('code')
    if not code:
        return 'Missing code'
    
    # Use code to get openId and session_key
    result = get_wechat_auth_result(code)
    open_id = result.get('openid')
    
    user = User.query.filter_by(open_id=open_id).first()
    if not user:
        # Create a new user
        user = User(open_id=open_id)
        db.session.add(user)
        db.session.commit()
        
    # Save user ID to session
    session['user_id'] = user.id
    return jsonify(message='Login succeeded!') 