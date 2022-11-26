from hanlders import cart


def data():
  return {
    "action": 5,
    "filter": {
      "id": 1,
      "count": 5
    }
  }


def test_put_product_to_cart(data=data()):
  true_data = {'code': 201, 'message': ' Товар Яблоки. Голден. в количестве 5 штук добавлен в корзину успешно'}

  assert cart.put_product_to_cart(data) == true_data
  