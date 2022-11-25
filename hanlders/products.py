import json


def get_product_list(data: dict):
    # {
    #     "action": 2,
    #     "filter": {
    #         "price": ['>100'|'<100'|'<=100'|'>=100'|None],
    #         "category": <int|None>
    #     }
    # }

    # {
    #     "code": 200,
    #     "data": "1. Груша (200 руб/кг) 10 шт.\n2. Яблоки (1000 руб/кг) 10шт."
    # }

    with open('data_sample/catalog.json', 'r', encoding='utf-8') as file:
        file_product = json.loads(file.read())

    try:
        results_data = []

        if not data.get('filter'):
            for item in file_product:
                results_data.append('\n'.join([f"{i['id']}. {i['name']} ({i['price']} руб/{i['unit']})" for i in item['products']]))
            return { "code": 200, "data": results_data }


        for item in file_product:
            for d_item in item['products']:
                if eval(f"{d_item['price']}{data.get('filter')['price']}"):
                    results_data.append(f"{d_item['id']}. {d_item['name']} ({d_item['price']} руб/{d_item['unit']})")
            
        return { "code": 200, "data": '\n'.join(results_data) }

    except Exception as ex:
        print(ex.with_traceback())
        return { "code": 400, "data": " " }
    


def get_single_product(data: dict):
    with open('data_sample/catalog.json', 'r', encoding='utf-8') as file:
        file_catalog = json.loads(file.read())

    try:
        for item in file_catalog:
            id = data.get('filter')['id']
            if item.get('id') == id:
                for products in item.get('products'):
                    if products['id'] == id:
                        return {
                            "code": 200,
                            "message": f"{products.get('name')}.Цена: {products.get('price')} рублей за кг Остаток на складе: {products.get('balance')} штук Описание: {products.get('description')}"}
            raise Exception
    except:
        return {
            "code": 404,
            "message": "Товара с таким номер не найдено"
        }
