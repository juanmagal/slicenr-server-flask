# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.alarm_list_single import AlarmListSingle
from openapi_server.models.amf_function_single import AmfFunctionSingle
from openapi_server.models.ausf_function_single import AusfFunctionSingle
from openapi_server.models.configurable5_qi_set_single import Configurable5QISetSingle
from openapi_server.models.dynamic5_qi_set_single import Dynamic5QISetSingle
from openapi_server.models.easdf_function_single import EASDFFunctionSingle
from openapi_server.models.ecm_connection_info_single import EcmConnectionInfoSingle
from openapi_server.models.file_download_job_single import FileDownloadJobSingle
from openapi_server.models.files_single import FilesSingle
from openapi_server.models.lmf_function_single import LmfFunctionSingle
from openapi_server.models.managed_element_single1_all_of_attributes import ManagedElementSingle1AllOfAttributes
from openapi_server.models.mns_agent_single import MnsAgentSingle
from openapi_server.models.n3iwf_function_single import N3iwfFunctionSingle
from openapi_server.models.nef_function_single import NefFunctionSingle
from openapi_server.models.ngeir_function_single import NgeirFunctionSingle
from openapi_server.models.nrf_function_single import NrfFunctionSingle
from openapi_server.models.nssf_function_single import NssfFunctionSingle
from openapi_server.models.ntf_subscription_control_single import NtfSubscriptionControlSingle
from openapi_server.models.nwdaf_function_single import NwdafFunctionSingle
from openapi_server.models.pcf_function_single import PcfFunctionSingle
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle
from openapi_server.models.scp_function_single import ScpFunctionSingle
from openapi_server.models.sepp_function_single import SeppFunctionSingle
from openapi_server.models.smf_function_single import SmfFunctionSingle
from openapi_server.models.smsf_function_single import SmsfFunctionSingle
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle
from openapi_server.models.trace_job_single import TraceJobSingle
from openapi_server.models.udm_function_single import UdmFunctionSingle
from openapi_server.models.udr_function_single import UdrFunctionSingle
from openapi_server.models.udsf_function_single import UdsfFunctionSingle
from openapi_server.models.upf_function_single import UpfFunctionSingle
from openapi_server.models.vs_data_container_single import VsDataContainerSingle
from openapi_server import util

from openapi_server.models.alarm_list_single import AlarmListSingle  # noqa: E501
from openapi_server.models.amf_function_single import AmfFunctionSingle  # noqa: E501
from openapi_server.models.ausf_function_single import AusfFunctionSingle  # noqa: E501
from openapi_server.models.configurable5_qi_set_single import Configurable5QISetSingle  # noqa: E501
from openapi_server.models.dynamic5_qi_set_single import Dynamic5QISetSingle  # noqa: E501
from openapi_server.models.easdf_function_single import EASDFFunctionSingle  # noqa: E501
from openapi_server.models.ecm_connection_info_single import EcmConnectionInfoSingle  # noqa: E501
from openapi_server.models.file_download_job_single import FileDownloadJobSingle  # noqa: E501
from openapi_server.models.files_single import FilesSingle  # noqa: E501
from openapi_server.models.lmf_function_single import LmfFunctionSingle  # noqa: E501
from openapi_server.models.managed_element_single1_all_of_attributes import ManagedElementSingle1AllOfAttributes  # noqa: E501
from openapi_server.models.mns_agent_single import MnsAgentSingle  # noqa: E501
from openapi_server.models.n3iwf_function_single import N3iwfFunctionSingle  # noqa: E501
from openapi_server.models.nef_function_single import NefFunctionSingle  # noqa: E501
from openapi_server.models.ngeir_function_single import NgeirFunctionSingle  # noqa: E501
from openapi_server.models.nrf_function_single import NrfFunctionSingle  # noqa: E501
from openapi_server.models.nssf_function_single import NssfFunctionSingle  # noqa: E501
from openapi_server.models.ntf_subscription_control_single import NtfSubscriptionControlSingle  # noqa: E501
from openapi_server.models.nwdaf_function_single import NwdafFunctionSingle  # noqa: E501
from openapi_server.models.pcf_function_single import PcfFunctionSingle  # noqa: E501
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle  # noqa: E501
from openapi_server.models.scp_function_single import ScpFunctionSingle  # noqa: E501
from openapi_server.models.sepp_function_single import SeppFunctionSingle  # noqa: E501
from openapi_server.models.smf_function_single import SmfFunctionSingle  # noqa: E501
from openapi_server.models.smsf_function_single import SmsfFunctionSingle  # noqa: E501
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle  # noqa: E501
from openapi_server.models.trace_job_single import TraceJobSingle  # noqa: E501
from openapi_server.models.udm_function_single import UdmFunctionSingle  # noqa: E501
from openapi_server.models.udr_function_single import UdrFunctionSingle  # noqa: E501
from openapi_server.models.udsf_function_single import UdsfFunctionSingle  # noqa: E501
from openapi_server.models.upf_function_single import UpfFunctionSingle  # noqa: E501
from openapi_server.models.vs_data_container_single import VsDataContainerSingle  # noqa: E501

