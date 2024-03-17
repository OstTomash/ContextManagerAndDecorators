def check_types(*expected_types):
    """
    Decorator that checks the types of arguments passed to the decorated function.

    Parameters:
        expected_types: tuple - Tuple of expected data types for the arguments.

    Returns:
        wrapper: function - Wrapper around the decorated function.

    Raises:
        TypeError: If the type of an argument does not match the expected type.

    Example usage:
        @check_types(int, str)
        def example_function(a, b):
            return a, b
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg, expected_type in zip(args, expected_types):
                if not isinstance(arg, expected_type):
                    raise TypeError(
                        f"Argument {arg} is not of expected type {expected_type.__name__}"
                    )

            return func(*args, **kwargs)

        return wrapper

    return decorator


@check_types(int, str)
def example_function(a, b):
    """
    Simple function which returns the value of an argument

    :param a: int
    :param b: str
    :return: tuple - Tuple of expected data
    """
    return a, b


try:
    result = example_function(2, "hello", True)
    print(result)
except TypeError as e:
    print(e)
