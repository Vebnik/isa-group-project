from hanlders import set_hello_message


def data():
  return {
    "action": 0,
    "filter": {}
  }


def test_hello_message_func():
  true_data = {
    "code": 200,
    "data": "Привет, пользователь! Рады тебя приветствовать в магазине. Здесь ты можешь просмотреть товары, купить что-то. Для более подробной информации вызови помощь командой '1'" 
  } 

  assert set_hello_message(data()) == true_data