class ManagedElementSingle1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, object_class=None, object_instance=None, vs_data_container=None, attributes=None, mns_agent=None, perf_metric_job=None, threshold_monitor=None, trace_job=None, ntf_subscription_control=None, alarm_list=None, file_download_job=None, files=None, amf_function=None, smf_function=None, upf_function=None, n3iwf_function=None, pcf_function=None, ausf_function=None, udm_function=None, udr_function=None, udsf_function=None, nrf_function=None, nssf_function=None, smsf_function=None, lmf_function=None, ngeir_function=None, sepp_function=None, nwdaf_function=None, scp_function=None, nef_function=None, configurable5_qi_set=None, dynamic5_qi_set=None, ecm_connection_info=None, easdf_function=None):  # noqa: E501
        """ManagedElementSingle1 - a model defined in OpenAPI

        :param id: The id of this ManagedElementSingle1.  # noqa: E501
        :type id: str
        :param object_class: The object_class of this ManagedElementSingle1.  # noqa: E501
        :type object_class: str
        :param object_instance: The object_instance of this ManagedElementSingle1.  # noqa: E501
        :type object_instance: str
        :param vs_data_container: The vs_data_container of this ManagedElementSingle1.  # noqa: E501
        :type vs_data_container: List[VsDataContainerSingle]
        :param attributes: The attributes of this ManagedElementSingle1.  # noqa: E501
        :type attributes: ManagedElementSingle1AllOfAttributes
        :param mns_agent: The mns_agent of this ManagedElementSingle1.  # noqa: E501
        :type mns_agent: List[MnsAgentSingle]
        :param perf_metric_job: The perf_metric_job of this ManagedElementSingle1.  # noqa: E501
        :type perf_metric_job: List[PerfMetricJobSingle]
        :param threshold_monitor: The threshold_monitor of this ManagedElementSingle1.  # noqa: E501
        :type threshold_monitor: List[ThresholdMonitorSingle]
        :param trace_job: The trace_job of this ManagedElementSingle1.  # noqa: E501
        :type trace_job: List[TraceJobSingle]
        :param ntf_subscription_control: The ntf_subscription_control of this ManagedElementSingle1.  # noqa: E501
        :type ntf_subscription_control: List[NtfSubscriptionControlSingle]
        :param alarm_list: The alarm_list of this ManagedElementSingle1.  # noqa: E501
        :type alarm_list: AlarmListSingle
        :param file_download_job: The file_download_job of this ManagedElementSingle1.  # noqa: E501
        :type file_download_job: List[FileDownloadJobSingle]
        :param files: The files of this ManagedElementSingle1.  # noqa: E501
        :type files: List[FilesSingle]
        :param amf_function: The amf_function of this ManagedElementSingle1.  # noqa: E501
        :type amf_function: List[AmfFunctionSingle]
        :param smf_function: The smf_function of this ManagedElementSingle1.  # noqa: E501
        :type smf_function: List[SmfFunctionSingle]
        :param upf_function: The upf_function of this ManagedElementSingle1.  # noqa: E501
        :type upf_function: List[UpfFunctionSingle]
        :param n3iwf_function: The n3iwf_function of this ManagedElementSingle1.  # noqa: E501
        :type n3iwf_function: List[N3iwfFunctionSingle]
        :param pcf_function: The pcf_function of this ManagedElementSingle1.  # noqa: E501
        :type pcf_function: List[PcfFunctionSingle]
        :param ausf_function: The ausf_function of this ManagedElementSingle1.  # noqa: E501
        :type ausf_function: List[AusfFunctionSingle]
        :param udm_function: The udm_function of this ManagedElementSingle1.  # noqa: E501
        :type udm_function: List[UdmFunctionSingle]
        :param udr_function: The udr_function of this ManagedElementSingle1.  # noqa: E501
        :type udr_function: List[UdrFunctionSingle]
        :param udsf_function: The udsf_function of this ManagedElementSingle1.  # noqa: E501
        :type udsf_function: List[UdsfFunctionSingle]
        :param nrf_function: The nrf_function of this ManagedElementSingle1.  # noqa: E501
        :type nrf_function: List[NrfFunctionSingle]
        :param nssf_function: The nssf_function of this ManagedElementSingle1.  # noqa: E501
        :type nssf_function: List[NssfFunctionSingle]
        :param smsf_function: The smsf_function of this ManagedElementSingle1.  # noqa: E501
        :type smsf_function: List[SmsfFunctionSingle]
        :param lmf_function: The lmf_function of this ManagedElementSingle1.  # noqa: E501
        :type lmf_function: List[LmfFunctionSingle]
        :param ngeir_function: The ngeir_function of this ManagedElementSingle1.  # noqa: E501
        :type ngeir_function: List[NgeirFunctionSingle]
        :param sepp_function: The sepp_function of this ManagedElementSingle1.  # noqa: E501
        :type sepp_function: List[SeppFunctionSingle]
        :param nwdaf_function: The nwdaf_function of this ManagedElementSingle1.  # noqa: E501
        :type nwdaf_function: List[NwdafFunctionSingle]
        :param scp_function: The scp_function of this ManagedElementSingle1.  # noqa: E501
        :type scp_function: List[ScpFunctionSingle]
        :param nef_function: The nef_function of this ManagedElementSingle1.  # noqa: E501
        :type nef_function: List[NefFunctionSingle]
        :param configurable5_qi_set: The configurable5_qi_set of this ManagedElementSingle1.  # noqa: E501
        :type configurable5_qi_set: List[Configurable5QISetSingle]
        :param dynamic5_qi_set: The dynamic5_qi_set of this ManagedElementSingle1.  # noqa: E501
        :type dynamic5_qi_set: List[Dynamic5QISetSingle]
        :param ecm_connection_info: The ecm_connection_info of this ManagedElementSingle1.  # noqa: E501
        :type ecm_connection_info: List[EcmConnectionInfoSingle]
        :param easdf_function: The easdf_function of this ManagedElementSingle1.  # noqa: E501
        :type easdf_function: List[EASDFFunctionSingle]
        """
        self.openapi_types = {
            'id': str,
            'object_class': str,
            'object_instance': str,
            'vs_data_container': List[VsDataContainerSingle],
            'attributes': ManagedElementSingle1AllOfAttributes,
            'mns_agent': List[MnsAgentSingle],
            'perf_metric_job': List[PerfMetricJobSingle],
            'threshold_monitor': List[ThresholdMonitorSingle],
            'trace_job': List[TraceJobSingle],
            'ntf_subscription_control': List[NtfSubscriptionControlSingle],
            'alarm_list': AlarmListSingle,
            'file_download_job': List[FileDownloadJobSingle],
            'files': List[FilesSingle],
            'amf_function': List[AmfFunctionSingle],
            'smf_function': List[SmfFunctionSingle],
            'upf_function': List[UpfFunctionSingle],
            'n3iwf_function': List[N3iwfFunctionSingle],
            'pcf_function': List[PcfFunctionSingle],
            'ausf_function': List[AusfFunctionSingle],
            'udm_function': List[UdmFunctionSingle],
            'udr_function': List[UdrFunctionSingle],
            'udsf_function': List[UdsfFunctionSingle],
            'nrf_function': List[NrfFunctionSingle],
            'nssf_function': List[NssfFunctionSingle],
            'smsf_function': List[SmsfFunctionSingle],
            'lmf_function': List[LmfFunctionSingle],
            'ngeir_function': List[NgeirFunctionSingle],
            'sepp_function': List[SeppFunctionSingle],
            'nwdaf_function': List[NwdafFunctionSingle],
            'scp_function': List[ScpFunctionSingle],
            'nef_function': List[NefFunctionSingle],
            'configurable5_qi_set': List[Configurable5QISetSingle],
            'dynamic5_qi_set': List[Dynamic5QISetSingle],
            'ecm_connection_info': List[EcmConnectionInfoSingle],
            'easdf_function': List[EASDFFunctionSingle]
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
            'amf_function': 'AmfFunction',
            'smf_function': 'SmfFunction',
            'upf_function': 'UpfFunction',
            'n3iwf_function': 'N3iwfFunction',
            'pcf_function': 'PcfFunction',
            'ausf_function': 'AusfFunction',
            'udm_function': 'UdmFunction',
            'udr_function': 'UdrFunction',
            'udsf_function': 'UdsfFunction',
            'nrf_function': 'NrfFunction',
            'nssf_function': 'NssfFunction',
            'smsf_function': 'SmsfFunction',
            'lmf_function': 'LmfFunction',
            'ngeir_function': 'NgeirFunction',
            'sepp_function': 'SeppFunction',
            'nwdaf_function': 'NwdafFunction',
            'scp_function': 'ScpFunction',
            'nef_function': 'NefFunction',
            'configurable5_qi_set': 'Configurable5QISet',
            'dynamic5_qi_set': 'Dynamic5QISet',
            'ecm_connection_info': 'EcmConnectionInfo',
            'easdf_function': 'EASDFFunction'
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
        self._amf_function = amf_function
        self._smf_function = smf_function
        self._upf_function = upf_function
        self._n3iwf_function = n3iwf_function
        self._pcf_function = pcf_function
        self._ausf_function = ausf_function
        self._udm_function = udm_function
        self._udr_function = udr_function
        self._udsf_function = udsf_function
        self._nrf_function = nrf_function
        self._nssf_function = nssf_function
        self._smsf_function = smsf_function
        self._lmf_function = lmf_function
        self._ngeir_function = ngeir_function
        self._sepp_function = sepp_function
        self._nwdaf_function = nwdaf_function
        self._scp_function = scp_function
        self._nef_function = nef_function
        self._configurable5_qi_set = configurable5_qi_set
        self._dynamic5_qi_set = dynamic5_qi_set
        self._ecm_connection_info = ecm_connection_info
        self._easdf_function = easdf_function

    @classmethod
    def from_dict(cls, dikt) -> 'ManagedElementSingle1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ManagedElement-Single_1 of this ManagedElementSingle1.  # noqa: E501
        :rtype: ManagedElementSingle1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this ManagedElementSingle1.


        :return: The id of this ManagedElementSingle1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ManagedElementSingle1.


        :param id: The id of this ManagedElementSingle1.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def object_class(self):
        """Gets the object_class of this ManagedElementSingle1.


        :return: The object_class of this ManagedElementSingle1.
        :rtype: str
        """
        return self._object_class

    @object_class.setter
    def object_class(self, object_class):
        """Sets the object_class of this ManagedElementSingle1.


        :param object_class: The object_class of this ManagedElementSingle1.
        :type object_class: str
        """

        self._object_class = object_class

    @property
    def object_instance(self):
        """Gets the object_instance of this ManagedElementSingle1.


        :return: The object_instance of this ManagedElementSingle1.
        :rtype: str
        """
        return self._object_instance

    @object_instance.setter
    def object_instance(self, object_instance):
        """Sets the object_instance of this ManagedElementSingle1.


        :param object_instance: The object_instance of this ManagedElementSingle1.
        :type object_instance: str
        """

        self._object_instance = object_instance

    @property
    def vs_data_container(self):
        """Gets the vs_data_container of this ManagedElementSingle1.


        :return: The vs_data_container of this ManagedElementSingle1.
        :rtype: List[VsDataContainerSingle]
        """
        return self._vs_data_container

    @vs_data_container.setter
    def vs_data_container(self, vs_data_container):
        """Sets the vs_data_container of this ManagedElementSingle1.


        :param vs_data_container: The vs_data_container of this ManagedElementSingle1.
        :type vs_data_container: List[VsDataContainerSingle]
        """

        self._vs_data_container = vs_data_container

    @property
    def attributes(self):
        """Gets the attributes of this ManagedElementSingle1.


        :return: The attributes of this ManagedElementSingle1.
        :rtype: ManagedElementSingle1AllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this ManagedElementSingle1.


        :param attributes: The attributes of this ManagedElementSingle1.
        :type attributes: ManagedElementSingle1AllOfAttributes
        """

        self._attributes = attributes

    @property
    def mns_agent(self):
        """Gets the mns_agent of this ManagedElementSingle1.


        :return: The mns_agent of this ManagedElementSingle1.
        :rtype: List[MnsAgentSingle]
        """
        return self._mns_agent

    @mns_agent.setter
    def mns_agent(self, mns_agent):
        """Sets the mns_agent of this ManagedElementSingle1.


        :param mns_agent: The mns_agent of this ManagedElementSingle1.
        :type mns_agent: List[MnsAgentSingle]
        """

        self._mns_agent = mns_agent

    @property
    def perf_metric_job(self):
        """Gets the perf_metric_job of this ManagedElementSingle1.


        :return: The perf_metric_job of this ManagedElementSingle1.
        :rtype: List[PerfMetricJobSingle]
        """
        return self._perf_metric_job

    @perf_metric_job.setter
    def perf_metric_job(self, perf_metric_job):
        """Sets the perf_metric_job of this ManagedElementSingle1.


        :param perf_metric_job: The perf_metric_job of this ManagedElementSingle1.
        :type perf_metric_job: List[PerfMetricJobSingle]
        """

        self._perf_metric_job = perf_metric_job

    @property
    def threshold_monitor(self):
        """Gets the threshold_monitor of this ManagedElementSingle1.


        :return: The threshold_monitor of this ManagedElementSingle1.
        :rtype: List[ThresholdMonitorSingle]
        """
        return self._threshold_monitor

    @threshold_monitor.setter
    def threshold_monitor(self, threshold_monitor):
        """Sets the threshold_monitor of this ManagedElementSingle1.


        :param threshold_monitor: The threshold_monitor of this ManagedElementSingle1.
        :type threshold_monitor: List[ThresholdMonitorSingle]
        """

        self._threshold_monitor = threshold_monitor

    @property
    def trace_job(self):
        """Gets the trace_job of this ManagedElementSingle1.


        :return: The trace_job of this ManagedElementSingle1.
        :rtype: List[TraceJobSingle]
        """
        return self._trace_job

    @trace_job.setter
    def trace_job(self, trace_job):
        """Sets the trace_job of this ManagedElementSingle1.


        :param trace_job: The trace_job of this ManagedElementSingle1.
        :type trace_job: List[TraceJobSingle]
        """

        self._trace_job = trace_job

    @property
    def ntf_subscription_control(self):
        """Gets the ntf_subscription_control of this ManagedElementSingle1.


        :return: The ntf_subscription_control of this ManagedElementSingle1.
        :rtype: List[NtfSubscriptionControlSingle]
        """
        return self._ntf_subscription_control

    @ntf_subscription_control.setter
    def ntf_subscription_control(self, ntf_subscription_control):
        """Sets the ntf_subscription_control of this ManagedElementSingle1.


        :param ntf_subscription_control: The ntf_subscription_control of this ManagedElementSingle1.
        :type ntf_subscription_control: List[NtfSubscriptionControlSingle]
        """

        self._ntf_subscription_control = ntf_subscription_control

    @property
    def alarm_list(self):
        """Gets the alarm_list of this ManagedElementSingle1.


        :return: The alarm_list of this ManagedElementSingle1.
        :rtype: AlarmListSingle
        """
        return self._alarm_list

    @alarm_list.setter
    def alarm_list(self, alarm_list):
        """Sets the alarm_list of this ManagedElementSingle1.


        :param alarm_list: The alarm_list of this ManagedElementSingle1.
        :type alarm_list: AlarmListSingle
        """

        self._alarm_list = alarm_list

    @property
    def file_download_job(self):
        """Gets the file_download_job of this ManagedElementSingle1.


        :return: The file_download_job of this ManagedElementSingle1.
        :rtype: List[FileDownloadJobSingle]
        """
        return self._file_download_job

    @file_download_job.setter
    def file_download_job(self, file_download_job):
        """Sets the file_download_job of this ManagedElementSingle1.


        :param file_download_job: The file_download_job of this ManagedElementSingle1.
        :type file_download_job: List[FileDownloadJobSingle]
        """

        self._file_download_job = file_download_job

    @property
    def files(self):
        """Gets the files of this ManagedElementSingle1.


        :return: The files of this ManagedElementSingle1.
        :rtype: List[FilesSingle]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this ManagedElementSingle1.


        :param files: The files of this ManagedElementSingle1.
        :type files: List[FilesSingle]
        """

        self._files = files

    @property
    def amf_function(self):
        """Gets the amf_function of this ManagedElementSingle1.


        :return: The amf_function of this ManagedElementSingle1.
        :rtype: List[AmfFunctionSingle]
        """
        return self._amf_function

    @amf_function.setter
    def amf_function(self, amf_function):
        """Sets the amf_function of this ManagedElementSingle1.


        :param amf_function: The amf_function of this ManagedElementSingle1.
        :type amf_function: List[AmfFunctionSingle]
        """

        self._amf_function = amf_function

    @property
    def smf_function(self):
        """Gets the smf_function of this ManagedElementSingle1.


        :return: The smf_function of this ManagedElementSingle1.
        :rtype: List[SmfFunctionSingle]
        """
        return self._smf_function

    @smf_function.setter
    def smf_function(self, smf_function):
        """Sets the smf_function of this ManagedElementSingle1.


        :param smf_function: The smf_function of this ManagedElementSingle1.
        :type smf_function: List[SmfFunctionSingle]
        """

        self._smf_function = smf_function

    @property
    def upf_function(self):
        """Gets the upf_function of this ManagedElementSingle1.


        :return: The upf_function of this ManagedElementSingle1.
        :rtype: List[UpfFunctionSingle]
        """
        return self._upf_function

    @upf_function.setter
    def upf_function(self, upf_function):
        """Sets the upf_function of this ManagedElementSingle1.


        :param upf_function: The upf_function of this ManagedElementSingle1.
        :type upf_function: List[UpfFunctionSingle]
        """

        self._upf_function = upf_function

    @property
    def n3iwf_function(self):
        """Gets the n3iwf_function of this ManagedElementSingle1.


        :return: The n3iwf_function of this ManagedElementSingle1.
        :rtype: List[N3iwfFunctionSingle]
        """
        return self._n3iwf_function

    @n3iwf_function.setter
    def n3iwf_function(self, n3iwf_function):
        """Sets the n3iwf_function of this ManagedElementSingle1.


        :param n3iwf_function: The n3iwf_function of this ManagedElementSingle1.
        :type n3iwf_function: List[N3iwfFunctionSingle]
        """

        self._n3iwf_function = n3iwf_function

    @property
    def pcf_function(self):
        """Gets the pcf_function of this ManagedElementSingle1.


        :return: The pcf_function of this ManagedElementSingle1.
        :rtype: List[PcfFunctionSingle]
        """
        return self._pcf_function

    @pcf_function.setter
    def pcf_function(self, pcf_function):
        """Sets the pcf_function of this ManagedElementSingle1.


        :param pcf_function: The pcf_function of this ManagedElementSingle1.
        :type pcf_function: List[PcfFunctionSingle]
        """

        self._pcf_function = pcf_function

    @property
    def ausf_function(self):
        """Gets the ausf_function of this ManagedElementSingle1.


        :return: The ausf_function of this ManagedElementSingle1.
        :rtype: List[AusfFunctionSingle]
        """
        return self._ausf_function

    @ausf_function.setter
    def ausf_function(self, ausf_function):
        """Sets the ausf_function of this ManagedElementSingle1.


        :param ausf_function: The ausf_function of this ManagedElementSingle1.
        :type ausf_function: List[AusfFunctionSingle]
        """

        self._ausf_function = ausf_function

    @property
    def udm_function(self):
        """Gets the udm_function of this ManagedElementSingle1.


        :return: The udm_function of this ManagedElementSingle1.
        :rtype: List[UdmFunctionSingle]
        """
        return self._udm_function

    @udm_function.setter
    def udm_function(self, udm_function):
        """Sets the udm_function of this ManagedElementSingle1.


        :param udm_function: The udm_function of this ManagedElementSingle1.
        :type udm_function: List[UdmFunctionSingle]
        """

        self._udm_function = udm_function

    @property
    def udr_function(self):
        """Gets the udr_function of this ManagedElementSingle1.


        :return: The udr_function of this ManagedElementSingle1.
        :rtype: List[UdrFunctionSingle]
        """
        return self._udr_function

    @udr_function.setter
    def udr_function(self, udr_function):
        """Sets the udr_function of this ManagedElementSingle1.


        :param udr_function: The udr_function of this ManagedElementSingle1.
        :type udr_function: List[UdrFunctionSingle]
        """

        self._udr_function = udr_function

    @property
    def udsf_function(self):
        """Gets the udsf_function of this ManagedElementSingle1.


        :return: The udsf_function of this ManagedElementSingle1.
        :rtype: List[UdsfFunctionSingle]
        """
        return self._udsf_function

    @udsf_function.setter
    def udsf_function(self, udsf_function):
        """Sets the udsf_function of this ManagedElementSingle1.


        :param udsf_function: The udsf_function of this ManagedElementSingle1.
        :type udsf_function: List[UdsfFunctionSingle]
        """

        self._udsf_function = udsf_function

    @property
    def nrf_function(self):
        """Gets the nrf_function of this ManagedElementSingle1.


        :return: The nrf_function of this ManagedElementSingle1.
        :rtype: List[NrfFunctionSingle]
        """
        return self._nrf_function

    @nrf_function.setter
    def nrf_function(self, nrf_function):
        """Sets the nrf_function of this ManagedElementSingle1.


        :param nrf_function: The nrf_function of this ManagedElementSingle1.
        :type nrf_function: List[NrfFunctionSingle]
        """

        self._nrf_function = nrf_function

    @property
    def nssf_function(self):
        """Gets the nssf_function of this ManagedElementSingle1.


        :return: The nssf_function of this ManagedElementSingle1.
        :rtype: List[NssfFunctionSingle]
        """
        return self._nssf_function

    @nssf_function.setter
    def nssf_function(self, nssf_function):
        """Sets the nssf_function of this ManagedElementSingle1.


        :param nssf_function: The nssf_function of this ManagedElementSingle1.
        :type nssf_function: List[NssfFunctionSingle]
        """

        self._nssf_function = nssf_function

    @property
    def smsf_function(self):
        """Gets the smsf_function of this ManagedElementSingle1.


        :return: The smsf_function of this ManagedElementSingle1.
        :rtype: List[SmsfFunctionSingle]
        """
        return self._smsf_function

    @smsf_function.setter
    def smsf_function(self, smsf_function):
        """Sets the smsf_function of this ManagedElementSingle1.


        :param smsf_function: The smsf_function of this ManagedElementSingle1.
        :type smsf_function: List[SmsfFunctionSingle]
        """

        self._smsf_function = smsf_function

    @property
    def lmf_function(self):
        """Gets the lmf_function of this ManagedElementSingle1.


        :return: The lmf_function of this ManagedElementSingle1.
        :rtype: List[LmfFunctionSingle]
        """
        return self._lmf_function

    @lmf_function.setter
    def lmf_function(self, lmf_function):
        """Sets the lmf_function of this ManagedElementSingle1.


        :param lmf_function: The lmf_function of this ManagedElementSingle1.
        :type lmf_function: List[LmfFunctionSingle]
        """

        self._lmf_function = lmf_function

    @property
    def ngeir_function(self):
        """Gets the ngeir_function of this ManagedElementSingle1.


        :return: The ngeir_function of this ManagedElementSingle1.
        :rtype: List[NgeirFunctionSingle]
        """
        return self._ngeir_function

    @ngeir_function.setter
    def ngeir_function(self, ngeir_function):
        """Sets the ngeir_function of this ManagedElementSingle1.


        :param ngeir_function: The ngeir_function of this ManagedElementSingle1.
        :type ngeir_function: List[NgeirFunctionSingle]
        """

        self._ngeir_function = ngeir_function

    @property
    def sepp_function(self):
        """Gets the sepp_function of this ManagedElementSingle1.


        :return: The sepp_function of this ManagedElementSingle1.
        :rtype: List[SeppFunctionSingle]
        """
        return self._sepp_function

    @sepp_function.setter
    def sepp_function(self, sepp_function):
        """Sets the sepp_function of this ManagedElementSingle1.


        :param sepp_function: The sepp_function of this ManagedElementSingle1.
        :type sepp_function: List[SeppFunctionSingle]
        """

        self._sepp_function = sepp_function

    @property
    def nwdaf_function(self):
        """Gets the nwdaf_function of this ManagedElementSingle1.


        :return: The nwdaf_function of this ManagedElementSingle1.
        :rtype: List[NwdafFunctionSingle]
        """
        return self._nwdaf_function

    @nwdaf_function.setter
    def nwdaf_function(self, nwdaf_function):
        """Sets the nwdaf_function of this ManagedElementSingle1.


        :param nwdaf_function: The nwdaf_function of this ManagedElementSingle1.
        :type nwdaf_function: List[NwdafFunctionSingle]
        """

        self._nwdaf_function = nwdaf_function

    @property
    def scp_function(self):
        """Gets the scp_function of this ManagedElementSingle1.


        :return: The scp_function of this ManagedElementSingle1.
        :rtype: List[ScpFunctionSingle]
        """
        return self._scp_function

    @scp_function.setter
    def scp_function(self, scp_function):
        """Sets the scp_function of this ManagedElementSingle1.


        :param scp_function: The scp_function of this ManagedElementSingle1.
        :type scp_function: List[ScpFunctionSingle]
        """

        self._scp_function = scp_function

    @property
    def nef_function(self):
        """Gets the nef_function of this ManagedElementSingle1.


        :return: The nef_function of this ManagedElementSingle1.
        :rtype: List[NefFunctionSingle]
        """
        return self._nef_function

    @nef_function.setter
    def nef_function(self, nef_function):
        """Sets the nef_function of this ManagedElementSingle1.


        :param nef_function: The nef_function of this ManagedElementSingle1.
        :type nef_function: List[NefFunctionSingle]
        """

        self._nef_function = nef_function

    @property
    def configurable5_qi_set(self):
        """Gets the configurable5_qi_set of this ManagedElementSingle1.


        :return: The configurable5_qi_set of this ManagedElementSingle1.
        :rtype: List[Configurable5QISetSingle]
        """
        return self._configurable5_qi_set

    @configurable5_qi_set.setter
    def configurable5_qi_set(self, configurable5_qi_set):
        """Sets the configurable5_qi_set of this ManagedElementSingle1.


        :param configurable5_qi_set: The configurable5_qi_set of this ManagedElementSingle1.
        :type configurable5_qi_set: List[Configurable5QISetSingle]
        """

        self._configurable5_qi_set = configurable5_qi_set

    @property
    def dynamic5_qi_set(self):
        """Gets the dynamic5_qi_set of this ManagedElementSingle1.


        :return: The dynamic5_qi_set of this ManagedElementSingle1.
        :rtype: List[Dynamic5QISetSingle]
        """
        return self._dynamic5_qi_set

    @dynamic5_qi_set.setter
    def dynamic5_qi_set(self, dynamic5_qi_set):
        """Sets the dynamic5_qi_set of this ManagedElementSingle1.


        :param dynamic5_qi_set: The dynamic5_qi_set of this ManagedElementSingle1.
        :type dynamic5_qi_set: List[Dynamic5QISetSingle]
        """

        self._dynamic5_qi_set = dynamic5_qi_set

    @property
    def ecm_connection_info(self):
        """Gets the ecm_connection_info of this ManagedElementSingle1.


        :return: The ecm_connection_info of this ManagedElementSingle1.
        :rtype: List[EcmConnectionInfoSingle]
        """
        return self._ecm_connection_info

    @ecm_connection_info.setter
    def ecm_connection_info(self, ecm_connection_info):
        """Sets the ecm_connection_info of this ManagedElementSingle1.


        :param ecm_connection_info: The ecm_connection_info of this ManagedElementSingle1.
        :type ecm_connection_info: List[EcmConnectionInfoSingle]
        """

        self._ecm_connection_info = ecm_connection_info

    @property
    def easdf_function(self):
        """Gets the easdf_function of this ManagedElementSingle1.


        :return: The easdf_function of this ManagedElementSingle1.
        :rtype: List[EASDFFunctionSingle]
        """
        return self._easdf_function

    @easdf_function.setter
    def easdf_function(self, easdf_function):
        """Sets the easdf_function of this ManagedElementSingle1.


        :param easdf_function: The easdf_function of this ManagedElementSingle1.
        :type easdf_function: List[EASDFFunctionSingle]
        """

        self._easdf_function = easdf_function
