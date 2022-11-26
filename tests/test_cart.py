from hanlders.cart import put_product_to_cart

def data ():
    return {
    {
        "action": 5,
        "filter": {
            "id": 1,
            "count": 5
        }
    }
}


def test_put_product_to_cart( d = data):
    assert put_product_to_cart(d) == {
        "code": 201,
        "message": "Товар 'Яблоки' в количестве 5 штук добавлен в корзину успешно"
    }


def data () :
    return {
    {
        "action": 5,
        "filter": {
            "id": 555,
            "count": 5
        }
    }
}


def test_put_product_to_cart_2(d = data):
    assert put_product_to_cart(d) == {
        "code": 404,
        "message": "Товара с таким номер не найдено."
    }


def data():
    return {
    {
        "action": 5,
        "filter": {
            "id": 1,
            "count": 11
        }
    }
}


def test_put_product_to_cart_3( d = data):
    assert put_product_to_cart(d) == {
        "code": 409,
        "message": "Невозможно добавить товар 'Яблоки' в количестве 11 штук в корзину, потому что их осталось всего 10."
    }


