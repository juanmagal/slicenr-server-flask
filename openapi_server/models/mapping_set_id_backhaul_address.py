# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.backhaul_address import BackhaulAddress
from openapi_server import util

from openapi_server.models.backhaul_address import BackhaulAddress  # noqa: E501

class MappingSetIDBackhaulAddress(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, set_id=None, backhaul_address=None):  # noqa: E501
        """MappingSetIDBackhaulAddress - a model defined in OpenAPI

        :param set_id: The set_id of this MappingSetIDBackhaulAddress.  # noqa: E501
        :type set_id: int
        :param backhaul_address: The backhaul_address of this MappingSetIDBackhaulAddress.  # noqa: E501
        :type backhaul_address: BackhaulAddress
        """
        self.openapi_types = {
            'set_id': int,
            'backhaul_address': BackhaulAddress
        }

        self.attribute_map = {
            'set_id': 'setID',
            'backhaul_address': 'backhaulAddress'
        }

        self._set_id = set_id
        self._backhaul_address = backhaul_address

    @classmethod
    def from_dict(cls, dikt) -> 'MappingSetIDBackhaulAddress':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MappingSetIDBackhaulAddress of this MappingSetIDBackhaulAddress.  # noqa: E501
        :rtype: MappingSetIDBackhaulAddress
        """
        return util.deserialize_model(dikt, cls)

    @property
    def set_id(self):
        """Gets the set_id of this MappingSetIDBackhaulAddress.


        :return: The set_id of this MappingSetIDBackhaulAddress.
        :rtype: int
        """
        return self._set_id

    @set_id.setter
    def set_id(self, set_id):
        """Sets the set_id of this MappingSetIDBackhaulAddress.


        :param set_id: The set_id of this MappingSetIDBackhaulAddress.
        :type set_id: int
        """

        self._set_id = set_id

    @property
    def backhaul_address(self):
        """Gets the backhaul_address of this MappingSetIDBackhaulAddress.


        :return: The backhaul_address of this MappingSetIDBackhaulAddress.
        :rtype: BackhaulAddress
        """
        return self._backhaul_address

    @backhaul_address.setter
    def backhaul_address(self, backhaul_address):
        """Sets the backhaul_address of this MappingSetIDBackhaulAddress.


        :param backhaul_address: The backhaul_address of this MappingSetIDBackhaulAddress.
        :type backhaul_address: BackhaulAddress
        """

        self._backhaul_address = backhaul_address
