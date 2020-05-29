import requests


class ApiMaster(object):

    @staticmethod
    def make_request(method, url, query_params=None, body=None):
        """
                Builds a Http request.

                :param method: GET/POST/PUT/DELETE
                :param url: Request Url
                :param query_params: Query parameters
                :param body: Body object for POST/PUT operations
                :return: response Object
                """
        try:
            response = requests.request(method, url, params=query_params, json=body)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            print("OOps: Something Else", err)
        except requests.exceptions.HTTPError as errh:
            print("Http Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)

        return response
