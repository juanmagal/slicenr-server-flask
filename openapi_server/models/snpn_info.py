# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.snpn_id import SnpnId
from openapi_server.models.snssai import Snssai
from openapi_server import util

from openapi_server.models.snpn_id import SnpnId  # noqa: E501
from openapi_server.models.snssai import Snssai  # noqa: E501

class SnpnInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, snpn_id=None, snssai=None):  # noqa: E501
        """SnpnInfo - a model defined in OpenAPI

        :param snpn_id: The snpn_id of this SnpnInfo.  # noqa: E501
        :type snpn_id: SnpnId
        :param snssai: The snssai of this SnpnInfo.  # noqa: E501
        :type snssai: Snssai
        """
        self.openapi_types = {
            'snpn_id': SnpnId,
            'snssai': Snssai
        }

        self.attribute_map = {
            'snpn_id': 'snpnId',
            'snssai': 'snssai'
        }

        self._snpn_id = snpn_id
        self._snssai = snssai

    @classmethod
    def from_dict(cls, dikt) -> 'SnpnInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SnpnInfo of this SnpnInfo.  # noqa: E501
        :rtype: SnpnInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def snpn_id(self):
        """Gets the snpn_id of this SnpnInfo.


        :return: The snpn_id of this SnpnInfo.
        :rtype: SnpnId
        """
        return self._snpn_id

    @snpn_id.setter
    def snpn_id(self, snpn_id):
        """Sets the snpn_id of this SnpnInfo.


        :param snpn_id: The snpn_id of this SnpnInfo.
        :type snpn_id: SnpnId
        """

        self._snpn_id = snpn_id

    @property
    def snssai(self):
        """Gets the snssai of this SnpnInfo.


        :return: The snssai of this SnpnInfo.
        :rtype: Snssai
        """
        return self._snssai

    @snssai.setter
    def snssai(self, snssai):
        """Sets the snssai of this SnpnInfo.


        :param snssai: The snssai of this SnpnInfo.
        :type snssai: Snssai
        """

        self._snssai = snssai