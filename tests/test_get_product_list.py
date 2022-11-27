from hanlders import products


def data():
  return {
    "action": 2,
    "filter": { "price": ">= 100", "category": 1 }
  }


def data_2():
  return {
  "action": 2,
  "filter": { "price": "< 100", "category": 1 }
}


def data_3():
  return {
  "action": 2,
  "filter": {}
}


def data_4():
  return {
    "action": 2,
    "filter": {},
    'is_test': True
  }


def test_get_product_list():
  true_data = {'code': 200, 'data': '1. Яблоки. Голден. (1000 руб/кг)\n3. Черешня. Хелл. (100 руб/кг)'}
  true_data_2 = {'code': 200, 'data': '2. Груша. Сильвер. (50 руб/кг)'}
  true_data_3 = {'code': 200, 'data': ['1. Яблоки. Голден. (1000 руб/кг)\n2. Груша. Сильвер. (50 руб/кг)\n3. Черешня. Хелл. (100 руб/кг)', '1. Яблоки. Голден. (1000 руб/кг)', '1. Яблоки. Голден. (1000 руб/кг)', '1. Яблоки. Голден. (1000 руб/кг)']}

  assert products.get_product_list(data()) == true_data
  assert products.get_product_list(data_2()) == true_data_2
  assert products.get_product_list(data_3()) == true_data_3


def test_get_product_list_neg():
  true_data = { "code": 400, "data": "Some error" }

  assert products.get_product_list(data_4()) == true_data