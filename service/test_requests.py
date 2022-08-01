import requests
from jsonpath import jsonpath
#https://httpbin.ceshiren.com


proxies = {
    'http':'http://127.0.0.1:8080',
    'https':'https://127.0.0.1'
}
def test_get():
    params = {'a':1,'b':2}
    r = requests.get('https://httpbin.ceshiren.com/get',params=params)
    assert r.status_code == 200
    # print(r)
    # print(type(r.text)) #text为str
    # print(type(r.json())) #json为dict格式
def test_post():
    params = {'a': 1, 'b': 2}
    #r = requests.post(url='https://httpbin.ceshiren.com/post',data=params)
    r = requests.post(url='https://httpbin.ceshiren.com/post',json=params)
    assert r.status_code == 200
    print(r.json())


def test_login():
    r = requests.post(
        url='https://litemall.hogwarts.ceshiren.com/admin/auth/login',
        headers = {'Origin':'https://litemall.hogwarts.ceshiren.com'},
        json= {
            'username':'admin123',
            'password':'admin123',
            'code':''
        }
    )
    assert r.status_code == 200
    print(r.text)
    assert r.json()['errmsg'] == '成功'


#善用cookie,解决验证码的问题
def test_user_list():

    r = requests.get(
        url='https://litemall.hogwarts.ceshiren.com/admin/user/list?page=1&limit=20&sort=add_time&order=desc',
        cookies = {'X-Litemall-Admin-Token':'48a111e0-86b4-4a58-b9b2-854a49081125'},
        headers = {'X-Litemall-Admin-Token':'48a111e0-86b4-4a58-b9b2-854a49081125'}
    )
    assert r.status_code == 200


#对于复杂数据结构的断言,用jsonpath
def test_category():
    r = requests.get(
        url = 'https://ceshiren.com/categories.json'
    )
    assert r.status_code == 200
    print(r.text)
    #assert r.json()['category_list']['categories'][0]['name'] == '提问区' #这种断言不稳定,而且语句太长
    assert '提问区' in jsonpath(r.json(),'$..name')