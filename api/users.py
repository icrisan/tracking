from api.api import ApiMaster
from api.enum import Method
from collections import UserList


class Users(object):
    response = None
    users_list = UserList()

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
