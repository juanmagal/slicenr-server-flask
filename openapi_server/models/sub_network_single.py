# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.alarm_list_single import AlarmListSingle
from openapi_server.models.cco_function_single import CCOFunctionSingle
from openapi_server.models.ces_management_function_single import CESManagementFunctionSingle
from openapi_server.models.cpci_configuration_function_single import CPCIConfigurationFunctionSingle
from openapi_server.models.configurable5_qi_set_single import Configurable5QISetSingle
from openapi_server.models.des_management_function_single import DESManagementFunctionSingle
from openapi_server.models.dlbo_function_single import DLBOFunctionSingle
from openapi_server.models.dmro_function_single import DMROFunctionSingle
from openapi_server.models.dpci_configuration_function_single import DPCIConfigurationFunctionSingle
from openapi_server.models.drach_optimization_function_single import DRACHOptimizationFunctionSingle
from openapi_server.models.dynamic5_qi_set_single import Dynamic5QISetSingle
from openapi_server.models.e_utran_frequency_single import EUtranFrequencySingle
from openapi_server.models.external_enb_function_single import ExternalENBFunctionSingle
from openapi_server.models.external_gnb_cu_cp_function_single import ExternalGnbCuCpFunctionSingle
from openapi_server.models.file_download_job_single import FileDownloadJobSingle
from openapi_server.models.files_single import FilesSingle
from openapi_server.models.managed_element_single import ManagedElementSingle
from openapi_server.models.management_data_collection_single import ManagementDataCollectionSingle
from openapi_server.models.management_node_single import ManagementNodeSingle
from openapi_server.models.me_context_single import MeContextSingle
from openapi_server.models.mns_agent_single import MnsAgentSingle
from openapi_server.models.mns_registry_single import MnsRegistrySingle
from openapi_server.models.nr_frequency_single import NRFrequencySingle
from openapi_server.models.ntf_subscription_control_single import NtfSubscriptionControlSingle
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle
from openapi_server.models.rim_rs_global_single import RimRSGlobalSingle
from openapi_server.models.sub_network_attr import SubNetworkAttr
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle
from openapi_server.models.trace_job_single import TraceJobSingle
from openapi_server.models.vs_data_container_single import VsDataContainerSingle
from openapi_server import util

from openapi_server.models.alarm_list_single import AlarmListSingle  # noqa: E501
from openapi_server.models.cco_function_single import CCOFunctionSingle  # noqa: E501
from openapi_server.models.ces_management_function_single import CESManagementFunctionSingle  # noqa: E501
from openapi_server.models.configurable5_qi_set_single import Configurable5QISetSingle  # noqa: E501
from openapi_server.models.cpci_configuration_function_single import CPCIConfigurationFunctionSingle  # noqa: E501
from openapi_server.models.des_management_function_single import DESManagementFunctionSingle  # noqa: E501
from openapi_server.models.dlbo_function_single import DLBOFunctionSingle  # noqa: E501
from openapi_server.models.dmro_function_single import DMROFunctionSingle  # noqa: E501
from openapi_server.models.dpci_configuration_function_single import DPCIConfigurationFunctionSingle  # noqa: E501
from openapi_server.models.drach_optimization_function_single import DRACHOptimizationFunctionSingle  # noqa: E501
from openapi_server.models.dynamic5_qi_set_single import Dynamic5QISetSingle  # noqa: E501
from openapi_server.models.e_utran_frequency_single import EUtranFrequencySingle  # noqa: E501
from openapi_server.models.external_enb_function_single import ExternalENBFunctionSingle  # noqa: E501
from openapi_server.models.external_gnb_cu_cp_function_single import ExternalGnbCuCpFunctionSingle  # noqa: E501
from openapi_server.models.file_download_job_single import FileDownloadJobSingle  # noqa: E501
from openapi_server.models.files_single import FilesSingle  # noqa: E501
from openapi_server.models.managed_element_single import ManagedElementSingle  # noqa: E501
from openapi_server.models.management_data_collection_single import ManagementDataCollectionSingle  # noqa: E501
from openapi_server.models.management_node_single import ManagementNodeSingle  # noqa: E501
from openapi_server.models.me_context_single import MeContextSingle  # noqa: E501
from openapi_server.models.mns_agent_single import MnsAgentSingle  # noqa: E501
from openapi_server.models.mns_registry_single import MnsRegistrySingle  # noqa: E501
from openapi_server.models.nr_frequency_single import NRFrequencySingle  # noqa: E501
from openapi_server.models.ntf_subscription_control_single import NtfSubscriptionControlSingle  # noqa: E501
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle  # noqa: E501
from openapi_server.models.rim_rs_global_single import RimRSGlobalSingle  # noqa: E501
from openapi_server.models.sub_network_attr import SubNetworkAttr  # noqa: E501
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle  # noqa: E501
from openapi_server.models.trace_job_single import TraceJobSingle  # noqa: E501
from openapi_server.models.vs_data_container_single import VsDataContainerSingle  # noqa: E501

