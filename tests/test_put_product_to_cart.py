from hanlders.cart import put_product_to_cart

data_1 = {
    "action": 5,
    "filter": {
        "id": 1,
        "count": 5
    }
}


def test_put_product_to_cart():
    assert put_product_to_cart(data_1) == {
        "code": 201,
        "message": " Товар Яблоки. Голден. в количестве 5 штук добавлен в корзину успешно"
    }


data_2 = {
    "action": 5,
    "filter": {
        "id": 555,
        "count": 5
    }
}


def test_put_product_to_cart_2():
    assert put_product_to_cart(data_2) == {
        "code": 404,
        "message": 'Товара с таким номер не найдено'
    }


data_3 = {
    "action": 5,
    "filter": {
        "id": 1,
        "count": 11
    }
}



def test_put_product_to_cart_3():
    assert put_product_to_cart(data_3) == {
        "code": 409,
        "message": 'Невозможно добавить товар Яблоки. Голден. в количестве 11 штук в корзину, потому что их осталось всего 10.'
    }


