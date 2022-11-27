from hanlders.categories import get_category_list


def data():
  return {
  "action": 3,
  "filter": {}
}

def test_get_category_list(data = data()):
  test_data = {'code': 200, 'data': '1. Фрукты 1\n2. Фрукты 2\n3. Фрукты 3\n4. Фрукты 4'}

  assert get_category_list(data) == test_data