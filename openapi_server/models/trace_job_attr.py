# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.anonymization_of_mdt_data_type import AnonymizationOfMDTDataType
from openapi_server.models.area_config import AreaConfig
from openapi_server.models.area_scope import AreaScope
from openapi_server.models.collection_period_m6_lte_type import CollectionPeriodM6LTEType
from openapi_server.models.collection_period_m6_nr_type import CollectionPeriodM6NRType
from openapi_server.models.collection_period_rrmlte_type import CollectionPeriodRRMLTEType
from openapi_server.models.collection_period_rrmnr_type import CollectionPeriodRRMNRType
from openapi_server.models.collection_period_rrmumts_type import CollectionPeriodRRMUMTSType
from openapi_server.models.event_list_for_event_triggered_measurement_type import EventListForEventTriggeredMeasurementType
from openapi_server.models.event_threshold_l1_type import EventThresholdL1Type
from openapi_server.models.event_threshold_type import EventThresholdType
from openapi_server.models.ip_addr import IpAddr
from openapi_server.models.job_type_type import JobTypeType
from openapi_server.models.list_of_interfaces_type import ListOfInterfacesType
from openapi_server.models.list_of_measurements_type import ListOfMeasurementsType
from openapi_server.models.logging_duration_type import LoggingDurationType
from openapi_server.models.logging_interval_type import LoggingIntervalType
from openapi_server.models.mbsfn_area import MbsfnArea
from openapi_server.models.measurement_period_lte_type import MeasurementPeriodLTEType
from openapi_server.models.measurement_period_umts_type import MeasurementPeriodUMTSType
from openapi_server.models.measurement_quantity_type import MeasurementQuantityType
from openapi_server.models.plmn_list_type_inner import PLMNListTypeInner
from openapi_server.models.plmn_target_type import PLMNTargetType
from openapi_server.models.positioning_method_type import PositioningMethodType
from openapi_server.models.report_amount_type import ReportAmountType
from openapi_server.models.report_interval_type import ReportIntervalType
from openapi_server.models.report_type_type import ReportTypeType
from openapi_server.models.time_to_trigger_l1_type import TimeToTriggerL1Type
from openapi_server.models.trace_depth_type import TraceDepthType
from openapi_server.models.trace_reference_type import TraceReferenceType
from openapi_server.models.trace_reporting_format_type import TraceReportingFormatType
from openapi_server.models.trace_target_type import TraceTargetType
from openapi_server.models.triggering_events_type import TriggeringEventsType
from openapi_server import util

from openapi_server.models.anonymization_of_mdt_data_type import AnonymizationOfMDTDataType  # noqa: E501
from openapi_server.models.area_config import AreaConfig  # noqa: E501
from openapi_server.models.area_scope import AreaScope  # noqa: E501
from openapi_server.models.collection_period_m6_lte_type import CollectionPeriodM6LTEType  # noqa: E501
from openapi_server.models.collection_period_m6_nr_type import CollectionPeriodM6NRType  # noqa: E501
from openapi_server.models.collection_period_rrmlte_type import CollectionPeriodRRMLTEType  # noqa: E501
from openapi_server.models.collection_period_rrmnr_type import CollectionPeriodRRMNRType  # noqa: E501
from openapi_server.models.collection_period_rrmumts_type import CollectionPeriodRRMUMTSType  # noqa: E501
from openapi_server.models.event_list_for_event_triggered_measurement_type import EventListForEventTriggeredMeasurementType  # noqa: E501
from openapi_server.models.event_threshold_l1_type import EventThresholdL1Type  # noqa: E501
from openapi_server.models.event_threshold_type import EventThresholdType  # noqa: E501
from openapi_server.models.ip_addr import IpAddr  # noqa: E501
from openapi_server.models.job_type_type import JobTypeType  # noqa: E501
from openapi_server.models.list_of_interfaces_type import ListOfInterfacesType  # noqa: E501
from openapi_server.models.list_of_measurements_type import ListOfMeasurementsType  # noqa: E501
from openapi_server.models.logging_duration_type import LoggingDurationType  # noqa: E501
from openapi_server.models.logging_interval_type import LoggingIntervalType  # noqa: E501
from openapi_server.models.mbsfn_area import MbsfnArea  # noqa: E501
from openapi_server.models.measurement_period_lte_type import MeasurementPeriodLTEType  # noqa: E501
from openapi_server.models.measurement_period_umts_type import MeasurementPeriodUMTSType  # noqa: E501
from openapi_server.models.measurement_quantity_type import MeasurementQuantityType  # noqa: E501
from openapi_server.models.plmn_list_type_inner import PLMNListTypeInner  # noqa: E501
from openapi_server.models.plmn_target_type import PLMNTargetType  # noqa: E501
from openapi_server.models.positioning_method_type import PositioningMethodType  # noqa: E501
from openapi_server.models.report_amount_type import ReportAmountType  # noqa: E501
from openapi_server.models.report_interval_type import ReportIntervalType  # noqa: E501
from openapi_server.models.report_type_type import ReportTypeType  # noqa: E501
from openapi_server.models.time_to_trigger_l1_type import TimeToTriggerL1Type  # noqa: E501
from openapi_server.models.trace_depth_type import TraceDepthType  # noqa: E501
from openapi_server.models.trace_reference_type import TraceReferenceType  # noqa: E501
from openapi_server.models.trace_reporting_format_type import TraceReportingFormatType  # noqa: E501
from openapi_server.models.trace_target_type import TraceTargetType  # noqa: E501
from openapi_server.models.triggering_events_type import TriggeringEventsType  # noqa: E501

