import json


def get_category_list(data):
    with open('test_data/catalog.json' if data.get('is_test') else 'data/catalog.json', 'r', encoding='utf-8') as file:
        file_catalog = json.loads(file.read())

    try:
        if data.get('is_neg_test'): raise Exception
        
        data = []
        
        for i in range(len(file_catalog)):
            data.append(f'{i+1}. {file_catalog[i].get("name")}')

        return { "code": 200, "data": '\n'.join(data) }

    except:
        return { "code": 400, "data": "Some error" }
