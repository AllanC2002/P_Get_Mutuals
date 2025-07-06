# app/queries/get_mutual_followers.py
from db.mysql_connection import get_userprofile_session
from models.profile_model import Profile, Followers

def get_mutual_followers(user_id):
    session = get_userprofile_session()

    followers = session.query(Followers.Id_Follower).filter_by(Id_Following=user_id, Status=1).all()
    follower_ids = {f.Id_Follower for f in followers}

    followings = session.query(Followers.Id_Following).filter_by(Id_Follower=user_id, Status=1).all()
    following_ids = {f.Id_Following for f in followings}

    mutual_ids = list(follower_ids & following_ids)

    mutual_users = session.query(Profile).filter(Profile.Id_User.in_(mutual_ids), Profile.Status_account == 1).all()

    result = [{"Id_User": user.Id_User, "User_mail": user.User_mail} for user in mutual_users]

    session.close()
    return result
