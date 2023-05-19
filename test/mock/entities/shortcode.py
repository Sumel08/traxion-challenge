from src.domain.entities.shortcode import ShortcodeEntity


def shortcode_entity_mock() -> ShortcodeEntity:
    return ShortcodeEntity('shortcode_mock', 'https://oscar.lemus.app', 'Personal Webpage')
