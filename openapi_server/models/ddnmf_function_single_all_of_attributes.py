# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.comm_model import CommModel
from openapi_server.models.managed_nf_profile import ManagedNFProfile
from openapi_server.models.pee_parameter import PeeParameter
from openapi_server.models.plmn_id import PlmnId
from openapi_server.models.supported_perf_metric_group import SupportedPerfMetricGroup
from openapi_server.models.vnf_parameter import VnfParameter
from openapi_server import util

from openapi_server.models.comm_model import CommModel  # noqa: E501
from openapi_server.models.managed_nf_profile import ManagedNFProfile  # noqa: E501
from openapi_server.models.pee_parameter import PeeParameter  # noqa: E501
from openapi_server.models.plmn_id import PlmnId  # noqa: E501
from openapi_server.models.supported_perf_metric_group import SupportedPerfMetricGroup  # noqa: E501
from openapi_server.models.vnf_parameter import VnfParameter  # noqa: E501

class DDNMFFunctionSingleAllOfAttributes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, user_label=None, vnf_parameters_list=None, pee_parameters_list=None, priority_label=None, supported_perf_metric_groups=None, supported_trace_metrics=None, plmn_id=None, s_bi_fqdn=None, managed_nf_profile=None, comm_model_list=None):  # noqa: E501
        """DDNMFFunctionSingleAllOfAttributes - a model defined in OpenAPI

        :param user_label: The user_label of this DDNMFFunctionSingleAllOfAttributes.  # noqa: E501
        :type user_label: str
        :param vnf_parameters_list: The vnf_parameters_list of this DDNMFFunctionSingleAllOfAttributes.  # noqa: E501
        :type vnf_parameters_list: List[VnfParameter]
        :param pee_parameters_list: The pee_parameters_list of this DDNMFFunctionSingleAllOfAttributes.  # noqa: E501
        :type pee_parameters_list: List[PeeParameter]
        :param priority_label: The priority_label of this DDNMFFunctionSingleAllOfAttributes.  # noqa: E501
        :type priority_label: int
        :param supported_perf_metric_groups: The supported_perf_metric_groups of this DDNMFFunctionSingleAllOfAttributes.  # noqa: E501
        :type supported_perf_metric_groups: List[SupportedPerfMetricGroup]
        :param supported_trace_metrics: The supported_trace_metrics of this DDNMFFunctionSingleAllOfAttributes.  # noqa: E501
        :type supported_trace_metrics: List[str]
        :param plmn_id: The plmn_id of this DDNMFFunctionSingleAllOfAttributes.  # noqa: E501
        :type plmn_id: PlmnId
        :param s_bi_fqdn: The s_bi_fqdn of this DDNMFFunctionSingleAllOfAttributes.  # noqa: E501
        :type s_bi_fqdn: str
        :param managed_nf_profile: The managed_nf_profile of this DDNMFFunctionSingleAllOfAttributes.  # noqa: E501
        :type managed_nf_profile: ManagedNFProfile
        :param comm_model_list: The comm_model_list of this DDNMFFunctionSingleAllOfAttributes.  # noqa: E501
        :type comm_model_list: List[CommModel]
        """
        self.openapi_types = {
            'user_label': str,
            'vnf_parameters_list': List[VnfParameter],
            'pee_parameters_list': List[PeeParameter],
            'priority_label': int,
            'supported_perf_metric_groups': List[SupportedPerfMetricGroup],
            'supported_trace_metrics': List[str],
            'plmn_id': PlmnId,
            's_bi_fqdn': str,
            'managed_nf_profile': ManagedNFProfile,
            'comm_model_list': List[CommModel]
        }

        self.attribute_map = {
            'user_label': 'userLabel',
            'vnf_parameters_list': 'vnfParametersList',
            'pee_parameters_list': 'peeParametersList',
            'priority_label': 'priorityLabel',
            'supported_perf_metric_groups': 'supportedPerfMetricGroups',
            'supported_trace_metrics': 'supportedTraceMetrics',
            'plmn_id': 'plmnId',
            's_bi_fqdn': 'sBIFqdn',
            'managed_nf_profile': 'managedNFProfile',
            'comm_model_list': 'commModelList'
        }

        self._user_label = user_label
        self._vnf_parameters_list = vnf_parameters_list
        self._pee_parameters_list = pee_parameters_list
        self._priority_label = priority_label
        self._supported_perf_metric_groups = supported_perf_metric_groups
        self._supported_trace_metrics = supported_trace_metrics
        self._plmn_id = plmn_id
        self._s_bi_fqdn = s_bi_fqdn
        self._managed_nf_profile = managed_nf_profile
        self._comm_model_list = comm_model_list

    @classmethod
    def from_dict(cls, dikt) -> 'DDNMFFunctionSingleAllOfAttributes':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DDNMFFunction_Single_allOf_attributes of this DDNMFFunctionSingleAllOfAttributes.  # noqa: E501
        :rtype: DDNMFFunctionSingleAllOfAttributes
        """
        return util.deserialize_model(dikt, cls)

    @property
    def user_label(self):
        """Gets the user_label of this DDNMFFunctionSingleAllOfAttributes.


        :return: The user_label of this DDNMFFunctionSingleAllOfAttributes.
        :rtype: str
        """
        return self._user_label

    @user_label.setter
    def user_label(self, user_label):
        """Sets the user_label of this DDNMFFunctionSingleAllOfAttributes.


        :param user_label: The user_label of this DDNMFFunctionSingleAllOfAttributes.
        :type user_label: str
        """

        self._user_label = user_label

    @property
    def vnf_parameters_list(self):
        """Gets the vnf_parameters_list of this DDNMFFunctionSingleAllOfAttributes.


        :return: The vnf_parameters_list of this DDNMFFunctionSingleAllOfAttributes.
        :rtype: List[VnfParameter]
        """
        return self._vnf_parameters_list

    @vnf_parameters_list.setter
    def vnf_parameters_list(self, vnf_parameters_list):
        """Sets the vnf_parameters_list of this DDNMFFunctionSingleAllOfAttributes.


        :param vnf_parameters_list: The vnf_parameters_list of this DDNMFFunctionSingleAllOfAttributes.
        :type vnf_parameters_list: List[VnfParameter]
        """

        self._vnf_parameters_list = vnf_parameters_list

    @property
    def pee_parameters_list(self):
        """Gets the pee_parameters_list of this DDNMFFunctionSingleAllOfAttributes.


        :return: The pee_parameters_list of this DDNMFFunctionSingleAllOfAttributes.
        :rtype: List[PeeParameter]
        """
        return self._pee_parameters_list

    @pee_parameters_list.setter
    def pee_parameters_list(self, pee_parameters_list):
        """Sets the pee_parameters_list of this DDNMFFunctionSingleAllOfAttributes.


        :param pee_parameters_list: The pee_parameters_list of this DDNMFFunctionSingleAllOfAttributes.
        :type pee_parameters_list: List[PeeParameter]
        """

        self._pee_parameters_list = pee_parameters_list

    @property
    def priority_label(self):
        """Gets the priority_label of this DDNMFFunctionSingleAllOfAttributes.


        :return: The priority_label of this DDNMFFunctionSingleAllOfAttributes.
        :rtype: int
        """
        return self._priority_label

    @priority_label.setter
    def priority_label(self, priority_label):
        """Sets the priority_label of this DDNMFFunctionSingleAllOfAttributes.


        :param priority_label: The priority_label of this DDNMFFunctionSingleAllOfAttributes.
        :type priority_label: int
        """

        self._priority_label = priority_label

    @property
    def supported_perf_metric_groups(self):
        """Gets the supported_perf_metric_groups of this DDNMFFunctionSingleAllOfAttributes.


        :return: The supported_perf_metric_groups of this DDNMFFunctionSingleAllOfAttributes.
        :rtype: List[SupportedPerfMetricGroup]
        """
        return self._supported_perf_metric_groups

    @supported_perf_metric_groups.setter
    def supported_perf_metric_groups(self, supported_perf_metric_groups):
        """Sets the supported_perf_metric_groups of this DDNMFFunctionSingleAllOfAttributes.


        :param supported_perf_metric_groups: The supported_perf_metric_groups of this DDNMFFunctionSingleAllOfAttributes.
        :type supported_perf_metric_groups: List[SupportedPerfMetricGroup]
        """

        self._supported_perf_metric_groups = supported_perf_metric_groups

    @property
    def supported_trace_metrics(self):
        """Gets the supported_trace_metrics of this DDNMFFunctionSingleAllOfAttributes.


        :return: The supported_trace_metrics of this DDNMFFunctionSingleAllOfAttributes.
        :rtype: List[str]
        """
        return self._supported_trace_metrics

    @supported_trace_metrics.setter
    def supported_trace_metrics(self, supported_trace_metrics):
        """Sets the supported_trace_metrics of this DDNMFFunctionSingleAllOfAttributes.


        :param supported_trace_metrics: The supported_trace_metrics of this DDNMFFunctionSingleAllOfAttributes.
        :type supported_trace_metrics: List[str]
        """

        self._supported_trace_metrics = supported_trace_metrics

    @property
    def plmn_id(self):
        """Gets the plmn_id of this DDNMFFunctionSingleAllOfAttributes.


        :return: The plmn_id of this DDNMFFunctionSingleAllOfAttributes.
        :rtype: PlmnId
        """
        return self._plmn_id

    @plmn_id.setter
    def plmn_id(self, plmn_id):
        """Sets the plmn_id of this DDNMFFunctionSingleAllOfAttributes.


        :param plmn_id: The plmn_id of this DDNMFFunctionSingleAllOfAttributes.
        :type plmn_id: PlmnId
        """

        self._plmn_id = plmn_id

    @property
    def s_bi_fqdn(self):
        """Gets the s_bi_fqdn of this DDNMFFunctionSingleAllOfAttributes.


        :return: The s_bi_fqdn of this DDNMFFunctionSingleAllOfAttributes.
        :rtype: str
        """
        return self._s_bi_fqdn

    @s_bi_fqdn.setter
    def s_bi_fqdn(self, s_bi_fqdn):
        """Sets the s_bi_fqdn of this DDNMFFunctionSingleAllOfAttributes.


        :param s_bi_fqdn: The s_bi_fqdn of this DDNMFFunctionSingleAllOfAttributes.
        :type s_bi_fqdn: str
        """

        self._s_bi_fqdn = s_bi_fqdn

    @property
    def managed_nf_profile(self):
        """Gets the managed_nf_profile of this DDNMFFunctionSingleAllOfAttributes.


        :return: The managed_nf_profile of this DDNMFFunctionSingleAllOfAttributes.
        :rtype: ManagedNFProfile
        """
        return self._managed_nf_profile

    @managed_nf_profile.setter
    def managed_nf_profile(self, managed_nf_profile):
        """Sets the managed_nf_profile of this DDNMFFunctionSingleAllOfAttributes.


        :param managed_nf_profile: The managed_nf_profile of this DDNMFFunctionSingleAllOfAttributes.
        :type managed_nf_profile: ManagedNFProfile
        """

        self._managed_nf_profile = managed_nf_profile

    @property
    def comm_model_list(self):
        """Gets the comm_model_list of this DDNMFFunctionSingleAllOfAttributes.


        :return: The comm_model_list of this DDNMFFunctionSingleAllOfAttributes.
        :rtype: List[CommModel]
        """
        return self._comm_model_list

    @comm_model_list.setter
    def comm_model_list(self, comm_model_list):
        """Sets the comm_model_list of this DDNMFFunctionSingleAllOfAttributes.


        :param comm_model_list: The comm_model_list of this DDNMFFunctionSingleAllOfAttributes.
        :type comm_model_list: List[CommModel]
        """

        self._comm_model_list = comm_model_list
