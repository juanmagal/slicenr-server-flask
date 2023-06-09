# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.epn3_single import EPN3Single
from openapi_server.models.epn4_single import EPN4Single
from openapi_server.models.epn6_single import EPN6Single
from openapi_server.models.epn9_single import EPN9Single
from openapi_server.models.eps5_u_single import EPS5USingle
from openapi_server import util

from openapi_server.models.epn3_single import EPN3Single  # noqa: E501
from openapi_server.models.epn4_single import EPN4Single  # noqa: E501
from openapi_server.models.epn6_single import EPN6Single  # noqa: E501
from openapi_server.models.epn9_single import EPN9Single  # noqa: E501
from openapi_server.models.eps5_u_single import EPS5USingle  # noqa: E501

class UpfFunctionSingleAllOf1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ep_n3=None, ep_n4=None, ep_n6=None, ep_n9=None, ep_s5_u=None):  # noqa: E501
        """UpfFunctionSingleAllOf1 - a model defined in OpenAPI

        :param ep_n3: The ep_n3 of this UpfFunctionSingleAllOf1.  # noqa: E501
        :type ep_n3: List[EPN3Single]
        :param ep_n4: The ep_n4 of this UpfFunctionSingleAllOf1.  # noqa: E501
        :type ep_n4: List[EPN4Single]
        :param ep_n6: The ep_n6 of this UpfFunctionSingleAllOf1.  # noqa: E501
        :type ep_n6: List[EPN6Single]
        :param ep_n9: The ep_n9 of this UpfFunctionSingleAllOf1.  # noqa: E501
        :type ep_n9: List[EPN9Single]
        :param ep_s5_u: The ep_s5_u of this UpfFunctionSingleAllOf1.  # noqa: E501
        :type ep_s5_u: List[EPS5USingle]
        """
        self.openapi_types = {
            'ep_n3': List[EPN3Single],
            'ep_n4': List[EPN4Single],
            'ep_n6': List[EPN6Single],
            'ep_n9': List[EPN9Single],
            'ep_s5_u': List[EPS5USingle]
        }

        self.attribute_map = {
            'ep_n3': 'EP_N3',
            'ep_n4': 'EP_N4',
            'ep_n6': 'EP_N6',
            'ep_n9': 'EP_N9',
            'ep_s5_u': 'EP_S5U'
        }

        self._ep_n3 = ep_n3
        self._ep_n4 = ep_n4
        self._ep_n6 = ep_n6
        self._ep_n9 = ep_n9
        self._ep_s5_u = ep_s5_u

    @classmethod
    def from_dict(cls, dikt) -> 'UpfFunctionSingleAllOf1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UpfFunction_Single_allOf_1 of this UpfFunctionSingleAllOf1.  # noqa: E501
        :rtype: UpfFunctionSingleAllOf1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ep_n3(self):
        """Gets the ep_n3 of this UpfFunctionSingleAllOf1.


        :return: The ep_n3 of this UpfFunctionSingleAllOf1.
        :rtype: List[EPN3Single]
        """
        return self._ep_n3

    @ep_n3.setter
    def ep_n3(self, ep_n3):
        """Sets the ep_n3 of this UpfFunctionSingleAllOf1.


        :param ep_n3: The ep_n3 of this UpfFunctionSingleAllOf1.
        :type ep_n3: List[EPN3Single]
        """

        self._ep_n3 = ep_n3

    @property
    def ep_n4(self):
        """Gets the ep_n4 of this UpfFunctionSingleAllOf1.


        :return: The ep_n4 of this UpfFunctionSingleAllOf1.
        :rtype: List[EPN4Single]
        """
        return self._ep_n4

    @ep_n4.setter
    def ep_n4(self, ep_n4):
        """Sets the ep_n4 of this UpfFunctionSingleAllOf1.


        :param ep_n4: The ep_n4 of this UpfFunctionSingleAllOf1.
        :type ep_n4: List[EPN4Single]
        """

        self._ep_n4 = ep_n4

    @property
    def ep_n6(self):
        """Gets the ep_n6 of this UpfFunctionSingleAllOf1.


        :return: The ep_n6 of this UpfFunctionSingleAllOf1.
        :rtype: List[EPN6Single]
        """
        return self._ep_n6

    @ep_n6.setter
    def ep_n6(self, ep_n6):
        """Sets the ep_n6 of this UpfFunctionSingleAllOf1.


        :param ep_n6: The ep_n6 of this UpfFunctionSingleAllOf1.
        :type ep_n6: List[EPN6Single]
        """

        self._ep_n6 = ep_n6

    @property
    def ep_n9(self):
        """Gets the ep_n9 of this UpfFunctionSingleAllOf1.


        :return: The ep_n9 of this UpfFunctionSingleAllOf1.
        :rtype: List[EPN9Single]
        """
        return self._ep_n9

    @ep_n9.setter
    def ep_n9(self, ep_n9):
        """Sets the ep_n9 of this UpfFunctionSingleAllOf1.


        :param ep_n9: The ep_n9 of this UpfFunctionSingleAllOf1.
        :type ep_n9: List[EPN9Single]
        """

        self._ep_n9 = ep_n9

    @property
    def ep_s5_u(self):
        """Gets the ep_s5_u of this UpfFunctionSingleAllOf1.


        :return: The ep_s5_u of this UpfFunctionSingleAllOf1.
        :rtype: List[EPS5USingle]
        """
        return self._ep_s5_u

    @ep_s5_u.setter
    def ep_s5_u(self, ep_s5_u):
        """Sets the ep_s5_u of this UpfFunctionSingleAllOf1.


        :param ep_s5_u: The ep_s5_u of this UpfFunctionSingleAllOf1.
        :type ep_s5_u: List[EPS5USingle]
        """

        self._ep_s5_u = ep_s5_u
