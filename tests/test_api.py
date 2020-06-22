from objects.api import ApiMaster
from objects.enum import Method


def test_api():
    response = ApiMaster.make_request(method=Method.GET.value, url="https://gorest.co.in/public-api/users",
                                      query_params="access-token=i_ENmVlv_jLFlzNJW-Po8EykdEDwEUgrKTLH",
                                      body=None)

    json = response.json()

    found = False
    for obj in json['result']:
        if obj["id"] == "1854":
            found = True
            break

    assert found == True
