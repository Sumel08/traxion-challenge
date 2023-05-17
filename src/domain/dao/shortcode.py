from abc import abstractmethod

from src.domain.dto.shortcode import ShortcodeDto
from src.util.singleton_meta import SingletonMeta


class ShortcodeDaoInterface(metaclass=SingletonMeta):

    @abstractmethod
    def create(self, shortcode: ShortcodeDto) -> ShortcodeDto:
        pass

    @abstractmethod
    def retrieve(self, code: str) -> ShortcodeDto:
        pass
