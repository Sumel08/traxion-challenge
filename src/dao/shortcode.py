import os
from typing import Optional

from src.domain.dao.shortcode import ShortcodeDaoInterface
from src.domain.dto.shortcode import ShortcodeDto
import boto3


class ShortcodeDao(ShortcodeDaoInterface):
    TABLE_NAME = os.environ['SHORTENER_TABLE_NAME']

    def __init__(self):
        self.dynamoClient = boto3.client('dynamodb')

    def create(self, shortcode: ShortcodeDto) -> ShortcodeDto:
        self.dynamoClient.put_item(
            TableName=self.TABLE_NAME,
            Item={"code": {'S': shortcode.code}, "url": {'S': shortcode.url}, "title": {'S': shortcode.title}}
        )
        return shortcode

    def retrieve(self, code: str) -> Optional[ShortcodeDto]:
        resp = self.dynamoClient.get_item(
            TableName=self.TABLE_NAME,
            Key={
                'code': {'S': code}
            }
        )
        if not resp.get('Item'):
            return None
        item = resp.get('Item')
        return ShortcodeDto(item.get('code').get('S'), item.get('url').get('S'), item.get('title').get('S'))
