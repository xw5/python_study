import json

def dict_to_json():
    dict1 = {}
    dict1['name'] = 'tom'
    dict1['age'] = 20
    dict1['sex'] = 'male'
    print('dict_to_json')
    print(dict1)
    jsons = json.dumps(dict1)
    print(jsons)
    print(type(jsons))

def json_to_dict():
    jsons = '{"name": "tony", "age": 28, "sex": "male", "phone": "123456", "email": "loadkernel@126.com"}'
    dict1 = json.loads(jsons)
    print('json_to_dict')
    print(dict1)
    print(type(dict1))

def dict_to_json_write_file():
    dict = {}
    dict['name'] = 'tom'
    dict['age'] = 10
    dict['sex'] = 'male'
    print('dict_to_json_write_file')
    print(dict)
    with open('test.json', 'w') as f:
        json.dump(dict, f)

def json_file_to_dict():
    with open('test.json', 'r') as f:
        dict1 = json.load(f)
        print('json_file_to_dict')
        print(dict1)
        print(type(dict1))

if __name__ == '__main__':
    dict_to_json()
    json_to_dict()
    dict_to_json_write_file()
    json_file_to_dict()