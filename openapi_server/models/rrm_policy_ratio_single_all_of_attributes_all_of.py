# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class RRMPolicyRatioSingleAllOfAttributesAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, r_rm_policy_max_ratio=None, r_rm_policy_min_ratio=None, r_rm_policy_dedicated_ratio=None):  # noqa: E501
        """RRMPolicyRatioSingleAllOfAttributesAllOf - a model defined in OpenAPI

        :param r_rm_policy_max_ratio: The r_rm_policy_max_ratio of this RRMPolicyRatioSingleAllOfAttributesAllOf.  # noqa: E501
        :type r_rm_policy_max_ratio: int
        :param r_rm_policy_min_ratio: The r_rm_policy_min_ratio of this RRMPolicyRatioSingleAllOfAttributesAllOf.  # noqa: E501
        :type r_rm_policy_min_ratio: int
        :param r_rm_policy_dedicated_ratio: The r_rm_policy_dedicated_ratio of this RRMPolicyRatioSingleAllOfAttributesAllOf.  # noqa: E501
        :type r_rm_policy_dedicated_ratio: int
        """
        self.openapi_types = {
            'r_rm_policy_max_ratio': int,
            'r_rm_policy_min_ratio': int,
            'r_rm_policy_dedicated_ratio': int
        }

        self.attribute_map = {
            'r_rm_policy_max_ratio': 'rRMPolicyMaxRatio',
            'r_rm_policy_min_ratio': 'rRMPolicyMinRatio',
            'r_rm_policy_dedicated_ratio': 'rRMPolicyDedicatedRatio'
        }

        self._r_rm_policy_max_ratio = r_rm_policy_max_ratio
        self._r_rm_policy_min_ratio = r_rm_policy_min_ratio
        self._r_rm_policy_dedicated_ratio = r_rm_policy_dedicated_ratio

    @classmethod
    def from_dict(cls, dikt) -> 'RRMPolicyRatioSingleAllOfAttributesAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RRMPolicyRatio_Single_allOf_attributes_allOf of this RRMPolicyRatioSingleAllOfAttributesAllOf.  # noqa: E501
        :rtype: RRMPolicyRatioSingleAllOfAttributesAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def r_rm_policy_max_ratio(self):
        """Gets the r_rm_policy_max_ratio of this RRMPolicyRatioSingleAllOfAttributesAllOf.


        :return: The r_rm_policy_max_ratio of this RRMPolicyRatioSingleAllOfAttributesAllOf.
        :rtype: int
        """
        return self._r_rm_policy_max_ratio

    @r_rm_policy_max_ratio.setter
    def r_rm_policy_max_ratio(self, r_rm_policy_max_ratio):
        """Sets the r_rm_policy_max_ratio of this RRMPolicyRatioSingleAllOfAttributesAllOf.


        :param r_rm_policy_max_ratio: The r_rm_policy_max_ratio of this RRMPolicyRatioSingleAllOfAttributesAllOf.
        :type r_rm_policy_max_ratio: int
        """

        self._r_rm_policy_max_ratio = r_rm_policy_max_ratio

    @property
    def r_rm_policy_min_ratio(self):
        """Gets the r_rm_policy_min_ratio of this RRMPolicyRatioSingleAllOfAttributesAllOf.


        :return: The r_rm_policy_min_ratio of this RRMPolicyRatioSingleAllOfAttributesAllOf.
        :rtype: int
        """
        return self._r_rm_policy_min_ratio

    @r_rm_policy_min_ratio.setter
    def r_rm_policy_min_ratio(self, r_rm_policy_min_ratio):
        """Sets the r_rm_policy_min_ratio of this RRMPolicyRatioSingleAllOfAttributesAllOf.


        :param r_rm_policy_min_ratio: The r_rm_policy_min_ratio of this RRMPolicyRatioSingleAllOfAttributesAllOf.
        :type r_rm_policy_min_ratio: int
        """

        self._r_rm_policy_min_ratio = r_rm_policy_min_ratio

    @property
    def r_rm_policy_dedicated_ratio(self):
        """Gets the r_rm_policy_dedicated_ratio of this RRMPolicyRatioSingleAllOfAttributesAllOf.


        :return: The r_rm_policy_dedicated_ratio of this RRMPolicyRatioSingleAllOfAttributesAllOf.
        :rtype: int
        """
        return self._r_rm_policy_dedicated_ratio

    @r_rm_policy_dedicated_ratio.setter
    def r_rm_policy_dedicated_ratio(self, r_rm_policy_dedicated_ratio):
        """Sets the r_rm_policy_dedicated_ratio of this RRMPolicyRatioSingleAllOfAttributesAllOf.


        :param r_rm_policy_dedicated_ratio: The r_rm_policy_dedicated_ratio of this RRMPolicyRatioSingleAllOfAttributesAllOf.
        :type r_rm_policy_dedicated_ratio: int
        """

        self._r_rm_policy_dedicated_ratio = r_rm_policy_dedicated_ratio
