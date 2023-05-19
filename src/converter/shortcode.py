from src.domain.converter.converter import Converter
from src.domain.dto.shortcode import ShortcodeDto
from src.domain.entities.shortcode import ShortcodeEntity


class ShortcodeConverter(Converter):
    """
    Implementation that will help us to convert between ShortcodeDto and ShortcodeEntity
    """

    def from_dto(self, dto: ShortcodeDto):
        return ShortcodeEntity(dto.code, dto.url, dto.title)

    def from_entity(self, entity: ShortcodeEntity):
        return ShortcodeDto(entity.code, entity.url, entity.title)