class SubNetworkSingle(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, object_class=None, object_instance=None, vs_data_container=None, attributes=None, management_node=None, mns_agent=None, me_context=None, perf_metric_job=None, threshold_monitor=None, trace_job=None, management_data_collection=None, ntf_subscription_control=None, alarm_list=None, file_download_job=None, files=None, mns_registry=None, sub_network=None, managed_element=None, nr_frequency=None, external_gnb_cu_cp_function=None, external_enb_function=None, e_utran_frequency=None, des_management_function=None, drach_optimization_function=None, dmro_function=None, dlbo_function=None, dpci_configuration_function=None, cpci_configuration_function=None, ces_management_function=None, configurable5_qi_set=None, rim_rs_global=None, dynamic5_qi_set=None, cco_function=None):  # noqa: E501
        """SubNetworkSingle - a model defined in OpenAPI

        :param id: The id of this SubNetworkSingle.  # noqa: E501
        :type id: str
        :param object_class: The object_class of this SubNetworkSingle.  # noqa: E501
        :type object_class: str
        :param object_instance: The object_instance of this SubNetworkSingle.  # noqa: E501
        :type object_instance: str
        :param vs_data_container: The vs_data_container of this SubNetworkSingle.  # noqa: E501
        :type vs_data_container: List[VsDataContainerSingle]
        :param attributes: The attributes of this SubNetworkSingle.  # noqa: E501
        :type attributes: SubNetworkAttr
        :param management_node: The management_node of this SubNetworkSingle.  # noqa: E501
        :type management_node: List[ManagementNodeSingle]
        :param mns_agent: The mns_agent of this SubNetworkSingle.  # noqa: E501
        :type mns_agent: List[MnsAgentSingle]
        :param me_context: The me_context of this SubNetworkSingle.  # noqa: E501
        :type me_context: List[MeContextSingle]
        :param perf_metric_job: The perf_metric_job of this SubNetworkSingle.  # noqa: E501
        :type perf_metric_job: List[PerfMetricJobSingle]
        :param threshold_monitor: The threshold_monitor of this SubNetworkSingle.  # noqa: E501
        :type threshold_monitor: List[ThresholdMonitorSingle]
        :param trace_job: The trace_job of this SubNetworkSingle.  # noqa: E501
        :type trace_job: List[TraceJobSingle]
        :param management_data_collection: The management_data_collection of this SubNetworkSingle.  # noqa: E501
        :type management_data_collection: List[ManagementDataCollectionSingle]
        :param ntf_subscription_control: The ntf_subscription_control of this SubNetworkSingle.  # noqa: E501
        :type ntf_subscription_control: List[NtfSubscriptionControlSingle]
        :param alarm_list: The alarm_list of this SubNetworkSingle.  # noqa: E501
        :type alarm_list: AlarmListSingle
        :param file_download_job: The file_download_job of this SubNetworkSingle.  # noqa: E501
        :type file_download_job: List[FileDownloadJobSingle]
        :param files: The files of this SubNetworkSingle.  # noqa: E501
        :type files: List[FilesSingle]
        :param mns_registry: The mns_registry of this SubNetworkSingle.  # noqa: E501
        :type mns_registry: MnsRegistrySingle
        :param sub_network: The sub_network of this SubNetworkSingle.  # noqa: E501
        :type sub_network: List[SubNetworkSingle]
        :param managed_element: The managed_element of this SubNetworkSingle.  # noqa: E501
        :type managed_element: List[ManagedElementSingle]
        :param nr_frequency: The nr_frequency of this SubNetworkSingle.  # noqa: E501
        :type nr_frequency: List[NRFrequencySingle]
        :param external_gnb_cu_cp_function: The external_gnb_cu_cp_function of this SubNetworkSingle.  # noqa: E501
        :type external_gnb_cu_cp_function: List[ExternalGnbCuCpFunctionSingle]
        :param external_enb_function: The external_enb_function of this SubNetworkSingle.  # noqa: E501
        :type external_enb_function: List[ExternalENBFunctionSingle]
        :param e_utran_frequency: The e_utran_frequency of this SubNetworkSingle.  # noqa: E501
        :type e_utran_frequency: List[EUtranFrequencySingle]
        :param des_management_function: The des_management_function of this SubNetworkSingle.  # noqa: E501
        :type des_management_function: DESManagementFunctionSingle
        :param drach_optimization_function: The drach_optimization_function of this SubNetworkSingle.  # noqa: E501
        :type drach_optimization_function: DRACHOptimizationFunctionSingle
        :param dmro_function: The dmro_function of this SubNetworkSingle.  # noqa: E501
        :type dmro_function: DMROFunctionSingle
        :param dlbo_function: The dlbo_function of this SubNetworkSingle.  # noqa: E501
        :type dlbo_function: DLBOFunctionSingle
        :param dpci_configuration_function: The dpci_configuration_function of this SubNetworkSingle.  # noqa: E501
        :type dpci_configuration_function: DPCIConfigurationFunctionSingle
        :param cpci_configuration_function: The cpci_configuration_function of this SubNetworkSingle.  # noqa: E501
        :type cpci_configuration_function: CPCIConfigurationFunctionSingle
        :param ces_management_function: The ces_management_function of this SubNetworkSingle.  # noqa: E501
        :type ces_management_function: CESManagementFunctionSingle
        :param configurable5_qi_set: The configurable5_qi_set of this SubNetworkSingle.  # noqa: E501
        :type configurable5_qi_set: List[Configurable5QISetSingle]
        :param rim_rs_global: The rim_rs_global of this SubNetworkSingle.  # noqa: E501
        :type rim_rs_global: RimRSGlobalSingle
        :param dynamic5_qi_set: The dynamic5_qi_set of this SubNetworkSingle.  # noqa: E501
        :type dynamic5_qi_set: List[Dynamic5QISetSingle]
        :param cco_function: The cco_function of this SubNetworkSingle.  # noqa: E501
        :type cco_function: CCOFunctionSingle
        """
        self.openapi_types = {
            'id': str,
            'object_class': str,
            'object_instance': str,
            'vs_data_container': List[VsDataContainerSingle],
            'attributes': SubNetworkAttr,
            'management_node': List[ManagementNodeSingle],
            'mns_agent': List[MnsAgentSingle],
            'me_context': List[MeContextSingle],
            'perf_metric_job': List[PerfMetricJobSingle],
            'threshold_monitor': List[ThresholdMonitorSingle],
            'trace_job': List[TraceJobSingle],
            'management_data_collection': List[ManagementDataCollectionSingle],
            'ntf_subscription_control': List[NtfSubscriptionControlSingle],
            'alarm_list': AlarmListSingle,
            'file_download_job': List[FileDownloadJobSingle],
            'files': List[FilesSingle],
            'mns_registry': MnsRegistrySingle,
            'sub_network': List[SubNetworkSingle],
            'managed_element': List[ManagedElementSingle],
            'nr_frequency': List[NRFrequencySingle],
            'external_gnb_cu_cp_function': List[ExternalGnbCuCpFunctionSingle],
            'external_enb_function': List[ExternalENBFunctionSingle],
            'e_utran_frequency': List[EUtranFrequencySingle],
            'des_management_function': DESManagementFunctionSingle,
            'drach_optimization_function': DRACHOptimizationFunctionSingle,
            'dmro_function': DMROFunctionSingle,
            'dlbo_function': DLBOFunctionSingle,
            'dpci_configuration_function': DPCIConfigurationFunctionSingle,
            'cpci_configuration_function': CPCIConfigurationFunctionSingle,
            'ces_management_function': CESManagementFunctionSingle,
            'configurable5_qi_set': List[Configurable5QISetSingle],
            'rim_rs_global': RimRSGlobalSingle,
            'dynamic5_qi_set': List[Dynamic5QISetSingle],
            'cco_function': CCOFunctionSingle
        }

        self.attribute_map = {
            'id': 'id',
            'object_class': 'objectClass',
            'object_instance': 'objectInstance',
            'vs_data_container': 'VsDataContainer',
            'attributes': 'attributes',
            'management_node': 'ManagementNode',
            'mns_agent': 'MnsAgent',
            'me_context': 'MeContext',
            'perf_metric_job': 'PerfMetricJob',
            'threshold_monitor': 'ThresholdMonitor',
            'trace_job': 'TraceJob',
            'management_data_collection': 'ManagementDataCollection',
            'ntf_subscription_control': 'NtfSubscriptionControl',
            'alarm_list': 'AlarmList',
            'file_download_job': 'FileDownloadJob',
            'files': 'Files',
            'mns_registry': 'MnsRegistry',
            'sub_network': 'SubNetwork',
            'managed_element': 'ManagedElement',
            'nr_frequency': 'NRFrequency',
            'external_gnb_cu_cp_function': 'ExternalGnbCuCpFunction',
            'external_enb_function': 'ExternalENBFunction',
            'e_utran_frequency': 'EUtranFrequency',
            'des_management_function': 'DESManagementFunction',
            'drach_optimization_function': 'DRACHOptimizationFunction',
            'dmro_function': 'DMROFunction',
            'dlbo_function': 'DLBOFunction',
            'dpci_configuration_function': 'DPCIConfigurationFunction',
            'cpci_configuration_function': 'CPCIConfigurationFunction',
            'ces_management_function': 'CESManagementFunction',
            'configurable5_qi_set': 'Configurable5QISet',
            'rim_rs_global': 'RimRSGlobal',
            'dynamic5_qi_set': 'Dynamic5QISet',
            'cco_function': 'CCOFunction'
        }

        self._id = id
        self._object_class = object_class
        self._object_instance = object_instance
        self._vs_data_container = vs_data_container
        self._attributes = attributes
        self._management_node = management_node
        self._mns_agent = mns_agent
        self._me_context = me_context
        self._perf_metric_job = perf_metric_job
        self._threshold_monitor = threshold_monitor
        self._trace_job = trace_job
        self._management_data_collection = management_data_collection
        self._ntf_subscription_control = ntf_subscription_control
        self._alarm_list = alarm_list
        self._file_download_job = file_download_job
        self._files = files
        self._mns_registry = mns_registry
        self._sub_network = sub_network
        self._managed_element = managed_element
        self._nr_frequency = nr_frequency
        self._external_gnb_cu_cp_function = external_gnb_cu_cp_function
        self._external_enb_function = external_enb_function
        self._e_utran_frequency = e_utran_frequency
        self._des_management_function = des_management_function
        self._drach_optimization_function = drach_optimization_function
        self._dmro_function = dmro_function
        self._dlbo_function = dlbo_function
        self._dpci_configuration_function = dpci_configuration_function
        self._cpci_configuration_function = cpci_configuration_function
        self._ces_management_function = ces_management_function
        self._configurable5_qi_set = configurable5_qi_set
        self._rim_rs_global = rim_rs_global
        self._dynamic5_qi_set = dynamic5_qi_set
        self._cco_function = cco_function

    @classmethod
    def from_dict(cls, dikt) -> 'SubNetworkSingle':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SubNetwork-Single of this SubNetworkSingle.  # noqa: E501
        :rtype: SubNetworkSingle
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this SubNetworkSingle.


        :return: The id of this SubNetworkSingle.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubNetworkSingle.


        :param id: The id of this SubNetworkSingle.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def object_class(self):
        """Gets the object_class of this SubNetworkSingle.


        :return: The object_class of this SubNetworkSingle.
        :rtype: str
        """
        return self._object_class

    @object_class.setter
    def object_class(self, object_class):
        """Sets the object_class of this SubNetworkSingle.


        :param object_class: The object_class of this SubNetworkSingle.
        :type object_class: str
        """

        self._object_class = object_class

    @property
    def object_instance(self):
        """Gets the object_instance of this SubNetworkSingle.


        :return: The object_instance of this SubNetworkSingle.
        :rtype: str
        """
        return self._object_instance

    @object_instance.setter
    def object_instance(self, object_instance):
        """Sets the object_instance of this SubNetworkSingle.


        :param object_instance: The object_instance of this SubNetworkSingle.
        :type object_instance: str
        """

        self._object_instance = object_instance

    @property
    def vs_data_container(self):
        """Gets the vs_data_container of this SubNetworkSingle.


        :return: The vs_data_container of this SubNetworkSingle.
        :rtype: List[VsDataContainerSingle]
        """
        return self._vs_data_container

    @vs_data_container.setter
    def vs_data_container(self, vs_data_container):
        """Sets the vs_data_container of this SubNetworkSingle.


        :param vs_data_container: The vs_data_container of this SubNetworkSingle.
        :type vs_data_container: List[VsDataContainerSingle]
        """

        self._vs_data_container = vs_data_container

    @property
    def attributes(self):
        """Gets the attributes of this SubNetworkSingle.


        :return: The attributes of this SubNetworkSingle.
        :rtype: SubNetworkAttr
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this SubNetworkSingle.


        :param attributes: The attributes of this SubNetworkSingle.
        :type attributes: SubNetworkAttr
        """

        self._attributes = attributes

    @property
    def management_node(self):
        """Gets the management_node of this SubNetworkSingle.


        :return: The management_node of this SubNetworkSingle.
        :rtype: List[ManagementNodeSingle]
        """
        return self._management_node

    @management_node.setter
    def management_node(self, management_node):
        """Sets the management_node of this SubNetworkSingle.


        :param management_node: The management_node of this SubNetworkSingle.
        :type management_node: List[ManagementNodeSingle]
        """

        self._management_node = management_node

    @property
    def mns_agent(self):
        """Gets the mns_agent of this SubNetworkSingle.


        :return: The mns_agent of this SubNetworkSingle.
        :rtype: List[MnsAgentSingle]
        """
        return self._mns_agent

    @mns_agent.setter
    def mns_agent(self, mns_agent):
        """Sets the mns_agent of this SubNetworkSingle.


        :param mns_agent: The mns_agent of this SubNetworkSingle.
        :type mns_agent: List[MnsAgentSingle]
        """

        self._mns_agent = mns_agent

    @property
    def me_context(self):
        """Gets the me_context of this SubNetworkSingle.


        :return: The me_context of this SubNetworkSingle.
        :rtype: List[MeContextSingle]
        """
        return self._me_context

    @me_context.setter
    def me_context(self, me_context):
        """Sets the me_context of this SubNetworkSingle.


        :param me_context: The me_context of this SubNetworkSingle.
        :type me_context: List[MeContextSingle]
        """

        self._me_context = me_context

    @property
    def perf_metric_job(self):
        """Gets the perf_metric_job of this SubNetworkSingle.


        :return: The perf_metric_job of this SubNetworkSingle.
        :rtype: List[PerfMetricJobSingle]
        """
        return self._perf_metric_job

    @perf_metric_job.setter
    def perf_metric_job(self, perf_metric_job):
        """Sets the perf_metric_job of this SubNetworkSingle.


        :param perf_metric_job: The perf_metric_job of this SubNetworkSingle.
        :type perf_metric_job: List[PerfMetricJobSingle]
        """

        self._perf_metric_job = perf_metric_job

    @property
    def threshold_monitor(self):
        """Gets the threshold_monitor of this SubNetworkSingle.


        :return: The threshold_monitor of this SubNetworkSingle.
        :rtype: List[ThresholdMonitorSingle]
        """
        return self._threshold_monitor

    @threshold_monitor.setter
    def threshold_monitor(self, threshold_monitor):
        """Sets the threshold_monitor of this SubNetworkSingle.


        :param threshold_monitor: The threshold_monitor of this SubNetworkSingle.
        :type threshold_monitor: List[ThresholdMonitorSingle]
        """

        self._threshold_monitor = threshold_monitor

    @property
    def trace_job(self):
        """Gets the trace_job of this SubNetworkSingle.


        :return: The trace_job of this SubNetworkSingle.
        :rtype: List[TraceJobSingle]
        """
        return self._trace_job

    @trace_job.setter
    def trace_job(self, trace_job):
        """Sets the trace_job of this SubNetworkSingle.


        :param trace_job: The trace_job of this SubNetworkSingle.
        :type trace_job: List[TraceJobSingle]
        """

        self._trace_job = trace_job

    @property
    def management_data_collection(self):
        """Gets the management_data_collection of this SubNetworkSingle.


        :return: The management_data_collection of this SubNetworkSingle.
        :rtype: List[ManagementDataCollectionSingle]
        """
        return self._management_data_collection

    @management_data_collection.setter
    def management_data_collection(self, management_data_collection):
        """Sets the management_data_collection of this SubNetworkSingle.


        :param management_data_collection: The management_data_collection of this SubNetworkSingle.
        :type management_data_collection: List[ManagementDataCollectionSingle]
        """

        self._management_data_collection = management_data_collection

    @property
    def ntf_subscription_control(self):
        """Gets the ntf_subscription_control of this SubNetworkSingle.


        :return: The ntf_subscription_control of this SubNetworkSingle.
        :rtype: List[NtfSubscriptionControlSingle]
        """
        return self._ntf_subscription_control

    @ntf_subscription_control.setter
    def ntf_subscription_control(self, ntf_subscription_control):
        """Sets the ntf_subscription_control of this SubNetworkSingle.


        :param ntf_subscription_control: The ntf_subscription_control of this SubNetworkSingle.
        :type ntf_subscription_control: List[NtfSubscriptionControlSingle]
        """

        self._ntf_subscription_control = ntf_subscription_control

    @property
    def alarm_list(self):
        """Gets the alarm_list of this SubNetworkSingle.


        :return: The alarm_list of this SubNetworkSingle.
        :rtype: AlarmListSingle
        """
        return self._alarm_list

    @alarm_list.setter
    def alarm_list(self, alarm_list):
        """Sets the alarm_list of this SubNetworkSingle.


        :param alarm_list: The alarm_list of this SubNetworkSingle.
        :type alarm_list: AlarmListSingle
        """

        self._alarm_list = alarm_list

    @property
    def file_download_job(self):
        """Gets the file_download_job of this SubNetworkSingle.


        :return: The file_download_job of this SubNetworkSingle.
        :rtype: List[FileDownloadJobSingle]
        """
        return self._file_download_job

    @file_download_job.setter
    def file_download_job(self, file_download_job):
        """Sets the file_download_job of this SubNetworkSingle.


        :param file_download_job: The file_download_job of this SubNetworkSingle.
        :type file_download_job: List[FileDownloadJobSingle]
        """

        self._file_download_job = file_download_job

    @property
    def files(self):
        """Gets the files of this SubNetworkSingle.


        :return: The files of this SubNetworkSingle.
        :rtype: List[FilesSingle]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this SubNetworkSingle.


        :param files: The files of this SubNetworkSingle.
        :type files: List[FilesSingle]
        """

        self._files = files

    @property
    def mns_registry(self):
        """Gets the mns_registry of this SubNetworkSingle.


        :return: The mns_registry of this SubNetworkSingle.
        :rtype: MnsRegistrySingle
        """
        return self._mns_registry

    @mns_registry.setter
    def mns_registry(self, mns_registry):
        """Sets the mns_registry of this SubNetworkSingle.


        :param mns_registry: The mns_registry of this SubNetworkSingle.
        :type mns_registry: MnsRegistrySingle
        """

        self._mns_registry = mns_registry

    @property
    def sub_network(self):
        """Gets the sub_network of this SubNetworkSingle.


        :return: The sub_network of this SubNetworkSingle.
        :rtype: List[SubNetworkSingle]
        """
        return self._sub_network

    @sub_network.setter
    def sub_network(self, sub_network):
        """Sets the sub_network of this SubNetworkSingle.


        :param sub_network: The sub_network of this SubNetworkSingle.
        :type sub_network: List[SubNetworkSingle]
        """

        self._sub_network = sub_network

    @property
    def managed_element(self):
        """Gets the managed_element of this SubNetworkSingle.


        :return: The managed_element of this SubNetworkSingle.
        :rtype: List[ManagedElementSingle]
        """
        return self._managed_element

    @managed_element.setter
    def managed_element(self, managed_element):
        """Sets the managed_element of this SubNetworkSingle.


        :param managed_element: The managed_element of this SubNetworkSingle.
        :type managed_element: List[ManagedElementSingle]
        """

        self._managed_element = managed_element

    @property
    def nr_frequency(self):
        """Gets the nr_frequency of this SubNetworkSingle.


        :return: The nr_frequency of this SubNetworkSingle.
        :rtype: List[NRFrequencySingle]
        """
        return self._nr_frequency

    @nr_frequency.setter
    def nr_frequency(self, nr_frequency):
        """Sets the nr_frequency of this SubNetworkSingle.


        :param nr_frequency: The nr_frequency of this SubNetworkSingle.
        :type nr_frequency: List[NRFrequencySingle]
        """
        if nr_frequency is not None and len(nr_frequency) < 1:
            raise ValueError("Invalid value for `nr_frequency`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._nr_frequency = nr_frequency

    @property
    def external_gnb_cu_cp_function(self):
        """Gets the external_gnb_cu_cp_function of this SubNetworkSingle.


        :return: The external_gnb_cu_cp_function of this SubNetworkSingle.
        :rtype: List[ExternalGnbCuCpFunctionSingle]
        """
        return self._external_gnb_cu_cp_function

    @external_gnb_cu_cp_function.setter
    def external_gnb_cu_cp_function(self, external_gnb_cu_cp_function):
        """Sets the external_gnb_cu_cp_function of this SubNetworkSingle.


        :param external_gnb_cu_cp_function: The external_gnb_cu_cp_function of this SubNetworkSingle.
        :type external_gnb_cu_cp_function: List[ExternalGnbCuCpFunctionSingle]
        """

        self._external_gnb_cu_cp_function = external_gnb_cu_cp_function

    @property
    def external_enb_function(self):
        """Gets the external_enb_function of this SubNetworkSingle.


        :return: The external_enb_function of this SubNetworkSingle.
        :rtype: List[ExternalENBFunctionSingle]
        """
        return self._external_enb_function

    @external_enb_function.setter
    def external_enb_function(self, external_enb_function):
        """Sets the external_enb_function of this SubNetworkSingle.


        :param external_enb_function: The external_enb_function of this SubNetworkSingle.
        :type external_enb_function: List[ExternalENBFunctionSingle]
        """

        self._external_enb_function = external_enb_function

    @property
    def e_utran_frequency(self):
        """Gets the e_utran_frequency of this SubNetworkSingle.


        :return: The e_utran_frequency of this SubNetworkSingle.
        :rtype: List[EUtranFrequencySingle]
        """
        return self._e_utran_frequency

    @e_utran_frequency.setter
    def e_utran_frequency(self, e_utran_frequency):
        """Sets the e_utran_frequency of this SubNetworkSingle.


        :param e_utran_frequency: The e_utran_frequency of this SubNetworkSingle.
        :type e_utran_frequency: List[EUtranFrequencySingle]
        """
        if e_utran_frequency is not None and len(e_utran_frequency) < 1:
            raise ValueError("Invalid value for `e_utran_frequency`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._e_utran_frequency = e_utran_frequency

    @property
    def des_management_function(self):
        """Gets the des_management_function of this SubNetworkSingle.


        :return: The des_management_function of this SubNetworkSingle.
        :rtype: DESManagementFunctionSingle
        """
        return self._des_management_function

    @des_management_function.setter
    def des_management_function(self, des_management_function):
        """Sets the des_management_function of this SubNetworkSingle.


        :param des_management_function: The des_management_function of this SubNetworkSingle.
        :type des_management_function: DESManagementFunctionSingle
        """

        self._des_management_function = des_management_function

    @property
    def drach_optimization_function(self):
        """Gets the drach_optimization_function of this SubNetworkSingle.


        :return: The drach_optimization_function of this SubNetworkSingle.
        :rtype: DRACHOptimizationFunctionSingle
        """
        return self._drach_optimization_function

    @drach_optimization_function.setter
    def drach_optimization_function(self, drach_optimization_function):
        """Sets the drach_optimization_function of this SubNetworkSingle.


        :param drach_optimization_function: The drach_optimization_function of this SubNetworkSingle.
        :type drach_optimization_function: DRACHOptimizationFunctionSingle
        """

        self._drach_optimization_function = drach_optimization_function

    @property
    def dmro_function(self):
        """Gets the dmro_function of this SubNetworkSingle.


        :return: The dmro_function of this SubNetworkSingle.
        :rtype: DMROFunctionSingle
        """
        return self._dmro_function

    @dmro_function.setter
    def dmro_function(self, dmro_function):
        """Sets the dmro_function of this SubNetworkSingle.


        :param dmro_function: The dmro_function of this SubNetworkSingle.
        :type dmro_function: DMROFunctionSingle
        """

        self._dmro_function = dmro_function

    @property
    def dlbo_function(self):
        """Gets the dlbo_function of this SubNetworkSingle.


        :return: The dlbo_function of this SubNetworkSingle.
        :rtype: DLBOFunctionSingle
        """
        return self._dlbo_function

    @dlbo_function.setter
    def dlbo_function(self, dlbo_function):
        """Sets the dlbo_function of this SubNetworkSingle.


        :param dlbo_function: The dlbo_function of this SubNetworkSingle.
        :type dlbo_function: DLBOFunctionSingle
        """

        self._dlbo_function = dlbo_function

    @property
    def dpci_configuration_function(self):
        """Gets the dpci_configuration_function of this SubNetworkSingle.


        :return: The dpci_configuration_function of this SubNetworkSingle.
        :rtype: DPCIConfigurationFunctionSingle
        """
        return self._dpci_configuration_function

    @dpci_configuration_function.setter
    def dpci_configuration_function(self, dpci_configuration_function):
        """Sets the dpci_configuration_function of this SubNetworkSingle.


        :param dpci_configuration_function: The dpci_configuration_function of this SubNetworkSingle.
        :type dpci_configuration_function: DPCIConfigurationFunctionSingle
        """

        self._dpci_configuration_function = dpci_configuration_function

    @property
    def cpci_configuration_function(self):
        """Gets the cpci_configuration_function of this SubNetworkSingle.


        :return: The cpci_configuration_function of this SubNetworkSingle.
        :rtype: CPCIConfigurationFunctionSingle
        """
        return self._cpci_configuration_function

    @cpci_configuration_function.setter
    def cpci_configuration_function(self, cpci_configuration_function):
        """Sets the cpci_configuration_function of this SubNetworkSingle.


        :param cpci_configuration_function: The cpci_configuration_function of this SubNetworkSingle.
        :type cpci_configuration_function: CPCIConfigurationFunctionSingle
        """

        self._cpci_configuration_function = cpci_configuration_function

    @property
    def ces_management_function(self):
        """Gets the ces_management_function of this SubNetworkSingle.


        :return: The ces_management_function of this SubNetworkSingle.
        :rtype: CESManagementFunctionSingle
        """
        return self._ces_management_function

    @ces_management_function.setter
    def ces_management_function(self, ces_management_function):
        """Sets the ces_management_function of this SubNetworkSingle.


        :param ces_management_function: The ces_management_function of this SubNetworkSingle.
        :type ces_management_function: CESManagementFunctionSingle
        """

        self._ces_management_function = ces_management_function

    @property
    def configurable5_qi_set(self):
        """Gets the configurable5_qi_set of this SubNetworkSingle.


        :return: The configurable5_qi_set of this SubNetworkSingle.
        :rtype: List[Configurable5QISetSingle]
        """
        return self._configurable5_qi_set

    @configurable5_qi_set.setter
    def configurable5_qi_set(self, configurable5_qi_set):
        """Sets the configurable5_qi_set of this SubNetworkSingle.


        :param configurable5_qi_set: The configurable5_qi_set of this SubNetworkSingle.
        :type configurable5_qi_set: List[Configurable5QISetSingle]
        """

        self._configurable5_qi_set = configurable5_qi_set

    @property
    def rim_rs_global(self):
        """Gets the rim_rs_global of this SubNetworkSingle.


        :return: The rim_rs_global of this SubNetworkSingle.
        :rtype: RimRSGlobalSingle
        """
        return self._rim_rs_global

    @rim_rs_global.setter
    def rim_rs_global(self, rim_rs_global):
        """Sets the rim_rs_global of this SubNetworkSingle.


        :param rim_rs_global: The rim_rs_global of this SubNetworkSingle.
        :type rim_rs_global: RimRSGlobalSingle
        """

        self._rim_rs_global = rim_rs_global

    @property
    def dynamic5_qi_set(self):
        """Gets the dynamic5_qi_set of this SubNetworkSingle.


        :return: The dynamic5_qi_set of this SubNetworkSingle.
        :rtype: List[Dynamic5QISetSingle]
        """
        return self._dynamic5_qi_set

    @dynamic5_qi_set.setter
    def dynamic5_qi_set(self, dynamic5_qi_set):
        """Sets the dynamic5_qi_set of this SubNetworkSingle.


        :param dynamic5_qi_set: The dynamic5_qi_set of this SubNetworkSingle.
        :type dynamic5_qi_set: List[Dynamic5QISetSingle]
        """

        self._dynamic5_qi_set = dynamic5_qi_set

    @property
    def cco_function(self):
        """Gets the cco_function of this SubNetworkSingle.


        :return: The cco_function of this SubNetworkSingle.
        :rtype: CCOFunctionSingle
        """
        return self._cco_function

    @cco_function.setter
    def cco_function(self, cco_function):
        """Sets the cco_function of this SubNetworkSingle.


        :param cco_function: The cco_function of this SubNetworkSingle.
        :type cco_function: CCOFunctionSingle
        """

        self._cco_function = cco_function
