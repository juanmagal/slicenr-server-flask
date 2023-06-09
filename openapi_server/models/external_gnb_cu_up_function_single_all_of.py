# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.epe1_single import EPE1Single
from openapi_server.models.epf1_u_single import EPF1USingle
from openapi_server.models.epxn_u_single import EPXnUSingle
from openapi_server import util

from openapi_server.models.epe1_single import EPE1Single  # noqa: E501
from openapi_server.models.epf1_u_single import EPF1USingle  # noqa: E501
from openapi_server.models.epxn_u_single import EPXnUSingle  # noqa: E501

class ExternalGnbCuUpFunctionSingleAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ep_e1=None, ep_f1_u=None, ep_xn_u=None):  # noqa: E501
        """ExternalGnbCuUpFunctionSingleAllOf - a model defined in OpenAPI

        :param ep_e1: The ep_e1 of this ExternalGnbCuUpFunctionSingleAllOf.  # noqa: E501
        :type ep_e1: List[EPE1Single]
        :param ep_f1_u: The ep_f1_u of this ExternalGnbCuUpFunctionSingleAllOf.  # noqa: E501
        :type ep_f1_u: List[EPF1USingle]
        :param ep_xn_u: The ep_xn_u of this ExternalGnbCuUpFunctionSingleAllOf.  # noqa: E501
        :type ep_xn_u: List[EPXnUSingle]
        """
        self.openapi_types = {
            'ep_e1': List[EPE1Single],
            'ep_f1_u': List[EPF1USingle],
            'ep_xn_u': List[EPXnUSingle]
        }

        self.attribute_map = {
            'ep_e1': 'EP_E1',
            'ep_f1_u': 'EP_F1U',
            'ep_xn_u': 'EP_XnU'
        }

        self._ep_e1 = ep_e1
        self._ep_f1_u = ep_f1_u
        self._ep_xn_u = ep_xn_u

    @classmethod
    def from_dict(cls, dikt) -> 'ExternalGnbCuUpFunctionSingleAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExternalGnbCuUpFunction_Single_allOf of this ExternalGnbCuUpFunctionSingleAllOf.  # noqa: E501
        :rtype: ExternalGnbCuUpFunctionSingleAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ep_e1(self):
        """Gets the ep_e1 of this ExternalGnbCuUpFunctionSingleAllOf.


        :return: The ep_e1 of this ExternalGnbCuUpFunctionSingleAllOf.
        :rtype: List[EPE1Single]
        """
        return self._ep_e1

    @ep_e1.setter
    def ep_e1(self, ep_e1):
        """Sets the ep_e1 of this ExternalGnbCuUpFunctionSingleAllOf.


        :param ep_e1: The ep_e1 of this ExternalGnbCuUpFunctionSingleAllOf.
        :type ep_e1: List[EPE1Single]
        """

        self._ep_e1 = ep_e1

    @property
    def ep_f1_u(self):
        """Gets the ep_f1_u of this ExternalGnbCuUpFunctionSingleAllOf.


        :return: The ep_f1_u of this ExternalGnbCuUpFunctionSingleAllOf.
        :rtype: List[EPF1USingle]
        """
        return self._ep_f1_u

    @ep_f1_u.setter
    def ep_f1_u(self, ep_f1_u):
        """Sets the ep_f1_u of this ExternalGnbCuUpFunctionSingleAllOf.


        :param ep_f1_u: The ep_f1_u of this ExternalGnbCuUpFunctionSingleAllOf.
        :type ep_f1_u: List[EPF1USingle]
        """

        self._ep_f1_u = ep_f1_u

    @property
    def ep_xn_u(self):
        """Gets the ep_xn_u of this ExternalGnbCuUpFunctionSingleAllOf.


        :return: The ep_xn_u of this ExternalGnbCuUpFunctionSingleAllOf.
        :rtype: List[EPXnUSingle]
        """
        return self._ep_xn_u

    @ep_xn_u.setter
    def ep_xn_u(self, ep_xn_u):
        """Sets the ep_xn_u of this ExternalGnbCuUpFunctionSingleAllOf.


        :param ep_xn_u: The ep_xn_u of this ExternalGnbCuUpFunctionSingleAllOf.
        :type ep_xn_u: List[EPXnUSingle]
        """

        self._ep_xn_u = ep_xn_u
