import json
from time import sleep

import consts
from hanlders import categories, products, set_hello_message, unknown_message, cart


def main(data):

    match data.get('action'):
        case consts.HELLO: # DEF
            return set_hello_message()
        case consts.LIST_PRODUCTS: # OK -> ⚗️
            return products.get_product_list(data)
        case consts.SINGLE_PRODUCT: # OK
            return products.get_single_product(data)
        case consts.LIST_CATEGORIES: # OK
            return categories.get_category_list(data)
        case consts.PUT_TO_THE_CART: # OK -> ⚗️
            return cart.put_product_to_cart(data)
        case consts.SHOW_CART: # OK -> ⚗️
            return cart.get_cart(data)
        case consts.EXIT: # DEF
            return 0
    
    return unknown_message()


if __name__ == '__main__':
    while True:
        with open('data_sample/command.json') as command_file:
            file_data = command_file.read()
        try:
            result = main(json.loads(file_data))
            print(result)

            #f = open('data_sample/command.json', 'r+')
            #f.truncate(0)
            break

            if result == 0:
                break

        except:
            print('Ожидаю команды... ')
            sleep(2)
