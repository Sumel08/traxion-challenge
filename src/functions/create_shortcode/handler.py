import json

from src.services.create_shortcode import CreateShortcodeService


def create_shortcode(event, context):
    body = json.loads(event.get('body'))

    service = CreateShortcodeService()

    response = service.handle_request(**body)

    return {
        "statusCode": response.code,
        "body": json.dumps({"data": response.data, "message": response.message})
    }
