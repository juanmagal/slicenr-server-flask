# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.external_enb_function_single_all_of_attributes import ExternalENBFunctionSingleAllOfAttributes
from openapi_server.models.external_eu_tran_cell_single import ExternalEUTranCellSingle
from openapi_server.models.managed_nf_service_single import ManagedNFServiceSingle
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle
from openapi_server.models.trace_job_single import TraceJobSingle
from openapi_server.models.vs_data_container_single import VsDataContainerSingle
from openapi_server import util

from openapi_server.models.external_enb_function_single_all_of_attributes import ExternalENBFunctionSingleAllOfAttributes  # noqa: E501
from openapi_server.models.external_eu_tran_cell_single import ExternalEUTranCellSingle  # noqa: E501
from openapi_server.models.managed_nf_service_single import ManagedNFServiceSingle  # noqa: E501
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle  # noqa: E501
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle  # noqa: E501
from openapi_server.models.trace_job_single import TraceJobSingle  # noqa: E501
from openapi_server.models.vs_data_container_single import VsDataContainerSingle  # noqa: E501

class ExternalENBFunctionSingle(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, object_class=None, object_instance=None, vs_data_container=None, attributes=None, perf_metric_job=None, threshold_monitor=None, managed_nf_service=None, trace_job=None, external_eu_tran_cell=None):  # noqa: E501
        """ExternalENBFunctionSingle - a model defined in OpenAPI

        :param id: The id of this ExternalENBFunctionSingle.  # noqa: E501
        :type id: str
        :param object_class: The object_class of this ExternalENBFunctionSingle.  # noqa: E501
        :type object_class: str
        :param object_instance: The object_instance of this ExternalENBFunctionSingle.  # noqa: E501
        :type object_instance: str
        :param vs_data_container: The vs_data_container of this ExternalENBFunctionSingle.  # noqa: E501
        :type vs_data_container: List[VsDataContainerSingle]
        :param attributes: The attributes of this ExternalENBFunctionSingle.  # noqa: E501
        :type attributes: ExternalENBFunctionSingleAllOfAttributes
        :param perf_metric_job: The perf_metric_job of this ExternalENBFunctionSingle.  # noqa: E501
        :type perf_metric_job: List[PerfMetricJobSingle]
        :param threshold_monitor: The threshold_monitor of this ExternalENBFunctionSingle.  # noqa: E501
        :type threshold_monitor: List[ThresholdMonitorSingle]
        :param managed_nf_service: The managed_nf_service of this ExternalENBFunctionSingle.  # noqa: E501
        :type managed_nf_service: List[ManagedNFServiceSingle]
        :param trace_job: The trace_job of this ExternalENBFunctionSingle.  # noqa: E501
        :type trace_job: List[TraceJobSingle]
        :param external_eu_tran_cell: The external_eu_tran_cell of this ExternalENBFunctionSingle.  # noqa: E501
        :type external_eu_tran_cell: List[ExternalEUTranCellSingle]
        """
        self.openapi_types = {
            'id': str,
            'object_class': str,
            'object_instance': str,
            'vs_data_container': List[VsDataContainerSingle],
            'attributes': ExternalENBFunctionSingleAllOfAttributes,
            'perf_metric_job': List[PerfMetricJobSingle],
            'threshold_monitor': List[ThresholdMonitorSingle],
            'managed_nf_service': List[ManagedNFServiceSingle],
            'trace_job': List[TraceJobSingle],
            'external_eu_tran_cell': List[ExternalEUTranCellSingle]
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
            'external_eu_tran_cell': 'ExternalEUTranCell'
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
        self._external_eu_tran_cell = external_eu_tran_cell

    @classmethod
    def from_dict(cls, dikt) -> 'ExternalENBFunctionSingle':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExternalENBFunction-Single of this ExternalENBFunctionSingle.  # noqa: E501
        :rtype: ExternalENBFunctionSingle
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this ExternalENBFunctionSingle.


        :return: The id of this ExternalENBFunctionSingle.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExternalENBFunctionSingle.


        :param id: The id of this ExternalENBFunctionSingle.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def object_class(self):
        """Gets the object_class of this ExternalENBFunctionSingle.


        :return: The object_class of this ExternalENBFunctionSingle.
        :rtype: str
        """
        return self._object_class

    @object_class.setter
    def object_class(self, object_class):
        """Sets the object_class of this ExternalENBFunctionSingle.


        :param object_class: The object_class of this ExternalENBFunctionSingle.
        :type object_class: str
        """

        self._object_class = object_class

    @property
    def object_instance(self):
        """Gets the object_instance of this ExternalENBFunctionSingle.


        :return: The object_instance of this ExternalENBFunctionSingle.
        :rtype: str
        """
        return self._object_instance

    @object_instance.setter
    def object_instance(self, object_instance):
        """Sets the object_instance of this ExternalENBFunctionSingle.


        :param object_instance: The object_instance of this ExternalENBFunctionSingle.
        :type object_instance: str
        """

        self._object_instance = object_instance

    @property
    def vs_data_container(self):
        """Gets the vs_data_container of this ExternalENBFunctionSingle.


        :return: The vs_data_container of this ExternalENBFunctionSingle.
        :rtype: List[VsDataContainerSingle]
        """
        return self._vs_data_container

    @vs_data_container.setter
    def vs_data_container(self, vs_data_container):
        """Sets the vs_data_container of this ExternalENBFunctionSingle.


        :param vs_data_container: The vs_data_container of this ExternalENBFunctionSingle.
        :type vs_data_container: List[VsDataContainerSingle]
        """

        self._vs_data_container = vs_data_container

    @property
    def attributes(self):
        """Gets the attributes of this ExternalENBFunctionSingle.


        :return: The attributes of this ExternalENBFunctionSingle.
        :rtype: ExternalENBFunctionSingleAllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this ExternalENBFunctionSingle.


        :param attributes: The attributes of this ExternalENBFunctionSingle.
        :type attributes: ExternalENBFunctionSingleAllOfAttributes
        """

        self._attributes = attributes

    @property
    def perf_metric_job(self):
        """Gets the perf_metric_job of this ExternalENBFunctionSingle.


        :return: The perf_metric_job of this ExternalENBFunctionSingle.
        :rtype: List[PerfMetricJobSingle]
        """
        return self._perf_metric_job

    @perf_metric_job.setter
    def perf_metric_job(self, perf_metric_job):
        """Sets the perf_metric_job of this ExternalENBFunctionSingle.


        :param perf_metric_job: The perf_metric_job of this ExternalENBFunctionSingle.
        :type perf_metric_job: List[PerfMetricJobSingle]
        """

        self._perf_metric_job = perf_metric_job

    @property
    def threshold_monitor(self):
        """Gets the threshold_monitor of this ExternalENBFunctionSingle.


        :return: The threshold_monitor of this ExternalENBFunctionSingle.
        :rtype: List[ThresholdMonitorSingle]
        """
        return self._threshold_monitor

    @threshold_monitor.setter
    def threshold_monitor(self, threshold_monitor):
        """Sets the threshold_monitor of this ExternalENBFunctionSingle.


        :param threshold_monitor: The threshold_monitor of this ExternalENBFunctionSingle.
        :type threshold_monitor: List[ThresholdMonitorSingle]
        """

        self._threshold_monitor = threshold_monitor

    @property
    def managed_nf_service(self):
        """Gets the managed_nf_service of this ExternalENBFunctionSingle.


        :return: The managed_nf_service of this ExternalENBFunctionSingle.
        :rtype: List[ManagedNFServiceSingle]
        """
        return self._managed_nf_service

    @managed_nf_service.setter
    def managed_nf_service(self, managed_nf_service):
        """Sets the managed_nf_service of this ExternalENBFunctionSingle.


        :param managed_nf_service: The managed_nf_service of this ExternalENBFunctionSingle.
        :type managed_nf_service: List[ManagedNFServiceSingle]
        """

        self._managed_nf_service = managed_nf_service

    @property
    def trace_job(self):
        """Gets the trace_job of this ExternalENBFunctionSingle.


        :return: The trace_job of this ExternalENBFunctionSingle.
        :rtype: List[TraceJobSingle]
        """
        return self._trace_job

    @trace_job.setter
    def trace_job(self, trace_job):
        """Sets the trace_job of this ExternalENBFunctionSingle.


        :param trace_job: The trace_job of this ExternalENBFunctionSingle.
        :type trace_job: List[TraceJobSingle]
        """

        self._trace_job = trace_job

    @property
    def external_eu_tran_cell(self):
        """Gets the external_eu_tran_cell of this ExternalENBFunctionSingle.


        :return: The external_eu_tran_cell of this ExternalENBFunctionSingle.
        :rtype: List[ExternalEUTranCellSingle]
        """
        return self._external_eu_tran_cell

    @external_eu_tran_cell.setter
    def external_eu_tran_cell(self, external_eu_tran_cell):
        """Sets the external_eu_tran_cell of this ExternalENBFunctionSingle.


        :param external_eu_tran_cell: The external_eu_tran_cell of this ExternalENBFunctionSingle.
        :type external_eu_tran_cell: List[ExternalEUTranCellSingle]
        """

        self._external_eu_tran_cell = external_eu_tran_cell
