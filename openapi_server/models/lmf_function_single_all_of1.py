# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.epnls_single import EPNLSSingle
from openapi_server import util

from openapi_server.models.epnls_single import EPNLSSingle  # noqa: E501

class LmfFunctionSingleAllOf1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ep_nls=None):  # noqa: E501
        """LmfFunctionSingleAllOf1 - a model defined in OpenAPI

        :param ep_nls: The ep_nls of this LmfFunctionSingleAllOf1.  # noqa: E501
        :type ep_nls: List[EPNLSSingle]
        """
        self.openapi_types = {
            'ep_nls': List[EPNLSSingle]
        }

        self.attribute_map = {
            'ep_nls': 'EP_NLS'
        }

        self._ep_nls = ep_nls

    @classmethod
    def from_dict(cls, dikt) -> 'LmfFunctionSingleAllOf1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LmfFunction_Single_allOf_1 of this LmfFunctionSingleAllOf1.  # noqa: E501
        :rtype: LmfFunctionSingleAllOf1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ep_nls(self):
        """Gets the ep_nls of this LmfFunctionSingleAllOf1.


        :return: The ep_nls of this LmfFunctionSingleAllOf1.
        :rtype: List[EPNLSSingle]
        """
        return self._ep_nls

    @ep_nls.setter
    def ep_nls(self, ep_nls):
        """Sets the ep_nls of this LmfFunctionSingleAllOf1.


        :param ep_nls: The ep_nls of this LmfFunctionSingleAllOf1.
        :type ep_nls: List[EPNLSSingle]
        """

        self._ep_nls = ep_nls
