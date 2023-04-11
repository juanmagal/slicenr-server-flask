# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.plmn_id import PlmnId
from openapi_server.models.snssai import Snssai
from openapi_server import util

from openapi_server.models.plmn_id import PlmnId  # noqa: E501
from openapi_server.models.snssai import Snssai  # noqa: E501

class PlmnInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, plmn_id=None, snssai=None):  # noqa: E501
        """PlmnInfo - a model defined in OpenAPI

        :param plmn_id: The plmn_id of this PlmnInfo.  # noqa: E501
        :type plmn_id: PlmnId
        :param snssai: The snssai of this PlmnInfo.  # noqa: E501
        :type snssai: Snssai
        """
        self.openapi_types = {
            'plmn_id': PlmnId,
            'snssai': Snssai
        }

        self.attribute_map = {
            'plmn_id': 'plmnId',
            'snssai': 'snssai'
        }

        self._plmn_id = plmn_id
        self._snssai = snssai

    @classmethod
    def from_dict(cls, dikt) -> 'PlmnInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PlmnInfo of this PlmnInfo.  # noqa: E501
        :rtype: PlmnInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def plmn_id(self):
        """Gets the plmn_id of this PlmnInfo.


        :return: The plmn_id of this PlmnInfo.
        :rtype: PlmnId
        """
        return self._plmn_id

    @plmn_id.setter
    def plmn_id(self, plmn_id):
        """Sets the plmn_id of this PlmnInfo.


        :param plmn_id: The plmn_id of this PlmnInfo.
        :type plmn_id: PlmnId
        """

        self._plmn_id = plmn_id

    @property
    def snssai(self):
        """Gets the snssai of this PlmnInfo.


        :return: The snssai of this PlmnInfo.
        :rtype: Snssai
        """
        return self._snssai

    @snssai.setter
    def snssai(self, snssai):
        """Sets the snssai of this PlmnInfo.


        :param snssai: The snssai of this PlmnInfo.
        :type snssai: Snssai
        """

        self._snssai = snssai