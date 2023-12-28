import requests
from config import Config

def create_object(class_name, data, headers):
    url = Config.B4A_API_URL + class_name
    response = requests.post(url, json=data, headers=headers)
    return response.json()

def read_objects(class_name, query, headers):
    url = Config.B4A_API_URL + class_name
    response = requests.get(url, params=query, headers=headers)
    return response.json()

def update_object(class_name, object_id, data, headers):
    url = Config.B4A_API_URL + class_name + "/" + object_id
    response = requests.put(url, json=data, headers=headers)
    return response.json()

def delete_object(class_name, object_id, headers):
    url = Config.B4A_API_URL + class_name + "/" + object_id
    response = requests.delete(url, headers=headers)
    return response.json()
