# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.file_download_job_single_all_of_attributes import FileDownloadJobSingleAllOfAttributes
from openapi_server import util

from openapi_server.models.file_download_job_single_all_of_attributes import FileDownloadJobSingleAllOfAttributes  # noqa: E501

class FileDownloadJobSingleAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attributes=None):  # noqa: E501
        """FileDownloadJobSingleAllOf - a model defined in OpenAPI

        :param attributes: The attributes of this FileDownloadJobSingleAllOf.  # noqa: E501
        :type attributes: FileDownloadJobSingleAllOfAttributes
        """
        self.openapi_types = {
            'attributes': FileDownloadJobSingleAllOfAttributes
        }

        self.attribute_map = {
            'attributes': 'attributes'
        }

        self._attributes = attributes

    @classmethod
    def from_dict(cls, dikt) -> 'FileDownloadJobSingleAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FileDownloadJob_Single_allOf of this FileDownloadJobSingleAllOf.  # noqa: E501
        :rtype: FileDownloadJobSingleAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attributes(self):
        """Gets the attributes of this FileDownloadJobSingleAllOf.


        :return: The attributes of this FileDownloadJobSingleAllOf.
        :rtype: FileDownloadJobSingleAllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this FileDownloadJobSingleAllOf.


        :param attributes: The attributes of this FileDownloadJobSingleAllOf.
        :type attributes: FileDownloadJobSingleAllOfAttributes
        """

        self._attributes = attributes
