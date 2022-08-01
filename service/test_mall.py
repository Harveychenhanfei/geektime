import requests

class TestMall:
    def setup_class(self):
        print('suite 数据初始化')
    def setup(self):
        print('case数据初始化')

    def test_login(self):
        r = requests.post(
            url='https://litemall.hogwarts.ceshiren.com/admin/auth/login',
            headers={'Origin': 'https://litemall.hogwarts.ceshiren.com'},
            json={
                'username': 'admin123',
                'password': 'admin123',
                'code': ''
            }
        )
        assert r.status_code == 200
        print(r.text)
        assert r.json()['errmsg'] == '成功'

    def test_login_wrong(self):
        r = requests.post(
            url='https://litemall.hogwarts.ceshiren.com/admin/auth/login',
            headers={'Origin': 'https://litemall.hogwarts.ceshiren.com'},
            json={
                'username': 'admin123',
                'password': 'wrong',
                'code': ''
            }
        )
        assert r.status_code == 200
        print(r.text)
        assert r.json()['errmsg'] == '用户帐号或密码不正确'

    def teardown(self):
        print('case teardown')

    def teardown_class(self):
        print('数据清理 teardown_class')
