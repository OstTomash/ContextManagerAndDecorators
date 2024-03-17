def called_decorator(func):
    """
    A decorator for function

    It prints messages before and after the function is called
    """
    def wrapper(*args, **kwargs):
        print('Function is been called')

        result = func(*args, **kwargs)

        print('Function is been called')

        return result

    return wrapper


@called_decorator
def get_info_about_person(name: str, birth_year: int, current_year: int):
    """
    Simple function that prints information about person

    :param name: string that represent the person's name'
    :param birth_year: integer that represent the person's birth year'
    :param current_year: integer that represent the current year
    :return: string
    """
    age = current_year - birth_year

    return f'{name} is {age} years'


print(get_info_about_person('John', 1989, 2024))
