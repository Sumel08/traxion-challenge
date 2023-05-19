import os
from typing import Dict, Union
from unittest import TestCase, mock

import boto3

from src.dao.shortcode import ShortcodeDao
from test.mock.dto.shortcode import shortcode_dto_mock
from test.mock.entities.shortcode import shortcode_entity_mock


class Boto3Mock:

    def __init__(self, client, **kwargs):
        pass

    # Your custom testing override
    def put_item(self, *args, **kwargs) -> dict[str, dict[str, Union[dict[str, str], str, int]]]:
        return {'ResponseMetadata': {'RequestId': '407OEC732L8TU76PD1EF7J83RNVV4KQNSO5AEMVJF66Q9ASUAAJG',
                                     'HTTPStatusCode': 200,
                                     'HTTPHeaders': {'server': 'Server', 'date': 'Fri, 19 May 2023 15:50:55 GMT',
                                                     'content-type': 'application/x-amz-json-1.0',
                                                     'content-length': '2', 'connection': 'keep-alive',
                                                     'x-amzn-requestid': '407OEC732L8TU76PD1EF7J83RNVV4KQNSO5AEMVJF66Q9ASUAAJG',
                                                     'x-amz-crc32': '2745614147'}, 'RetryAttempts': 0}}

    def get_item(self, *args, **kwargs):
        shortcode_entity = shortcode_entity_mock()
        code = kwargs.get('Key').get('code').get('S')
        if code == shortcode_entity.code:
            return {'Item': {'code': {'S': shortcode_entity.code}, 'url': {'S': shortcode_entity.url},
                             'title': {'S': shortcode_entity.title}},
                    'ResponseMetadata': {'RequestId': 'MJTT64SCCFT9S2P0UVGMHIF543VV4KQNSO5AEMVJF66Q9ASUAAJG',
                                         'HTTPStatusCode': 200,
                                         'HTTPHeaders': {'server': 'Server', 'date': 'Fri, 19 May 2023 16:10:41 GMT',
                                                         'content-type': 'application/x-amz-json-1.0',
                                                         'content-length': '117', 'connection': 'keep-alive',
                                                         'x-amzn-requestid': 'MJTT64SCCFT9S2P0UVGMHIF543VV4KQNSO5AEMVJF66Q9ASUAAJG',
                                                         'x-amz-crc32': '48579742'}, 'RetryAttempts': 0}}
        return {'ResponseMetadata': {'RequestId': 'GMTO954I5EMST1716H9QUDQ5L7VV4KQNSO5AEMVJF66Q9ASUAAJG',
                                     'HTTPStatusCode': 200,
                                     'HTTPHeaders': {'server': 'Server', 'date': 'Fri, 19 May 2023 16:10:23 GMT',
                                                     'content-type': 'application/x-amz-json-1.0',
                                                     'content-length': '2', 'connection': 'keep-alive',
                                                     'x-amzn-requestid': 'GMTO954I5EMST1716H9QUDQ5L7VV4KQNSO5AEMVJF66Q9ASUAAJG',
                                                     'x-amz-crc32': '2745614147'}, 'RetryAttempts': 0}}


class ShortcodeTest(TestCase):
    def setUp(self) -> None:
        with mock.patch.object(boto3, 'client', new=Boto3Mock):
            self.shortcode_dto_mock = shortcode_dto_mock()
            self.shortcode_entity_mock = shortcode_entity_mock()
            self.shortcode_dao = ShortcodeDao()

    def test_create_shortcode(self):
        shortcode_dao = ShortcodeDao()
        object_created = shortcode_dao.create(self.shortcode_dto_mock)
        self.assertEqual(object_created.__class__.__name__, 'ShortcodeDto')
        self.assertEqual(object_created.url, self.shortcode_dto_mock.url)

    def test_retrieve_shortcode(self):
        shortcode_dao = ShortcodeDao()
        object_retrieved = shortcode_dao.retrieve(self.shortcode_dto_mock.code)
        self.assertEqual(object_retrieved.__class__.__name__, 'ShortcodeDto')
        self.assertEqual(object_retrieved.code, self.shortcode_entity_mock.code)

    def test_retrieve_shortcode_failed(self):
        shortcode_dao = ShortcodeDao()
        object_retrieved = shortcode_dao.retrieve('fake_code')
        self.assertEqual(object_retrieved.__class__.__name__, 'NoneType')
