from hanlders.cart import put_product_to_cart


def data_1():
    return {
        "action": 5,
        "filter": { "id": 1, "count": 5 }
    }


def data_2():
    return {
        "action": 5,
        "filter": { "id": 555, "count": 5 }
    }


def data_3():
    return {
        "action": 5,
        "filter": { "id": 1, "count": 11 }
    }


def test_put_product_to_cart():
    true_data = { "code": 201, "message": " Товар Яблоки. Голден. в количестве 5 штук добавлен в корзину успешно" }

    assert put_product_to_cart(data_1()) == true_data


def test_put_product_to_cart_2():
    tru_data = { "code": 404, "message": 'Товара с таким номер не найдено' }
    
    assert put_product_to_cart(data_2()) == tru_data


def test_put_product_to_cart_3():
    true_data = {
        "code": 409,
        "message": 'Невозможно добавить товар Яблоки. Голден. в количестве 11 штук в корзину, потому что их осталось всего 10.'
    }

    assert put_product_to_cart(data_3()) == true_data


