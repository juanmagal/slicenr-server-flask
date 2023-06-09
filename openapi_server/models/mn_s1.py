# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.mn_s_one_of import MnSOneOf
from openapi_server.models.sub_network_single import SubNetworkSingle
from openapi_server import util

from openapi_server.models.mn_s_one_of import MnSOneOf  # noqa: E501
from openapi_server.models.sub_network_single import SubNetworkSingle  # noqa: E501

class MnS1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, sub_network=None):  # noqa: E501
        """MnS1 - a model defined in OpenAPI

        :param sub_network: The sub_network of this MnS1.  # noqa: E501
        :type sub_network: List[SubNetworkSingle]
        """
        self.openapi_types = {
            'sub_network': List[SubNetworkSingle]
        }

        self.attribute_map = {
            'sub_network': 'SubNetwork'
        }

        self._sub_network = sub_network

    @classmethod
    def from_dict(cls, dikt) -> 'MnS1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MnS_1 of this MnS1.  # noqa: E501
        :rtype: MnS1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sub_network(self):
        """Gets the sub_network of this MnS1.


        :return: The sub_network of this MnS1.
        :rtype: List[SubNetworkSingle]
        """
        return self._sub_network

    @sub_network.setter
    def sub_network(self, sub_network):
        """Sets the sub_network of this MnS1.


        :param sub_network: The sub_network of this MnS1.
        :type sub_network: List[SubNetworkSingle]
        """

        self._sub_network = sub_network
