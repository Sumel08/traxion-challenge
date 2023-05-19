class ShortcodeEntity:
    """
    Model that describes the structure of our database entity
    """

    def __init__(self, code, url, title):
        self.code = code
        self.url = url
        self.title = title
