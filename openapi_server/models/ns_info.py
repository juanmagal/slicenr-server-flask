# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class NsInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ns_instance_id=None, ns_name=None):  # noqa: E501
        """NsInfo - a model defined in OpenAPI

        :param ns_instance_id: The ns_instance_id of this NsInfo.  # noqa: E501
        :type ns_instance_id: str
        :param ns_name: The ns_name of this NsInfo.  # noqa: E501
        :type ns_name: str
        """
        self.openapi_types = {
            'ns_instance_id': str,
            'ns_name': str
        }

        self.attribute_map = {
            'ns_instance_id': 'nsInstanceId',
            'ns_name': 'nsName'
        }

        self._ns_instance_id = ns_instance_id
        self._ns_name = ns_name

    @classmethod
    def from_dict(cls, dikt) -> 'NsInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NsInfo of this NsInfo.  # noqa: E501
        :rtype: NsInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ns_instance_id(self):
        """Gets the ns_instance_id of this NsInfo.


        :return: The ns_instance_id of this NsInfo.
        :rtype: str
        """
        return self._ns_instance_id

    @ns_instance_id.setter
    def ns_instance_id(self, ns_instance_id):
        """Sets the ns_instance_id of this NsInfo.


        :param ns_instance_id: The ns_instance_id of this NsInfo.
        :type ns_instance_id: str
        """

        self._ns_instance_id = ns_instance_id

    @property
    def ns_name(self):
        """Gets the ns_name of this NsInfo.


        :return: The ns_name of this NsInfo.
        :rtype: str
        """
        return self._ns_name

    @ns_name.setter
    def ns_name(self, ns_name):
        """Sets the ns_name of this NsInfo.


        :param ns_name: The ns_name of this NsInfo.
        :type ns_name: str
        """

        self._ns_name = ns_name
