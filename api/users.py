from api.api import ApiMaster
from api.enum import Method
from collections import UserList
from api.user import User


class Users(object):
    response = None
    users_list = UserList()
    user_list = UserList()

    def __init__(self):
        pass

    def get_users(self):
        json = self.get_response().json()

        for obj in json['result']:
            self.users_list.append(obj)

        return self.users_list

    def get_response(self):
        response = ApiMaster.make_request(method=Method.GET.value, url="https://gorest.co.in/public-api/users",
                                          query_params="access-token=i_ENmVlv_jLFlzNJW-Po8EykdEDwEUgrKTLH",
                                          body=None)

        return response

    def get_user_objects_list(self):
        for obj in self.users_list:
            self.user_list.append(
                User(obj['id'], obj['first_name'], obj['last_name'], obj['gender'], obj['dob'], obj['email'],
                     obj['phone'], obj['website'], obj['address'], obj['status']))

        return self.user_list
