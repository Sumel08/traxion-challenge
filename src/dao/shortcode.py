import os
from typing import Optional

from src.converter.shortcode import ShortcodeConverter
from src.domain.dao.shortcode import ShortcodeDaoInterface
from src.domain.dto.shortcode import ShortcodeDto
import boto3

from src.domain.entities.shortcode import ShortcodeEntity


class ShortcodeDao(ShortcodeDaoInterface):
    """
    Implementation of the dao definition for Shortcode Model
    """
    TABLE_NAME = os.environ.get('SHORTENER_TABLE_NAME', None)

    def __init__(self):
        self.shortcode_converter = ShortcodeConverter()
        self.dynamo_client = boto3.client('dynamodb')

    def create(self, shortcode: ShortcodeDto) -> ShortcodeDto:
        entity = self.shortcode_converter.from_dto(shortcode)
        self.dynamo_client.put_item(
            TableName=self.TABLE_NAME,
            Item={"code": {'S': entity.code}, "url": {'S': entity.url}, "title": {'S': entity.title}},
        )
        return self.shortcode_converter.from_entity(entity)

    def retrieve(self, code: str) -> Optional[ShortcodeDto]:
        resp = self.dynamo_client.get_item(
            TableName=self.TABLE_NAME,
            Key={
                'code': {'S': code}
            }
        )
        if resp.get('Item', None) is None:
            return None
        item = resp.get('Item')
        shortcode_entity = ShortcodeEntity(item.get('code').get('S'), item.get('url').get('S'),
                                           item.get('title').get('S'))
        return self.shortcode_converter.from_entity(shortcode_entity)
