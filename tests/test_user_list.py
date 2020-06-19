from objects.user import User
from objects.users import Users


def test_user_list():
    user = User(id="1840", first_name="Pasquale", last_name="Lind", gender="female", dob="1933-10-22",
                email="kavon67@example.com", phone="984.723.4385 x80657",
                website="http://pfannerstill.info/esse-vel-cum-id-et-quis-inventore",
                address="8292 Bruen Extensions\nNew Chloehaven, SD 15313", status="active")

    users = Users()

    print(users.get_users())
    assert users.check_user(user, users.users_list) is True
