from abc import abstractmethod

from src.domain.dto.shortcode import ShortcodeDto
from src.util.singleton_meta import SingletonMeta


class ShortcodeDaoInterface(metaclass=SingletonMeta):
    """
    Define the structure desired in order to get access to the database
    """

    @abstractmethod
    def create(self, shortcode: ShortcodeDto) -> ShortcodeDto:
        """
        Creates a new record in database
        :param shortcode:
        :return:
        """
        pass

    @abstractmethod
    def retrieve(self, code: str) -> ShortcodeDto:
        """
        Retrieves a record stored in database
        :param code:
        :return:
        """
        pass
