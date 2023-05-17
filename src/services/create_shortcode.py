
from src.dao.shortcode import ShortcodeDao
from src.domain.dto.shortcode import ShortcodeDto
from src.domain.service.handler_service import ServiceHandler, ServiceResponse
from src.util.utilities import create_unique_code


class CreateShortcodeService(ServiceHandler):

    def __init__(self):
        self.shortcodeDao = ShortcodeDao()

    def handle_request(self, *args, **kwargs) -> ServiceResponse:

        shortcode = ShortcodeDto(create_unique_code(4), kwargs.get('url'), kwargs.get('title'))
        shortcode = self.shortcodeDao.create(shortcode)
        response_data = {"url": shortcode.code}
        return ServiceResponse(response_data, '', 200)


