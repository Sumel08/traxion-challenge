import unittest

from src.converter.shortcode import ShortcodeConverter
from test.mock.dto.shortcode import shortcode_dto_mock
from test.mock.entities.shortcode import shortcode_entity_mock


class ShortcodeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.converter = ShortcodeConverter()
        self.shortcode_entity_mock = shortcode_entity_mock()
        self.shortcode_dto_mock = shortcode_dto_mock()

    def test_convert_entity_to_dto(self):
        shortcode_dto = self.converter.from_entity(self.shortcode_entity_mock)
        self.assertEqual(shortcode_dto.__class__.__name__, 'ShortcodeDto')
        self.assertEqual(shortcode_dto.code, self.shortcode_entity_mock.code)
        self.assertEqual(shortcode_dto.url, self.shortcode_entity_mock.url)
        self.assertEqual(shortcode_dto.title, self.shortcode_entity_mock.title)

    def test_convert_dto_to_entity(self):
        shortcode_entity = self.converter.from_dto(self.shortcode_dto_mock)
        self.assertEqual(shortcode_entity.__class__.__name__, 'ShortcodeEntity')
        self.assertEqual(shortcode_entity.code, self.shortcode_dto_mock.code)
        self.assertEqual(shortcode_entity.url, self.shortcode_dto_mock.url)
        self.assertEqual(shortcode_entity.title, self.shortcode_dto_mock.title)

    def test_convert_list_entity_to_dto(self):
        shortcode_dto_list = self.converter.from_entity_list([self.shortcode_entity_mock, self.shortcode_entity_mock])
        self.assertEqual(len(shortcode_dto_list), 2)
        for dto in shortcode_dto_list:
            self.assertEqual(dto.__class__.__name__, 'ShortcodeDto')

    def test_convert_list_dto_to_entity(self):
        shortcode_entity_list = self.converter.from_dto_list([self.shortcode_dto_mock, self.shortcode_dto_mock])
        self.assertEqual(len(shortcode_entity_list), 2)
        for dto in shortcode_entity_list:
            self.assertEqual(dto.__class__.__name__, 'ShortcodeEntity')
