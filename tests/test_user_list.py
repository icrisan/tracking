from api.user import User
from api.users import Users


def test_user_list():
    user = User(id="1805", first_name="Conor", last_name="Schuppe", gender="male", dob="1973-04-29",
                email="dickinson.claude@example.com", phone="1-672-893-5182 x11108",
                website="http://www.mann.com/ratione-saepe-cum-enim",
                address="580 Isabelle Branch\nPort Laurel, VA 12016", status="inactive")

    print(user.last_name)
    print('-----------')

    users = Users()

    print(Users.get_users(self=users))
    print('-----------')
    print(Users.get_response(self=users))
    print('-----------')
    print(Users.get_user_objects_list(self=users))
