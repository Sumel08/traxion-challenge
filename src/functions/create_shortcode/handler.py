import json

from src.services.create_shortcode import CreateShortcodeService


def create_shortcode(event, context):
    """
    Just resolve the event and calls the service class, this is a kind of middleware in order to be able to migrate
    from serverless lambda and keep all the functionality not coupled with the framework
    :param event:
    :param context:
    :return:
    """
    body = json.loads(event.get('body'))

    service = CreateShortcodeService()

    response = service.handle_request(**body)

    return {
        "statusCode": response.code,
        "body": json.dumps({"data": response.data, "message": response.message})
    }
