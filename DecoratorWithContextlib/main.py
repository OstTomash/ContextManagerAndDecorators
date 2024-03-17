from contextlib import contextmanager


@contextmanager
def file_opener(filename: str, mode: str):
    """
    Simple decorator with using contextlib context manager

    Open a file, yield it and close the file.

    Open a file and
    :param filename: string name of the file to open
    :param mode: string name of the mode of reading
    :yield: file object
    """
    file = None

    try:
        file = open(filename, mode)

        yield file
    except Exception as exception:
        print(exception)
    finally:
        file.close()


with file_opener('file.txt', 'r') as f:
    print(f.read())
