# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.epn27_single import EPN27Single
from openapi_server import util

from openapi_server.models.epn27_single import EPN27Single  # noqa: E501

class NrfFunctionSingleAllOf1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ep_n27=None):  # noqa: E501
        """NrfFunctionSingleAllOf1 - a model defined in OpenAPI

        :param ep_n27: The ep_n27 of this NrfFunctionSingleAllOf1.  # noqa: E501
        :type ep_n27: List[EPN27Single]
        """
        self.openapi_types = {
            'ep_n27': List[EPN27Single]
        }

        self.attribute_map = {
            'ep_n27': 'EP_N27'
        }

        self._ep_n27 = ep_n27

    @classmethod
    def from_dict(cls, dikt) -> 'NrfFunctionSingleAllOf1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NrfFunction_Single_allOf_1 of this NrfFunctionSingleAllOf1.  # noqa: E501
        :rtype: NrfFunctionSingleAllOf1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ep_n27(self):
        """Gets the ep_n27 of this NrfFunctionSingleAllOf1.


        :return: The ep_n27 of this NrfFunctionSingleAllOf1.
        :rtype: List[EPN27Single]
        """
        return self._ep_n27

    @ep_n27.setter
    def ep_n27(self, ep_n27):
        """Sets the ep_n27 of this NrfFunctionSingleAllOf1.


        :param ep_n27: The ep_n27 of this NrfFunctionSingleAllOf1.
        :type ep_n27: List[EPN27Single]
        """

        self._ep_n27 = ep_n27
