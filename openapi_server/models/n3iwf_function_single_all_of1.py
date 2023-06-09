# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.epn3_single import EPN3Single
from openapi_server.models.epn4_single import EPN4Single
from openapi_server import util

from openapi_server.models.epn3_single import EPN3Single  # noqa: E501
from openapi_server.models.epn4_single import EPN4Single  # noqa: E501

class N3iwfFunctionSingleAllOf1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ep_n3=None, ep_n4=None):  # noqa: E501
        """N3iwfFunctionSingleAllOf1 - a model defined in OpenAPI

        :param ep_n3: The ep_n3 of this N3iwfFunctionSingleAllOf1.  # noqa: E501
        :type ep_n3: List[EPN3Single]
        :param ep_n4: The ep_n4 of this N3iwfFunctionSingleAllOf1.  # noqa: E501
        :type ep_n4: List[EPN4Single]
        """
        self.openapi_types = {
            'ep_n3': List[EPN3Single],
            'ep_n4': List[EPN4Single]
        }

        self.attribute_map = {
            'ep_n3': 'EP_N3',
            'ep_n4': 'EP_N4'
        }

        self._ep_n3 = ep_n3
        self._ep_n4 = ep_n4

    @classmethod
    def from_dict(cls, dikt) -> 'N3iwfFunctionSingleAllOf1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The N3iwfFunction_Single_allOf_1 of this N3iwfFunctionSingleAllOf1.  # noqa: E501
        :rtype: N3iwfFunctionSingleAllOf1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ep_n3(self):
        """Gets the ep_n3 of this N3iwfFunctionSingleAllOf1.


        :return: The ep_n3 of this N3iwfFunctionSingleAllOf1.
        :rtype: List[EPN3Single]
        """
        return self._ep_n3

    @ep_n3.setter
    def ep_n3(self, ep_n3):
        """Sets the ep_n3 of this N3iwfFunctionSingleAllOf1.


        :param ep_n3: The ep_n3 of this N3iwfFunctionSingleAllOf1.
        :type ep_n3: List[EPN3Single]
        """

        self._ep_n3 = ep_n3

    @property
    def ep_n4(self):
        """Gets the ep_n4 of this N3iwfFunctionSingleAllOf1.


        :return: The ep_n4 of this N3iwfFunctionSingleAllOf1.
        :rtype: List[EPN4Single]
        """
        return self._ep_n4

    @ep_n4.setter
    def ep_n4(self, ep_n4):
        """Sets the ep_n4 of this N3iwfFunctionSingleAllOf1.


        :param ep_n4: The ep_n4 of this N3iwfFunctionSingleAllOf1.
        :type ep_n4: List[EPN4Single]
        """

        self._ep_n4 = ep_n4
