# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.s2t_post200_response import S2tPost200Response  # noqa: E501
from openapi_server.models.s2t_post_request import S2tPostRequest  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_s2t_post(self):
        """Test case for s2t_post

        Transcribe audio to text
        """
        s2t_post_request = {"config":{"encoding":"LINEAR16","sampleRateHertz":16000,"languageCode":"en-US"},"audio":{"content":"<Base64-encoded audio>"}}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/s2t',
            method='POST',
            headers=headers,
            data=json.dumps(s2t_post_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
