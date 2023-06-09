# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.alarm_list_single import AlarmListSingle
from openapi_server.models.file_download_job_single import FileDownloadJobSingle
from openapi_server.models.files_single import FilesSingle
from openapi_server.models.mns_agent_single import MnsAgentSingle
from openapi_server.models.ntf_subscription_control_single import NtfSubscriptionControlSingle
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle
from openapi_server.models.trace_job_single import TraceJobSingle
from openapi_server import util

from openapi_server.models.alarm_list_single import AlarmListSingle  # noqa: E501
from openapi_server.models.file_download_job_single import FileDownloadJobSingle  # noqa: E501
from openapi_server.models.files_single import FilesSingle  # noqa: E501
from openapi_server.models.mns_agent_single import MnsAgentSingle  # noqa: E501
from openapi_server.models.ntf_subscription_control_single import NtfSubscriptionControlSingle  # noqa: E501
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle  # noqa: E501
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle  # noqa: E501
from openapi_server.models.trace_job_single import TraceJobSingle  # noqa: E501

class ManagedElementNcO(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, mns_agent=None, perf_metric_job=None, threshold_monitor=None, trace_job=None, ntf_subscription_control=None, alarm_list=None, file_download_job=None, files=None):  # noqa: E501
        """ManagedElementNcO - a model defined in OpenAPI

        :param mns_agent: The mns_agent of this ManagedElementNcO.  # noqa: E501
        :type mns_agent: List[MnsAgentSingle]
        :param perf_metric_job: The perf_metric_job of this ManagedElementNcO.  # noqa: E501
        :type perf_metric_job: List[PerfMetricJobSingle]
        :param threshold_monitor: The threshold_monitor of this ManagedElementNcO.  # noqa: E501
        :type threshold_monitor: List[ThresholdMonitorSingle]
        :param trace_job: The trace_job of this ManagedElementNcO.  # noqa: E501
        :type trace_job: List[TraceJobSingle]
        :param ntf_subscription_control: The ntf_subscription_control of this ManagedElementNcO.  # noqa: E501
        :type ntf_subscription_control: List[NtfSubscriptionControlSingle]
        :param alarm_list: The alarm_list of this ManagedElementNcO.  # noqa: E501
        :type alarm_list: AlarmListSingle
        :param file_download_job: The file_download_job of this ManagedElementNcO.  # noqa: E501
        :type file_download_job: List[FileDownloadJobSingle]
        :param files: The files of this ManagedElementNcO.  # noqa: E501
        :type files: List[FilesSingle]
        """
        self.openapi_types = {
            'mns_agent': List[MnsAgentSingle],
            'perf_metric_job': List[PerfMetricJobSingle],
            'threshold_monitor': List[ThresholdMonitorSingle],
            'trace_job': List[TraceJobSingle],
            'ntf_subscription_control': List[NtfSubscriptionControlSingle],
            'alarm_list': AlarmListSingle,
            'file_download_job': List[FileDownloadJobSingle],
            'files': List[FilesSingle]
        }

        self.attribute_map = {
            'mns_agent': 'MnsAgent',
            'perf_metric_job': 'PerfMetricJob',
            'threshold_monitor': 'ThresholdMonitor',
            'trace_job': 'TraceJob',
            'ntf_subscription_control': 'NtfSubscriptionControl',
            'alarm_list': 'AlarmList',
            'file_download_job': 'FileDownloadJob',
            'files': 'Files'
        }

        self._mns_agent = mns_agent
        self._perf_metric_job = perf_metric_job
        self._threshold_monitor = threshold_monitor
        self._trace_job = trace_job
        self._ntf_subscription_control = ntf_subscription_control
        self._alarm_list = alarm_list
        self._file_download_job = file_download_job
        self._files = files

    @classmethod
    def from_dict(cls, dikt) -> 'ManagedElementNcO':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ManagedElement-ncO of this ManagedElementNcO.  # noqa: E501
        :rtype: ManagedElementNcO
        """
        return util.deserialize_model(dikt, cls)

    @property
    def mns_agent(self):
        """Gets the mns_agent of this ManagedElementNcO.


        :return: The mns_agent of this ManagedElementNcO.
        :rtype: List[MnsAgentSingle]
        """
        return self._mns_agent

    @mns_agent.setter
    def mns_agent(self, mns_agent):
        """Sets the mns_agent of this ManagedElementNcO.


        :param mns_agent: The mns_agent of this ManagedElementNcO.
        :type mns_agent: List[MnsAgentSingle]
        """

        self._mns_agent = mns_agent

    @property
    def perf_metric_job(self):
        """Gets the perf_metric_job of this ManagedElementNcO.


        :return: The perf_metric_job of this ManagedElementNcO.
        :rtype: List[PerfMetricJobSingle]
        """
        return self._perf_metric_job

    @perf_metric_job.setter
    def perf_metric_job(self, perf_metric_job):
        """Sets the perf_metric_job of this ManagedElementNcO.


        :param perf_metric_job: The perf_metric_job of this ManagedElementNcO.
        :type perf_metric_job: List[PerfMetricJobSingle]
        """

        self._perf_metric_job = perf_metric_job

    @property
    def threshold_monitor(self):
        """Gets the threshold_monitor of this ManagedElementNcO.


        :return: The threshold_monitor of this ManagedElementNcO.
        :rtype: List[ThresholdMonitorSingle]
        """
        return self._threshold_monitor

    @threshold_monitor.setter
    def threshold_monitor(self, threshold_monitor):
        """Sets the threshold_monitor of this ManagedElementNcO.


        :param threshold_monitor: The threshold_monitor of this ManagedElementNcO.
        :type threshold_monitor: List[ThresholdMonitorSingle]
        """

        self._threshold_monitor = threshold_monitor

    @property
    def trace_job(self):
        """Gets the trace_job of this ManagedElementNcO.


        :return: The trace_job of this ManagedElementNcO.
        :rtype: List[TraceJobSingle]
        """
        return self._trace_job

    @trace_job.setter
    def trace_job(self, trace_job):
        """Sets the trace_job of this ManagedElementNcO.


        :param trace_job: The trace_job of this ManagedElementNcO.
        :type trace_job: List[TraceJobSingle]
        """

        self._trace_job = trace_job

    @property
    def ntf_subscription_control(self):
        """Gets the ntf_subscription_control of this ManagedElementNcO.


        :return: The ntf_subscription_control of this ManagedElementNcO.
        :rtype: List[NtfSubscriptionControlSingle]
        """
        return self._ntf_subscription_control

    @ntf_subscription_control.setter
    def ntf_subscription_control(self, ntf_subscription_control):
        """Sets the ntf_subscription_control of this ManagedElementNcO.


        :param ntf_subscription_control: The ntf_subscription_control of this ManagedElementNcO.
        :type ntf_subscription_control: List[NtfSubscriptionControlSingle]
        """

        self._ntf_subscription_control = ntf_subscription_control

    @property
    def alarm_list(self):
        """Gets the alarm_list of this ManagedElementNcO.


        :return: The alarm_list of this ManagedElementNcO.
        :rtype: AlarmListSingle
        """
        return self._alarm_list

    @alarm_list.setter
    def alarm_list(self, alarm_list):
        """Sets the alarm_list of this ManagedElementNcO.


        :param alarm_list: The alarm_list of this ManagedElementNcO.
        :type alarm_list: AlarmListSingle
        """

        self._alarm_list = alarm_list

    @property
    def file_download_job(self):
        """Gets the file_download_job of this ManagedElementNcO.


        :return: The file_download_job of this ManagedElementNcO.
        :rtype: List[FileDownloadJobSingle]
        """
        return self._file_download_job

    @file_download_job.setter
    def file_download_job(self, file_download_job):
        """Sets the file_download_job of this ManagedElementNcO.


        :param file_download_job: The file_download_job of this ManagedElementNcO.
        :type file_download_job: List[FileDownloadJobSingle]
        """

        self._file_download_job = file_download_job

    @property
    def files(self):
        """Gets the files of this ManagedElementNcO.


        :return: The files of this ManagedElementNcO.
        :rtype: List[FilesSingle]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this ManagedElementNcO.


        :param files: The files of this ManagedElementNcO.
        :type files: List[FilesSingle]
        """

        self._files = files
