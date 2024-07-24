import requests

from constans import Constants
from base_api.test_base_api import BaseApi

constants = Constants()


class CreateOrderApi(BaseApi):
    URL_TEST = f'{constants.BASE_API_URL}api/v1/orders'

    def create_order_and_return_status_code(self, color: str):
        data = {
            "firstName": 'Naruto',
            "lastName": 'Uchiha',
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": '+7 800 355 35 35',
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [color]
        }

        response = requests.post(url=self.URL_TEST, json=data)
        return response.status_code

    def create_order_and_return_body(self, color: str):
        data = {
            "firstName": 'Naruto',
            "lastName": 'Uchiha',
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": '+7 800 355 35 35',
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [color]
        }

        response = requests.post(url=self.URL_TEST, json=data)
        return response.json()

    def get_list_order(self):
        response = requests.get(url=self.URL_TEST)
        return response.json()
