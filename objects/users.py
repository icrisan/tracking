from objects.api import ApiMaster
from objects.enum import Method
from objects.user import User
from objects.parsers import is_found


class Users(object):
    users_list = []

    # private attribute
    __user_list = []
    # private attribute
    __response = None

    def __init__(self):
        pass

    def get_users(self):
        json = self.__get_response().json()

        for obj in json['result']:
            self.users_list.append(obj)

        return self.users_list

    # private method
    def __get_response(self):
        __response = ApiMaster.make_request(method=Method.GET.value, url="https://gorest.co.in/public-api/users",
                                            query_params="access-token=i_ENmVlv_jLFlzNJW-Po8EykdEDwEUgrKTLH",
                                            body=None)

        return __response

    # private method
    def __get_user_objects_list(self):
        for obj in self.users_list:
            self.__user_list.append(
                User(obj['id'], obj['first_name'], obj['last_name'], obj['gender'], obj['dob'], obj['email'],
                     obj['phone'], obj['website'], obj['address'], obj['status']))

        return self.__user_list

    def check_user(self, user, users_list):
        return is_found(user, users_list)
