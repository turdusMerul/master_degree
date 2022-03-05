def validate_input(_function: function) -> function:
    def wrapped(_test_input, _err_msg):
        __result = _function(_test_input, _err_msg)

    return wrapped


@validate_input
def get_input(_test_input: str = None, _err_msg: str = None):
    
    pass




"""
    def print_is_num_in_range(_number: int, _range: list) -> None:
        '''Выводит в консоль сообщение с информацией о том,
        находится ли введённое пользователем число в диапозоне от -1 до 17'''
        print(f"{_number}{' ' if _number in _range else ' НЕ '}находится в диапозоне от -1 до 17")


    if __name__ == "__main__":
        # если данный модуль является основным, то будут вызваны тесты
        tests = {
            "ыякесмк": True
        }
        for test, answer in tests.items():
            print_is_num_in_range(get_input(test), range(-1, 17))
        
"""