def function_info(func):
    """
    Decorator for printing information about function

    This decorator will print information about function before invoking it,
    with message which includes function name and parameters.
    And after invoke function will print message which include result.

    :param func: simple function, which can accept positioning and keyword arguments
    :return: function wrapper
    """
    def wrapper(*args, **kwargs):
        print(
            f'{func.__name__} is been called with parameters: {list(args) + list(kwargs.items())}.'
        )

        func(*args, **kwargs)

        print(f"Function {func.__name__} return value: {func(*args, **kwargs)}")

    return wrapper


@function_info
def get_info_about_person(name: str, age: int, country: str, city: str) -> str:
    """
    Simple function which returns information about person based on parameters

    :param name: str, name of person
    :param age: int, age of person
    :param country: str, country where person is located
    :param city: str, city where person is located
    :return: string with information about person
    """
    return f'{name} is {age} years, live in {country} at the {city} city'


get_info_about_person('Ostap', age=28, country='Ukraine', city='Lviv')
