from hanlders import help



def data():
  return {
    "action": 1,
    "filter": {}
  }


def test_help(data=data()):
  true_data = {
    "code": 200,
    "data": "1 - Вывести это сообщение.\n2 - Показать список продуктов. Можно передать в тело номер категории, чтобы получить товары определенной категории. ..."
  }

  assert help(data) == true_data
