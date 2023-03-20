import requests
import random

TOKEN = '09db7b369137f2e55f6c60182945f1a12f5dc5b42f8818bed25034d8242d5f58'

baseurl = 'https://gorest.co.in'

headers = {
    'Authorization': 'Bearer ' + TOKEN,
    'Content-Type': 'application/json'
}


def test_get():
    user_id = 53
    response = requests.get(url=f'{baseurl}/public/v2/users/{user_id}')
    response_json = response.json()
    assert response.status_code == 200
    for key in ['name', 'email', 'gender', 'id', 'status']:
        assert key in response_json


def test_patch():
    # создание строки с рандомным числом для избежания конфликта создания не уникального пользователя
    random_number = str(random.randint(0, 100000))
    # создание пользователя
    user_data = {"name": f"Mazur Daniil {random_number}", "gender": "male",
                 "email": f"test-user-{random_number}@15ce.com", "status": "active"}
    response = requests.post(url=f'{baseurl}/public/v2/users/',
                             headers=headers,
                             json=user_data)
    assert response.status_code == 201

    user_id = response.json()['id']
    # частичное редактирование пользователя
    response = requests.patch(url=f'{baseurl}/public/v2/users/{user_id}',
                              headers=headers,
                              json={'name': f'Mazur Updated {random_number}'})
    assert response.status_code == 200


def test_read_user_by_id():
    user_id = 232567
    response = requests.get(url=f'{baseurl}/public/v2/users/{user_id}')
    response_json = response.json()
    assert response.status_code == 200
    for key in ['name', 'email', 'gender', 'id', 'status']:
        assert key in response_json


# #проверить, что у каждого пользователя есть ключи
# def test_read_all_users():
#     response = requests.get(url=f'{baseurl}/public/v2/users')
#     response_json = response.json()
#     assert response.status_code == 200
#     for key in ['email', 'gender', 'id', 'name', 'status']:
#         assert key in response_json
#         for key in res

def test_create_user():
    random_number = str(random.randint(0, 100000))
    user_data = {"name": f"Tkachuk Anastasiya {random_number}", "gender": "male",
                 "email": f"tkachuk.anastasiyakja{random_number}@15ce.com", "status": "active"}
    response = requests.post(url=f'{baseurl}/public/v2/users/',
                             headers=headers,
                             json=user_data)
    response_json = response.json()
    assert response.status_code == 201
    for key in ['name', 'email', 'gender', 'id', 'status']:
        assert key in response_json


def test_update_user():
    random_number = str(random.randint(0, 100000))
    user_data = {"name": f"Tkachuk Anastasiya {random_number}", "gender": "male",
                 "email": f"tkachuk.anastasiyakja{random_number}@15ce.com", "status": "active"}
    response = requests.post(url=f'{baseurl}/public/v2/users/',
                             headers=headers,
                             json=user_data)
    response_json = response.json()
    assert response.status_code == 201
    user_id = response.json()['id']
    response = requests.patch(url=f'{baseurl}/public/v2/users/{user_id}',
                              headers=headers,
                              json={'name': f'Tkachuk Nastya {random_number}'})
    assert response.status_code == 200
    for key in ['name', 'email', 'gender', 'id', 'status']:
        assert key in response_json


def test_rewrite_user_put():
    random_number = str(random.randint(0, 100000))
    user_data = {"name": f"Tkachuk Anastasiya {random_number}", "gender": "female",
                 "email": f"tkachuk.anastasiyakja{random_number}@15ce.com", "status": "active"}
    response = requests.post(url=f'{baseurl}/public/v2/users/',
                             headers=headers,
                             json=user_data)
    response_json = response.json()
    assert response.status_code == 201
    user_id = response.json()['id']
    response = requests.put(url=f'{baseurl}/public/v2/users/{user_id}',
                            headers=headers,
                            json={'name': f'TkachukN {random_number}', "gender": "male",
                                  "email": f"tk.anastasiya{random_number}@15ce.com", "status": "active"})
    assert response.status_code == 200
    for key in ['name', 'email', 'gender', 'id', 'status']:
        assert key in response_json


def test_delete_user_put():
    random_number = str(random.randint(0, 100000))
    user_data = {"name": f"Tkachuk Anastasiya {random_number}", "gender": "female",
                 "email": f"tkachuk.anastasiyakja{random_number}@15ce.com", "status": "active"}
    response = requests.post(url=f'{baseurl}/public/v2/users/',
                             headers=headers,
                             json=user_data)
    response_json = response.json()

    user_id = response.json()['id']
    response = requests.delete(url=f'{baseurl}/public/v2/users/{user_id}',
                               headers=headers)
    assert response.status_code == 204
    for key in ['name', 'email', 'gender', 'id', 'status']:
        assert key in response_json


def test_full_flow():
    random_number = str(random.randint(0, 100000))
    user_data = {"name": f"Tkachuk Anastasiya {random_number}", "gender": "female",
                 "email": f"tkachuk.anastasiyakja{random_number}@15ce.com", "status": "active"}
    response = requests.post(url=f'{baseurl}/public/v2/users/',
                             headers=headers,
                             json=user_data)
    response_json = response.json()
    assert response.status_code == 201

    user_id = response.json()['id']
    response = requests.patch(url=f'{baseurl}/public/v2/users/{user_id}',
                              headers=headers,
                              json={'name': f'Tkachuk Nastya {random_number}'})
    assert response.status_code == 200
    for key in ['name', 'email', 'gender', 'id', 'status']:
        assert key in response_json

    response = requests.put(url=f'{baseurl}/public/v2/users/{user_id}',
                            headers=headers,
                            json={'name': f'TkachukN {random_number}', "gender": "male",
                                  "email": f"tk.anastasiya{random_number}@15ce.com", "status": "active"})
    assert response.status_code == 200
    for key in ['name', 'email', 'gender', 'id', 'status']:
        assert key in response_json

    response = requests.delete(url=f'{baseurl}/public/v2/users/{user_id}',
                               headers=headers)
    assert response.status_code == 204
    for key in ['name', 'email', 'gender', 'id', 'status']:
        assert key in response_json
