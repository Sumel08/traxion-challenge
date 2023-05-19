from unittest import TestCase, mock

from src.dao.shortcode import ShortcodeDao
from src.services.resolve_shortcode import ResolveShortcodeService
from test.mock.dto.shortcode import shortcode_dto_mock


def mock_shortcode_dao_retrieve(self, code: str):
    if code == shortcode_dto_mock().code:
        return shortcode_dto_mock()
    return None


@mock.patch.object(ShortcodeDao, 'retrieve', new=mock_shortcode_dao_retrieve)
class TestResolveShortcode(TestCase):
    def setUp(self) -> None:
        self.service = ResolveShortcodeService()

    def test_handle_successful_request(self):
        response = self.service.handle_request(code=shortcode_dto_mock().code)
        self.assertEqual(response.code, 302)
        self.assertEqual(response.data.get('url'), shortcode_dto_mock().url)

    def test_handle_bad_request(self):
        response = self.service.handle_request()
        self.assertEqual(response.code, 400)
        self.assertEqual(response.data.get('code'), 'required')

    def test_handle_code_not_found_request(self):
        response = self.service.handle_request(code='fake_code')
        self.assertEqual(response.code, 404)
        self.assertEqual(response.message, 'Code Not Found')
