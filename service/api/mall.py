import requests
from requests import Response


class Mall:
    def login(self,username,password,code) -> Response: #类型提示
        r = requests.post(
            url='https://litemall.hogwarts.ceshiren.com/admin/auth/login',
            headers={'Origin': 'https://litemall.hogwarts.ceshiren.com'},
            json={
                'username': username,
                'password': password,
                'code': code
            }
        )
        return r

    def list_user(self):
        pass

    def list_orders(self):
        pass

    def logout(self):
        pass
