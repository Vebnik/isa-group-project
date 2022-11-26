import json
import pprint as pp


def put_product_to_cart(data):
    with open('data_sample/catalog.json', encoding='utf-8') as catalog_file:
        file_catalog = json.loads(catalog_file.read())
    try:
        for i in file_catalog:
            id = data.get('filter')['id']
            count = data.get('filter')['count']
            if i.get('id') == id:
                for products in i.get('products'):
                    if products['id'] == id and products['balance'] >= count:
                        basket = { 'name': products['name'], 'price': products['price'], 'count': count }

                        with open('data_sample/cart.json', 'r', encoding='utf-8') as cart_file:

                            cart_data = json.load(cart_file)
                            cart_data.append(basket)

                            with open('data_sample/cart.json', 'w', encoding='utf-8') as cart_file_pass:
                                cart_file_pass.write(json.dumps(cart_data, indent=2))

                        return {
                            "code": 201,
                            "message": f" Товар {products['name']} в количестве {count} штук добавлен в корзину успешно"
                        }
                    if products['balance'] < count:
                        return {
                            "code": 409,
                            "message": f"Невозможно добавить товар {products['name']} в количестве {count} штук в корзину, потому что их осталось всего {products['balance']}."
                        }
            raise Exception
    except Exception as ex:
        return {
            "code": 404,
            "message": "Товара с таким номер не найдено"
        }


def get_cart(data):
    with open('data_sample/cart.json', 'r', encoding='utf-8') as file_cart:
        data_cart = json.loads(file_cart.read())
        message = []

        for index in range(len(data_cart)):
            message.append(f'{index+1}. {data_cart[index]["name"]} ({data_cart[index]["price"]} руб.кг) добавлено {data_cart[index]["count"]} штука')
        return {
                "code": 200,
                "message": "\n".join(message)
            }




