from src.domain.dao.shortcode import ShortcodeDaoInterface
from src.domain.dto.shortcode import ShortcodeDto


class ShortcodeDao(ShortcodeDaoInterface):

    def create(self, shortcode: ShortcodeDto) -> ShortcodeDto:
        print(shortcode.code)
        return shortcode

    def retrieve(self, code: str) -> ShortcodeDto:
        pass
