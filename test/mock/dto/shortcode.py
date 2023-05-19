from src.domain.dto.shortcode import ShortcodeDto


def shortcode_dto_mock() -> ShortcodeDto:
    return ShortcodeDto('shortcode_mock', 'https://oscar.lemus.app', 'Personal Webpage')
