from src.dao.shortcode import ShortcodeDao
from src.domain.service.handler_service import ServiceHandler, ServiceResponse


class ResolveShortcodeService(ServiceHandler):

    def __init__(self):
        self.shortcodeDao = ShortcodeDao()

    def handle_request(self, *args, **kwargs) -> ServiceResponse:
        """
        Function that resolve the given code and fetch from dynamo its relation
        with the original URL
        :param args:
        :param kwargs: Must pass the code
        :return: A ServiceResponse instance
        """
        if not kwargs.get('code'):
            return ServiceResponse({'code': 'required'}, 'Bad request', 400)

        shortcode = self.shortcodeDao.retrieve(kwargs.get('code'))
        if not shortcode:
            return ServiceResponse(None, 'Code Not Found', 404)
        response_data = {"url": shortcode.url}
        return ServiceResponse(response_data, '', 302)
