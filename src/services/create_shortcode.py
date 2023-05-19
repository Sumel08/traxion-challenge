import os

from src.dao.shortcode import ShortcodeDao
from src.domain.dto.shortcode import ShortcodeDto
from src.domain.service.handler_service import ServiceHandler, ServiceResponse
from src.util.utilities import Utilities


class CreateShortcodeService(ServiceHandler):

    def __init__(self):
        self.shortcodeDao = ShortcodeDao()

    def handle_request(self, *args, **kwargs) -> ServiceResponse:
        """
        Function that creates in dynamoDB a new record with the original url and return a code
        related wit it, in order to resolve in another method
        :param args:
        :param kwargs:
        :return:
        """
        if not kwargs.get('url') or not kwargs.get('title'):
            return ServiceResponse({'url': 'required', 'title': 'required'}, 'Bad request', 400)

        shortcode = ShortcodeDto(Utilities.create_unique_code(6), kwargs.get('url'), kwargs.get('title'))
        shortcode = self.shortcodeDao.create(shortcode)
        response_data = {"url": os.environ.get('SHORT_URL').format(shortcode.code)}
        return ServiceResponse(response_data, '', 201)
