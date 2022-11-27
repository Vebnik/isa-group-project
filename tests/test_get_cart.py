from hanlders import cart


def data():
  return {
    "action": 6
  }


def test_get_cart(data=data()):
  true_data = {'code': 200, 'message': '1. Яблоки. Голден. (1000 руб/кг) добавлено 5 штук\n2. Яблоки. Голден. (1000 руб/кг) добавлено 5 штук'}
  assert cart.get_cart(data) == true_data