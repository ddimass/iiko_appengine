import requests


class Iiko:
    """This class describe IIKO api"""

    user = 'demoDelivery'
    password = 'PI1yFaKFCGvvJKi'
    org = '';
    token = ''
    products = []

    def __init__(self):
        pass

    def __repr__(self):
        return Iiko.products

    @staticmethod
    def auth():
        if Iiko.token:
            payload = {'access_token': Iiko.token, 'request_timeout': '00:02:00'}
            res = requests.get('https://iiko.biz:9900/api/0/organization/list', params=payload).json()
            if 'httpStatusCode' in res:
                payload = {'user_id': Iiko.user, 'user_secret': Iiko.password}
                Iiko.token = requests.get('https://iiko.biz:9900/api/0/auth/access_token', params=payload).json()
        else:
            payload = {'user_id': Iiko.user, 'user_secret': Iiko.password}
            Iiko.token = requests.get('https://iiko.biz:9900/api/0/auth/access_token', params=payload).json()

    @staticmethod
    def getId():
        payload = {'access_token': Iiko.token, 'request_timeout': '00:02:00'}
        Iiko.org = requests.get('https://iiko.biz:9900/api/0/organization/list', params=payload).json()[0]

    @staticmethod
    def logout():
        Iiko.auth()
        payload = {'access_token': Iiko.token, 'request_timeout': '00:02:00'}
        return requests.get('https://iiko.biz:9900/api/0/organization/list', params=payload)

    @staticmethod
    def get_menu():
        """Getting full menu from Iiko api"""
        Iiko.auth()
        Iiko.getId()
        payload = {'access_token': Iiko.token, 'organizationId': Iiko.org['id']}
        Iiko.products = requests.get('https://iiko.biz:9900/api/0/nomenclature/' + Iiko.org['id'], params=payload).json()
        return Iiko.products








