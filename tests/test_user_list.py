from objects.user import User
from objects.users import Users


def test_user_list():
    user = User(id="1854", first_name="C", last_name="Ext_Pmt_01", gender="male", dob="1935-07-18",
                email="zetta23@example.net", phone="(561) 326-6099 x6922",
                website="http://kuhn.net/cumque-quisquam-illum-necessitatibus-ut-laborum-placeat",
                address="694 Cronin Shore\nDionfurt, IL 55781-1993", status="inactive")

    users = Users()

    users.get_users()
    assert users.check_user(user, users.users_list) is True
