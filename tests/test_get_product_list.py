from hanlders import products


def data():
  return   {
    "action": 2,
    "filter": {
      "price": ">= 100",
      "category": 1
    }
  }


def test_get_product_list(data=data()):
  true_data = {'code': 200, 'data': '1. Яблоки. Голден. (1000 руб/кг)\n3. Черешня. Хелл. (100 руб/кг)'}

  assert products.get_product_list(data) == true_data