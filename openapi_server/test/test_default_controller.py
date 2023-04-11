# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.error_response import ErrorResponse  # noqa: E501
from openapi_server.models.patch_item import PatchItem  # noqa: E501
from openapi_server.models.resource import Resource  # noqa: E501
from openapi_server.models.scope import Scope  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_class_nameid_delete(self):
        """Test case for class_nameid_delete

        Deletes one resource
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/3GPPManagement/ProvMnS/XXX/{class_nameid}'.format(class_name='class_name_example', id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_class_nameid_get(self):
        """Test case for class_nameid_get

        Reads one or multiple resources
        """
        query_string = [('scope', {'key': openapi_server.Scope()}),
                        ('filter', 'filter_example'),
                        ('attributes', ['attributes_example']),
                        ('fields', ['fields_example'])]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/3GPPManagement/ProvMnS/XXX/{class_nameid}'.format(class_name='class_name_example', id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_class_nameid_patch(self):
        """Test case for class_nameid_patch

        Patches one or multiple resources
        """
        resource = openapi_server.Resource()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/merge-patch+json',
        }
        response = self.client.open(
            '/3GPPManagement/ProvMnS/XXX/{class_nameid}'.format(class_name='class_name_example', id='id_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(resource),
            content_type='application/merge-patch+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_class_nameid_put(self):
        """Test case for class_nameid_put

        Replaces a complete single resource or creates it if it does not exist
        """
        resource = null
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/3GPPManagement/ProvMnS/XXX/{class_nameid}'.format(class_name='class_name_example', id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(resource),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
