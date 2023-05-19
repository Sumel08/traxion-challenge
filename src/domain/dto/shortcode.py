class ShortcodeDto:
    """
    Describes the structure of the object that the application will manage
    """

    def __init__(self, code, url, title):
        self.code = code
        self.url = url
        self.title = title
