import json


def get_category_list(data):
    with open('data/catalog.json', 'r', encoding='utf-8') as file:
        file_catalog = json.loads(file.read())

    try:
        data = []
        
        for i in range(len(file_catalog)):
            data.append(f'{i+1}. {file_catalog[i].get("name")}')

        return { "code": 200, "data": '\n'.join(data) }

    except:
        return { "code": 400, "data": "Some error" }
