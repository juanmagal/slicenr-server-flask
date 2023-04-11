# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.e_utran_cell_relation_single_all_of_attributes import EUtranCellRelationSingleAllOfAttributes
from openapi_server.models.managed_nf_service_single import ManagedNFServiceSingle
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle
from openapi_server.models.trace_job_single import TraceJobSingle
from openapi_server.models.vs_data_container_single import VsDataContainerSingle
from openapi_server import util

from openapi_server.models.e_utran_cell_relation_single_all_of_attributes import EUtranCellRelationSingleAllOfAttributes  # noqa: E501
from openapi_server.models.managed_nf_service_single import ManagedNFServiceSingle  # noqa: E501
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle  # noqa: E501
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle  # noqa: E501
from openapi_server.models.trace_job_single import TraceJobSingle  # noqa: E501
from openapi_server.models.vs_data_container_single import VsDataContainerSingle  # noqa: E501

class EUtranCellRelationSingle(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, object_class=None, object_instance=None, vs_data_container=None, attributes=None, perf_metric_job=None, threshold_monitor=None, managed_nf_service=None, trace_job=None):  # noqa: E501
        """EUtranCellRelationSingle - a model defined in OpenAPI

        :param id: The id of this EUtranCellRelationSingle.  # noqa: E501
        :type id: str
        :param object_class: The object_class of this EUtranCellRelationSingle.  # noqa: E501
        :type object_class: str
        :param object_instance: The object_instance of this EUtranCellRelationSingle.  # noqa: E501
        :type object_instance: str
        :param vs_data_container: The vs_data_container of this EUtranCellRelationSingle.  # noqa: E501
        :type vs_data_container: List[VsDataContainerSingle]
        :param attributes: The attributes of this EUtranCellRelationSingle.  # noqa: E501
        :type attributes: EUtranCellRelationSingleAllOfAttributes
        :param perf_metric_job: The perf_metric_job of this EUtranCellRelationSingle.  # noqa: E501
        :type perf_metric_job: List[PerfMetricJobSingle]
        :param threshold_monitor: The threshold_monitor of this EUtranCellRelationSingle.  # noqa: E501
        :type threshold_monitor: List[ThresholdMonitorSingle]
        :param managed_nf_service: The managed_nf_service of this EUtranCellRelationSingle.  # noqa: E501
        :type managed_nf_service: List[ManagedNFServiceSingle]
        :param trace_job: The trace_job of this EUtranCellRelationSingle.  # noqa: E501
        :type trace_job: List[TraceJobSingle]
        """
        self.openapi_types = {
            'id': str,
            'object_class': str,
            'object_instance': str,
            'vs_data_container': List[VsDataContainerSingle],
            'attributes': EUtranCellRelationSingleAllOfAttributes,
            'perf_metric_job': List[PerfMetricJobSingle],
            'threshold_monitor': List[ThresholdMonitorSingle],
            'managed_nf_service': List[ManagedNFServiceSingle],
            'trace_job': List[TraceJobSingle]
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
            'trace_job': 'TraceJob'
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

    @classmethod
    def from_dict(cls, dikt) -> 'EUtranCellRelationSingle':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EUtranCellRelation-Single of this EUtranCellRelationSingle.  # noqa: E501
        :rtype: EUtranCellRelationSingle
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this EUtranCellRelationSingle.


        :return: The id of this EUtranCellRelationSingle.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EUtranCellRelationSingle.


        :param id: The id of this EUtranCellRelationSingle.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def object_class(self):
        """Gets the object_class of this EUtranCellRelationSingle.


        :return: The object_class of this EUtranCellRelationSingle.
        :rtype: str
        """
        return self._object_class

    @object_class.setter
    def object_class(self, object_class):
        """Sets the object_class of this EUtranCellRelationSingle.


        :param object_class: The object_class of this EUtranCellRelationSingle.
        :type object_class: str
        """

        self._object_class = object_class

    @property
    def object_instance(self):
        """Gets the object_instance of this EUtranCellRelationSingle.


        :return: The object_instance of this EUtranCellRelationSingle.
        :rtype: str
        """
        return self._object_instance

    @object_instance.setter
    def object_instance(self, object_instance):
        """Sets the object_instance of this EUtranCellRelationSingle.


        :param object_instance: The object_instance of this EUtranCellRelationSingle.
        :type object_instance: str
        """

        self._object_instance = object_instance

    @property
    def vs_data_container(self):
        """Gets the vs_data_container of this EUtranCellRelationSingle.


        :return: The vs_data_container of this EUtranCellRelationSingle.
        :rtype: List[VsDataContainerSingle]
        """
        return self._vs_data_container

    @vs_data_container.setter
    def vs_data_container(self, vs_data_container):
        """Sets the vs_data_container of this EUtranCellRelationSingle.


        :param vs_data_container: The vs_data_container of this EUtranCellRelationSingle.
        :type vs_data_container: List[VsDataContainerSingle]
        """

        self._vs_data_container = vs_data_container

    @property
    def attributes(self):
        """Gets the attributes of this EUtranCellRelationSingle.


        :return: The attributes of this EUtranCellRelationSingle.
        :rtype: EUtranCellRelationSingleAllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this EUtranCellRelationSingle.


        :param attributes: The attributes of this EUtranCellRelationSingle.
        :type attributes: EUtranCellRelationSingleAllOfAttributes
        """

        self._attributes = attributes

    @property
    def perf_metric_job(self):
        """Gets the perf_metric_job of this EUtranCellRelationSingle.


        :return: The perf_metric_job of this EUtranCellRelationSingle.
        :rtype: List[PerfMetricJobSingle]
        """
        return self._perf_metric_job

    @perf_metric_job.setter
    def perf_metric_job(self, perf_metric_job):
        """Sets the perf_metric_job of this EUtranCellRelationSingle.


        :param perf_metric_job: The perf_metric_job of this EUtranCellRelationSingle.
        :type perf_metric_job: List[PerfMetricJobSingle]
        """

        self._perf_metric_job = perf_metric_job

    @property
    def threshold_monitor(self):
        """Gets the threshold_monitor of this EUtranCellRelationSingle.


        :return: The threshold_monitor of this EUtranCellRelationSingle.
        :rtype: List[ThresholdMonitorSingle]
        """
        return self._threshold_monitor

    @threshold_monitor.setter
    def threshold_monitor(self, threshold_monitor):
        """Sets the threshold_monitor of this EUtranCellRelationSingle.


        :param threshold_monitor: The threshold_monitor of this EUtranCellRelationSingle.
        :type threshold_monitor: List[ThresholdMonitorSingle]
        """

        self._threshold_monitor = threshold_monitor

    @property
    def managed_nf_service(self):
        """Gets the managed_nf_service of this EUtranCellRelationSingle.


        :return: The managed_nf_service of this EUtranCellRelationSingle.
        :rtype: List[ManagedNFServiceSingle]
        """
        return self._managed_nf_service

    @managed_nf_service.setter
    def managed_nf_service(self, managed_nf_service):
        """Sets the managed_nf_service of this EUtranCellRelationSingle.


        :param managed_nf_service: The managed_nf_service of this EUtranCellRelationSingle.
        :type managed_nf_service: List[ManagedNFServiceSingle]
        """

        self._managed_nf_service = managed_nf_service

    @property
    def trace_job(self):
        """Gets the trace_job of this EUtranCellRelationSingle.


        :return: The trace_job of this EUtranCellRelationSingle.
        :rtype: List[TraceJobSingle]
        """
        return self._trace_job

    @trace_job.setter
    def trace_job(self, trace_job):
        """Sets the trace_job of this EUtranCellRelationSingle.


        :param trace_job: The trace_job of this EUtranCellRelationSingle.
        :type trace_job: List[TraceJobSingle]
        """

        self._trace_job = trace_job
