from flask import Blueprint, session

session_bp = Blueprint('session', __name__)


@session_bp.route('/views')
def views():
    views = session.get("views", None)
    if views is not None:
        session['views'] = views + 1
    else:
        session['views'] = 1
    return {'views': session['views']}

'''
Sessions
Because sessions are stored client-side, restarting the server won’t clear the session cookie.

However, if the client clears their cookies, the information from the session will disappear.
Sessions summary
Sessions are a useful way to store user-specific information with a secure cookie in the client’s 
browser. It will persist until the client clears their cookies.

The library we will use for auth with Flask applications uses sessions—we won’t 
have to interact with the session object directly
'''