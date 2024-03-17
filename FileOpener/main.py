class FileOpener:
    """
    This class is a simple decorator.

    This class allows users to open and close file.

    Attributes:
        - filename (string): filename of the file to be opened.
        - mode (string): mode of action with file.

    Methods:
        - __init__ - initialize the Decorator.
        - __enter__ - open file and return it.
        - __exit__ - close file.
    """
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


with FileOpener('file.txt', 'r') as f:
    f.read()
