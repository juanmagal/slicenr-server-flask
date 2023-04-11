# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.epe1_single import EPE1Single
from openapi_server.models.epf1_u_single import EPF1USingle
from openapi_server.models.epng_u_single import EPNgUSingle
from openapi_server.models.eps1_u_single import EPS1USingle
from openapi_server.models.epx2_u_single import EPX2USingle
from openapi_server.models.epxn_u_single import EPXnUSingle
from openapi_server.models.rrm_policy_ratio_single import RRMPolicyRatioSingle
from openapi_server import util

from openapi_server.models.epe1_single import EPE1Single  # noqa: E501
from openapi_server.models.epf1_u_single import EPF1USingle  # noqa: E501
from openapi_server.models.epng_u_single import EPNgUSingle  # noqa: E501
from openapi_server.models.eps1_u_single import EPS1USingle  # noqa: E501
from openapi_server.models.epx2_u_single import EPX2USingle  # noqa: E501
from openapi_server.models.epxn_u_single import EPXnUSingle  # noqa: E501
from openapi_server.models.rrm_policy_ratio_single import RRMPolicyRatioSingle  # noqa: E501

class GnbCuUpFunctionSingleAllOf1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, rrm_policy_ratio=None, ep_e1=None, ep_xn_u=None, ep_f1_u=None, ep_ng_u=None, ep_x2_u=None, ep_s1_u=None):  # noqa: E501
        """GnbCuUpFunctionSingleAllOf1 - a model defined in OpenAPI

        :param rrm_policy_ratio: The rrm_policy_ratio of this GnbCuUpFunctionSingleAllOf1.  # noqa: E501
        :type rrm_policy_ratio: List[RRMPolicyRatioSingle]
        :param ep_e1: The ep_e1 of this GnbCuUpFunctionSingleAllOf1.  # noqa: E501
        :type ep_e1: EPE1Single
        :param ep_xn_u: The ep_xn_u of this GnbCuUpFunctionSingleAllOf1.  # noqa: E501
        :type ep_xn_u: List[EPXnUSingle]
        :param ep_f1_u: The ep_f1_u of this GnbCuUpFunctionSingleAllOf1.  # noqa: E501
        :type ep_f1_u: List[EPF1USingle]
        :param ep_ng_u: The ep_ng_u of this GnbCuUpFunctionSingleAllOf1.  # noqa: E501
        :type ep_ng_u: List[EPNgUSingle]
        :param ep_x2_u: The ep_x2_u of this GnbCuUpFunctionSingleAllOf1.  # noqa: E501
        :type ep_x2_u: List[EPX2USingle]
        :param ep_s1_u: The ep_s1_u of this GnbCuUpFunctionSingleAllOf1.  # noqa: E501
        :type ep_s1_u: List[EPS1USingle]
        """
        self.openapi_types = {
            'rrm_policy_ratio': List[RRMPolicyRatioSingle],
            'ep_e1': EPE1Single,
            'ep_xn_u': List[EPXnUSingle],
            'ep_f1_u': List[EPF1USingle],
            'ep_ng_u': List[EPNgUSingle],
            'ep_x2_u': List[EPX2USingle],
            'ep_s1_u': List[EPS1USingle]
        }

        self.attribute_map = {
            'rrm_policy_ratio': 'RRMPolicyRatio',
            'ep_e1': 'EP_E1',
            'ep_xn_u': 'EP_XnU',
            'ep_f1_u': 'EP_F1U',
            'ep_ng_u': 'EP_NgU',
            'ep_x2_u': 'EP_X2U',
            'ep_s1_u': 'EP_S1U'
        }

        self._rrm_policy_ratio = rrm_policy_ratio
        self._ep_e1 = ep_e1
        self._ep_xn_u = ep_xn_u
        self._ep_f1_u = ep_f1_u
        self._ep_ng_u = ep_ng_u
        self._ep_x2_u = ep_x2_u
        self._ep_s1_u = ep_s1_u

    @classmethod
    def from_dict(cls, dikt) -> 'GnbCuUpFunctionSingleAllOf1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GnbCuUpFunction_Single_allOf_1 of this GnbCuUpFunctionSingleAllOf1.  # noqa: E501
        :rtype: GnbCuUpFunctionSingleAllOf1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def rrm_policy_ratio(self):
        """Gets the rrm_policy_ratio of this GnbCuUpFunctionSingleAllOf1.


        :return: The rrm_policy_ratio of this GnbCuUpFunctionSingleAllOf1.
        :rtype: List[RRMPolicyRatioSingle]
        """
        return self._rrm_policy_ratio

    @rrm_policy_ratio.setter
    def rrm_policy_ratio(self, rrm_policy_ratio):
        """Sets the rrm_policy_ratio of this GnbCuUpFunctionSingleAllOf1.


        :param rrm_policy_ratio: The rrm_policy_ratio of this GnbCuUpFunctionSingleAllOf1.
        :type rrm_policy_ratio: List[RRMPolicyRatioSingle]
        """

        self._rrm_policy_ratio = rrm_policy_ratio

    @property
    def ep_e1(self):
        """Gets the ep_e1 of this GnbCuUpFunctionSingleAllOf1.


        :return: The ep_e1 of this GnbCuUpFunctionSingleAllOf1.
        :rtype: EPE1Single
        """
        return self._ep_e1

    @ep_e1.setter
    def ep_e1(self, ep_e1):
        """Sets the ep_e1 of this GnbCuUpFunctionSingleAllOf1.


        :param ep_e1: The ep_e1 of this GnbCuUpFunctionSingleAllOf1.
        :type ep_e1: EPE1Single
        """

        self._ep_e1 = ep_e1

    @property
    def ep_xn_u(self):
        """Gets the ep_xn_u of this GnbCuUpFunctionSingleAllOf1.


        :return: The ep_xn_u of this GnbCuUpFunctionSingleAllOf1.
        :rtype: List[EPXnUSingle]
        """
        return self._ep_xn_u

    @ep_xn_u.setter
    def ep_xn_u(self, ep_xn_u):
        """Sets the ep_xn_u of this GnbCuUpFunctionSingleAllOf1.


        :param ep_xn_u: The ep_xn_u of this GnbCuUpFunctionSingleAllOf1.
        :type ep_xn_u: List[EPXnUSingle]
        """

        self._ep_xn_u = ep_xn_u

    @property
    def ep_f1_u(self):
        """Gets the ep_f1_u of this GnbCuUpFunctionSingleAllOf1.


        :return: The ep_f1_u of this GnbCuUpFunctionSingleAllOf1.
        :rtype: List[EPF1USingle]
        """
        return self._ep_f1_u

    @ep_f1_u.setter
    def ep_f1_u(self, ep_f1_u):
        """Sets the ep_f1_u of this GnbCuUpFunctionSingleAllOf1.


        :param ep_f1_u: The ep_f1_u of this GnbCuUpFunctionSingleAllOf1.
        :type ep_f1_u: List[EPF1USingle]
        """

        self._ep_f1_u = ep_f1_u

    @property
    def ep_ng_u(self):
        """Gets the ep_ng_u of this GnbCuUpFunctionSingleAllOf1.


        :return: The ep_ng_u of this GnbCuUpFunctionSingleAllOf1.
        :rtype: List[EPNgUSingle]
        """
        return self._ep_ng_u

    @ep_ng_u.setter
    def ep_ng_u(self, ep_ng_u):
        """Sets the ep_ng_u of this GnbCuUpFunctionSingleAllOf1.


        :param ep_ng_u: The ep_ng_u of this GnbCuUpFunctionSingleAllOf1.
        :type ep_ng_u: List[EPNgUSingle]
        """

        self._ep_ng_u = ep_ng_u

    @property
    def ep_x2_u(self):
        """Gets the ep_x2_u of this GnbCuUpFunctionSingleAllOf1.


        :return: The ep_x2_u of this GnbCuUpFunctionSingleAllOf1.
        :rtype: List[EPX2USingle]
        """
        return self._ep_x2_u

    @ep_x2_u.setter
    def ep_x2_u(self, ep_x2_u):
        """Sets the ep_x2_u of this GnbCuUpFunctionSingleAllOf1.


        :param ep_x2_u: The ep_x2_u of this GnbCuUpFunctionSingleAllOf1.
        :type ep_x2_u: List[EPX2USingle]
        """

        self._ep_x2_u = ep_x2_u

    @property
    def ep_s1_u(self):
        """Gets the ep_s1_u of this GnbCuUpFunctionSingleAllOf1.


        :return: The ep_s1_u of this GnbCuUpFunctionSingleAllOf1.
        :rtype: List[EPS1USingle]
        """
        return self._ep_s1_u

    @ep_s1_u.setter
    def ep_s1_u(self, ep_s1_u):
        """Sets the ep_s1_u of this GnbCuUpFunctionSingleAllOf1.


        :param ep_s1_u: The ep_s1_u of this GnbCuUpFunctionSingleAllOf1.
        :type ep_s1_u: List[EPS1USingle]
        """

        self._ep_s1_u = ep_s1_u