class TraceJobAttr(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, job_type=None, list_of_interfaces=None, list_of_ne_types=None, p_lmn_target=None, trace_reporting_consumer_uri=None, trace_collection_entity_ip_address=None, trace_depth=None, trace_reference=None, trace_recording_session_reference=None, job_id=None, trace_reporting_format=None, trace_target=None, triggering_events=None, anonymization_of_mdt_data=None, area_configuration_for_neigh_cell=None, area_scope=None, beam_level_measurement=None, collection_period_rrmlte=None, collection_period_m6_lte=None, collection_period_m7_lte=None, collection_period_rrmumts=None, collection_period_rrmnr=None, collection_period_m6_nr=None, collection_period_m7_nr=None, event_list_for_event_triggered_measurement=None, event_threshold=None, list_of_measurements=None, logging_duration=None, logging_interval=None, event_threshold_l1=None, hysteresis_l1=None, time_to_trigger_l1=None, m_bsfn_area_list=None, measurement_period_lte=None, measurement_period_umts=None, measurement_quantity=None, event_threshold_uph_umts=None, p_lmn_list=None, positioning_method=None, report_amount=None, reporting_trigger=None, report_interval=None, report_type=None, sensor_information=None, trace_collection_entity_id=None, excess_packet_delay_thresholds=None):  # noqa: E501
        """TraceJobAttr - a model defined in OpenAPI

        :param job_type: The job_type of this TraceJobAttr.  # noqa: E501
        :type job_type: JobTypeType
        :param list_of_interfaces: The list_of_interfaces of this TraceJobAttr.  # noqa: E501
        :type list_of_interfaces: ListOfInterfacesType
        :param list_of_ne_types: The list_of_ne_types of this TraceJobAttr.  # noqa: E501
        :type list_of_ne_types: List[str]
        :param p_lmn_target: The p_lmn_target of this TraceJobAttr.  # noqa: E501
        :type p_lmn_target: PLMNTargetType
        :param trace_reporting_consumer_uri: The trace_reporting_consumer_uri of this TraceJobAttr.  # noqa: E501
        :type trace_reporting_consumer_uri: str
        :param trace_collection_entity_ip_address: The trace_collection_entity_ip_address of this TraceJobAttr.  # noqa: E501
        :type trace_collection_entity_ip_address: IpAddr
        :param trace_depth: The trace_depth of this TraceJobAttr.  # noqa: E501
        :type trace_depth: TraceDepthType
        :param trace_reference: The trace_reference of this TraceJobAttr.  # noqa: E501
        :type trace_reference: TraceReferenceType
        :param trace_recording_session_reference: The trace_recording_session_reference of this TraceJobAttr.  # noqa: E501
        :type trace_recording_session_reference: str
        :param job_id: The job_id of this TraceJobAttr.  # noqa: E501
        :type job_id: str
        :param trace_reporting_format: The trace_reporting_format of this TraceJobAttr.  # noqa: E501
        :type trace_reporting_format: TraceReportingFormatType
        :param trace_target: The trace_target of this TraceJobAttr.  # noqa: E501
        :type trace_target: TraceTargetType
        :param triggering_events: The triggering_events of this TraceJobAttr.  # noqa: E501
        :type triggering_events: TriggeringEventsType
        :param anonymization_of_mdt_data: The anonymization_of_mdt_data of this TraceJobAttr.  # noqa: E501
        :type anonymization_of_mdt_data: AnonymizationOfMDTDataType
        :param area_configuration_for_neigh_cell: The area_configuration_for_neigh_cell of this TraceJobAttr.  # noqa: E501
        :type area_configuration_for_neigh_cell: AreaConfig
        :param area_scope: The area_scope of this TraceJobAttr.  # noqa: E501
        :type area_scope: List[AreaScope]
        :param beam_level_measurement: The beam_level_measurement of this TraceJobAttr.  # noqa: E501
        :type beam_level_measurement: bool
        :param collection_period_rrmlte: The collection_period_rrmlte of this TraceJobAttr.  # noqa: E501
        :type collection_period_rrmlte: CollectionPeriodRRMLTEType
        :param collection_period_m6_lte: The collection_period_m6_lte of this TraceJobAttr.  # noqa: E501
        :type collection_period_m6_lte: CollectionPeriodM6LTEType
        :param collection_period_m7_lte: The collection_period_m7_lte of this TraceJobAttr.  # noqa: E501
        :type collection_period_m7_lte: int
        :param collection_period_rrmumts: The collection_period_rrmumts of this TraceJobAttr.  # noqa: E501
        :type collection_period_rrmumts: CollectionPeriodRRMUMTSType
        :param collection_period_rrmnr: The collection_period_rrmnr of this TraceJobAttr.  # noqa: E501
        :type collection_period_rrmnr: CollectionPeriodRRMNRType
        :param collection_period_m6_nr: The collection_period_m6_nr of this TraceJobAttr.  # noqa: E501
        :type collection_period_m6_nr: CollectionPeriodM6NRType
        :param collection_period_m7_nr: The collection_period_m7_nr of this TraceJobAttr.  # noqa: E501
        :type collection_period_m7_nr: int
        :param event_list_for_event_triggered_measurement: The event_list_for_event_triggered_measurement of this TraceJobAttr.  # noqa: E501
        :type event_list_for_event_triggered_measurement: EventListForEventTriggeredMeasurementType
        :param event_threshold: The event_threshold of this TraceJobAttr.  # noqa: E501
        :type event_threshold: EventThresholdType
        :param list_of_measurements: The list_of_measurements of this TraceJobAttr.  # noqa: E501
        :type list_of_measurements: ListOfMeasurementsType
        :param logging_duration: The logging_duration of this TraceJobAttr.  # noqa: E501
        :type logging_duration: LoggingDurationType
        :param logging_interval: The logging_interval of this TraceJobAttr.  # noqa: E501
        :type logging_interval: LoggingIntervalType
        :param event_threshold_l1: The event_threshold_l1 of this TraceJobAttr.  # noqa: E501
        :type event_threshold_l1: EventThresholdL1Type
        :param hysteresis_l1: The hysteresis_l1 of this TraceJobAttr.  # noqa: E501
        :type hysteresis_l1: int
        :param time_to_trigger_l1: The time_to_trigger_l1 of this TraceJobAttr.  # noqa: E501
        :type time_to_trigger_l1: TimeToTriggerL1Type
        :param m_bsfn_area_list: The m_bsfn_area_list of this TraceJobAttr.  # noqa: E501
        :type m_bsfn_area_list: List[MbsfnArea]
        :param measurement_period_lte: The measurement_period_lte of this TraceJobAttr.  # noqa: E501
        :type measurement_period_lte: MeasurementPeriodLTEType
        :param measurement_period_umts: The measurement_period_umts of this TraceJobAttr.  # noqa: E501
        :type measurement_period_umts: MeasurementPeriodUMTSType
        :param measurement_quantity: The measurement_quantity of this TraceJobAttr.  # noqa: E501
        :type measurement_quantity: MeasurementQuantityType
        :param event_threshold_uph_umts: The event_threshold_uph_umts of this TraceJobAttr.  # noqa: E501
        :type event_threshold_uph_umts: int
        :param p_lmn_list: The p_lmn_list of this TraceJobAttr.  # noqa: E501
        :type p_lmn_list: List[PLMNListTypeInner]
        :param positioning_method: The positioning_method of this TraceJobAttr.  # noqa: E501
        :type positioning_method: PositioningMethodType
        :param report_amount: The report_amount of this TraceJobAttr.  # noqa: E501
        :type report_amount: ReportAmountType
        :param reporting_trigger: The reporting_trigger of this TraceJobAttr.  # noqa: E501
        :type reporting_trigger: List[str]
        :param report_interval: The report_interval of this TraceJobAttr.  # noqa: E501
        :type report_interval: ReportIntervalType
        :param report_type: The report_type of this TraceJobAttr.  # noqa: E501
        :type report_type: ReportTypeType
        :param sensor_information: The sensor_information of this TraceJobAttr.  # noqa: E501
        :type sensor_information: List[str]
        :param trace_collection_entity_id: The trace_collection_entity_id of this TraceJobAttr.  # noqa: E501
        :type trace_collection_entity_id: int
        :param excess_packet_delay_thresholds: The excess_packet_delay_thresholds of this TraceJobAttr.  # noqa: E501
        :type excess_packet_delay_thresholds: object
        """
        self.openapi_types = {
            'job_type': JobTypeType,
            'list_of_interfaces': ListOfInterfacesType,
            'list_of_ne_types': List[str],
            'p_lmn_target': PLMNTargetType,
            'trace_reporting_consumer_uri': str,
            'trace_collection_entity_ip_address': IpAddr,
            'trace_depth': TraceDepthType,
            'trace_reference': TraceReferenceType,
            'trace_recording_session_reference': str,
            'job_id': str,
            'trace_reporting_format': TraceReportingFormatType,
            'trace_target': TraceTargetType,
            'triggering_events': TriggeringEventsType,
            'anonymization_of_mdt_data': AnonymizationOfMDTDataType,
            'area_configuration_for_neigh_cell': AreaConfig,
            'area_scope': List[AreaScope],
            'beam_level_measurement': bool,
            'collection_period_rrmlte': CollectionPeriodRRMLTEType,
            'collection_period_m6_lte': CollectionPeriodM6LTEType,
            'collection_period_m7_lte': int,
            'collection_period_rrmumts': CollectionPeriodRRMUMTSType,
            'collection_period_rrmnr': CollectionPeriodRRMNRType,
            'collection_period_m6_nr': CollectionPeriodM6NRType,
            'collection_period_m7_nr': int,
            'event_list_for_event_triggered_measurement': EventListForEventTriggeredMeasurementType,
            'event_threshold': EventThresholdType,
            'list_of_measurements': ListOfMeasurementsType,
            'logging_duration': LoggingDurationType,
            'logging_interval': LoggingIntervalType,
            'event_threshold_l1': EventThresholdL1Type,
            'hysteresis_l1': int,
            'time_to_trigger_l1': TimeToTriggerL1Type,
            'm_bsfn_area_list': List[MbsfnArea],
            'measurement_period_lte': MeasurementPeriodLTEType,
            'measurement_period_umts': MeasurementPeriodUMTSType,
            'measurement_quantity': MeasurementQuantityType,
            'event_threshold_uph_umts': int,
            'p_lmn_list': List[PLMNListTypeInner],
            'positioning_method': PositioningMethodType,
            'report_amount': ReportAmountType,
            'reporting_trigger': List[str],
            'report_interval': ReportIntervalType,
            'report_type': ReportTypeType,
            'sensor_information': List[str],
            'trace_collection_entity_id': int,
            'excess_packet_delay_thresholds': object
        }

        self.attribute_map = {
            'job_type': 'jobType',
            'list_of_interfaces': 'listOfInterfaces',
            'list_of_ne_types': 'listOfNETypes',
            'p_lmn_target': 'pLMNTarget',
            'trace_reporting_consumer_uri': 'traceReportingConsumerUri',
            'trace_collection_entity_ip_address': 'traceCollectionEntityIPAddress',
            'trace_depth': 'traceDepth',
            'trace_reference': 'traceReference',
            'trace_recording_session_reference': 'traceRecordingSessionReference',
            'job_id': 'jobId',
            'trace_reporting_format': 'traceReportingFormat',
            'trace_target': 'traceTarget',
            'triggering_events': 'triggeringEvents',
            'anonymization_of_mdt_data': 'anonymizationOfMDTData',
            'area_configuration_for_neigh_cell': 'areaConfigurationForNeighCell',
            'area_scope': 'areaScope',
            'beam_level_measurement': 'beamLevelMeasurement',
            'collection_period_rrmlte': 'collectionPeriodRRMLTE',
            'collection_period_m6_lte': 'collectionPeriodM6LTE',
            'collection_period_m7_lte': 'collectionPeriodM7LTE',
            'collection_period_rrmumts': 'collectionPeriodRRMUMTS',
            'collection_period_rrmnr': 'collectionPeriodRRMNR',
            'collection_period_m6_nr': 'collectionPeriodM6NR',
            'collection_period_m7_nr': 'collectionPeriodM7NR',
            'event_list_for_event_triggered_measurement': 'eventListForEventTriggeredMeasurement',
            'event_threshold': 'eventThreshold',
            'list_of_measurements': 'listOfMeasurements',
            'logging_duration': 'loggingDuration',
            'logging_interval': 'loggingInterval',
            'event_threshold_l1': 'eventThresholdL1',
            'hysteresis_l1': 'hysteresisL1',
            'time_to_trigger_l1': 'timeToTriggerL1',
            'm_bsfn_area_list': 'mBSFNAreaList',
            'measurement_period_lte': 'measurementPeriodLTE',
            'measurement_period_umts': 'measurementPeriodUMTS',
            'measurement_quantity': 'measurementQuantity',
            'event_threshold_uph_umts': 'eventThresholdUphUMTS',
            'p_lmn_list': 'pLMNList',
            'positioning_method': 'positioningMethod',
            'report_amount': 'reportAmount',
            'reporting_trigger': 'reportingTrigger',
            'report_interval': 'reportInterval',
            'report_type': 'reportType',
            'sensor_information': 'sensorInformation',
            'trace_collection_entity_id': 'traceCollectionEntityId',
            'excess_packet_delay_thresholds': 'excessPacketDelayThresholds'
        }

        self._job_type = job_type
        self._list_of_interfaces = list_of_interfaces
        self._list_of_ne_types = list_of_ne_types
        self._p_lmn_target = p_lmn_target
        self._trace_reporting_consumer_uri = trace_reporting_consumer_uri
        self._trace_collection_entity_ip_address = trace_collection_entity_ip_address
        self._trace_depth = trace_depth
        self._trace_reference = trace_reference
        self._trace_recording_session_reference = trace_recording_session_reference
        self._job_id = job_id
        self._trace_reporting_format = trace_reporting_format
        self._trace_target = trace_target
        self._triggering_events = triggering_events
        self._anonymization_of_mdt_data = anonymization_of_mdt_data
        self._area_configuration_for_neigh_cell = area_configuration_for_neigh_cell
        self._area_scope = area_scope
        self._beam_level_measurement = beam_level_measurement
        self._collection_period_rrmlte = collection_period_rrmlte
        self._collection_period_m6_lte = collection_period_m6_lte
        self._collection_period_m7_lte = collection_period_m7_lte
        self._collection_period_rrmumts = collection_period_rrmumts
        self._collection_period_rrmnr = collection_period_rrmnr
        self._collection_period_m6_nr = collection_period_m6_nr
        self._collection_period_m7_nr = collection_period_m7_nr
        self._event_list_for_event_triggered_measurement = event_list_for_event_triggered_measurement
        self._event_threshold = event_threshold
        self._list_of_measurements = list_of_measurements
        self._logging_duration = logging_duration
        self._logging_interval = logging_interval
        self._event_threshold_l1 = event_threshold_l1
        self._hysteresis_l1 = hysteresis_l1
        self._time_to_trigger_l1 = time_to_trigger_l1
        self._m_bsfn_area_list = m_bsfn_area_list
        self._measurement_period_lte = measurement_period_lte
        self._measurement_period_umts = measurement_period_umts
        self._measurement_quantity = measurement_quantity
        self._event_threshold_uph_umts = event_threshold_uph_umts
        self._p_lmn_list = p_lmn_list
        self._positioning_method = positioning_method
        self._report_amount = report_amount
        self._reporting_trigger = reporting_trigger
        self._report_interval = report_interval
        self._report_type = report_type
        self._sensor_information = sensor_information
        self._trace_collection_entity_id = trace_collection_entity_id
        self._excess_packet_delay_thresholds = excess_packet_delay_thresholds

    @classmethod
    def from_dict(cls, dikt) -> 'TraceJobAttr':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TraceJob-Attr of this TraceJobAttr.  # noqa: E501
        :rtype: TraceJobAttr
        """
        return util.deserialize_model(dikt, cls)

    @property
    def job_type(self):
        """Gets the job_type of this TraceJobAttr.


        :return: The job_type of this TraceJobAttr.
        :rtype: JobTypeType
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this TraceJobAttr.


        :param job_type: The job_type of this TraceJobAttr.
        :type job_type: JobTypeType
        """

        self._job_type = job_type

    @property
    def list_of_interfaces(self):
        """Gets the list_of_interfaces of this TraceJobAttr.


        :return: The list_of_interfaces of this TraceJobAttr.
        :rtype: ListOfInterfacesType
        """
        return self._list_of_interfaces

    @list_of_interfaces.setter
    def list_of_interfaces(self, list_of_interfaces):
        """Sets the list_of_interfaces of this TraceJobAttr.


        :param list_of_interfaces: The list_of_interfaces of this TraceJobAttr.
        :type list_of_interfaces: ListOfInterfacesType
        """

        self._list_of_interfaces = list_of_interfaces

    @property
    def list_of_ne_types(self):
        """Gets the list_of_ne_types of this TraceJobAttr.

        The Network Element types where Trace Session activation is needed. See 3GPP TS 32.422 clause 5.4 for additional details.  # noqa: E501

        :return: The list_of_ne_types of this TraceJobAttr.
        :rtype: List[str]
        """
        return self._list_of_ne_types

    @list_of_ne_types.setter
    def list_of_ne_types(self, list_of_ne_types):
        """Sets the list_of_ne_types of this TraceJobAttr.

        The Network Element types where Trace Session activation is needed. See 3GPP TS 32.422 clause 5.4 for additional details.  # noqa: E501

        :param list_of_ne_types: The list_of_ne_types of this TraceJobAttr.
        :type list_of_ne_types: List[str]
        """
        allowed_values = ["MSC_SERVER", "SGSN", "MGW", "GGSN", "RNC", "BM_SC", "MME", "SGW", "PGW", "ENB", "EN_GNB", "GNB_CU_CP", "GNB_CU_UP", "GNB_DU", "AMF", "PCF", "SMF", "UPF", "AUSF", "SMSF", "HSS", "UDM"]  # noqa: E501
        if not set(list_of_ne_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `list_of_ne_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(list_of_ne_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._list_of_ne_types = list_of_ne_types

    @property
    def p_lmn_target(self):
        """Gets the p_lmn_target of this TraceJobAttr.


        :return: The p_lmn_target of this TraceJobAttr.
        :rtype: PLMNTargetType
        """
        return self._p_lmn_target

    @p_lmn_target.setter
    def p_lmn_target(self, p_lmn_target):
        """Sets the p_lmn_target of this TraceJobAttr.


        :param p_lmn_target: The p_lmn_target of this TraceJobAttr.
        :type p_lmn_target: PLMNTargetType
        """

        self._p_lmn_target = p_lmn_target

    @property
    def trace_reporting_consumer_uri(self):
        """Gets the trace_reporting_consumer_uri of this TraceJobAttr.


        :return: The trace_reporting_consumer_uri of this TraceJobAttr.
        :rtype: str
        """
        return self._trace_reporting_consumer_uri

    @trace_reporting_consumer_uri.setter
    def trace_reporting_consumer_uri(self, trace_reporting_consumer_uri):
        """Sets the trace_reporting_consumer_uri of this TraceJobAttr.


        :param trace_reporting_consumer_uri: The trace_reporting_consumer_uri of this TraceJobAttr.
        :type trace_reporting_consumer_uri: str
        """

        self._trace_reporting_consumer_uri = trace_reporting_consumer_uri

    @property
    def trace_collection_entity_ip_address(self):
        """Gets the trace_collection_entity_ip_address of this TraceJobAttr.


        :return: The trace_collection_entity_ip_address of this TraceJobAttr.
        :rtype: IpAddr
        """
        return self._trace_collection_entity_ip_address

    @trace_collection_entity_ip_address.setter
    def trace_collection_entity_ip_address(self, trace_collection_entity_ip_address):
        """Sets the trace_collection_entity_ip_address of this TraceJobAttr.


        :param trace_collection_entity_ip_address: The trace_collection_entity_ip_address of this TraceJobAttr.
        :type trace_collection_entity_ip_address: IpAddr
        """

        self._trace_collection_entity_ip_address = trace_collection_entity_ip_address

    @property
    def trace_depth(self):
        """Gets the trace_depth of this TraceJobAttr.


        :return: The trace_depth of this TraceJobAttr.
        :rtype: TraceDepthType
        """
        return self._trace_depth

    @trace_depth.setter
    def trace_depth(self, trace_depth):
        """Sets the trace_depth of this TraceJobAttr.


        :param trace_depth: The trace_depth of this TraceJobAttr.
        :type trace_depth: TraceDepthType
        """

        self._trace_depth = trace_depth

    @property
    def trace_reference(self):
        """Gets the trace_reference of this TraceJobAttr.


        :return: The trace_reference of this TraceJobAttr.
        :rtype: TraceReferenceType
        """
        return self._trace_reference

    @trace_reference.setter
    def trace_reference(self, trace_reference):
        """Sets the trace_reference of this TraceJobAttr.


        :param trace_reference: The trace_reference of this TraceJobAttr.
        :type trace_reference: TraceReferenceType
        """

        self._trace_reference = trace_reference

    @property
    def trace_recording_session_reference(self):
        """Gets the trace_recording_session_reference of this TraceJobAttr.


        :return: The trace_recording_session_reference of this TraceJobAttr.
        :rtype: str
        """
        return self._trace_recording_session_reference

    @trace_recording_session_reference.setter
    def trace_recording_session_reference(self, trace_recording_session_reference):
        """Sets the trace_recording_session_reference of this TraceJobAttr.


        :param trace_recording_session_reference: The trace_recording_session_reference of this TraceJobAttr.
        :type trace_recording_session_reference: str
        """

        self._trace_recording_session_reference = trace_recording_session_reference

    @property
    def job_id(self):
        """Gets the job_id of this TraceJobAttr.


        :return: The job_id of this TraceJobAttr.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this TraceJobAttr.


        :param job_id: The job_id of this TraceJobAttr.
        :type job_id: str
        """

        self._job_id = job_id

    @property
    def trace_reporting_format(self):
        """Gets the trace_reporting_format of this TraceJobAttr.


        :return: The trace_reporting_format of this TraceJobAttr.
        :rtype: TraceReportingFormatType
        """
        return self._trace_reporting_format

    @trace_reporting_format.setter
    def trace_reporting_format(self, trace_reporting_format):
        """Sets the trace_reporting_format of this TraceJobAttr.


        :param trace_reporting_format: The trace_reporting_format of this TraceJobAttr.
        :type trace_reporting_format: TraceReportingFormatType
        """

        self._trace_reporting_format = trace_reporting_format

    @property
    def trace_target(self):
        """Gets the trace_target of this TraceJobAttr.


        :return: The trace_target of this TraceJobAttr.
        :rtype: TraceTargetType
        """
        return self._trace_target

    @trace_target.setter
    def trace_target(self, trace_target):
        """Sets the trace_target of this TraceJobAttr.


        :param trace_target: The trace_target of this TraceJobAttr.
        :type trace_target: TraceTargetType
        """

        self._trace_target = trace_target

    @property
    def triggering_events(self):
        """Gets the triggering_events of this TraceJobAttr.


        :return: The triggering_events of this TraceJobAttr.
        :rtype: TriggeringEventsType
        """
        return self._triggering_events

    @triggering_events.setter
    def triggering_events(self, triggering_events):
        """Sets the triggering_events of this TraceJobAttr.


        :param triggering_events: The triggering_events of this TraceJobAttr.
        :type triggering_events: TriggeringEventsType
        """

        self._triggering_events = triggering_events

    @property
    def anonymization_of_mdt_data(self):
        """Gets the anonymization_of_mdt_data of this TraceJobAttr.


        :return: The anonymization_of_mdt_data of this TraceJobAttr.
        :rtype: AnonymizationOfMDTDataType
        """
        return self._anonymization_of_mdt_data

    @anonymization_of_mdt_data.setter
    def anonymization_of_mdt_data(self, anonymization_of_mdt_data):
        """Sets the anonymization_of_mdt_data of this TraceJobAttr.


        :param anonymization_of_mdt_data: The anonymization_of_mdt_data of this TraceJobAttr.
        :type anonymization_of_mdt_data: AnonymizationOfMDTDataType
        """

        self._anonymization_of_mdt_data = anonymization_of_mdt_data

    @property
    def area_configuration_for_neigh_cell(self):
        """Gets the area_configuration_for_neigh_cell of this TraceJobAttr.


        :return: The area_configuration_for_neigh_cell of this TraceJobAttr.
        :rtype: AreaConfig
        """
        return self._area_configuration_for_neigh_cell

    @area_configuration_for_neigh_cell.setter
    def area_configuration_for_neigh_cell(self, area_configuration_for_neigh_cell):
        """Sets the area_configuration_for_neigh_cell of this TraceJobAttr.


        :param area_configuration_for_neigh_cell: The area_configuration_for_neigh_cell of this TraceJobAttr.
        :type area_configuration_for_neigh_cell: AreaConfig
        """

        self._area_configuration_for_neigh_cell = area_configuration_for_neigh_cell

    @property
    def area_scope(self):
        """Gets the area_scope of this TraceJobAttr.


        :return: The area_scope of this TraceJobAttr.
        :rtype: List[AreaScope]
        """
        return self._area_scope

    @area_scope.setter
    def area_scope(self, area_scope):
        """Sets the area_scope of this TraceJobAttr.


        :param area_scope: The area_scope of this TraceJobAttr.
        :type area_scope: List[AreaScope]
        """

        self._area_scope = area_scope

    @property
    def beam_level_measurement(self):
        """Gets the beam_level_measurement of this TraceJobAttr.

        Determines whether beam level measurements shall be included in case of immediate MDT M1 measurement in NR. For additional details see 3GPP TS 32.422 clause 5.10.40.  # noqa: E501

        :return: The beam_level_measurement of this TraceJobAttr.
        :rtype: bool
        """
        return self._beam_level_measurement

    @beam_level_measurement.setter
    def beam_level_measurement(self, beam_level_measurement):
        """Sets the beam_level_measurement of this TraceJobAttr.

        Determines whether beam level measurements shall be included in case of immediate MDT M1 measurement in NR. For additional details see 3GPP TS 32.422 clause 5.10.40.  # noqa: E501

        :param beam_level_measurement: The beam_level_measurement of this TraceJobAttr.
        :type beam_level_measurement: bool
        """

        self._beam_level_measurement = beam_level_measurement

    @property
    def collection_period_rrmlte(self):
        """Gets the collection_period_rrmlte of this TraceJobAttr.


        :return: The collection_period_rrmlte of this TraceJobAttr.
        :rtype: CollectionPeriodRRMLTEType
        """
        return self._collection_period_rrmlte

    @collection_period_rrmlte.setter
    def collection_period_rrmlte(self, collection_period_rrmlte):
        """Sets the collection_period_rrmlte of this TraceJobAttr.


        :param collection_period_rrmlte: The collection_period_rrmlte of this TraceJobAttr.
        :type collection_period_rrmlte: CollectionPeriodRRMLTEType
        """

        self._collection_period_rrmlte = collection_period_rrmlte

    @property
    def collection_period_m6_lte(self):
        """Gets the collection_period_m6_lte of this TraceJobAttr.


        :return: The collection_period_m6_lte of this TraceJobAttr.
        :rtype: CollectionPeriodM6LTEType
        """
        return self._collection_period_m6_lte

    @collection_period_m6_lte.setter
    def collection_period_m6_lte(self, collection_period_m6_lte):
        """Sets the collection_period_m6_lte of this TraceJobAttr.


        :param collection_period_m6_lte: The collection_period_m6_lte of this TraceJobAttr.
        :type collection_period_m6_lte: CollectionPeriodM6LTEType
        """

        self._collection_period_m6_lte = collection_period_m6_lte

    @property
    def collection_period_m7_lte(self):
        """Gets the collection_period_m7_lte of this TraceJobAttr.

        See details in 3GPP TS 32.422 clause 5.10.33.  # noqa: E501

        :return: The collection_period_m7_lte of this TraceJobAttr.
        :rtype: int
        """
        return self._collection_period_m7_lte

    @collection_period_m7_lte.setter
    def collection_period_m7_lte(self, collection_period_m7_lte):
        """Sets the collection_period_m7_lte of this TraceJobAttr.

        See details in 3GPP TS 32.422 clause 5.10.33.  # noqa: E501

        :param collection_period_m7_lte: The collection_period_m7_lte of this TraceJobAttr.
        :type collection_period_m7_lte: int
        """
        if collection_period_m7_lte is not None and collection_period_m7_lte > 60:  # noqa: E501
            raise ValueError("Invalid value for `collection_period_m7_lte`, must be a value less than or equal to `60`")  # noqa: E501
        if collection_period_m7_lte is not None and collection_period_m7_lte < 1:  # noqa: E501
            raise ValueError("Invalid value for `collection_period_m7_lte`, must be a value greater than or equal to `1`")  # noqa: E501

        self._collection_period_m7_lte = collection_period_m7_lte

    @property
    def collection_period_rrmumts(self):
        """Gets the collection_period_rrmumts of this TraceJobAttr.


        :return: The collection_period_rrmumts of this TraceJobAttr.
        :rtype: CollectionPeriodRRMUMTSType
        """
        return self._collection_period_rrmumts

    @collection_period_rrmumts.setter
    def collection_period_rrmumts(self, collection_period_rrmumts):
        """Sets the collection_period_rrmumts of this TraceJobAttr.


        :param collection_period_rrmumts: The collection_period_rrmumts of this TraceJobAttr.
        :type collection_period_rrmumts: CollectionPeriodRRMUMTSType
        """

        self._collection_period_rrmumts = collection_period_rrmumts

    @property
    def collection_period_rrmnr(self):
        """Gets the collection_period_rrmnr of this TraceJobAttr.


        :return: The collection_period_rrmnr of this TraceJobAttr.
        :rtype: CollectionPeriodRRMNRType
        """
        return self._collection_period_rrmnr

    @collection_period_rrmnr.setter
    def collection_period_rrmnr(self, collection_period_rrmnr):
        """Sets the collection_period_rrmnr of this TraceJobAttr.


        :param collection_period_rrmnr: The collection_period_rrmnr of this TraceJobAttr.
        :type collection_period_rrmnr: CollectionPeriodRRMNRType
        """

        self._collection_period_rrmnr = collection_period_rrmnr

    @property
    def collection_period_m6_nr(self):
        """Gets the collection_period_m6_nr of this TraceJobAttr.


        :return: The collection_period_m6_nr of this TraceJobAttr.
        :rtype: CollectionPeriodM6NRType
        """
        return self._collection_period_m6_nr

    @collection_period_m6_nr.setter
    def collection_period_m6_nr(self, collection_period_m6_nr):
        """Sets the collection_period_m6_nr of this TraceJobAttr.


        :param collection_period_m6_nr: The collection_period_m6_nr of this TraceJobAttr.
        :type collection_period_m6_nr: CollectionPeriodM6NRType
        """

        self._collection_period_m6_nr = collection_period_m6_nr

    @property
    def collection_period_m7_nr(self):
        """Gets the collection_period_m7_nr of this TraceJobAttr.

        See details in 3GPP TS 32.422 clause 5.10.35.  # noqa: E501

        :return: The collection_period_m7_nr of this TraceJobAttr.
        :rtype: int
        """
        return self._collection_period_m7_nr

    @collection_period_m7_nr.setter
    def collection_period_m7_nr(self, collection_period_m7_nr):
        """Sets the collection_period_m7_nr of this TraceJobAttr.

        See details in 3GPP TS 32.422 clause 5.10.35.  # noqa: E501

        :param collection_period_m7_nr: The collection_period_m7_nr of this TraceJobAttr.
        :type collection_period_m7_nr: int
        """
        if collection_period_m7_nr is not None and collection_period_m7_nr > 60:  # noqa: E501
            raise ValueError("Invalid value for `collection_period_m7_nr`, must be a value less than or equal to `60`")  # noqa: E501
        if collection_period_m7_nr is not None and collection_period_m7_nr < 1:  # noqa: E501
            raise ValueError("Invalid value for `collection_period_m7_nr`, must be a value greater than or equal to `1`")  # noqa: E501

        self._collection_period_m7_nr = collection_period_m7_nr

    @property
    def event_list_for_event_triggered_measurement(self):
        """Gets the event_list_for_event_triggered_measurement of this TraceJobAttr.


        :return: The event_list_for_event_triggered_measurement of this TraceJobAttr.
        :rtype: EventListForEventTriggeredMeasurementType
        """
        return self._event_list_for_event_triggered_measurement

    @event_list_for_event_triggered_measurement.setter
    def event_list_for_event_triggered_measurement(self, event_list_for_event_triggered_measurement):
        """Sets the event_list_for_event_triggered_measurement of this TraceJobAttr.


        :param event_list_for_event_triggered_measurement: The event_list_for_event_triggered_measurement of this TraceJobAttr.
        :type event_list_for_event_triggered_measurement: EventListForEventTriggeredMeasurementType
        """

        self._event_list_for_event_triggered_measurement = event_list_for_event_triggered_measurement

    @property
    def event_threshold(self):
        """Gets the event_threshold of this TraceJobAttr.


        :return: The event_threshold of this TraceJobAttr.
        :rtype: EventThresholdType
        """
        return self._event_threshold

    @event_threshold.setter
    def event_threshold(self, event_threshold):
        """Sets the event_threshold of this TraceJobAttr.


        :param event_threshold: The event_threshold of this TraceJobAttr.
        :type event_threshold: EventThresholdType
        """

        self._event_threshold = event_threshold

    @property
    def list_of_measurements(self):
        """Gets the list_of_measurements of this TraceJobAttr.


        :return: The list_of_measurements of this TraceJobAttr.
        :rtype: ListOfMeasurementsType
        """
        return self._list_of_measurements

    @list_of_measurements.setter
    def list_of_measurements(self, list_of_measurements):
        """Sets the list_of_measurements of this TraceJobAttr.


        :param list_of_measurements: The list_of_measurements of this TraceJobAttr.
        :type list_of_measurements: ListOfMeasurementsType
        """

        self._list_of_measurements = list_of_measurements

    @property
    def logging_duration(self):
        """Gets the logging_duration of this TraceJobAttr.


        :return: The logging_duration of this TraceJobAttr.
        :rtype: LoggingDurationType
        """
        return self._logging_duration

    @logging_duration.setter
    def logging_duration(self, logging_duration):
        """Sets the logging_duration of this TraceJobAttr.


        :param logging_duration: The logging_duration of this TraceJobAttr.
        :type logging_duration: LoggingDurationType
        """

        self._logging_duration = logging_duration

    @property
    def logging_interval(self):
        """Gets the logging_interval of this TraceJobAttr.


        :return: The logging_interval of this TraceJobAttr.
        :rtype: LoggingIntervalType
        """
        return self._logging_interval

    @logging_interval.setter
    def logging_interval(self, logging_interval):
        """Sets the logging_interval of this TraceJobAttr.


        :param logging_interval: The logging_interval of this TraceJobAttr.
        :type logging_interval: LoggingIntervalType
        """

        self._logging_interval = logging_interval

    @property
    def event_threshold_l1(self):
        """Gets the event_threshold_l1 of this TraceJobAttr.


        :return: The event_threshold_l1 of this TraceJobAttr.
        :rtype: EventThresholdL1Type
        """
        return self._event_threshold_l1

    @event_threshold_l1.setter
    def event_threshold_l1(self, event_threshold_l1):
        """Sets the event_threshold_l1 of this TraceJobAttr.


        :param event_threshold_l1: The event_threshold_l1 of this TraceJobAttr.
        :type event_threshold_l1: EventThresholdL1Type
        """

        self._event_threshold_l1 = event_threshold_l1

    @property
    def hysteresis_l1(self):
        """Gets the hysteresis_l1 of this TraceJobAttr.

        See details in 3GPP TS 32.422 clause 5.10.Y.  # noqa: E501

        :return: The hysteresis_l1 of this TraceJobAttr.
        :rtype: int
        """
        return self._hysteresis_l1

    @hysteresis_l1.setter
    def hysteresis_l1(self, hysteresis_l1):
        """Sets the hysteresis_l1 of this TraceJobAttr.

        See details in 3GPP TS 32.422 clause 5.10.Y.  # noqa: E501

        :param hysteresis_l1: The hysteresis_l1 of this TraceJobAttr.
        :type hysteresis_l1: int
        """
        if hysteresis_l1 is not None and hysteresis_l1 > 30:  # noqa: E501
            raise ValueError("Invalid value for `hysteresis_l1`, must be a value less than or equal to `30`")  # noqa: E501
        if hysteresis_l1 is not None and hysteresis_l1 < 0:  # noqa: E501
            raise ValueError("Invalid value for `hysteresis_l1`, must be a value greater than or equal to `0`")  # noqa: E501

        self._hysteresis_l1 = hysteresis_l1

    @property
    def time_to_trigger_l1(self):
        """Gets the time_to_trigger_l1 of this TraceJobAttr.


        :return: The time_to_trigger_l1 of this TraceJobAttr.
        :rtype: TimeToTriggerL1Type
        """
        return self._time_to_trigger_l1

    @time_to_trigger_l1.setter
    def time_to_trigger_l1(self, time_to_trigger_l1):
        """Sets the time_to_trigger_l1 of this TraceJobAttr.


        :param time_to_trigger_l1: The time_to_trigger_l1 of this TraceJobAttr.
        :type time_to_trigger_l1: TimeToTriggerL1Type
        """

        self._time_to_trigger_l1 = time_to_trigger_l1

    @property
    def m_bsfn_area_list(self):
        """Gets the m_bsfn_area_list of this TraceJobAttr.


        :return: The m_bsfn_area_list of this TraceJobAttr.
        :rtype: List[MbsfnArea]
        """
        return self._m_bsfn_area_list

    @m_bsfn_area_list.setter
    def m_bsfn_area_list(self, m_bsfn_area_list):
        """Sets the m_bsfn_area_list of this TraceJobAttr.


        :param m_bsfn_area_list: The m_bsfn_area_list of this TraceJobAttr.
        :type m_bsfn_area_list: List[MbsfnArea]
        """

        self._m_bsfn_area_list = m_bsfn_area_list

    @property
    def measurement_period_lte(self):
        """Gets the measurement_period_lte of this TraceJobAttr.


        :return: The measurement_period_lte of this TraceJobAttr.
        :rtype: MeasurementPeriodLTEType
        """
        return self._measurement_period_lte

    @measurement_period_lte.setter
    def measurement_period_lte(self, measurement_period_lte):
        """Sets the measurement_period_lte of this TraceJobAttr.


        :param measurement_period_lte: The measurement_period_lte of this TraceJobAttr.
        :type measurement_period_lte: MeasurementPeriodLTEType
        """

        self._measurement_period_lte = measurement_period_lte

    @property
    def measurement_period_umts(self):
        """Gets the measurement_period_umts of this TraceJobAttr.


        :return: The measurement_period_umts of this TraceJobAttr.
        :rtype: MeasurementPeriodUMTSType
        """
        return self._measurement_period_umts

    @measurement_period_umts.setter
    def measurement_period_umts(self, measurement_period_umts):
        """Sets the measurement_period_umts of this TraceJobAttr.


        :param measurement_period_umts: The measurement_period_umts of this TraceJobAttr.
        :type measurement_period_umts: MeasurementPeriodUMTSType
        """

        self._measurement_period_umts = measurement_period_umts

    @property
    def measurement_quantity(self):
        """Gets the measurement_quantity of this TraceJobAttr.


        :return: The measurement_quantity of this TraceJobAttr.
        :rtype: MeasurementQuantityType
        """
        return self._measurement_quantity

    @measurement_quantity.setter
    def measurement_quantity(self, measurement_quantity):
        """Sets the measurement_quantity of this TraceJobAttr.


        :param measurement_quantity: The measurement_quantity of this TraceJobAttr.
        :type measurement_quantity: MeasurementQuantityType
        """

        self._measurement_quantity = measurement_quantity

    @property
    def event_threshold_uph_umts(self):
        """Gets the event_threshold_uph_umts of this TraceJobAttr.

        See details in 3GPP TS 32.422 clause 5.10.A.  # noqa: E501

        :return: The event_threshold_uph_umts of this TraceJobAttr.
        :rtype: int
        """
        return self._event_threshold_uph_umts

    @event_threshold_uph_umts.setter
    def event_threshold_uph_umts(self, event_threshold_uph_umts):
        """Sets the event_threshold_uph_umts of this TraceJobAttr.

        See details in 3GPP TS 32.422 clause 5.10.A.  # noqa: E501

        :param event_threshold_uph_umts: The event_threshold_uph_umts of this TraceJobAttr.
        :type event_threshold_uph_umts: int
        """
        if event_threshold_uph_umts is not None and event_threshold_uph_umts > 31:  # noqa: E501
            raise ValueError("Invalid value for `event_threshold_uph_umts`, must be a value less than or equal to `31`")  # noqa: E501
        if event_threshold_uph_umts is not None and event_threshold_uph_umts < 0:  # noqa: E501
            raise ValueError("Invalid value for `event_threshold_uph_umts`, must be a value greater than or equal to `0`")  # noqa: E501

        self._event_threshold_uph_umts = event_threshold_uph_umts

    @property
    def p_lmn_list(self):
        """Gets the p_lmn_list of this TraceJobAttr.

        See details in 3GPP TS 32.422 clause 5.10.24.  # noqa: E501

        :return: The p_lmn_list of this TraceJobAttr.
        :rtype: List[PLMNListTypeInner]
        """
        return self._p_lmn_list

    @p_lmn_list.setter
    def p_lmn_list(self, p_lmn_list):
        """Sets the p_lmn_list of this TraceJobAttr.

        See details in 3GPP TS 32.422 clause 5.10.24.  # noqa: E501

        :param p_lmn_list: The p_lmn_list of this TraceJobAttr.
        :type p_lmn_list: List[PLMNListTypeInner]
        """
        if p_lmn_list is not None and len(p_lmn_list) > 16:
            raise ValueError("Invalid value for `p_lmn_list`, number of items must be less than or equal to `16`")  # noqa: E501

        self._p_lmn_list = p_lmn_list

    @property
    def positioning_method(self):
        """Gets the positioning_method of this TraceJobAttr.


        :return: The positioning_method of this TraceJobAttr.
        :rtype: PositioningMethodType
        """
        return self._positioning_method

    @positioning_method.setter
    def positioning_method(self, positioning_method):
        """Sets the positioning_method of this TraceJobAttr.


        :param positioning_method: The positioning_method of this TraceJobAttr.
        :type positioning_method: PositioningMethodType
        """

        self._positioning_method = positioning_method

    @property
    def report_amount(self):
        """Gets the report_amount of this TraceJobAttr.


        :return: The report_amount of this TraceJobAttr.
        :rtype: ReportAmountType
        """
        return self._report_amount

    @report_amount.setter
    def report_amount(self, report_amount):
        """Sets the report_amount of this TraceJobAttr.


        :param report_amount: The report_amount of this TraceJobAttr.
        :type report_amount: ReportAmountType
        """

        self._report_amount = report_amount

    @property
    def reporting_trigger(self):
        """Gets the reporting_trigger of this TraceJobAttr.

        See details in 3GPP TS 32.422 clause 5.10.4.  # noqa: E501

        :return: The reporting_trigger of this TraceJobAttr.
        :rtype: List[str]
        """
        return self._reporting_trigger

    @reporting_trigger.setter
    def reporting_trigger(self, reporting_trigger):
        """Sets the reporting_trigger of this TraceJobAttr.

        See details in 3GPP TS 32.422 clause 5.10.4.  # noqa: E501

        :param reporting_trigger: The reporting_trigger of this TraceJobAttr.
        :type reporting_trigger: List[str]
        """
        allowed_values = ["PERIODICAL", "A2_FOR_LTE_NR", "1F_FOR_UMTS", "1I_FOR_UMTS_MCPS_TDD", "A2_TRIGGERED_PERIODIC_FOR_LTE_NR", "ALL_CONFIGURED_RRM_FOR_LTE_NR", "ALL_CONFIGURED_RRM_FOR_UMTS"]  # noqa: E501
        if not set(reporting_trigger).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `reporting_trigger` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(reporting_trigger) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._reporting_trigger = reporting_trigger

    @property
    def report_interval(self):
        """Gets the report_interval of this TraceJobAttr.


        :return: The report_interval of this TraceJobAttr.
        :rtype: ReportIntervalType
        """
        return self._report_interval

    @report_interval.setter
    def report_interval(self, report_interval):
        """Sets the report_interval of this TraceJobAttr.


        :param report_interval: The report_interval of this TraceJobAttr.
        :type report_interval: ReportIntervalType
        """

        self._report_interval = report_interval

    @property
    def report_type(self):
        """Gets the report_type of this TraceJobAttr.


        :return: The report_type of this TraceJobAttr.
        :rtype: ReportTypeType
        """
        return self._report_type

    @report_type.setter
    def report_type(self, report_type):
        """Sets the report_type of this TraceJobAttr.


        :param report_type: The report_type of this TraceJobAttr.
        :type report_type: ReportTypeType
        """

        self._report_type = report_type

    @property
    def sensor_information(self):
        """Gets the sensor_information of this TraceJobAttr.

        See details in 3GPP TS 32.422 clause 5.10.29.  # noqa: E501

        :return: The sensor_information of this TraceJobAttr.
        :rtype: List[str]
        """
        return self._sensor_information

    @sensor_information.setter
    def sensor_information(self, sensor_information):
        """Sets the sensor_information of this TraceJobAttr.

        See details in 3GPP TS 32.422 clause 5.10.29.  # noqa: E501

        :param sensor_information: The sensor_information of this TraceJobAttr.
        :type sensor_information: List[str]
        """
        allowed_values = ["BAROMETRIC_PRESSURE", "UE_SPEED", "UE_ORIENTATION"]  # noqa: E501
        if not set(sensor_information).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `sensor_information` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(sensor_information) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._sensor_information = sensor_information

    @property
    def trace_collection_entity_id(self):
        """Gets the trace_collection_entity_id of this TraceJobAttr.

        See details in 3GPP TS 32.422 clause 5.10.11. Only TCE Id value may be sent over the air to the UE being configured for Logged MDT.  # noqa: E501

        :return: The trace_collection_entity_id of this TraceJobAttr.
        :rtype: int
        """
        return self._trace_collection_entity_id

    @trace_collection_entity_id.setter
    def trace_collection_entity_id(self, trace_collection_entity_id):
        """Sets the trace_collection_entity_id of this TraceJobAttr.

        See details in 3GPP TS 32.422 clause 5.10.11. Only TCE Id value may be sent over the air to the UE being configured for Logged MDT.  # noqa: E501

        :param trace_collection_entity_id: The trace_collection_entity_id of this TraceJobAttr.
        :type trace_collection_entity_id: int
        """

        self._trace_collection_entity_id = trace_collection_entity_id

    @property
    def excess_packet_delay_thresholds(self):
        """Gets the excess_packet_delay_thresholds of this TraceJobAttr.

        Excess Packet Delay Threshold for NR MDT. See details in 3GPP TS 32.422 clause 4.1.1 and 4.1.2.  # noqa: E501

        :return: The excess_packet_delay_thresholds of this TraceJobAttr.
        :rtype: object
        """
        return self._excess_packet_delay_thresholds

    @excess_packet_delay_thresholds.setter
    def excess_packet_delay_thresholds(self, excess_packet_delay_thresholds):
        """Sets the excess_packet_delay_thresholds of this TraceJobAttr.

        Excess Packet Delay Threshold for NR MDT. See details in 3GPP TS 32.422 clause 4.1.1 and 4.1.2.  # noqa: E501

        :param excess_packet_delay_thresholds: The excess_packet_delay_thresholds of this TraceJobAttr.
        :type excess_packet_delay_thresholds: object
        """

        self._excess_packet_delay_thresholds = excess_packet_delay_thresholds
