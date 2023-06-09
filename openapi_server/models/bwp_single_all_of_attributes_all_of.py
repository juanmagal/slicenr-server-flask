# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.bwp_context import BwpContext
from openapi_server.models.cyclic_prefix import CyclicPrefix
from openapi_server.models.is_initial_bwp import IsInitialBwp
from openapi_server import util

from openapi_server.models.bwp_context import BwpContext  # noqa: E501
from openapi_server.models.cyclic_prefix import CyclicPrefix  # noqa: E501
from openapi_server.models.is_initial_bwp import IsInitialBwp  # noqa: E501

class BwpSingleAllOfAttributesAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, bwp_context=None, is_initial_bwp=None, sub_carrier_spacing=None, cyclic_prefix=None, start_rb=None, number_of_rbs=None):  # noqa: E501
        """BwpSingleAllOfAttributesAllOf - a model defined in OpenAPI

        :param bwp_context: The bwp_context of this BwpSingleAllOfAttributesAllOf.  # noqa: E501
        :type bwp_context: BwpContext
        :param is_initial_bwp: The is_initial_bwp of this BwpSingleAllOfAttributesAllOf.  # noqa: E501
        :type is_initial_bwp: IsInitialBwp
        :param sub_carrier_spacing: The sub_carrier_spacing of this BwpSingleAllOfAttributesAllOf.  # noqa: E501
        :type sub_carrier_spacing: int
        :param cyclic_prefix: The cyclic_prefix of this BwpSingleAllOfAttributesAllOf.  # noqa: E501
        :type cyclic_prefix: CyclicPrefix
        :param start_rb: The start_rb of this BwpSingleAllOfAttributesAllOf.  # noqa: E501
        :type start_rb: int
        :param number_of_rbs: The number_of_rbs of this BwpSingleAllOfAttributesAllOf.  # noqa: E501
        :type number_of_rbs: int
        """
        self.openapi_types = {
            'bwp_context': BwpContext,
            'is_initial_bwp': IsInitialBwp,
            'sub_carrier_spacing': int,
            'cyclic_prefix': CyclicPrefix,
            'start_rb': int,
            'number_of_rbs': int
        }

        self.attribute_map = {
            'bwp_context': 'bwpContext',
            'is_initial_bwp': 'isInitialBwp',
            'sub_carrier_spacing': 'subCarrierSpacing',
            'cyclic_prefix': 'cyclicPrefix',
            'start_rb': 'startRB',
            'number_of_rbs': 'numberOfRBs'
        }

        self._bwp_context = bwp_context
        self._is_initial_bwp = is_initial_bwp
        self._sub_carrier_spacing = sub_carrier_spacing
        self._cyclic_prefix = cyclic_prefix
        self._start_rb = start_rb
        self._number_of_rbs = number_of_rbs

    @classmethod
    def from_dict(cls, dikt) -> 'BwpSingleAllOfAttributesAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Bwp_Single_allOf_attributes_allOf of this BwpSingleAllOfAttributesAllOf.  # noqa: E501
        :rtype: BwpSingleAllOfAttributesAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def bwp_context(self):
        """Gets the bwp_context of this BwpSingleAllOfAttributesAllOf.


        :return: The bwp_context of this BwpSingleAllOfAttributesAllOf.
        :rtype: BwpContext
        """
        return self._bwp_context

    @bwp_context.setter
    def bwp_context(self, bwp_context):
        """Sets the bwp_context of this BwpSingleAllOfAttributesAllOf.


        :param bwp_context: The bwp_context of this BwpSingleAllOfAttributesAllOf.
        :type bwp_context: BwpContext
        """

        self._bwp_context = bwp_context

    @property
    def is_initial_bwp(self):
        """Gets the is_initial_bwp of this BwpSingleAllOfAttributesAllOf.


        :return: The is_initial_bwp of this BwpSingleAllOfAttributesAllOf.
        :rtype: IsInitialBwp
        """
        return self._is_initial_bwp

    @is_initial_bwp.setter
    def is_initial_bwp(self, is_initial_bwp):
        """Sets the is_initial_bwp of this BwpSingleAllOfAttributesAllOf.


        :param is_initial_bwp: The is_initial_bwp of this BwpSingleAllOfAttributesAllOf.
        :type is_initial_bwp: IsInitialBwp
        """

        self._is_initial_bwp = is_initial_bwp

    @property
    def sub_carrier_spacing(self):
        """Gets the sub_carrier_spacing of this BwpSingleAllOfAttributesAllOf.


        :return: The sub_carrier_spacing of this BwpSingleAllOfAttributesAllOf.
        :rtype: int
        """
        return self._sub_carrier_spacing

    @sub_carrier_spacing.setter
    def sub_carrier_spacing(self, sub_carrier_spacing):
        """Sets the sub_carrier_spacing of this BwpSingleAllOfAttributesAllOf.


        :param sub_carrier_spacing: The sub_carrier_spacing of this BwpSingleAllOfAttributesAllOf.
        :type sub_carrier_spacing: int
        """

        self._sub_carrier_spacing = sub_carrier_spacing

    @property
    def cyclic_prefix(self):
        """Gets the cyclic_prefix of this BwpSingleAllOfAttributesAllOf.


        :return: The cyclic_prefix of this BwpSingleAllOfAttributesAllOf.
        :rtype: CyclicPrefix
        """
        return self._cyclic_prefix

    @cyclic_prefix.setter
    def cyclic_prefix(self, cyclic_prefix):
        """Sets the cyclic_prefix of this BwpSingleAllOfAttributesAllOf.


        :param cyclic_prefix: The cyclic_prefix of this BwpSingleAllOfAttributesAllOf.
        :type cyclic_prefix: CyclicPrefix
        """

        self._cyclic_prefix = cyclic_prefix

    @property
    def start_rb(self):
        """Gets the start_rb of this BwpSingleAllOfAttributesAllOf.


        :return: The start_rb of this BwpSingleAllOfAttributesAllOf.
        :rtype: int
        """
        return self._start_rb

    @start_rb.setter
    def start_rb(self, start_rb):
        """Sets the start_rb of this BwpSingleAllOfAttributesAllOf.


        :param start_rb: The start_rb of this BwpSingleAllOfAttributesAllOf.
        :type start_rb: int
        """

        self._start_rb = start_rb

    @property
    def number_of_rbs(self):
        """Gets the number_of_rbs of this BwpSingleAllOfAttributesAllOf.


        :return: The number_of_rbs of this BwpSingleAllOfAttributesAllOf.
        :rtype: int
        """
        return self._number_of_rbs

    @number_of_rbs.setter
    def number_of_rbs(self, number_of_rbs):
        """Sets the number_of_rbs of this BwpSingleAllOfAttributesAllOf.


        :param number_of_rbs: The number_of_rbs of this BwpSingleAllOfAttributesAllOf.
        :type number_of_rbs: int
        """

        self._number_of_rbs = number_of_rbs
