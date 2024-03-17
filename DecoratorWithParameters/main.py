from time import sleep


def sleeper(seconds):
    """
    Decorator for decorator, which "sleeps" for `seconds` seconds

    :param seconds: int, number of seconds to sleep
    :return: function
    """
    def decorator(func):
        """
        Decorator for function. Add sleep time before the function is called

        :param func: function which have been passed as argument
        :return: function wrapped with sleep timme
        """
        def wrapper(*args, **kwargs):
            sleep(seconds)
            func(*args, **kwargs)

        return wrapper

    return decorator


@sleeper(5)
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
