# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.epn22_single import EPN22Single
from openapi_server.models.epn31_single import EPN31Single
from openapi_server.models.managed_nf_service_single import ManagedNFServiceSingle
from openapi_server.models.nssf_function_single_all_of_attributes import NssfFunctionSingleAllOfAttributes
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle
from openapi_server.models.trace_job_single import TraceJobSingle
from openapi_server.models.vs_data_container_single import VsDataContainerSingle
from openapi_server import util

from openapi_server.models.epn22_single import EPN22Single  # noqa: E501
from openapi_server.models.epn31_single import EPN31Single  # noqa: E501
from openapi_server.models.managed_nf_service_single import ManagedNFServiceSingle  # noqa: E501
from openapi_server.models.nssf_function_single_all_of_attributes import NssfFunctionSingleAllOfAttributes  # noqa: E501
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle  # noqa: E501
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle  # noqa: E501
from openapi_server.models.trace_job_single import TraceJobSingle  # noqa: E501
from openapi_server.models.vs_data_container_single import VsDataContainerSingle  # noqa: E501

class NssfFunctionSingle(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, object_class=None, object_instance=None, vs_data_container=None, attributes=None, perf_metric_job=None, threshold_monitor=None, managed_nf_service=None, trace_job=None, ep_n22=None, ep_n31=None):  # noqa: E501
        """NssfFunctionSingle - a model defined in OpenAPI

        :param id: The id of this NssfFunctionSingle.  # noqa: E501
        :type id: str
        :param object_class: The object_class of this NssfFunctionSingle.  # noqa: E501
        :type object_class: str
        :param object_instance: The object_instance of this NssfFunctionSingle.  # noqa: E501
        :type object_instance: str
        :param vs_data_container: The vs_data_container of this NssfFunctionSingle.  # noqa: E501
        :type vs_data_container: List[VsDataContainerSingle]
        :param attributes: The attributes of this NssfFunctionSingle.  # noqa: E501
        :type attributes: NssfFunctionSingleAllOfAttributes
        :param perf_metric_job: The perf_metric_job of this NssfFunctionSingle.  # noqa: E501
        :type perf_metric_job: List[PerfMetricJobSingle]
        :param threshold_monitor: The threshold_monitor of this NssfFunctionSingle.  # noqa: E501
        :type threshold_monitor: List[ThresholdMonitorSingle]
        :param managed_nf_service: The managed_nf_service of this NssfFunctionSingle.  # noqa: E501
        :type managed_nf_service: List[ManagedNFServiceSingle]
        :param trace_job: The trace_job of this NssfFunctionSingle.  # noqa: E501
        :type trace_job: List[TraceJobSingle]
        :param ep_n22: The ep_n22 of this NssfFunctionSingle.  # noqa: E501
        :type ep_n22: List[EPN22Single]
        :param ep_n31: The ep_n31 of this NssfFunctionSingle.  # noqa: E501
        :type ep_n31: List[EPN31Single]
        """
        self.openapi_types = {
            'id': str,
            'object_class': str,
            'object_instance': str,
            'vs_data_container': List[VsDataContainerSingle],
            'attributes': NssfFunctionSingleAllOfAttributes,
            'perf_metric_job': List[PerfMetricJobSingle],
            'threshold_monitor': List[ThresholdMonitorSingle],
            'managed_nf_service': List[ManagedNFServiceSingle],
            'trace_job': List[TraceJobSingle],
            'ep_n22': List[EPN22Single],
            'ep_n31': List[EPN31Single]
        }

        self.attribute_map = {
            'id': 'id',
            'object_class': 'objectClass',
            'object_instance': 'objectInstance',
            'vs_data_container': 'VsDataContainer',
            'attributes': 'attributes',
            'perf_metric_job': 'PerfMetricJob',
            'threshold_monitor': 'ThresholdMonitor',
            'managed_nf_service': 'ManagedNFService',
            'trace_job': 'TraceJob',
            'ep_n22': 'EP_N22',
            'ep_n31': 'EP_N31'
        }

        self._id = id
        self._object_class = object_class
        self._object_instance = object_instance
        self._vs_data_container = vs_data_container
        self._attributes = attributes
        self._perf_metric_job = perf_metric_job
        self._threshold_monitor = threshold_monitor
        self._managed_nf_service = managed_nf_service
        self._trace_job = trace_job
        self._ep_n22 = ep_n22
        self._ep_n31 = ep_n31

    @classmethod
    def from_dict(cls, dikt) -> 'NssfFunctionSingle':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NssfFunction-Single of this NssfFunctionSingle.  # noqa: E501
        :rtype: NssfFunctionSingle
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this NssfFunctionSingle.


        :return: The id of this NssfFunctionSingle.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NssfFunctionSingle.


        :param id: The id of this NssfFunctionSingle.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def object_class(self):
        """Gets the object_class of this NssfFunctionSingle.


        :return: The object_class of this NssfFunctionSingle.
        :rtype: str
        """
        return self._object_class

    @object_class.setter
    def object_class(self, object_class):
        """Sets the object_class of this NssfFunctionSingle.


        :param object_class: The object_class of this NssfFunctionSingle.
        :type object_class: str
        """

        self._object_class = object_class

    @property
    def object_instance(self):
        """Gets the object_instance of this NssfFunctionSingle.


        :return: The object_instance of this NssfFunctionSingle.
        :rtype: str
        """
        return self._object_instance

    @object_instance.setter
    def object_instance(self, object_instance):
        """Sets the object_instance of this NssfFunctionSingle.


        :param object_instance: The object_instance of this NssfFunctionSingle.
        :type object_instance: str
        """

        self._object_instance = object_instance

    @property
    def vs_data_container(self):
        """Gets the vs_data_container of this NssfFunctionSingle.


        :return: The vs_data_container of this NssfFunctionSingle.
        :rtype: List[VsDataContainerSingle]
        """
        return self._vs_data_container

    @vs_data_container.setter
    def vs_data_container(self, vs_data_container):
        """Sets the vs_data_container of this NssfFunctionSingle.


        :param vs_data_container: The vs_data_container of this NssfFunctionSingle.
        :type vs_data_container: List[VsDataContainerSingle]
        """

        self._vs_data_container = vs_data_container

    @property
    def attributes(self):
        """Gets the attributes of this NssfFunctionSingle.


        :return: The attributes of this NssfFunctionSingle.
        :rtype: NssfFunctionSingleAllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this NssfFunctionSingle.


        :param attributes: The attributes of this NssfFunctionSingle.
        :type attributes: NssfFunctionSingleAllOfAttributes
        """

        self._attributes = attributes

    @property
    def perf_metric_job(self):
        """Gets the perf_metric_job of this NssfFunctionSingle.


        :return: The perf_metric_job of this NssfFunctionSingle.
        :rtype: List[PerfMetricJobSingle]
        """
        return self._perf_metric_job

    @perf_metric_job.setter
    def perf_metric_job(self, perf_metric_job):
        """Sets the perf_metric_job of this NssfFunctionSingle.


        :param perf_metric_job: The perf_metric_job of this NssfFunctionSingle.
        :type perf_metric_job: List[PerfMetricJobSingle]
        """

        self._perf_metric_job = perf_metric_job

    @property
    def threshold_monitor(self):
        """Gets the threshold_monitor of this NssfFunctionSingle.


        :return: The threshold_monitor of this NssfFunctionSingle.
        :rtype: List[ThresholdMonitorSingle]
        """
        return self._threshold_monitor

    @threshold_monitor.setter
    def threshold_monitor(self, threshold_monitor):
        """Sets the threshold_monitor of this NssfFunctionSingle.


        :param threshold_monitor: The threshold_monitor of this NssfFunctionSingle.
        :type threshold_monitor: List[ThresholdMonitorSingle]
        """

        self._threshold_monitor = threshold_monitor

    @property
    def managed_nf_service(self):
        """Gets the managed_nf_service of this NssfFunctionSingle.


        :return: The managed_nf_service of this NssfFunctionSingle.
        :rtype: List[ManagedNFServiceSingle]
        """
        return self._managed_nf_service

    @managed_nf_service.setter
    def managed_nf_service(self, managed_nf_service):
        """Sets the managed_nf_service of this NssfFunctionSingle.


        :param managed_nf_service: The managed_nf_service of this NssfFunctionSingle.
        :type managed_nf_service: List[ManagedNFServiceSingle]
        """

        self._managed_nf_service = managed_nf_service

    @property
    def trace_job(self):
        """Gets the trace_job of this NssfFunctionSingle.


        :return: The trace_job of this NssfFunctionSingle.
        :rtype: List[TraceJobSingle]
        """
        return self._trace_job

    @trace_job.setter
    def trace_job(self, trace_job):
        """Sets the trace_job of this NssfFunctionSingle.


        :param trace_job: The trace_job of this NssfFunctionSingle.
        :type trace_job: List[TraceJobSingle]
        """

        self._trace_job = trace_job

    @property
    def ep_n22(self):
        """Gets the ep_n22 of this NssfFunctionSingle.


        :return: The ep_n22 of this NssfFunctionSingle.
        :rtype: List[EPN22Single]
        """
        return self._ep_n22

    @ep_n22.setter
    def ep_n22(self, ep_n22):
        """Sets the ep_n22 of this NssfFunctionSingle.


        :param ep_n22: The ep_n22 of this NssfFunctionSingle.
        :type ep_n22: List[EPN22Single]
        """

        self._ep_n22 = ep_n22

    @property
    def ep_n31(self):
        """Gets the ep_n31 of this NssfFunctionSingle.


        :return: The ep_n31 of this NssfFunctionSingle.
        :rtype: List[EPN31Single]
        """
        return self._ep_n31

    @ep_n31.setter
    def ep_n31(self, ep_n31):
        """Sets the ep_n31 of this NssfFunctionSingle.


        :param ep_n31: The ep_n31 of this NssfFunctionSingle.
        :type ep_n31: List[EPN31Single]
        """

        self._ep_n31 = ep_n31
