import json


def get_product_list(data):
    pass


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
