import secrets
import string


class Utilities:

    @staticmethod
    def create_unique_code(length: int) -> str:
        """
        Function that creates a random unique code of length given
        :param length: number of characters of the random code
        :return: A unique code of length given
        """
        return ''.join(secrets.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase)
                       for i in range(length))
