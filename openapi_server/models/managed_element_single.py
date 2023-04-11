# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.alarm_list_single import AlarmListSingle
from openapi_server.models.ces_management_function_single import CESManagementFunctionSingle
from openapi_server.models.cpci_configuration_function_single import CPCIConfigurationFunctionSingle
from openapi_server.models.configurable5_qi_set_single import Configurable5QISetSingle
from openapi_server.models.des_management_function_single import DESManagementFunctionSingle
from openapi_server.models.dlbo_function_single import DLBOFunctionSingle
from openapi_server.models.dmro_function_single import DMROFunctionSingle
from openapi_server.models.dpci_configuration_function_single import DPCIConfigurationFunctionSingle
from openapi_server.models.drach_optimization_function_single import DRACHOptimizationFunctionSingle
from openapi_server.models.dynamic5_qi_set_single import Dynamic5QISetSingle
from openapi_server.models.file_download_job_single import FileDownloadJobSingle
from openapi_server.models.files_single import FilesSingle
from openapi_server.models.gnb_cu_cp_function_single import GnbCuCpFunctionSingle
from openapi_server.models.gnb_cu_up_function_single import GnbCuUpFunctionSingle
from openapi_server.models.gnb_du_function_single import GnbDuFunctionSingle
from openapi_server.models.managed_element_attr import ManagedElementAttr
from openapi_server.models.mns_agent_single import MnsAgentSingle
from openapi_server.models.ntf_subscription_control_single import NtfSubscriptionControlSingle
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle
from openapi_server.models.trace_job_single import TraceJobSingle
from openapi_server.models.vs_data_container_single import VsDataContainerSingle
from openapi_server import util

from openapi_server.models.alarm_list_single import AlarmListSingle  # noqa: E501
from openapi_server.models.ces_management_function_single import CESManagementFunctionSingle  # noqa: E501
from openapi_server.models.configurable5_qi_set_single import Configurable5QISetSingle  # noqa: E501
from openapi_server.models.cpci_configuration_function_single import CPCIConfigurationFunctionSingle  # noqa: E501
from openapi_server.models.des_management_function_single import DESManagementFunctionSingle  # noqa: E501
from openapi_server.models.dlbo_function_single import DLBOFunctionSingle  # noqa: E501
from openapi_server.models.dmro_function_single import DMROFunctionSingle  # noqa: E501
from openapi_server.models.dpci_configuration_function_single import DPCIConfigurationFunctionSingle  # noqa: E501
from openapi_server.models.drach_optimization_function_single import DRACHOptimizationFunctionSingle  # noqa: E501
from openapi_server.models.dynamic5_qi_set_single import Dynamic5QISetSingle  # noqa: E501
from openapi_server.models.file_download_job_single import FileDownloadJobSingle  # noqa: E501
from openapi_server.models.files_single import FilesSingle  # noqa: E501
from openapi_server.models.gnb_cu_cp_function_single import GnbCuCpFunctionSingle  # noqa: E501
from openapi_server.models.gnb_cu_up_function_single import GnbCuUpFunctionSingle  # noqa: E501
from openapi_server.models.gnb_du_function_single import GnbDuFunctionSingle  # noqa: E501
from openapi_server.models.managed_element_attr import ManagedElementAttr  # noqa: E501
from openapi_server.models.mns_agent_single import MnsAgentSingle  # noqa: E501
from openapi_server.models.ntf_subscription_control_single import NtfSubscriptionControlSingle  # noqa: E501
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle  # noqa: E501
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle  # noqa: E501
from openapi_server.models.trace_job_single import TraceJobSingle  # noqa: E501
from openapi_server.models.vs_data_container_single import VsDataContainerSingle  # noqa: E501

