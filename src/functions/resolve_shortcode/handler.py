import json

from src.services.resolve_shortcode import ResolveShortcodeService


def resolve_shortcode(event, context):
    """
    Just resolve the event and calls the service class, this is a kind of middleware in order to be able to migrate
    from serverless lambda and keep all the functionality not coupled with the framework
    :param event:
    :param context:
    :return:
    """
    params = event.get('pathParameters')
    service = ResolveShortcodeService()

    response = service.handle_request(**params)

    if response.code != 302:
        return {
            "statusCode": response.code,
            "body": json.dumps({"data": response.data, "message": response.message})
        }

    return {
        "statusCode": response.code,
        "body": json.dumps({"data": response.data, "message": response.message}),
        "headers": {
            "Location": response.data.get('url'),
        },
    }
