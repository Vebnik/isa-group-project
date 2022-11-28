from hanlders.categories import get_category_list


def data():
  return {
  "action": 3,
  "filter": {},
  "is_test": True
}

def data_2():
  return {
  "action": 3,
  "filter": {},
  "is_neg_test": True
}


def test_get_category_list():
  test_data = {'code': 200, 'data': '1. Фрукты 1\n2. Фрукты 2\n3. Фрукты 3\n4. Фрукты 4'}

  assert get_category_list(data()) == test_data


def test_get_category_list_neg():
  test_data = {"code": 400, "data": "Some error" }

  assert get_category_list(data_2()) == test_data