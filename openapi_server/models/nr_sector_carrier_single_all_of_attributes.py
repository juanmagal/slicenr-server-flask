# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.pee_parameter import PeeParameter
from openapi_server.models.supported_perf_metric_group import SupportedPerfMetricGroup
from openapi_server.models.tx_direction import TxDirection
from openapi_server.models.vnf_parameter import VnfParameter
from openapi_server import util

from openapi_server.models.pee_parameter import PeeParameter  # noqa: E501
from openapi_server.models.supported_perf_metric_group import SupportedPerfMetricGroup  # noqa: E501
from openapi_server.models.tx_direction import TxDirection  # noqa: E501
from openapi_server.models.vnf_parameter import VnfParameter  # noqa: E501

class NrSectorCarrierSingleAllOfAttributes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, user_label=None, vnf_parameters_list=None, pee_parameters_list=None, priority_label=None, supported_perf_metric_groups=None, supported_trace_metrics=None, tx_direction=None, configured_max_tx_power=None, arfcn_dl=None, arfcn_ul=None, b_s_channel_bw_dl=None, b_s_channel_bw_ul=None, sector_equipment_function_ref=None):  # noqa: E501
        """NrSectorCarrierSingleAllOfAttributes - a model defined in OpenAPI

        :param user_label: The user_label of this NrSectorCarrierSingleAllOfAttributes.  # noqa: E501
        :type user_label: str
        :param vnf_parameters_list: The vnf_parameters_list of this NrSectorCarrierSingleAllOfAttributes.  # noqa: E501
        :type vnf_parameters_list: List[VnfParameter]
        :param pee_parameters_list: The pee_parameters_list of this NrSectorCarrierSingleAllOfAttributes.  # noqa: E501
        :type pee_parameters_list: List[PeeParameter]
        :param priority_label: The priority_label of this NrSectorCarrierSingleAllOfAttributes.  # noqa: E501
        :type priority_label: int
        :param supported_perf_metric_groups: The supported_perf_metric_groups of this NrSectorCarrierSingleAllOfAttributes.  # noqa: E501
        :type supported_perf_metric_groups: List[SupportedPerfMetricGroup]
        :param supported_trace_metrics: The supported_trace_metrics of this NrSectorCarrierSingleAllOfAttributes.  # noqa: E501
        :type supported_trace_metrics: List[str]
        :param tx_direction: The tx_direction of this NrSectorCarrierSingleAllOfAttributes.  # noqa: E501
        :type tx_direction: TxDirection
        :param configured_max_tx_power: The configured_max_tx_power of this NrSectorCarrierSingleAllOfAttributes.  # noqa: E501
        :type configured_max_tx_power: int
        :param arfcn_dl: The arfcn_dl of this NrSectorCarrierSingleAllOfAttributes.  # noqa: E501
        :type arfcn_dl: int
        :param arfcn_ul: The arfcn_ul of this NrSectorCarrierSingleAllOfAttributes.  # noqa: E501
        :type arfcn_ul: int
        :param b_s_channel_bw_dl: The b_s_channel_bw_dl of this NrSectorCarrierSingleAllOfAttributes.  # noqa: E501
        :type b_s_channel_bw_dl: int
        :param b_s_channel_bw_ul: The b_s_channel_bw_ul of this NrSectorCarrierSingleAllOfAttributes.  # noqa: E501
        :type b_s_channel_bw_ul: int
        :param sector_equipment_function_ref: The sector_equipment_function_ref of this NrSectorCarrierSingleAllOfAttributes.  # noqa: E501
        :type sector_equipment_function_ref: str
        """
        self.openapi_types = {
            'user_label': str,
            'vnf_parameters_list': List[VnfParameter],
            'pee_parameters_list': List[PeeParameter],
            'priority_label': int,
            'supported_perf_metric_groups': List[SupportedPerfMetricGroup],
            'supported_trace_metrics': List[str],
            'tx_direction': TxDirection,
            'configured_max_tx_power': int,
            'arfcn_dl': int,
            'arfcn_ul': int,
            'b_s_channel_bw_dl': int,
            'b_s_channel_bw_ul': int,
            'sector_equipment_function_ref': str
        }

        self.attribute_map = {
            'user_label': 'userLabel',
            'vnf_parameters_list': 'vnfParametersList',
            'pee_parameters_list': 'peeParametersList',
            'priority_label': 'priorityLabel',
            'supported_perf_metric_groups': 'supportedPerfMetricGroups',
            'supported_trace_metrics': 'supportedTraceMetrics',
            'tx_direction': 'txDirection',
            'configured_max_tx_power': 'configuredMaxTxPower',
            'arfcn_dl': 'arfcnDL',
            'arfcn_ul': 'arfcnUL',
            'b_s_channel_bw_dl': 'bSChannelBwDL',
            'b_s_channel_bw_ul': 'bSChannelBwUL',
            'sector_equipment_function_ref': 'sectorEquipmentFunctionRef'
        }

        self._user_label = user_label
        self._vnf_parameters_list = vnf_parameters_list
        self._pee_parameters_list = pee_parameters_list
        self._priority_label = priority_label
        self._supported_perf_metric_groups = supported_perf_metric_groups
        self._supported_trace_metrics = supported_trace_metrics
        self._tx_direction = tx_direction
        self._configured_max_tx_power = configured_max_tx_power
        self._arfcn_dl = arfcn_dl
        self._arfcn_ul = arfcn_ul
        self._b_s_channel_bw_dl = b_s_channel_bw_dl
        self._b_s_channel_bw_ul = b_s_channel_bw_ul
        self._sector_equipment_function_ref = sector_equipment_function_ref

    @classmethod
    def from_dict(cls, dikt) -> 'NrSectorCarrierSingleAllOfAttributes':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NrSectorCarrier_Single_allOf_attributes of this NrSectorCarrierSingleAllOfAttributes.  # noqa: E501
        :rtype: NrSectorCarrierSingleAllOfAttributes
        """
        return util.deserialize_model(dikt, cls)

    @property
    def user_label(self):
        """Gets the user_label of this NrSectorCarrierSingleAllOfAttributes.


        :return: The user_label of this NrSectorCarrierSingleAllOfAttributes.
        :rtype: str
        """
        return self._user_label

    @user_label.setter
    def user_label(self, user_label):
        """Sets the user_label of this NrSectorCarrierSingleAllOfAttributes.


        :param user_label: The user_label of this NrSectorCarrierSingleAllOfAttributes.
        :type user_label: str
        """

        self._user_label = user_label

    @property
    def vnf_parameters_list(self):
        """Gets the vnf_parameters_list of this NrSectorCarrierSingleAllOfAttributes.


        :return: The vnf_parameters_list of this NrSectorCarrierSingleAllOfAttributes.
        :rtype: List[VnfParameter]
        """
        return self._vnf_parameters_list

    @vnf_parameters_list.setter
    def vnf_parameters_list(self, vnf_parameters_list):
        """Sets the vnf_parameters_list of this NrSectorCarrierSingleAllOfAttributes.


        :param vnf_parameters_list: The vnf_parameters_list of this NrSectorCarrierSingleAllOfAttributes.
        :type vnf_parameters_list: List[VnfParameter]
        """

        self._vnf_parameters_list = vnf_parameters_list

    @property
    def pee_parameters_list(self):
        """Gets the pee_parameters_list of this NrSectorCarrierSingleAllOfAttributes.


        :return: The pee_parameters_list of this NrSectorCarrierSingleAllOfAttributes.
        :rtype: List[PeeParameter]
        """
        return self._pee_parameters_list

    @pee_parameters_list.setter
    def pee_parameters_list(self, pee_parameters_list):
        """Sets the pee_parameters_list of this NrSectorCarrierSingleAllOfAttributes.


        :param pee_parameters_list: The pee_parameters_list of this NrSectorCarrierSingleAllOfAttributes.
        :type pee_parameters_list: List[PeeParameter]
        """

        self._pee_parameters_list = pee_parameters_list

    @property
    def priority_label(self):
        """Gets the priority_label of this NrSectorCarrierSingleAllOfAttributes.


        :return: The priority_label of this NrSectorCarrierSingleAllOfAttributes.
        :rtype: int
        """
        return self._priority_label

    @priority_label.setter
    def priority_label(self, priority_label):
        """Sets the priority_label of this NrSectorCarrierSingleAllOfAttributes.


        :param priority_label: The priority_label of this NrSectorCarrierSingleAllOfAttributes.
        :type priority_label: int
        """

        self._priority_label = priority_label

    @property
    def supported_perf_metric_groups(self):
        """Gets the supported_perf_metric_groups of this NrSectorCarrierSingleAllOfAttributes.


        :return: The supported_perf_metric_groups of this NrSectorCarrierSingleAllOfAttributes.
        :rtype: List[SupportedPerfMetricGroup]
        """
        return self._supported_perf_metric_groups

    @supported_perf_metric_groups.setter
    def supported_perf_metric_groups(self, supported_perf_metric_groups):
        """Sets the supported_perf_metric_groups of this NrSectorCarrierSingleAllOfAttributes.


        :param supported_perf_metric_groups: The supported_perf_metric_groups of this NrSectorCarrierSingleAllOfAttributes.
        :type supported_perf_metric_groups: List[SupportedPerfMetricGroup]
        """

        self._supported_perf_metric_groups = supported_perf_metric_groups

    @property
    def supported_trace_metrics(self):
        """Gets the supported_trace_metrics of this NrSectorCarrierSingleAllOfAttributes.


        :return: The supported_trace_metrics of this NrSectorCarrierSingleAllOfAttributes.
        :rtype: List[str]
        """
        return self._supported_trace_metrics

    @supported_trace_metrics.setter
    def supported_trace_metrics(self, supported_trace_metrics):
        """Sets the supported_trace_metrics of this NrSectorCarrierSingleAllOfAttributes.


        :param supported_trace_metrics: The supported_trace_metrics of this NrSectorCarrierSingleAllOfAttributes.
        :type supported_trace_metrics: List[str]
        """

        self._supported_trace_metrics = supported_trace_metrics

    @property
    def tx_direction(self):
        """Gets the tx_direction of this NrSectorCarrierSingleAllOfAttributes.


        :return: The tx_direction of this NrSectorCarrierSingleAllOfAttributes.
        :rtype: TxDirection
        """
        return self._tx_direction

    @tx_direction.setter
    def tx_direction(self, tx_direction):
        """Sets the tx_direction of this NrSectorCarrierSingleAllOfAttributes.


        :param tx_direction: The tx_direction of this NrSectorCarrierSingleAllOfAttributes.
        :type tx_direction: TxDirection
        """

        self._tx_direction = tx_direction

    @property
    def configured_max_tx_power(self):
        """Gets the configured_max_tx_power of this NrSectorCarrierSingleAllOfAttributes.


        :return: The configured_max_tx_power of this NrSectorCarrierSingleAllOfAttributes.
        :rtype: int
        """
        return self._configured_max_tx_power

    @configured_max_tx_power.setter
    def configured_max_tx_power(self, configured_max_tx_power):
        """Sets the configured_max_tx_power of this NrSectorCarrierSingleAllOfAttributes.


        :param configured_max_tx_power: The configured_max_tx_power of this NrSectorCarrierSingleAllOfAttributes.
        :type configured_max_tx_power: int
        """

        self._configured_max_tx_power = configured_max_tx_power

    @property
    def arfcn_dl(self):
        """Gets the arfcn_dl of this NrSectorCarrierSingleAllOfAttributes.


        :return: The arfcn_dl of this NrSectorCarrierSingleAllOfAttributes.
        :rtype: int
        """
        return self._arfcn_dl

    @arfcn_dl.setter
    def arfcn_dl(self, arfcn_dl):
        """Sets the arfcn_dl of this NrSectorCarrierSingleAllOfAttributes.


        :param arfcn_dl: The arfcn_dl of this NrSectorCarrierSingleAllOfAttributes.
        :type arfcn_dl: int
        """

        self._arfcn_dl = arfcn_dl

    @property
    def arfcn_ul(self):
        """Gets the arfcn_ul of this NrSectorCarrierSingleAllOfAttributes.


        :return: The arfcn_ul of this NrSectorCarrierSingleAllOfAttributes.
        :rtype: int
        """
        return self._arfcn_ul

    @arfcn_ul.setter
    def arfcn_ul(self, arfcn_ul):
        """Sets the arfcn_ul of this NrSectorCarrierSingleAllOfAttributes.


        :param arfcn_ul: The arfcn_ul of this NrSectorCarrierSingleAllOfAttributes.
        :type arfcn_ul: int
        """

        self._arfcn_ul = arfcn_ul

    @property
    def b_s_channel_bw_dl(self):
        """Gets the b_s_channel_bw_dl of this NrSectorCarrierSingleAllOfAttributes.


        :return: The b_s_channel_bw_dl of this NrSectorCarrierSingleAllOfAttributes.
        :rtype: int
        """
        return self._b_s_channel_bw_dl

    @b_s_channel_bw_dl.setter
    def b_s_channel_bw_dl(self, b_s_channel_bw_dl):
        """Sets the b_s_channel_bw_dl of this NrSectorCarrierSingleAllOfAttributes.


        :param b_s_channel_bw_dl: The b_s_channel_bw_dl of this NrSectorCarrierSingleAllOfAttributes.
        :type b_s_channel_bw_dl: int
        """

        self._b_s_channel_bw_dl = b_s_channel_bw_dl

    @property
    def b_s_channel_bw_ul(self):
        """Gets the b_s_channel_bw_ul of this NrSectorCarrierSingleAllOfAttributes.


        :return: The b_s_channel_bw_ul of this NrSectorCarrierSingleAllOfAttributes.
        :rtype: int
        """
        return self._b_s_channel_bw_ul

    @b_s_channel_bw_ul.setter
    def b_s_channel_bw_ul(self, b_s_channel_bw_ul):
        """Sets the b_s_channel_bw_ul of this NrSectorCarrierSingleAllOfAttributes.


        :param b_s_channel_bw_ul: The b_s_channel_bw_ul of this NrSectorCarrierSingleAllOfAttributes.
        :type b_s_channel_bw_ul: int
        """

        self._b_s_channel_bw_ul = b_s_channel_bw_ul

    @property
    def sector_equipment_function_ref(self):
        """Gets the sector_equipment_function_ref of this NrSectorCarrierSingleAllOfAttributes.


        :return: The sector_equipment_function_ref of this NrSectorCarrierSingleAllOfAttributes.
        :rtype: str
        """
        return self._sector_equipment_function_ref

    @sector_equipment_function_ref.setter
    def sector_equipment_function_ref(self, sector_equipment_function_ref):
        """Sets the sector_equipment_function_ref of this NrSectorCarrierSingleAllOfAttributes.


        :param sector_equipment_function_ref: The sector_equipment_function_ref of this NrSectorCarrierSingleAllOfAttributes.
        :type sector_equipment_function_ref: str
        """

        self._sector_equipment_function_ref = sector_equipment_function_ref
