from hanlders import products


def data_1():
  return {
    "action": 4,
    "filter": { "id": 2 }
  }

def data_2(): 
  return {
    "action": 4,
    "filter": { "id": 10 }
  }


def test_get_single_product_pos():
  true_data = {
    'code': 200, 
    'message': ['Яблоки. Голден.\nЦена: 1000 рублей за кг\nОстаток на складе: 10 штук\nОписание: Зеленые яблоки, отлично подходят для приготовления пирога']
  }

  assert products.get_single_product(data_1()) == true_data


def test_get_single_product_neg():
  true_data = {
    'code': 404, 
    'message': 'Товара с таким номер не найдено'
  }

  assert products.get_single_product(data_2()) == true_data

