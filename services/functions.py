from models.models import Profile, Followers
from conections.mysql import conection_userprofile

def get_mutuals_f(user_id):
    session = conection_userprofile()

    followers = session.query(Followers.Id_Follower).filter_by(Id_Following=user_id, Status=1).all()
    follower_ids = {f.Id_Follower for f in followers}

    followings = session.query(Followers.Id_Following).filter_by(Id_Follower=user_id, Status=1).all()
    following_ids = {f.Id_Following for f in followings}

    mutual_ids = list(follower_ids & following_ids)

    mutual_users = session.query(Profile).filter(Profile.Id_User.in_(mutual_ids), Profile.Status_account == 1).all()

    result = []
    for user in mutual_users:
        result.append({
            "Id_User": user.Id_User,
            "User_mail": user.User_mail
            #"Name": user.Name,
            #"Lastname": user.Lastname,
            #"Email": user.User_mail,
            #"Description": user.Description
        })

    session.close()
    return result
