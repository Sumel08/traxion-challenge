from unittest import TestCase, mock
import os

from src.dao.shortcode import ShortcodeDao
from src.domain.dto.shortcode import ShortcodeDto
from src.services.create_shortcode import CreateShortcodeService
from src.util.utilities import Utilities
from test.mock.dto.shortcode import shortcode_dto_mock


def mock_shortcode_dao_crate(self, shortcode: ShortcodeDto):
    return shortcode


def mock_create_unique_code(length: int):
    return 'fake_code'


@mock.patch.dict(os.environ, SHORT_URL='http://localhost:3000/{}')
@mock.patch.object(ShortcodeDao, 'create', new=mock_shortcode_dao_crate)
@mock.patch.object(Utilities, 'create_unique_code', new=mock_create_unique_code)
class TestCreateShortcode(TestCase):
    def setUp(self) -> None:
        self.service = CreateShortcodeService()
        self.shortcode_dto = shortcode_dto_mock()

    def test_handle_successful_request(self):
        response = self.service.handle_request(url=self.shortcode_dto.url, title=self.shortcode_dto.title)
        self.assertEqual(response.code, 201)
        self.assertEqual(response.data.get('url'), 'http://localhost:3000/fake_code')

    def test_handle_bad_request(self):
        response = self.service.handle_request()
        self.assertEqual(response.code, 400)
        self.assertEqual(response.data.get('url'), 'required')
        self.assertEqual(response.data.get('title'), 'required')
