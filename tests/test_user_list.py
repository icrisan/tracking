from api.user import User
from api.users import Users


def test_user_list():
    users = Users()

    print(users.get_users())
    print('-----------')

    print(users.get_user_objects_list())
    print('-----------')

    print(users.is_found(users.users_list, 'first_name', 'Ophelia'))
    print('-----------')

    assert users.is_found(users.users_list, 'first_name', 'Ophelia') == True
