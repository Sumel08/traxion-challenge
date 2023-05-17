import json

from src.services.resolve_shortcode import ResolveShortcodeService


def resolve_shortcode(event, context):
    params = event.get('pathParameters')
    service = ResolveShortcodeService()

    response = service.handle_request(**params)

    return {
        "statusCode": response.code,
        "body": json.dumps({"data": response.data, "message": response.message}),
        "headers": {
            "Location": response.data.get('url'),
        },
    }
