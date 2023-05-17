
from src.dao.shortcode import ShortcodeDao
from src.domain.dto.shortcode import ShortcodeDto
from src.domain.service.handler_service import ServiceHandler, ServiceResponse
from src.util.utilities import create_unique_code


class ResolveShortcodeService(ServiceHandler):

    def __init__(self):
        self.shortcodeDao = ShortcodeDao()

    def handle_request(self, *args, **kwargs) -> ServiceResponse:

        shortcode = self.shortcodeDao.retrieve(kwargs.get('code'))
        if not shortcode:
            return ServiceResponse(None, 'Code Not Found', 404)
        response_data = {"url": shortcode.url}
        return ServiceResponse(response_data, '', 302)
