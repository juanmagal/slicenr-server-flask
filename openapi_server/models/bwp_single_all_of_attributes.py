# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.bwp_context import BwpContext
from openapi_server.models.cyclic_prefix import CyclicPrefix
from openapi_server.models.is_initial_bwp import IsInitialBwp
from openapi_server.models.pee_parameter import PeeParameter
from openapi_server.models.supported_perf_metric_group import SupportedPerfMetricGroup
from openapi_server.models.vnf_parameter import VnfParameter
from openapi_server import util

from openapi_server.models.bwp_context import BwpContext  # noqa: E501
from openapi_server.models.cyclic_prefix import CyclicPrefix  # noqa: E501
from openapi_server.models.is_initial_bwp import IsInitialBwp  # noqa: E501
from openapi_server.models.pee_parameter import PeeParameter  # noqa: E501
from openapi_server.models.supported_perf_metric_group import SupportedPerfMetricGroup  # noqa: E501
from openapi_server.models.vnf_parameter import VnfParameter  # noqa: E501

class BwpSingleAllOfAttributes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, user_label=None, vnf_parameters_list=None, pee_parameters_list=None, priority_label=None, supported_perf_metric_groups=None, supported_trace_metrics=None, bwp_context=None, is_initial_bwp=None, sub_carrier_spacing=None, cyclic_prefix=None, start_rb=None, number_of_rbs=None):  # noqa: E501
        """BwpSingleAllOfAttributes - a model defined in OpenAPI

        :param user_label: The user_label of this BwpSingleAllOfAttributes.  # noqa: E501
        :type user_label: str
        :param vnf_parameters_list: The vnf_parameters_list of this BwpSingleAllOfAttributes.  # noqa: E501
        :type vnf_parameters_list: List[VnfParameter]
        :param pee_parameters_list: The pee_parameters_list of this BwpSingleAllOfAttributes.  # noqa: E501
        :type pee_parameters_list: List[PeeParameter]
        :param priority_label: The priority_label of this BwpSingleAllOfAttributes.  # noqa: E501
        :type priority_label: int
        :param supported_perf_metric_groups: The supported_perf_metric_groups of this BwpSingleAllOfAttributes.  # noqa: E501
        :type supported_perf_metric_groups: List[SupportedPerfMetricGroup]
        :param supported_trace_metrics: The supported_trace_metrics of this BwpSingleAllOfAttributes.  # noqa: E501
        :type supported_trace_metrics: List[str]
        :param bwp_context: The bwp_context of this BwpSingleAllOfAttributes.  # noqa: E501
        :type bwp_context: BwpContext
        :param is_initial_bwp: The is_initial_bwp of this BwpSingleAllOfAttributes.  # noqa: E501
        :type is_initial_bwp: IsInitialBwp
        :param sub_carrier_spacing: The sub_carrier_spacing of this BwpSingleAllOfAttributes.  # noqa: E501
        :type sub_carrier_spacing: int
        :param cyclic_prefix: The cyclic_prefix of this BwpSingleAllOfAttributes.  # noqa: E501
        :type cyclic_prefix: CyclicPrefix
        :param start_rb: The start_rb of this BwpSingleAllOfAttributes.  # noqa: E501
        :type start_rb: int
        :param number_of_rbs: The number_of_rbs of this BwpSingleAllOfAttributes.  # noqa: E501
        :type number_of_rbs: int
        """
        self.openapi_types = {
            'user_label': str,
            'vnf_parameters_list': List[VnfParameter],
            'pee_parameters_list': List[PeeParameter],
            'priority_label': int,
            'supported_perf_metric_groups': List[SupportedPerfMetricGroup],
            'supported_trace_metrics': List[str],
            'bwp_context': BwpContext,
            'is_initial_bwp': IsInitialBwp,
            'sub_carrier_spacing': int,
            'cyclic_prefix': CyclicPrefix,
            'start_rb': int,
            'number_of_rbs': int
        }

        self.attribute_map = {
            'user_label': 'userLabel',
            'vnf_parameters_list': 'vnfParametersList',
            'pee_parameters_list': 'peeParametersList',
            'priority_label': 'priorityLabel',
            'supported_perf_metric_groups': 'supportedPerfMetricGroups',
            'supported_trace_metrics': 'supportedTraceMetrics',
            'bwp_context': 'bwpContext',
            'is_initial_bwp': 'isInitialBwp',
            'sub_carrier_spacing': 'subCarrierSpacing',
            'cyclic_prefix': 'cyclicPrefix',
            'start_rb': 'startRB',
            'number_of_rbs': 'numberOfRBs'
        }

        self._user_label = user_label
        self._vnf_parameters_list = vnf_parameters_list
        self._pee_parameters_list = pee_parameters_list
        self._priority_label = priority_label
        self._supported_perf_metric_groups = supported_perf_metric_groups
        self._supported_trace_metrics = supported_trace_metrics
        self._bwp_context = bwp_context
        self._is_initial_bwp = is_initial_bwp
        self._sub_carrier_spacing = sub_carrier_spacing
        self._cyclic_prefix = cyclic_prefix
        self._start_rb = start_rb
        self._number_of_rbs = number_of_rbs

    @classmethod
    def from_dict(cls, dikt) -> 'BwpSingleAllOfAttributes':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Bwp_Single_allOf_attributes of this BwpSingleAllOfAttributes.  # noqa: E501
        :rtype: BwpSingleAllOfAttributes
        """
        return util.deserialize_model(dikt, cls)

    @property
    def user_label(self):
        """Gets the user_label of this BwpSingleAllOfAttributes.


        :return: The user_label of this BwpSingleAllOfAttributes.
        :rtype: str
        """
        return self._user_label

    @user_label.setter
    def user_label(self, user_label):
        """Sets the user_label of this BwpSingleAllOfAttributes.


        :param user_label: The user_label of this BwpSingleAllOfAttributes.
        :type user_label: str
        """

        self._user_label = user_label

    @property
    def vnf_parameters_list(self):
        """Gets the vnf_parameters_list of this BwpSingleAllOfAttributes.


        :return: The vnf_parameters_list of this BwpSingleAllOfAttributes.
        :rtype: List[VnfParameter]
        """
        return self._vnf_parameters_list

    @vnf_parameters_list.setter
    def vnf_parameters_list(self, vnf_parameters_list):
        """Sets the vnf_parameters_list of this BwpSingleAllOfAttributes.


        :param vnf_parameters_list: The vnf_parameters_list of this BwpSingleAllOfAttributes.
        :type vnf_parameters_list: List[VnfParameter]
        """

        self._vnf_parameters_list = vnf_parameters_list

    @property
    def pee_parameters_list(self):
        """Gets the pee_parameters_list of this BwpSingleAllOfAttributes.


        :return: The pee_parameters_list of this BwpSingleAllOfAttributes.
        :rtype: List[PeeParameter]
        """
        return self._pee_parameters_list

    @pee_parameters_list.setter
    def pee_parameters_list(self, pee_parameters_list):
        """Sets the pee_parameters_list of this BwpSingleAllOfAttributes.


        :param pee_parameters_list: The pee_parameters_list of this BwpSingleAllOfAttributes.
        :type pee_parameters_list: List[PeeParameter]
        """

        self._pee_parameters_list = pee_parameters_list

    @property
    def priority_label(self):
        """Gets the priority_label of this BwpSingleAllOfAttributes.


        :return: The priority_label of this BwpSingleAllOfAttributes.
        :rtype: int
        """
        return self._priority_label

    @priority_label.setter
    def priority_label(self, priority_label):
        """Sets the priority_label of this BwpSingleAllOfAttributes.


        :param priority_label: The priority_label of this BwpSingleAllOfAttributes.
        :type priority_label: int
        """

        self._priority_label = priority_label

    @property
    def supported_perf_metric_groups(self):
        """Gets the supported_perf_metric_groups of this BwpSingleAllOfAttributes.


        :return: The supported_perf_metric_groups of this BwpSingleAllOfAttributes.
        :rtype: List[SupportedPerfMetricGroup]
        """
        return self._supported_perf_metric_groups

    @supported_perf_metric_groups.setter
    def supported_perf_metric_groups(self, supported_perf_metric_groups):
        """Sets the supported_perf_metric_groups of this BwpSingleAllOfAttributes.


        :param supported_perf_metric_groups: The supported_perf_metric_groups of this BwpSingleAllOfAttributes.
        :type supported_perf_metric_groups: List[SupportedPerfMetricGroup]
        """

        self._supported_perf_metric_groups = supported_perf_metric_groups

    @property
    def supported_trace_metrics(self):
        """Gets the supported_trace_metrics of this BwpSingleAllOfAttributes.


        :return: The supported_trace_metrics of this BwpSingleAllOfAttributes.
        :rtype: List[str]
        """
        return self._supported_trace_metrics

    @supported_trace_metrics.setter
    def supported_trace_metrics(self, supported_trace_metrics):
        """Sets the supported_trace_metrics of this BwpSingleAllOfAttributes.


        :param supported_trace_metrics: The supported_trace_metrics of this BwpSingleAllOfAttributes.
        :type supported_trace_metrics: List[str]
        """

        self._supported_trace_metrics = supported_trace_metrics

    @property
    def bwp_context(self):
        """Gets the bwp_context of this BwpSingleAllOfAttributes.


        :return: The bwp_context of this BwpSingleAllOfAttributes.
        :rtype: BwpContext
        """
        return self._bwp_context

    @bwp_context.setter
    def bwp_context(self, bwp_context):
        """Sets the bwp_context of this BwpSingleAllOfAttributes.


        :param bwp_context: The bwp_context of this BwpSingleAllOfAttributes.
        :type bwp_context: BwpContext
        """

        self._bwp_context = bwp_context

    @property
    def is_initial_bwp(self):
        """Gets the is_initial_bwp of this BwpSingleAllOfAttributes.


        :return: The is_initial_bwp of this BwpSingleAllOfAttributes.
        :rtype: IsInitialBwp
        """
        return self._is_initial_bwp

    @is_initial_bwp.setter
    def is_initial_bwp(self, is_initial_bwp):
        """Sets the is_initial_bwp of this BwpSingleAllOfAttributes.


        :param is_initial_bwp: The is_initial_bwp of this BwpSingleAllOfAttributes.
        :type is_initial_bwp: IsInitialBwp
        """

        self._is_initial_bwp = is_initial_bwp

    @property
    def sub_carrier_spacing(self):
        """Gets the sub_carrier_spacing of this BwpSingleAllOfAttributes.


        :return: The sub_carrier_spacing of this BwpSingleAllOfAttributes.
        :rtype: int
        """
        return self._sub_carrier_spacing

    @sub_carrier_spacing.setter
    def sub_carrier_spacing(self, sub_carrier_spacing):
        """Sets the sub_carrier_spacing of this BwpSingleAllOfAttributes.


        :param sub_carrier_spacing: The sub_carrier_spacing of this BwpSingleAllOfAttributes.
        :type sub_carrier_spacing: int
        """

        self._sub_carrier_spacing = sub_carrier_spacing

    @property
    def cyclic_prefix(self):
        """Gets the cyclic_prefix of this BwpSingleAllOfAttributes.


        :return: The cyclic_prefix of this BwpSingleAllOfAttributes.
        :rtype: CyclicPrefix
        """
        return self._cyclic_prefix

    @cyclic_prefix.setter
    def cyclic_prefix(self, cyclic_prefix):
        """Sets the cyclic_prefix of this BwpSingleAllOfAttributes.


        :param cyclic_prefix: The cyclic_prefix of this BwpSingleAllOfAttributes.
        :type cyclic_prefix: CyclicPrefix
        """

        self._cyclic_prefix = cyclic_prefix

    @property
    def start_rb(self):
        """Gets the start_rb of this BwpSingleAllOfAttributes.


        :return: The start_rb of this BwpSingleAllOfAttributes.
        :rtype: int
        """
        return self._start_rb

    @start_rb.setter
    def start_rb(self, start_rb):
        """Sets the start_rb of this BwpSingleAllOfAttributes.


        :param start_rb: The start_rb of this BwpSingleAllOfAttributes.
        :type start_rb: int
        """

        self._start_rb = start_rb

    @property
    def number_of_rbs(self):
        """Gets the number_of_rbs of this BwpSingleAllOfAttributes.


        :return: The number_of_rbs of this BwpSingleAllOfAttributes.
        :rtype: int
        """
        return self._number_of_rbs

    @number_of_rbs.setter
    def number_of_rbs(self, number_of_rbs):
        """Sets the number_of_rbs of this BwpSingleAllOfAttributes.


        :param number_of_rbs: The number_of_rbs of this BwpSingleAllOfAttributes.
        :type number_of_rbs: int
        """

        self._number_of_rbs = number_of_rbs
