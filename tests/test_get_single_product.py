from hanlders import products


data_1 = {
  "action": 4,
  "filter": {
    "id": 2
  }
}

data_2 = {
  "action": 4,
  "filter": {
    "id": 10
  }
}

def test_get_single_product_pos(data=data_1):

  assert products.get_single_product(data) == {
    'code': 200, 
    'message': ['Яблоки. Голден.\nЦена: 1000 рублей за кг\nОстаток на складе: 10 штук\nОписание: Зеленые яблоки, отлично подходят для приготовления пирога']
  }


def test_get_single_product_neg(data=data_2):

  assert products.get_single_product(data) == {
    'code': 404, 
    'message': 'Товара с таким номер не найдено'
  }

