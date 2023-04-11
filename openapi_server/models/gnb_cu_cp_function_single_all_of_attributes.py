# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.mapping_set_id_backhaul_address import MappingSetIDBackhaulAddress
from openapi_server.models.pee_parameter import PeeParameter
from openapi_server.models.plmn_id import PlmnId
from openapi_server.models.supported_perf_metric_group import SupportedPerfMetricGroup
from openapi_server.models.tce_mapping_info import TceMappingInfo
from openapi_server.models.vnf_parameter import VnfParameter
from openapi_server import util

from openapi_server.models.mapping_set_id_backhaul_address import MappingSetIDBackhaulAddress  # noqa: E501
from openapi_server.models.pee_parameter import PeeParameter  # noqa: E501
from openapi_server.models.plmn_id import PlmnId  # noqa: E501
from openapi_server.models.supported_perf_metric_group import SupportedPerfMetricGroup  # noqa: E501
from openapi_server.models.tce_mapping_info import TceMappingInfo  # noqa: E501
from openapi_server.models.vnf_parameter import VnfParameter  # noqa: E501

class GnbCuCpFunctionSingleAllOfAttributes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, user_label=None, vnf_parameters_list=None, pee_parameters_list=None, priority_label=None, supported_perf_metric_groups=None, supported_trace_metrics=None, gnb_id=None, gnb_id_length=None, gnb_cu_name=None, plmn_id=None, x2_block_list=None, xn_block_list=None, x2_allow_list=None, xn_allow_list=None, x2_ho_black_list=None, xn_ho_black_list=None, mapping_set_id_backhaul_address=None, tce_mapping_info_list=None, configurable5_qi_set_ref=None, dynamic5_qi_set_ref=None, d_cho_control=None, d_dapsho_control=None):  # noqa: E501
        """GnbCuCpFunctionSingleAllOfAttributes - a model defined in OpenAPI

        :param user_label: The user_label of this GnbCuCpFunctionSingleAllOfAttributes.  # noqa: E501
        :type user_label: str
        :param vnf_parameters_list: The vnf_parameters_list of this GnbCuCpFunctionSingleAllOfAttributes.  # noqa: E501
        :type vnf_parameters_list: List[VnfParameter]
        :param pee_parameters_list: The pee_parameters_list of this GnbCuCpFunctionSingleAllOfAttributes.  # noqa: E501
        :type pee_parameters_list: List[PeeParameter]
        :param priority_label: The priority_label of this GnbCuCpFunctionSingleAllOfAttributes.  # noqa: E501
        :type priority_label: int
        :param supported_perf_metric_groups: The supported_perf_metric_groups of this GnbCuCpFunctionSingleAllOfAttributes.  # noqa: E501
        :type supported_perf_metric_groups: List[SupportedPerfMetricGroup]
        :param supported_trace_metrics: The supported_trace_metrics of this GnbCuCpFunctionSingleAllOfAttributes.  # noqa: E501
        :type supported_trace_metrics: List[str]
        :param gnb_id: The gnb_id of this GnbCuCpFunctionSingleAllOfAttributes.  # noqa: E501
        :type gnb_id: str
        :param gnb_id_length: The gnb_id_length of this GnbCuCpFunctionSingleAllOfAttributes.  # noqa: E501
        :type gnb_id_length: int
        :param gnb_cu_name: The gnb_cu_name of this GnbCuCpFunctionSingleAllOfAttributes.  # noqa: E501
        :type gnb_cu_name: str
        :param plmn_id: The plmn_id of this GnbCuCpFunctionSingleAllOfAttributes.  # noqa: E501
        :type plmn_id: PlmnId
        :param x2_block_list: The x2_block_list of this GnbCuCpFunctionSingleAllOfAttributes.  # noqa: E501
        :type x2_block_list: List[str]
        :param xn_block_list: The xn_block_list of this GnbCuCpFunctionSingleAllOfAttributes.  # noqa: E501
        :type xn_block_list: List[str]
        :param x2_allow_list: The x2_allow_list of this GnbCuCpFunctionSingleAllOfAttributes.  # noqa: E501
        :type x2_allow_list: List[str]
        :param xn_allow_list: The xn_allow_list of this GnbCuCpFunctionSingleAllOfAttributes.  # noqa: E501
        :type xn_allow_list: List[str]
        :param x2_ho_black_list: The x2_ho_black_list of this GnbCuCpFunctionSingleAllOfAttributes.  # noqa: E501
        :type x2_ho_black_list: List[str]
        :param xn_ho_black_list: The xn_ho_black_list of this GnbCuCpFunctionSingleAllOfAttributes.  # noqa: E501
        :type xn_ho_black_list: List[str]
        :param mapping_set_id_backhaul_address: The mapping_set_id_backhaul_address of this GnbCuCpFunctionSingleAllOfAttributes.  # noqa: E501
        :type mapping_set_id_backhaul_address: MappingSetIDBackhaulAddress
        :param tce_mapping_info_list: The tce_mapping_info_list of this GnbCuCpFunctionSingleAllOfAttributes.  # noqa: E501
        :type tce_mapping_info_list: List[TceMappingInfo]
        :param configurable5_qi_set_ref: The configurable5_qi_set_ref of this GnbCuCpFunctionSingleAllOfAttributes.  # noqa: E501
        :type configurable5_qi_set_ref: str
        :param dynamic5_qi_set_ref: The dynamic5_qi_set_ref of this GnbCuCpFunctionSingleAllOfAttributes.  # noqa: E501
        :type dynamic5_qi_set_ref: str
        :param d_cho_control: The d_cho_control of this GnbCuCpFunctionSingleAllOfAttributes.  # noqa: E501
        :type d_cho_control: bool
        :param d_dapsho_control: The d_dapsho_control of this GnbCuCpFunctionSingleAllOfAttributes.  # noqa: E501
        :type d_dapsho_control: bool
        """
        self.openapi_types = {
            'user_label': str,
            'vnf_parameters_list': List[VnfParameter],
            'pee_parameters_list': List[PeeParameter],
            'priority_label': int,
            'supported_perf_metric_groups': List[SupportedPerfMetricGroup],
            'supported_trace_metrics': List[str],
            'gnb_id': str,
            'gnb_id_length': int,
            'gnb_cu_name': str,
            'plmn_id': PlmnId,
            'x2_block_list': List[str],
            'xn_block_list': List[str],
            'x2_allow_list': List[str],
            'xn_allow_list': List[str],
            'x2_ho_black_list': List[str],
            'xn_ho_black_list': List[str],
            'mapping_set_id_backhaul_address': MappingSetIDBackhaulAddress,
            'tce_mapping_info_list': List[TceMappingInfo],
            'configurable5_qi_set_ref': str,
            'dynamic5_qi_set_ref': str,
            'd_cho_control': bool,
            'd_dapsho_control': bool
        }

        self.attribute_map = {
            'user_label': 'userLabel',
            'vnf_parameters_list': 'vnfParametersList',
            'pee_parameters_list': 'peeParametersList',
            'priority_label': 'priorityLabel',
            'supported_perf_metric_groups': 'supportedPerfMetricGroups',
            'supported_trace_metrics': 'supportedTraceMetrics',
            'gnb_id': 'gnbId',
            'gnb_id_length': 'gnbIdLength',
            'gnb_cu_name': 'gnbCuName',
            'plmn_id': 'plmnId',
            'x2_block_list': 'x2BlockList',
            'xn_block_list': 'xnBlockList',
            'x2_allow_list': 'x2AllowList',
            'xn_allow_list': 'xnAllowList',
            'x2_ho_black_list': 'x2HOBlackList',
            'xn_ho_black_list': 'xnHOBlackList',
            'mapping_set_id_backhaul_address': 'mappingSetIDBackhaulAddress',
            'tce_mapping_info_list': 'tceMappingInfoList',
            'configurable5_qi_set_ref': 'configurable5QISetRef',
            'dynamic5_qi_set_ref': 'dynamic5QISetRef',
            'd_cho_control': 'dCHOControl',
            'd_dapsho_control': 'dDAPSHOControl'
        }

        self._user_label = user_label
        self._vnf_parameters_list = vnf_parameters_list
        self._pee_parameters_list = pee_parameters_list
        self._priority_label = priority_label
        self._supported_perf_metric_groups = supported_perf_metric_groups
        self._supported_trace_metrics = supported_trace_metrics
        self._gnb_id = gnb_id
        self._gnb_id_length = gnb_id_length
        self._gnb_cu_name = gnb_cu_name
        self._plmn_id = plmn_id
        self._x2_block_list = x2_block_list
        self._xn_block_list = xn_block_list
        self._x2_allow_list = x2_allow_list
        self._xn_allow_list = xn_allow_list
        self._x2_ho_black_list = x2_ho_black_list
        self._xn_ho_black_list = xn_ho_black_list
        self._mapping_set_id_backhaul_address = mapping_set_id_backhaul_address
        self._tce_mapping_info_list = tce_mapping_info_list
        self._configurable5_qi_set_ref = configurable5_qi_set_ref
        self._dynamic5_qi_set_ref = dynamic5_qi_set_ref
        self._d_cho_control = d_cho_control
        self._d_dapsho_control = d_dapsho_control

    @classmethod
    def from_dict(cls, dikt) -> 'GnbCuCpFunctionSingleAllOfAttributes':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GnbCuCpFunction_Single_allOf_attributes of this GnbCuCpFunctionSingleAllOfAttributes.  # noqa: E501
        :rtype: GnbCuCpFunctionSingleAllOfAttributes
        """
        return util.deserialize_model(dikt, cls)

    @property
    def user_label(self):
        """Gets the user_label of this GnbCuCpFunctionSingleAllOfAttributes.


        :return: The user_label of this GnbCuCpFunctionSingleAllOfAttributes.
        :rtype: str
        """
        return self._user_label

    @user_label.setter
    def user_label(self, user_label):
        """Sets the user_label of this GnbCuCpFunctionSingleAllOfAttributes.


        :param user_label: The user_label of this GnbCuCpFunctionSingleAllOfAttributes.
        :type user_label: str
        """

        self._user_label = user_label

    @property
    def vnf_parameters_list(self):
        """Gets the vnf_parameters_list of this GnbCuCpFunctionSingleAllOfAttributes.


        :return: The vnf_parameters_list of this GnbCuCpFunctionSingleAllOfAttributes.
        :rtype: List[VnfParameter]
        """
        return self._vnf_parameters_list

    @vnf_parameters_list.setter
    def vnf_parameters_list(self, vnf_parameters_list):
        """Sets the vnf_parameters_list of this GnbCuCpFunctionSingleAllOfAttributes.


        :param vnf_parameters_list: The vnf_parameters_list of this GnbCuCpFunctionSingleAllOfAttributes.
        :type vnf_parameters_list: List[VnfParameter]
        """

        self._vnf_parameters_list = vnf_parameters_list

    @property
    def pee_parameters_list(self):
        """Gets the pee_parameters_list of this GnbCuCpFunctionSingleAllOfAttributes.


        :return: The pee_parameters_list of this GnbCuCpFunctionSingleAllOfAttributes.
        :rtype: List[PeeParameter]
        """
        return self._pee_parameters_list

    @pee_parameters_list.setter
    def pee_parameters_list(self, pee_parameters_list):
        """Sets the pee_parameters_list of this GnbCuCpFunctionSingleAllOfAttributes.


        :param pee_parameters_list: The pee_parameters_list of this GnbCuCpFunctionSingleAllOfAttributes.
        :type pee_parameters_list: List[PeeParameter]
        """

        self._pee_parameters_list = pee_parameters_list

    @property
    def priority_label(self):
        """Gets the priority_label of this GnbCuCpFunctionSingleAllOfAttributes.


        :return: The priority_label of this GnbCuCpFunctionSingleAllOfAttributes.
        :rtype: int
        """
        return self._priority_label

    @priority_label.setter
    def priority_label(self, priority_label):
        """Sets the priority_label of this GnbCuCpFunctionSingleAllOfAttributes.


        :param priority_label: The priority_label of this GnbCuCpFunctionSingleAllOfAttributes.
        :type priority_label: int
        """

        self._priority_label = priority_label

    @property
    def supported_perf_metric_groups(self):
        """Gets the supported_perf_metric_groups of this GnbCuCpFunctionSingleAllOfAttributes.


        :return: The supported_perf_metric_groups of this GnbCuCpFunctionSingleAllOfAttributes.
        :rtype: List[SupportedPerfMetricGroup]
        """
        return self._supported_perf_metric_groups

    @supported_perf_metric_groups.setter
    def supported_perf_metric_groups(self, supported_perf_metric_groups):
        """Sets the supported_perf_metric_groups of this GnbCuCpFunctionSingleAllOfAttributes.


        :param supported_perf_metric_groups: The supported_perf_metric_groups of this GnbCuCpFunctionSingleAllOfAttributes.
        :type supported_perf_metric_groups: List[SupportedPerfMetricGroup]
        """

        self._supported_perf_metric_groups = supported_perf_metric_groups

    @property
    def supported_trace_metrics(self):
        """Gets the supported_trace_metrics of this GnbCuCpFunctionSingleAllOfAttributes.


        :return: The supported_trace_metrics of this GnbCuCpFunctionSingleAllOfAttributes.
        :rtype: List[str]
        """
        return self._supported_trace_metrics

    @supported_trace_metrics.setter
    def supported_trace_metrics(self, supported_trace_metrics):
        """Sets the supported_trace_metrics of this GnbCuCpFunctionSingleAllOfAttributes.


        :param supported_trace_metrics: The supported_trace_metrics of this GnbCuCpFunctionSingleAllOfAttributes.
        :type supported_trace_metrics: List[str]
        """

        self._supported_trace_metrics = supported_trace_metrics

    @property
    def gnb_id(self):
        """Gets the gnb_id of this GnbCuCpFunctionSingleAllOfAttributes.


        :return: The gnb_id of this GnbCuCpFunctionSingleAllOfAttributes.
        :rtype: str
        """
        return self._gnb_id

    @gnb_id.setter
    def gnb_id(self, gnb_id):
        """Sets the gnb_id of this GnbCuCpFunctionSingleAllOfAttributes.


        :param gnb_id: The gnb_id of this GnbCuCpFunctionSingleAllOfAttributes.
        :type gnb_id: str
        """

        self._gnb_id = gnb_id

    @property
    def gnb_id_length(self):
        """Gets the gnb_id_length of this GnbCuCpFunctionSingleAllOfAttributes.


        :return: The gnb_id_length of this GnbCuCpFunctionSingleAllOfAttributes.
        :rtype: int
        """
        return self._gnb_id_length

    @gnb_id_length.setter
    def gnb_id_length(self, gnb_id_length):
        """Sets the gnb_id_length of this GnbCuCpFunctionSingleAllOfAttributes.


        :param gnb_id_length: The gnb_id_length of this GnbCuCpFunctionSingleAllOfAttributes.
        :type gnb_id_length: int
        """
        if gnb_id_length is not None and gnb_id_length > 32:  # noqa: E501
            raise ValueError("Invalid value for `gnb_id_length`, must be a value less than or equal to `32`")  # noqa: E501
        if gnb_id_length is not None and gnb_id_length < 22:  # noqa: E501
            raise ValueError("Invalid value for `gnb_id_length`, must be a value greater than or equal to `22`")  # noqa: E501

        self._gnb_id_length = gnb_id_length

    @property
    def gnb_cu_name(self):
        """Gets the gnb_cu_name of this GnbCuCpFunctionSingleAllOfAttributes.


        :return: The gnb_cu_name of this GnbCuCpFunctionSingleAllOfAttributes.
        :rtype: str
        """
        return self._gnb_cu_name

    @gnb_cu_name.setter
    def gnb_cu_name(self, gnb_cu_name):
        """Sets the gnb_cu_name of this GnbCuCpFunctionSingleAllOfAttributes.


        :param gnb_cu_name: The gnb_cu_name of this GnbCuCpFunctionSingleAllOfAttributes.
        :type gnb_cu_name: str
        """
        if gnb_cu_name is not None and len(gnb_cu_name) > 150:
            raise ValueError("Invalid value for `gnb_cu_name`, length must be less than or equal to `150`")  # noqa: E501

        self._gnb_cu_name = gnb_cu_name

    @property
    def plmn_id(self):
        """Gets the plmn_id of this GnbCuCpFunctionSingleAllOfAttributes.


        :return: The plmn_id of this GnbCuCpFunctionSingleAllOfAttributes.
        :rtype: PlmnId
        """
        return self._plmn_id

    @plmn_id.setter
    def plmn_id(self, plmn_id):
        """Sets the plmn_id of this GnbCuCpFunctionSingleAllOfAttributes.


        :param plmn_id: The plmn_id of this GnbCuCpFunctionSingleAllOfAttributes.
        :type plmn_id: PlmnId
        """

        self._plmn_id = plmn_id

    @property
    def x2_block_list(self):
        """Gets the x2_block_list of this GnbCuCpFunctionSingleAllOfAttributes.


        :return: The x2_block_list of this GnbCuCpFunctionSingleAllOfAttributes.
        :rtype: List[str]
        """
        return self._x2_block_list

    @x2_block_list.setter
    def x2_block_list(self, x2_block_list):
        """Sets the x2_block_list of this GnbCuCpFunctionSingleAllOfAttributes.


        :param x2_block_list: The x2_block_list of this GnbCuCpFunctionSingleAllOfAttributes.
        :type x2_block_list: List[str]
        """

        self._x2_block_list = x2_block_list

    @property
    def xn_block_list(self):
        """Gets the xn_block_list of this GnbCuCpFunctionSingleAllOfAttributes.


        :return: The xn_block_list of this GnbCuCpFunctionSingleAllOfAttributes.
        :rtype: List[str]
        """
        return self._xn_block_list

    @xn_block_list.setter
    def xn_block_list(self, xn_block_list):
        """Sets the xn_block_list of this GnbCuCpFunctionSingleAllOfAttributes.


        :param xn_block_list: The xn_block_list of this GnbCuCpFunctionSingleAllOfAttributes.
        :type xn_block_list: List[str]
        """

        self._xn_block_list = xn_block_list

    @property
    def x2_allow_list(self):
        """Gets the x2_allow_list of this GnbCuCpFunctionSingleAllOfAttributes.


        :return: The x2_allow_list of this GnbCuCpFunctionSingleAllOfAttributes.
        :rtype: List[str]
        """
        return self._x2_allow_list

    @x2_allow_list.setter
    def x2_allow_list(self, x2_allow_list):
        """Sets the x2_allow_list of this GnbCuCpFunctionSingleAllOfAttributes.


        :param x2_allow_list: The x2_allow_list of this GnbCuCpFunctionSingleAllOfAttributes.
        :type x2_allow_list: List[str]
        """

        self._x2_allow_list = x2_allow_list

    @property
    def xn_allow_list(self):
        """Gets the xn_allow_list of this GnbCuCpFunctionSingleAllOfAttributes.


        :return: The xn_allow_list of this GnbCuCpFunctionSingleAllOfAttributes.
        :rtype: List[str]
        """
        return self._xn_allow_list

    @xn_allow_list.setter
    def xn_allow_list(self, xn_allow_list):
        """Sets the xn_allow_list of this GnbCuCpFunctionSingleAllOfAttributes.


        :param xn_allow_list: The xn_allow_list of this GnbCuCpFunctionSingleAllOfAttributes.
        :type xn_allow_list: List[str]
        """

        self._xn_allow_list = xn_allow_list

    @property
    def x2_ho_black_list(self):
        """Gets the x2_ho_black_list of this GnbCuCpFunctionSingleAllOfAttributes.


        :return: The x2_ho_black_list of this GnbCuCpFunctionSingleAllOfAttributes.
        :rtype: List[str]
        """
        return self._x2_ho_black_list

    @x2_ho_black_list.setter
    def x2_ho_black_list(self, x2_ho_black_list):
        """Sets the x2_ho_black_list of this GnbCuCpFunctionSingleAllOfAttributes.


        :param x2_ho_black_list: The x2_ho_black_list of this GnbCuCpFunctionSingleAllOfAttributes.
        :type x2_ho_black_list: List[str]
        """

        self._x2_ho_black_list = x2_ho_black_list

    @property
    def xn_ho_black_list(self):
        """Gets the xn_ho_black_list of this GnbCuCpFunctionSingleAllOfAttributes.


        :return: The xn_ho_black_list of this GnbCuCpFunctionSingleAllOfAttributes.
        :rtype: List[str]
        """
        return self._xn_ho_black_list

    @xn_ho_black_list.setter
    def xn_ho_black_list(self, xn_ho_black_list):
        """Sets the xn_ho_black_list of this GnbCuCpFunctionSingleAllOfAttributes.


        :param xn_ho_black_list: The xn_ho_black_list of this GnbCuCpFunctionSingleAllOfAttributes.
        :type xn_ho_black_list: List[str]
        """

        self._xn_ho_black_list = xn_ho_black_list

    @property
    def mapping_set_id_backhaul_address(self):
        """Gets the mapping_set_id_backhaul_address of this GnbCuCpFunctionSingleAllOfAttributes.


        :return: The mapping_set_id_backhaul_address of this GnbCuCpFunctionSingleAllOfAttributes.
        :rtype: MappingSetIDBackhaulAddress
        """
        return self._mapping_set_id_backhaul_address

    @mapping_set_id_backhaul_address.setter
    def mapping_set_id_backhaul_address(self, mapping_set_id_backhaul_address):
        """Sets the mapping_set_id_backhaul_address of this GnbCuCpFunctionSingleAllOfAttributes.


        :param mapping_set_id_backhaul_address: The mapping_set_id_backhaul_address of this GnbCuCpFunctionSingleAllOfAttributes.
        :type mapping_set_id_backhaul_address: MappingSetIDBackhaulAddress
        """

        self._mapping_set_id_backhaul_address = mapping_set_id_backhaul_address

    @property
    def tce_mapping_info_list(self):
        """Gets the tce_mapping_info_list of this GnbCuCpFunctionSingleAllOfAttributes.


        :return: The tce_mapping_info_list of this GnbCuCpFunctionSingleAllOfAttributes.
        :rtype: List[TceMappingInfo]
        """
        return self._tce_mapping_info_list

    @tce_mapping_info_list.setter
    def tce_mapping_info_list(self, tce_mapping_info_list):
        """Sets the tce_mapping_info_list of this GnbCuCpFunctionSingleAllOfAttributes.


        :param tce_mapping_info_list: The tce_mapping_info_list of this GnbCuCpFunctionSingleAllOfAttributes.
        :type tce_mapping_info_list: List[TceMappingInfo]
        """

        self._tce_mapping_info_list = tce_mapping_info_list

    @property
    def configurable5_qi_set_ref(self):
        """Gets the configurable5_qi_set_ref of this GnbCuCpFunctionSingleAllOfAttributes.


        :return: The configurable5_qi_set_ref of this GnbCuCpFunctionSingleAllOfAttributes.
        :rtype: str
        """
        return self._configurable5_qi_set_ref

    @configurable5_qi_set_ref.setter
    def configurable5_qi_set_ref(self, configurable5_qi_set_ref):
        """Sets the configurable5_qi_set_ref of this GnbCuCpFunctionSingleAllOfAttributes.


        :param configurable5_qi_set_ref: The configurable5_qi_set_ref of this GnbCuCpFunctionSingleAllOfAttributes.
        :type configurable5_qi_set_ref: str
        """

        self._configurable5_qi_set_ref = configurable5_qi_set_ref

    @property
    def dynamic5_qi_set_ref(self):
        """Gets the dynamic5_qi_set_ref of this GnbCuCpFunctionSingleAllOfAttributes.


        :return: The dynamic5_qi_set_ref of this GnbCuCpFunctionSingleAllOfAttributes.
        :rtype: str
        """
        return self._dynamic5_qi_set_ref

    @dynamic5_qi_set_ref.setter
    def dynamic5_qi_set_ref(self, dynamic5_qi_set_ref):
        """Sets the dynamic5_qi_set_ref of this GnbCuCpFunctionSingleAllOfAttributes.


        :param dynamic5_qi_set_ref: The dynamic5_qi_set_ref of this GnbCuCpFunctionSingleAllOfAttributes.
        :type dynamic5_qi_set_ref: str
        """

        self._dynamic5_qi_set_ref = dynamic5_qi_set_ref

    @property
    def d_cho_control(self):
        """Gets the d_cho_control of this GnbCuCpFunctionSingleAllOfAttributes.


        :return: The d_cho_control of this GnbCuCpFunctionSingleAllOfAttributes.
        :rtype: bool
        """
        return self._d_cho_control

    @d_cho_control.setter
    def d_cho_control(self, d_cho_control):
        """Sets the d_cho_control of this GnbCuCpFunctionSingleAllOfAttributes.


        :param d_cho_control: The d_cho_control of this GnbCuCpFunctionSingleAllOfAttributes.
        :type d_cho_control: bool
        """

        self._d_cho_control = d_cho_control

    @property
    def d_dapsho_control(self):
        """Gets the d_dapsho_control of this GnbCuCpFunctionSingleAllOfAttributes.


        :return: The d_dapsho_control of this GnbCuCpFunctionSingleAllOfAttributes.
        :rtype: bool
        """
        return self._d_dapsho_control

    @d_dapsho_control.setter
    def d_dapsho_control(self, d_dapsho_control):
        """Sets the d_dapsho_control of this GnbCuCpFunctionSingleAllOfAttributes.


        :param d_dapsho_control: The d_dapsho_control of this GnbCuCpFunctionSingleAllOfAttributes.
        :type d_dapsho_control: bool
        """

        self._d_dapsho_control = d_dapsho_control