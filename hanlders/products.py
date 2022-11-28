import json


def get_product_list(data: dict):
    with open('test_data/catalog.json' if data.get('is_test') else 'data/catalog.json', 'r', encoding='utf-8') as file:
        file_product = json.loads(file.read())

    try:

        if data.get('is_neg_test'): raise Exception

        results_data = []

        if not data.get('filter'):
            for item in file_product:
                results_data.append('\n'.join([f"{i['id']}. {i['name']} ({i['price']} руб/{i['unit']})" for i in item['products']]))
            return { "code": 200, "data": results_data }

        for item in file_product:
            for d_item in item['products']:
                if eval(f"{d_item['price']}{data.get('filter')['price']}") and item['id'] == data.get('filter')['category']:
                    results_data.append(f"{d_item['id']}. {d_item['name']} ({d_item['price']} руб/{d_item['unit']})")
            
        return { "code": 200, "data": '\n'.join(results_data) }

    except Exception:
        return { "code": 400, "data": "Some error" }
    


def get_single_product(data: dict):
    with open('test_data/catalog.json' if data.get('is_test') else 'data/catalog.json', 'r', encoding='utf-8') as file:
        file_catalog = json.loads(file.read())

    try:
        for item in file_catalog:
            id = data.get('filter')['id']
            data_products = []

            if item.get('id') == id:
                for products in item.get('products'):
                    format_str = f"{products.get('name')}\nЦена: {products.get('price')} рублей за кг\nОстаток на складе: {products.get('balance')} штук\nОписание: {products.get('description')}"
                    data_products.append(format_str)
                        
                return { "code": 200, "message": data_products }

        raise Exception

    except:
        return { "code": 404, "message": "Товара с таким номер не найдено" }