class ManagedElementSingle(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, object_class=None, object_instance=None, vs_data_container=None, attributes=None, mns_agent=None, perf_metric_job=None, threshold_monitor=None, trace_job=None, ntf_subscription_control=None, alarm_list=None, file_download_job=None, files=None, gnb_du_function=None, gnb_cu_up_function=None, gnb_cu_cp_function=None, des_management_function=None, drach_optimization_function=None, dmro_function=None, dlbo_function=None, dpci_configuration_function=None, cpci_configuration_function=None, ces_management_function=None, configurable5_qi_set=None, dynamic5_qi_set=None):  # noqa: E501
        """ManagedElementSingle - a model defined in OpenAPI

        :param id: The id of this ManagedElementSingle.  # noqa: E501
        :type id: str
        :param object_class: The object_class of this ManagedElementSingle.  # noqa: E501
        :type object_class: str
        :param object_instance: The object_instance of this ManagedElementSingle.  # noqa: E501
        :type object_instance: str
        :param vs_data_container: The vs_data_container of this ManagedElementSingle.  # noqa: E501
        :type vs_data_container: List[VsDataContainerSingle]
        :param attributes: The attributes of this ManagedElementSingle.  # noqa: E501
        :type attributes: ManagedElementAttr
        :param mns_agent: The mns_agent of this ManagedElementSingle.  # noqa: E501
        :type mns_agent: List[MnsAgentSingle]
        :param perf_metric_job: The perf_metric_job of this ManagedElementSingle.  # noqa: E501
        :type perf_metric_job: List[PerfMetricJobSingle]
        :param threshold_monitor: The threshold_monitor of this ManagedElementSingle.  # noqa: E501
        :type threshold_monitor: List[ThresholdMonitorSingle]
        :param trace_job: The trace_job of this ManagedElementSingle.  # noqa: E501
        :type trace_job: List[TraceJobSingle]
        :param ntf_subscription_control: The ntf_subscription_control of this ManagedElementSingle.  # noqa: E501
        :type ntf_subscription_control: List[NtfSubscriptionControlSingle]
        :param alarm_list: The alarm_list of this ManagedElementSingle.  # noqa: E501
        :type alarm_list: AlarmListSingle
        :param file_download_job: The file_download_job of this ManagedElementSingle.  # noqa: E501
        :type file_download_job: List[FileDownloadJobSingle]
        :param files: The files of this ManagedElementSingle.  # noqa: E501
        :type files: List[FilesSingle]
        :param gnb_du_function: The gnb_du_function of this ManagedElementSingle.  # noqa: E501
        :type gnb_du_function: List[GnbDuFunctionSingle]
        :param gnb_cu_up_function: The gnb_cu_up_function of this ManagedElementSingle.  # noqa: E501
        :type gnb_cu_up_function: List[GnbCuUpFunctionSingle]
        :param gnb_cu_cp_function: The gnb_cu_cp_function of this ManagedElementSingle.  # noqa: E501
        :type gnb_cu_cp_function: List[GnbCuCpFunctionSingle]
        :param des_management_function: The des_management_function of this ManagedElementSingle.  # noqa: E501
        :type des_management_function: DESManagementFunctionSingle
        :param drach_optimization_function: The drach_optimization_function of this ManagedElementSingle.  # noqa: E501
        :type drach_optimization_function: DRACHOptimizationFunctionSingle
        :param dmro_function: The dmro_function of this ManagedElementSingle.  # noqa: E501
        :type dmro_function: DMROFunctionSingle
        :param dlbo_function: The dlbo_function of this ManagedElementSingle.  # noqa: E501
        :type dlbo_function: DLBOFunctionSingle
        :param dpci_configuration_function: The dpci_configuration_function of this ManagedElementSingle.  # noqa: E501
        :type dpci_configuration_function: DPCIConfigurationFunctionSingle
        :param cpci_configuration_function: The cpci_configuration_function of this ManagedElementSingle.  # noqa: E501
        :type cpci_configuration_function: CPCIConfigurationFunctionSingle
        :param ces_management_function: The ces_management_function of this ManagedElementSingle.  # noqa: E501
        :type ces_management_function: CESManagementFunctionSingle
        :param configurable5_qi_set: The configurable5_qi_set of this ManagedElementSingle.  # noqa: E501
        :type configurable5_qi_set: List[Configurable5QISetSingle]
        :param dynamic5_qi_set: The dynamic5_qi_set of this ManagedElementSingle.  # noqa: E501
        :type dynamic5_qi_set: List[Dynamic5QISetSingle]
        """
        self.openapi_types = {
            'id': str,
            'object_class': str,
            'object_instance': str,
            'vs_data_container': List[VsDataContainerSingle],
            'attributes': ManagedElementAttr,
            'mns_agent': List[MnsAgentSingle],
            'perf_metric_job': List[PerfMetricJobSingle],
            'threshold_monitor': List[ThresholdMonitorSingle],
            'trace_job': List[TraceJobSingle],
            'ntf_subscription_control': List[NtfSubscriptionControlSingle],
            'alarm_list': AlarmListSingle,
            'file_download_job': List[FileDownloadJobSingle],
            'files': List[FilesSingle],
            'gnb_du_function': List[GnbDuFunctionSingle],
            'gnb_cu_up_function': List[GnbCuUpFunctionSingle],
            'gnb_cu_cp_function': List[GnbCuCpFunctionSingle],
            'des_management_function': DESManagementFunctionSingle,
            'drach_optimization_function': DRACHOptimizationFunctionSingle,
            'dmro_function': DMROFunctionSingle,
            'dlbo_function': DLBOFunctionSingle,
            'dpci_configuration_function': DPCIConfigurationFunctionSingle,
            'cpci_configuration_function': CPCIConfigurationFunctionSingle,
            'ces_management_function': CESManagementFunctionSingle,
            'configurable5_qi_set': List[Configurable5QISetSingle],
            'dynamic5_qi_set': List[Dynamic5QISetSingle]
        }

        self.attribute_map = {
            'id': 'id',
            'object_class': 'objectClass',
            'object_instance': 'objectInstance',
            'vs_data_container': 'VsDataContainer',
            'attributes': 'attributes',
            'mns_agent': 'MnsAgent',
            'perf_metric_job': 'PerfMetricJob',
            'threshold_monitor': 'ThresholdMonitor',
            'trace_job': 'TraceJob',
            'ntf_subscription_control': 'NtfSubscriptionControl',
            'alarm_list': 'AlarmList',
            'file_download_job': 'FileDownloadJob',
            'files': 'Files',
            'gnb_du_function': 'GnbDuFunction',
            'gnb_cu_up_function': 'GnbCuUpFunction',
            'gnb_cu_cp_function': 'GnbCuCpFunction',
            'des_management_function': 'DESManagementFunction',
            'drach_optimization_function': 'DRACHOptimizationFunction',
            'dmro_function': 'DMROFunction',
            'dlbo_function': 'DLBOFunction',
            'dpci_configuration_function': 'DPCIConfigurationFunction',
            'cpci_configuration_function': 'CPCIConfigurationFunction',
            'ces_management_function': 'CESManagementFunction',
            'configurable5_qi_set': 'Configurable5QISet',
            'dynamic5_qi_set': 'Dynamic5QISet'
        }

        self._id = id
        self._object_class = object_class
        self._object_instance = object_instance
        self._vs_data_container = vs_data_container
        self._attributes = attributes
        self._mns_agent = mns_agent
        self._perf_metric_job = perf_metric_job
        self._threshold_monitor = threshold_monitor
        self._trace_job = trace_job
        self._ntf_subscription_control = ntf_subscription_control
        self._alarm_list = alarm_list
        self._file_download_job = file_download_job
        self._files = files
        self._gnb_du_function = gnb_du_function
        self._gnb_cu_up_function = gnb_cu_up_function
        self._gnb_cu_cp_function = gnb_cu_cp_function
        self._des_management_function = des_management_function
        self._drach_optimization_function = drach_optimization_function
        self._dmro_function = dmro_function
        self._dlbo_function = dlbo_function
        self._dpci_configuration_function = dpci_configuration_function
        self._cpci_configuration_function = cpci_configuration_function
        self._ces_management_function = ces_management_function
        self._configurable5_qi_set = configurable5_qi_set
        self._dynamic5_qi_set = dynamic5_qi_set

    @classmethod
    def from_dict(cls, dikt) -> 'ManagedElementSingle':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ManagedElement-Single of this ManagedElementSingle.  # noqa: E501
        :rtype: ManagedElementSingle
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this ManagedElementSingle.


        :return: The id of this ManagedElementSingle.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ManagedElementSingle.


        :param id: The id of this ManagedElementSingle.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def object_class(self):
        """Gets the object_class of this ManagedElementSingle.


        :return: The object_class of this ManagedElementSingle.
        :rtype: str
        """
        return self._object_class

    @object_class.setter
    def object_class(self, object_class):
        """Sets the object_class of this ManagedElementSingle.


        :param object_class: The object_class of this ManagedElementSingle.
        :type object_class: str
        """

        self._object_class = object_class

    @property
    def object_instance(self):
        """Gets the object_instance of this ManagedElementSingle.


        :return: The object_instance of this ManagedElementSingle.
        :rtype: str
        """
        return self._object_instance

    @object_instance.setter
    def object_instance(self, object_instance):
        """Sets the object_instance of this ManagedElementSingle.


        :param object_instance: The object_instance of this ManagedElementSingle.
        :type object_instance: str
        """

        self._object_instance = object_instance

    @property
    def vs_data_container(self):
        """Gets the vs_data_container of this ManagedElementSingle.


        :return: The vs_data_container of this ManagedElementSingle.
        :rtype: List[VsDataContainerSingle]
        """
        return self._vs_data_container

    @vs_data_container.setter
    def vs_data_container(self, vs_data_container):
        """Sets the vs_data_container of this ManagedElementSingle.


        :param vs_data_container: The vs_data_container of this ManagedElementSingle.
        :type vs_data_container: List[VsDataContainerSingle]
        """

        self._vs_data_container = vs_data_container

    @property
    def attributes(self):
        """Gets the attributes of this ManagedElementSingle.


        :return: The attributes of this ManagedElementSingle.
        :rtype: ManagedElementAttr
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this ManagedElementSingle.


        :param attributes: The attributes of this ManagedElementSingle.
        :type attributes: ManagedElementAttr
        """

        self._attributes = attributes

    @property
    def mns_agent(self):
        """Gets the mns_agent of this ManagedElementSingle.


        :return: The mns_agent of this ManagedElementSingle.
        :rtype: List[MnsAgentSingle]
        """
        return self._mns_agent

    @mns_agent.setter
    def mns_agent(self, mns_agent):
        """Sets the mns_agent of this ManagedElementSingle.


        :param mns_agent: The mns_agent of this ManagedElementSingle.
        :type mns_agent: List[MnsAgentSingle]
        """

        self._mns_agent = mns_agent

    @property
    def perf_metric_job(self):
        """Gets the perf_metric_job of this ManagedElementSingle.


        :return: The perf_metric_job of this ManagedElementSingle.
        :rtype: List[PerfMetricJobSingle]
        """
        return self._perf_metric_job

    @perf_metric_job.setter
    def perf_metric_job(self, perf_metric_job):
        """Sets the perf_metric_job of this ManagedElementSingle.


        :param perf_metric_job: The perf_metric_job of this ManagedElementSingle.
        :type perf_metric_job: List[PerfMetricJobSingle]
        """

        self._perf_metric_job = perf_metric_job

    @property
    def threshold_monitor(self):
        """Gets the threshold_monitor of this ManagedElementSingle.


        :return: The threshold_monitor of this ManagedElementSingle.
        :rtype: List[ThresholdMonitorSingle]
        """
        return self._threshold_monitor

    @threshold_monitor.setter
    def threshold_monitor(self, threshold_monitor):
        """Sets the threshold_monitor of this ManagedElementSingle.


        :param threshold_monitor: The threshold_monitor of this ManagedElementSingle.
        :type threshold_monitor: List[ThresholdMonitorSingle]
        """

        self._threshold_monitor = threshold_monitor

    @property
    def trace_job(self):
        """Gets the trace_job of this ManagedElementSingle.


        :return: The trace_job of this ManagedElementSingle.
        :rtype: List[TraceJobSingle]
        """
        return self._trace_job

    @trace_job.setter
    def trace_job(self, trace_job):
        """Sets the trace_job of this ManagedElementSingle.


        :param trace_job: The trace_job of this ManagedElementSingle.
        :type trace_job: List[TraceJobSingle]
        """

        self._trace_job = trace_job

    @property
    def ntf_subscription_control(self):
        """Gets the ntf_subscription_control of this ManagedElementSingle.


        :return: The ntf_subscription_control of this ManagedElementSingle.
        :rtype: List[NtfSubscriptionControlSingle]
        """
        return self._ntf_subscription_control

    @ntf_subscription_control.setter
    def ntf_subscription_control(self, ntf_subscription_control):
        """Sets the ntf_subscription_control of this ManagedElementSingle.


        :param ntf_subscription_control: The ntf_subscription_control of this ManagedElementSingle.
        :type ntf_subscription_control: List[NtfSubscriptionControlSingle]
        """

        self._ntf_subscription_control = ntf_subscription_control

    @property
    def alarm_list(self):
        """Gets the alarm_list of this ManagedElementSingle.


        :return: The alarm_list of this ManagedElementSingle.
        :rtype: AlarmListSingle
        """
        return self._alarm_list

    @alarm_list.setter
    def alarm_list(self, alarm_list):
        """Sets the alarm_list of this ManagedElementSingle.


        :param alarm_list: The alarm_list of this ManagedElementSingle.
        :type alarm_list: AlarmListSingle
        """

        self._alarm_list = alarm_list

    @property
    def file_download_job(self):
        """Gets the file_download_job of this ManagedElementSingle.


        :return: The file_download_job of this ManagedElementSingle.
        :rtype: List[FileDownloadJobSingle]
        """
        return self._file_download_job

    @file_download_job.setter
    def file_download_job(self, file_download_job):
        """Sets the file_download_job of this ManagedElementSingle.


        :param file_download_job: The file_download_job of this ManagedElementSingle.
        :type file_download_job: List[FileDownloadJobSingle]
        """

        self._file_download_job = file_download_job

    @property
    def files(self):
        """Gets the files of this ManagedElementSingle.


        :return: The files of this ManagedElementSingle.
        :rtype: List[FilesSingle]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this ManagedElementSingle.


        :param files: The files of this ManagedElementSingle.
        :type files: List[FilesSingle]
        """

        self._files = files

    @property
    def gnb_du_function(self):
        """Gets the gnb_du_function of this ManagedElementSingle.


        :return: The gnb_du_function of this ManagedElementSingle.
        :rtype: List[GnbDuFunctionSingle]
        """
        return self._gnb_du_function

    @gnb_du_function.setter
    def gnb_du_function(self, gnb_du_function):
        """Sets the gnb_du_function of this ManagedElementSingle.


        :param gnb_du_function: The gnb_du_function of this ManagedElementSingle.
        :type gnb_du_function: List[GnbDuFunctionSingle]
        """

        self._gnb_du_function = gnb_du_function

    @property
    def gnb_cu_up_function(self):
        """Gets the gnb_cu_up_function of this ManagedElementSingle.


        :return: The gnb_cu_up_function of this ManagedElementSingle.
        :rtype: List[GnbCuUpFunctionSingle]
        """
        return self._gnb_cu_up_function

    @gnb_cu_up_function.setter
    def gnb_cu_up_function(self, gnb_cu_up_function):
        """Sets the gnb_cu_up_function of this ManagedElementSingle.


        :param gnb_cu_up_function: The gnb_cu_up_function of this ManagedElementSingle.
        :type gnb_cu_up_function: List[GnbCuUpFunctionSingle]
        """

        self._gnb_cu_up_function = gnb_cu_up_function

    @property
    def gnb_cu_cp_function(self):
        """Gets the gnb_cu_cp_function of this ManagedElementSingle.


        :return: The gnb_cu_cp_function of this ManagedElementSingle.
        :rtype: List[GnbCuCpFunctionSingle]
        """
        return self._gnb_cu_cp_function

    @gnb_cu_cp_function.setter
    def gnb_cu_cp_function(self, gnb_cu_cp_function):
        """Sets the gnb_cu_cp_function of this ManagedElementSingle.


        :param gnb_cu_cp_function: The gnb_cu_cp_function of this ManagedElementSingle.
        :type gnb_cu_cp_function: List[GnbCuCpFunctionSingle]
        """

        self._gnb_cu_cp_function = gnb_cu_cp_function

    @property
    def des_management_function(self):
        """Gets the des_management_function of this ManagedElementSingle.


        :return: The des_management_function of this ManagedElementSingle.
        :rtype: DESManagementFunctionSingle
        """
        return self._des_management_function

    @des_management_function.setter
    def des_management_function(self, des_management_function):
        """Sets the des_management_function of this ManagedElementSingle.


        :param des_management_function: The des_management_function of this ManagedElementSingle.
        :type des_management_function: DESManagementFunctionSingle
        """

        self._des_management_function = des_management_function

    @property
    def drach_optimization_function(self):
        """Gets the drach_optimization_function of this ManagedElementSingle.


        :return: The drach_optimization_function of this ManagedElementSingle.
        :rtype: DRACHOptimizationFunctionSingle
        """
        return self._drach_optimization_function

    @drach_optimization_function.setter
    def drach_optimization_function(self, drach_optimization_function):
        """Sets the drach_optimization_function of this ManagedElementSingle.


        :param drach_optimization_function: The drach_optimization_function of this ManagedElementSingle.
        :type drach_optimization_function: DRACHOptimizationFunctionSingle
        """

        self._drach_optimization_function = drach_optimization_function

    @property
    def dmro_function(self):
        """Gets the dmro_function of this ManagedElementSingle.


        :return: The dmro_function of this ManagedElementSingle.
        :rtype: DMROFunctionSingle
        """
        return self._dmro_function

    @dmro_function.setter
    def dmro_function(self, dmro_function):
        """Sets the dmro_function of this ManagedElementSingle.


        :param dmro_function: The dmro_function of this ManagedElementSingle.
        :type dmro_function: DMROFunctionSingle
        """

        self._dmro_function = dmro_function

    @property
    def dlbo_function(self):
        """Gets the dlbo_function of this ManagedElementSingle.


        :return: The dlbo_function of this ManagedElementSingle.
        :rtype: DLBOFunctionSingle
        """
        return self._dlbo_function

    @dlbo_function.setter
    def dlbo_function(self, dlbo_function):
        """Sets the dlbo_function of this ManagedElementSingle.


        :param dlbo_function: The dlbo_function of this ManagedElementSingle.
        :type dlbo_function: DLBOFunctionSingle
        """

        self._dlbo_function = dlbo_function

    @property
    def dpci_configuration_function(self):
        """Gets the dpci_configuration_function of this ManagedElementSingle.


        :return: The dpci_configuration_function of this ManagedElementSingle.
        :rtype: DPCIConfigurationFunctionSingle
        """
        return self._dpci_configuration_function

    @dpci_configuration_function.setter
    def dpci_configuration_function(self, dpci_configuration_function):
        """Sets the dpci_configuration_function of this ManagedElementSingle.


        :param dpci_configuration_function: The dpci_configuration_function of this ManagedElementSingle.
        :type dpci_configuration_function: DPCIConfigurationFunctionSingle
        """

        self._dpci_configuration_function = dpci_configuration_function

    @property
    def cpci_configuration_function(self):
        """Gets the cpci_configuration_function of this ManagedElementSingle.


        :return: The cpci_configuration_function of this ManagedElementSingle.
        :rtype: CPCIConfigurationFunctionSingle
        """
        return self._cpci_configuration_function

    @cpci_configuration_function.setter
    def cpci_configuration_function(self, cpci_configuration_function):
        """Sets the cpci_configuration_function of this ManagedElementSingle.


        :param cpci_configuration_function: The cpci_configuration_function of this ManagedElementSingle.
        :type cpci_configuration_function: CPCIConfigurationFunctionSingle
        """

        self._cpci_configuration_function = cpci_configuration_function

    @property
    def ces_management_function(self):
        """Gets the ces_management_function of this ManagedElementSingle.


        :return: The ces_management_function of this ManagedElementSingle.
        :rtype: CESManagementFunctionSingle
        """
        return self._ces_management_function

    @ces_management_function.setter
    def ces_management_function(self, ces_management_function):
        """Sets the ces_management_function of this ManagedElementSingle.


        :param ces_management_function: The ces_management_function of this ManagedElementSingle.
        :type ces_management_function: CESManagementFunctionSingle
        """

        self._ces_management_function = ces_management_function

    @property
    def configurable5_qi_set(self):
        """Gets the configurable5_qi_set of this ManagedElementSingle.


        :return: The configurable5_qi_set of this ManagedElementSingle.
        :rtype: List[Configurable5QISetSingle]
        """
        return self._configurable5_qi_set

    @configurable5_qi_set.setter
    def configurable5_qi_set(self, configurable5_qi_set):
        """Sets the configurable5_qi_set of this ManagedElementSingle.


        :param configurable5_qi_set: The configurable5_qi_set of this ManagedElementSingle.
        :type configurable5_qi_set: List[Configurable5QISetSingle]
        """

        self._configurable5_qi_set = configurable5_qi_set

    @property
    def dynamic5_qi_set(self):
        """Gets the dynamic5_qi_set of this ManagedElementSingle.


        :return: The dynamic5_qi_set of this ManagedElementSingle.
        :rtype: List[Dynamic5QISetSingle]
        """
        return self._dynamic5_qi_set

    @dynamic5_qi_set.setter
    def dynamic5_qi_set(self, dynamic5_qi_set):
        """Sets the dynamic5_qi_set of this ManagedElementSingle.


        :param dynamic5_qi_set: The dynamic5_qi_set of this ManagedElementSingle.
        :type dynamic5_qi_set: List[Dynamic5QISetSingle]
        """

        self._dynamic5_qi_set = dynamic5_qi_set