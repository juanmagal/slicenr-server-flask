# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.administrative_state import AdministrativeState
from openapi_server.models.alarm_list_single import AlarmListSingle
from openapi_server.models.amf_function_single import AmfFunctionSingle
from openapi_server.models.amf_region_single import AmfRegionSingle
from openapi_server.models.amf_set_single import AmfSetSingle
from openapi_server.models.assurance_closed_control_loop_single import AssuranceClosedControlLoopSingle
from openapi_server.models.assurance_goal_single import AssuranceGoalSingle
from openapi_server.models.assurance_report_single_all_of_attributes import AssuranceReportSingleAllOfAttributes
from openapi_server.models.ausf_function_single import AusfFunctionSingle
from openapi_server.models.beam_single import BeamSingle
from openapi_server.models.bwp_single import BwpSingle
from openapi_server.models.cco_function_single import CCOFunctionSingle
from openapi_server.models.ces_management_function_single import CESManagementFunctionSingle
from openapi_server.models.cpci_configuration_function_single import CPCIConfigurationFunctionSingle
from openapi_server.models.common_beamforming_function_single import CommonBeamformingFunctionSingle
from openapi_server.models.configurable5_qi_set_single import Configurable5QISetSingle
from openapi_server.models.danr_management_function_single import DANRManagementFunctionSingle
from openapi_server.models.des_management_function_single import DESManagementFunctionSingle
from openapi_server.models.dlbo_function_single import DLBOFunctionSingle
from openapi_server.models.dmro_function_single import DMROFunctionSingle
from openapi_server.models.dpci_configuration_function_single import DPCIConfigurationFunctionSingle
from openapi_server.models.drach_optimization_function_single import DRACHOptimizationFunctionSingle
from openapi_server.models.dynamic5_qi_set_single import Dynamic5QISetSingle
from openapi_server.models.easdf_function_single import EASDFFunctionSingle
from openapi_server.models.epe1_single import EPE1Single
from openapi_server.models.epf1_c_single import EPF1CSingle
from openapi_server.models.epf1_u_single import EPF1USingle
from openapi_server.models.epmapsmsc_single import EPMAPSMSCSingle
from openapi_server.models.epn10_single import EPN10Single
from openapi_server.models.epn11_single import EPN11Single
from openapi_server.models.epn12_single import EPN12Single
from openapi_server.models.epn13_single import EPN13Single
from openapi_server.models.epn14_single import EPN14Single
from openapi_server.models.epn15_single import EPN15Single
from openapi_server.models.epn16_single import EPN16Single
from openapi_server.models.epn17_single import EPN17Single
from openapi_server.models.epn20_single import EPN20Single
from openapi_server.models.epn21_single import EPN21Single
from openapi_server.models.epn22_single import EPN22Single
from openapi_server.models.epn26_single import EPN26Single
from openapi_server.models.epn27_single import EPN27Single
from openapi_server.models.epn2_single import EPN2Single
from openapi_server.models.epn31_single import EPN31Single
from openapi_server.models.epn32_single import EPN32Single
from openapi_server.models.epn33_single import EPN33Single
from openapi_server.models.epn3_single import EPN3Single
from openapi_server.models.epn4_single import EPN4Single
from openapi_server.models.epn5_single import EPN5Single
from openapi_server.models.epn60_single import EPN60Single
from openapi_server.models.epn6_single import EPN6Single
from openapi_server.models.epn7_single import EPN7Single
from openapi_server.models.epn88_single import EPN88Single
from openapi_server.models.epn8_single import EPN8Single
from openapi_server.models.epn9_single import EPN9Single
from openapi_server.models.epnlg_single import EPNLGSingle
from openapi_server.models.epnls_single import EPNLSSingle
from openapi_server.models.epng_c_single import EPNgCSingle
from openapi_server.models.epng_u_single import EPNgUSingle
from openapi_server.models.ep_npc4_single import EPNpc4Single
from openapi_server.models.ep_npc6_single import EPNpc6Single
from openapi_server.models.ep_npc7_single import EPNpc7Single
from openapi_server.models.ep_npc8_single import EPNpc8Single
from openapi_server.models.eprx_single import EPRxSingle
from openapi_server.models.eps1_u_single import EPS1USingle
from openapi_server.models.eps5_c_single import EPS5CSingle
from openapi_server.models.eps5_u_single import EPS5USingle
from openapi_server.models.ep_transport_single import EPTransportSingle
from openapi_server.models.epx2_c_single import EPX2CSingle
from openapi_server.models.epx2_u_single import EPX2USingle
from openapi_server.models.epxn_c_single import EPXnCSingle
from openapi_server.models.epxn_u_single import EPXnUSingle
from openapi_server.models.e_utran_cell_relation_single import EUtranCellRelationSingle
from openapi_server.models.e_utran_freq_relation_single import EUtranFreqRelationSingle
from openapi_server.models.e_utran_frequency_single import EUtranFrequencySingle
from openapi_server.models.ecm_connection_info_single import EcmConnectionInfoSingle
from openapi_server.models.external_amf_function_single import ExternalAmfFunctionSingle
from openapi_server.models.external_enb_function_single import ExternalENBFunctionSingle
from openapi_server.models.external_eu_tran_cell_single import ExternalEUTranCellSingle
from openapi_server.models.external_gnb_cu_cp_function_single import ExternalGnbCuCpFunctionSingle
from openapi_server.models.external_nr_cell_cu_single import ExternalNrCellCuSingle
from openapi_server.models.external_nrf_function_single import ExternalNrfFunctionSingle
from openapi_server.models.external_nssf_function_single import ExternalNssfFunctionSingle
from openapi_server.models.feasibility_check_and_reservation_job_single import FeasibilityCheckAndReservationJobSingle
from openapi_server.models.file_download_job_single import FileDownloadJobSingle
from openapi_server.models.files_single import FilesSingle
from openapi_server.models.five_qi_dscp_mapping_set_single import FiveQiDscpMappingSetSingle
from openapi_server.models.fulfilment_info import FulfilmentInfo
from openapi_server.models.gnb_cu_cp_function_single import GnbCuCpFunctionSingle
from openapi_server.models.gnb_cu_up_function_single import GnbCuUpFunctionSingle
from openapi_server.models.gnb_du_function_single import GnbDuFunctionSingle
from openapi_server.models.gtp_u_path_qo_s_monitoring_control_single import GtpUPathQoSMonitoringControlSingle
from openapi_server.models.heartbeat_control_single import HeartbeatControlSingle
from openapi_server.models.intent_context import IntentContext
from openapi_server.models.intent_single import IntentSingle
from openapi_server.models.intent_single_all_of_intent_expectations_inner import IntentSingleAllOfIntentExpectationsInner
from openapi_server.models.lmf_function_single import LmfFunctionSingle
from openapi_server.models.managed_element_single import ManagedElementSingle
from openapi_server.models.managed_nf_service_single import ManagedNFServiceSingle
from openapi_server.models.management_data_collection_single import ManagementDataCollectionSingle
from openapi_server.models.management_node_single import ManagementNodeSingle
from openapi_server.models.me_context_single import MeContextSingle
from openapi_server.models.mns_agent_single import MnsAgentSingle
from openapi_server.models.mns_info_single import MnsInfoSingle
from openapi_server.models.mns_registry_single import MnsRegistrySingle
from openapi_server.models.n3iwf_function_single import N3iwfFunctionSingle
from openapi_server.models.nr_cell_relation_single import NRCellRelationSingle
from openapi_server.models.nr_freq_relation_single import NRFreqRelationSingle
from openapi_server.models.nr_frequency_single import NRFrequencySingle
from openapi_server.models.nef_function_single import NefFunctionSingle
from openapi_server.models.network_slice_single import NetworkSliceSingle
from openapi_server.models.network_slice_subnet_provider_capabilities_single import NetworkSliceSubnetProviderCapabilitiesSingle
from openapi_server.models.network_slice_subnet_single import NetworkSliceSubnetSingle
from openapi_server.models.ngeir_function_single import NgeirFunctionSingle
from openapi_server.models.nr_cell_cu_single import NrCellCuSingle
from openapi_server.models.nr_cell_du_single import NrCellDuSingle
from openapi_server.models.nr_operator_cell_du_single import NrOperatorCellDuSingle
from openapi_server.models.nr_sector_carrier_single import NrSectorCarrierSingle
from openapi_server.models.nrf_function_single import NrfFunctionSingle
from openapi_server.models.nssf_function_single import NssfFunctionSingle
from openapi_server.models.ntf_subscription_control_single import NtfSubscriptionControlSingle
from openapi_server.models.nwdaf_function_single import NwdafFunctionSingle
from openapi_server.models.operator_du_single import OperatorDuSingle
from openapi_server.models.pcf_function_single import PcfFunctionSingle
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle
from openapi_server.models.plmn_info import PlmnInfo
from openapi_server.models.predefined_pcc_rule_set_single import PredefinedPccRuleSetSingle
from openapi_server.models.qfqo_s_monitoring_control_single import QFQoSMonitoringControlSingle
from openapi_server.models.rrm_policy_ratio_single import RRMPolicyRatioSingle
from openapi_server.models.resource_one_of import ResourceOneOf
from openapi_server.models.resource_one_of1 import ResourceOneOf1
from openapi_server.models.rim_rs_global_single import RimRSGlobalSingle
from openapi_server.models.rim_rs_set_single import RimRSSetSingle
from openapi_server.models.scp_function_single import ScpFunctionSingle
from openapi_server.models.sepp_function_single import SeppFunctionSingle
from openapi_server.models.smf_function_single import SmfFunctionSingle
from openapi_server.models.smsf_function_single import SmsfFunctionSingle
from openapi_server.models.sub_network_single import SubNetworkSingle
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle
from openapi_server.models.trace_job_single import TraceJobSingle
from openapi_server.models.udm_function_single import UdmFunctionSingle
from openapi_server.models.udr_function_single import UdrFunctionSingle
from openapi_server.models.udsf_function_single import UdsfFunctionSingle
from openapi_server.models.upf_function_single import UpfFunctionSingle
from openapi_server.models.vs_data_container_single import VsDataContainerSingle
from openapi_server import util

from openapi_server.models.administrative_state import AdministrativeState  # noqa: E501
from openapi_server.models.alarm_list_single import AlarmListSingle  # noqa: E501
from openapi_server.models.amf_function_single import AmfFunctionSingle  # noqa: E501
from openapi_server.models.amf_region_single import AmfRegionSingle  # noqa: E501
from openapi_server.models.amf_set_single import AmfSetSingle  # noqa: E501
from openapi_server.models.assurance_closed_control_loop_single import AssuranceClosedControlLoopSingle  # noqa: E501
from openapi_server.models.assurance_goal_single import AssuranceGoalSingle  # noqa: E501
from openapi_server.models.assurance_report_single_all_of_attributes import AssuranceReportSingleAllOfAttributes  # noqa: E501
from openapi_server.models.ausf_function_single import AusfFunctionSingle  # noqa: E501
from openapi_server.models.beam_single import BeamSingle  # noqa: E501
from openapi_server.models.bwp_single import BwpSingle  # noqa: E501
from openapi_server.models.cco_function_single import CCOFunctionSingle  # noqa: E501
from openapi_server.models.ces_management_function_single import CESManagementFunctionSingle  # noqa: E501
from openapi_server.models.common_beamforming_function_single import CommonBeamformingFunctionSingle  # noqa: E501
from openapi_server.models.configurable5_qi_set_single import Configurable5QISetSingle  # noqa: E501
from openapi_server.models.cpci_configuration_function_single import CPCIConfigurationFunctionSingle  # noqa: E501
from openapi_server.models.danr_management_function_single import DANRManagementFunctionSingle  # noqa: E501
from openapi_server.models.des_management_function_single import DESManagementFunctionSingle  # noqa: E501
from openapi_server.models.dlbo_function_single import DLBOFunctionSingle  # noqa: E501
from openapi_server.models.dmro_function_single import DMROFunctionSingle  # noqa: E501
from openapi_server.models.dpci_configuration_function_single import DPCIConfigurationFunctionSingle  # noqa: E501
from openapi_server.models.drach_optimization_function_single import DRACHOptimizationFunctionSingle  # noqa: E501
from openapi_server.models.dynamic5_qi_set_single import Dynamic5QISetSingle  # noqa: E501
from openapi_server.models.e_utran_cell_relation_single import EUtranCellRelationSingle  # noqa: E501
from openapi_server.models.e_utran_freq_relation_single import EUtranFreqRelationSingle  # noqa: E501
from openapi_server.models.e_utran_frequency_single import EUtranFrequencySingle  # noqa: E501
from openapi_server.models.easdf_function_single import EASDFFunctionSingle  # noqa: E501
from openapi_server.models.ecm_connection_info_single import EcmConnectionInfoSingle  # noqa: E501
from openapi_server.models.ep_npc4_single import EPNpc4Single  # noqa: E501
from openapi_server.models.ep_npc6_single import EPNpc6Single  # noqa: E501
from openapi_server.models.ep_npc7_single import EPNpc7Single  # noqa: E501
from openapi_server.models.ep_npc8_single import EPNpc8Single  # noqa: E501
from openapi_server.models.ep_transport_single import EPTransportSingle  # noqa: E501
from openapi_server.models.epe1_single import EPE1Single  # noqa: E501
from openapi_server.models.epf1_c_single import EPF1CSingle  # noqa: E501
from openapi_server.models.epf1_u_single import EPF1USingle  # noqa: E501
from openapi_server.models.epmapsmsc_single import EPMAPSMSCSingle  # noqa: E501
from openapi_server.models.epn10_single import EPN10Single  # noqa: E501
from openapi_server.models.epn11_single import EPN11Single  # noqa: E501
from openapi_server.models.epn12_single import EPN12Single  # noqa: E501
from openapi_server.models.epn13_single import EPN13Single  # noqa: E501
from openapi_server.models.epn14_single import EPN14Single  # noqa: E501
from openapi_server.models.epn15_single import EPN15Single  # noqa: E501
from openapi_server.models.epn16_single import EPN16Single  # noqa: E501
from openapi_server.models.epn17_single import EPN17Single  # noqa: E501
from openapi_server.models.epn20_single import EPN20Single  # noqa: E501
from openapi_server.models.epn21_single import EPN21Single  # noqa: E501
from openapi_server.models.epn22_single import EPN22Single  # noqa: E501
from openapi_server.models.epn26_single import EPN26Single  # noqa: E501
from openapi_server.models.epn27_single import EPN27Single  # noqa: E501
from openapi_server.models.epn2_single import EPN2Single  # noqa: E501
from openapi_server.models.epn31_single import EPN31Single  # noqa: E501
from openapi_server.models.epn32_single import EPN32Single  # noqa: E501
from openapi_server.models.epn33_single import EPN33Single  # noqa: E501
from openapi_server.models.epn3_single import EPN3Single  # noqa: E501
from openapi_server.models.epn4_single import EPN4Single  # noqa: E501
from openapi_server.models.epn5_single import EPN5Single  # noqa: E501
from openapi_server.models.epn60_single import EPN60Single  # noqa: E501
from openapi_server.models.epn6_single import EPN6Single  # noqa: E501
from openapi_server.models.epn7_single import EPN7Single  # noqa: E501
from openapi_server.models.epn88_single import EPN88Single  # noqa: E501
from openapi_server.models.epn8_single import EPN8Single  # noqa: E501
from openapi_server.models.epn9_single import EPN9Single  # noqa: E501
from openapi_server.models.epng_c_single import EPNgCSingle  # noqa: E501
from openapi_server.models.epng_u_single import EPNgUSingle  # noqa: E501
from openapi_server.models.epnlg_single import EPNLGSingle  # noqa: E501
from openapi_server.models.epnls_single import EPNLSSingle  # noqa: E501
from openapi_server.models.eprx_single import EPRxSingle  # noqa: E501
from openapi_server.models.eps1_u_single import EPS1USingle  # noqa: E501
from openapi_server.models.eps5_c_single import EPS5CSingle  # noqa: E501
from openapi_server.models.eps5_u_single import EPS5USingle  # noqa: E501
from openapi_server.models.epx2_c_single import EPX2CSingle  # noqa: E501
from openapi_server.models.epx2_u_single import EPX2USingle  # noqa: E501
from openapi_server.models.epxn_c_single import EPXnCSingle  # noqa: E501
from openapi_server.models.epxn_u_single import EPXnUSingle  # noqa: E501
from openapi_server.models.external_amf_function_single import ExternalAmfFunctionSingle  # noqa: E501
from openapi_server.models.external_enb_function_single import ExternalENBFunctionSingle  # noqa: E501
from openapi_server.models.external_eu_tran_cell_single import ExternalEUTranCellSingle  # noqa: E501
from openapi_server.models.external_gnb_cu_cp_function_single import ExternalGnbCuCpFunctionSingle  # noqa: E501
from openapi_server.models.external_nr_cell_cu_single import ExternalNrCellCuSingle  # noqa: E501
from openapi_server.models.external_nrf_function_single import ExternalNrfFunctionSingle  # noqa: E501
from openapi_server.models.external_nssf_function_single import ExternalNssfFunctionSingle  # noqa: E501
from openapi_server.models.feasibility_check_and_reservation_job_single import FeasibilityCheckAndReservationJobSingle  # noqa: E501
from openapi_server.models.file_download_job_single import FileDownloadJobSingle  # noqa: E501
from openapi_server.models.files_single import FilesSingle  # noqa: E501
from openapi_server.models.five_qi_dscp_mapping_set_single import FiveQiDscpMappingSetSingle  # noqa: E501
from openapi_server.models.fulfilment_info import FulfilmentInfo  # noqa: E501
from openapi_server.models.gnb_cu_cp_function_single import GnbCuCpFunctionSingle  # noqa: E501
from openapi_server.models.gnb_cu_up_function_single import GnbCuUpFunctionSingle  # noqa: E501
from openapi_server.models.gnb_du_function_single import GnbDuFunctionSingle  # noqa: E501
from openapi_server.models.gtp_u_path_qo_s_monitoring_control_single import GtpUPathQoSMonitoringControlSingle  # noqa: E501
from openapi_server.models.heartbeat_control_single import HeartbeatControlSingle  # noqa: E501
from openapi_server.models.intent_context import IntentContext  # noqa: E501
from openapi_server.models.intent_single import IntentSingle  # noqa: E501
from openapi_server.models.intent_single_all_of_intent_expectations_inner import IntentSingleAllOfIntentExpectationsInner  # noqa: E501
from openapi_server.models.lmf_function_single import LmfFunctionSingle  # noqa: E501
from openapi_server.models.managed_element_single import ManagedElementSingle  # noqa: E501
from openapi_server.models.managed_nf_service_single import ManagedNFServiceSingle  # noqa: E501
from openapi_server.models.management_data_collection_single import ManagementDataCollectionSingle  # noqa: E501
from openapi_server.models.management_node_single import ManagementNodeSingle  # noqa: E501
from openapi_server.models.me_context_single import MeContextSingle  # noqa: E501
from openapi_server.models.mns_agent_single import MnsAgentSingle  # noqa: E501
from openapi_server.models.mns_info_single import MnsInfoSingle  # noqa: E501
from openapi_server.models.mns_registry_single import MnsRegistrySingle  # noqa: E501
from openapi_server.models.n3iwf_function_single import N3iwfFunctionSingle  # noqa: E501
from openapi_server.models.nef_function_single import NefFunctionSingle  # noqa: E501
from openapi_server.models.network_slice_single import NetworkSliceSingle  # noqa: E501
from openapi_server.models.network_slice_subnet_provider_capabilities_single import NetworkSliceSubnetProviderCapabilitiesSingle  # noqa: E501
from openapi_server.models.network_slice_subnet_single import NetworkSliceSubnetSingle  # noqa: E501
from openapi_server.models.ngeir_function_single import NgeirFunctionSingle  # noqa: E501
from openapi_server.models.nr_cell_cu_single import NrCellCuSingle  # noqa: E501
from openapi_server.models.nr_cell_du_single import NrCellDuSingle  # noqa: E501
from openapi_server.models.nr_cell_relation_single import NRCellRelationSingle  # noqa: E501
from openapi_server.models.nr_freq_relation_single import NRFreqRelationSingle  # noqa: E501
from openapi_server.models.nr_frequency_single import NRFrequencySingle  # noqa: E501
from openapi_server.models.nr_operator_cell_du_single import NrOperatorCellDuSingle  # noqa: E501
from openapi_server.models.nr_sector_carrier_single import NrSectorCarrierSingle  # noqa: E501
from openapi_server.models.nrf_function_single import NrfFunctionSingle  # noqa: E501
from openapi_server.models.nssf_function_single import NssfFunctionSingle  # noqa: E501
from openapi_server.models.ntf_subscription_control_single import NtfSubscriptionControlSingle  # noqa: E501
from openapi_server.models.nwdaf_function_single import NwdafFunctionSingle  # noqa: E501
from openapi_server.models.operator_du_single import OperatorDuSingle  # noqa: E501
from openapi_server.models.pcf_function_single import PcfFunctionSingle  # noqa: E501
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle  # noqa: E501
from openapi_server.models.plmn_info import PlmnInfo  # noqa: E501
from openapi_server.models.predefined_pcc_rule_set_single import PredefinedPccRuleSetSingle  # noqa: E501
from openapi_server.models.qfqo_s_monitoring_control_single import QFQoSMonitoringControlSingle  # noqa: E501
from openapi_server.models.resource_one_of import ResourceOneOf  # noqa: E501
from openapi_server.models.resource_one_of1 import ResourceOneOf1  # noqa: E501
from openapi_server.models.rim_rs_global_single import RimRSGlobalSingle  # noqa: E501
from openapi_server.models.rim_rs_set_single import RimRSSetSingle  # noqa: E501
from openapi_server.models.rrm_policy_ratio_single import RRMPolicyRatioSingle  # noqa: E501
from openapi_server.models.scp_function_single import ScpFunctionSingle  # noqa: E501
from openapi_server.models.sepp_function_single import SeppFunctionSingle  # noqa: E501
from openapi_server.models.smf_function_single import SmfFunctionSingle  # noqa: E501
from openapi_server.models.smsf_function_single import SmsfFunctionSingle  # noqa: E501
from openapi_server.models.sub_network_single import SubNetworkSingle  # noqa: E501
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle  # noqa: E501
from openapi_server.models.trace_job_single import TraceJobSingle  # noqa: E501
from openapi_server.models.udm_function_single import UdmFunctionSingle  # noqa: E501
from openapi_server.models.udr_function_single import UdrFunctionSingle  # noqa: E501
from openapi_server.models.udsf_function_single import UdsfFunctionSingle  # noqa: E501
from openapi_server.models.upf_function_single import UpfFunctionSingle  # noqa: E501
from openapi_server.models.vs_data_container_single import VsDataContainerSingle  # noqa: E501

class Resource(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, object_class=None, object_instance=None, attributes=None, vs_data_container=None, mns_agent=None, files=None, heartbeat_control=None, mns_info=None, mns_label=None, mns_type=None, mns_version=None, mns_address=None, mns_scope=None, sub_network=None, managed_element=None, management_node=None, me_context=None, perf_metric_job=None, threshold_monitor=None, trace_job=None, management_data_collection=None, ntf_subscription_control=None, alarm_list=None, file_download_job=None, mns_registry=None, nr_frequency=None, external_gnb_cu_cp_function=None, external_enb_function=None, e_utran_frequency=None, des_management_function=None, drach_optimization_function=None, dmro_function=None, dlbo_function=None, dpci_configuration_function=None, cpci_configuration_function=None, ces_management_function=None, configurable5_qi_set=None, rim_rs_global=None, dynamic5_qi_set=None, cco_function=None, gnb_du_function=None, gnb_cu_up_function=None, gnb_cu_cp_function=None, managed_nf_service=None, rrm_policy_ratio=None, nr_cell_du=None, bwp_multiple=None, nr_sector_carrier_multiple=None, ep_f1_c=None, ep_f1_u=None, operator_du=None, ep_e1=None, ep_xn_u=None, ep_ng_u=None, ep_x2_u=None, ep_s1_u=None, nr_cell_cu=None, ep_xn_c=None, ep_ng_c=None, ep_x2_c=None, danr_management_function=None, gnb_id=None, gnb_id_length=None, nr_cell_relation=None, e_utran_cell_relation=None, nr_freq_relation=None, e_utran_freq_relation=None, nr_operator_cell_du=None, cell_local_id=None, administrative_state=None, plmn_info_list=None, nr_tac=None, common_beamforming_function=None, beam=None, rim_rs_set=None, external_nr_cell_cu=None, external_eu_tran_cell=None, external_amf_function=None, external_nrf_function=None, external_nssf_function=None, amf_set=None, amf_region=None, ecm_connection_info=None, amf_function=None, smf_function=None, upf_function=None, n3iwf_function=None, pcf_function=None, ausf_function=None, udm_function=None, udr_function=None, udsf_function=None, nrf_function=None, nssf_function=None, smsf_function=None, lmf_function=None, ngeir_function=None, sepp_function=None, nwdaf_function=None, scp_function=None, nef_function=None, easdf_function=None, ep_n2=None, ep_n8=None, ep_n11=None, ep_n12=None, ep_n14=None, ep_n15=None, ep_n17=None, ep_n20=None, ep_n22=None, ep_n26=None, ep_nls=None, ep_nlg=None, ep_n4=None, ep_n7=None, ep_n10=None, ep_n16=None, ep_s5_c=None, five_qi_dscp_mapping_set=None, gtp_u_path_qo_s_monitoring_control=None, qfqo_s_monitoring_control=None, predefined_pcc_rule_set=None, ep_n3=None, ep_n6=None, ep_n9=None, ep_s5_u=None, ep_n5=None, ep_rx=None, ep_n13=None, ep_n27=None, ep_n31=None, ep_n21=None, ep_map_smsc=None, ep_n32=None, ep_n33=None, ep_n60=None, ep_npc4=None, ep_npc6=None, ep_npc7=None, ep_npc8=None, ep_n88=None, network_slice=None, network_slice_subnet=None, ep_transport=None, network_slice_subnet_provider_capabilities=None, feasibility_check_and_reservation_job=None, assurance_goal=None, assurance_closed_control_loop=None, intent=None, user_label=None, intent_expectations=None, intent_contexts=None, intent_fulfilment_info=None):  # noqa: E501
        """Resource - a model defined in OpenAPI

        :param id: The id of this Resource.  # noqa: E501
        :type id: str
        :param object_class: The object_class of this Resource.  # noqa: E501
        :type object_class: str
        :param object_instance: The object_instance of this Resource.  # noqa: E501
        :type object_instance: str
        :param attributes: The attributes of this Resource.  # noqa: E501
        :type attributes: AssuranceReportSingleAllOfAttributes
        :param vs_data_container: The vs_data_container of this Resource.  # noqa: E501
        :type vs_data_container: List[VsDataContainerSingle]
        :param mns_agent: The mns_agent of this Resource.  # noqa: E501
        :type mns_agent: List[MnsAgentSingle]
        :param files: The files of this Resource.  # noqa: E501
        :type files: List[FilesSingle]
        :param heartbeat_control: The heartbeat_control of this Resource.  # noqa: E501
        :type heartbeat_control: HeartbeatControlSingle
        :param mns_info: The mns_info of this Resource.  # noqa: E501
        :type mns_info: List[MnsInfoSingle]
        :param mns_label: The mns_label of this Resource.  # noqa: E501
        :type mns_label: str
        :param mns_type: The mns_type of this Resource.  # noqa: E501
        :type mns_type: str
        :param mns_version: The mns_version of this Resource.  # noqa: E501
        :type mns_version: str
        :param mns_address: The mns_address of this Resource.  # noqa: E501
        :type mns_address: str
        :param mns_scope: The mns_scope of this Resource.  # noqa: E501
        :type mns_scope: List[str]
        :param sub_network: The sub_network of this Resource.  # noqa: E501
        :type sub_network: List[SubNetworkSingle]
        :param managed_element: The managed_element of this Resource.  # noqa: E501
        :type managed_element: List[ManagedElementSingle]
        :param management_node: The management_node of this Resource.  # noqa: E501
        :type management_node: List[ManagementNodeSingle]
        :param me_context: The me_context of this Resource.  # noqa: E501
        :type me_context: List[MeContextSingle]
        :param perf_metric_job: The perf_metric_job of this Resource.  # noqa: E501
        :type perf_metric_job: List[PerfMetricJobSingle]
        :param threshold_monitor: The threshold_monitor of this Resource.  # noqa: E501
        :type threshold_monitor: List[ThresholdMonitorSingle]
        :param trace_job: The trace_job of this Resource.  # noqa: E501
        :type trace_job: List[TraceJobSingle]
        :param management_data_collection: The management_data_collection of this Resource.  # noqa: E501
        :type management_data_collection: List[ManagementDataCollectionSingle]
        :param ntf_subscription_control: The ntf_subscription_control of this Resource.  # noqa: E501
        :type ntf_subscription_control: List[NtfSubscriptionControlSingle]
        :param alarm_list: The alarm_list of this Resource.  # noqa: E501
        :type alarm_list: AlarmListSingle
        :param file_download_job: The file_download_job of this Resource.  # noqa: E501
        :type file_download_job: List[FileDownloadJobSingle]
        :param mns_registry: The mns_registry of this Resource.  # noqa: E501
        :type mns_registry: MnsRegistrySingle
        :param nr_frequency: The nr_frequency of this Resource.  # noqa: E501
        :type nr_frequency: List[NRFrequencySingle]
        :param external_gnb_cu_cp_function: The external_gnb_cu_cp_function of this Resource.  # noqa: E501
        :type external_gnb_cu_cp_function: List[ExternalGnbCuCpFunctionSingle]
        :param external_enb_function: The external_enb_function of this Resource.  # noqa: E501
        :type external_enb_function: List[ExternalENBFunctionSingle]
        :param e_utran_frequency: The e_utran_frequency of this Resource.  # noqa: E501
        :type e_utran_frequency: List[EUtranFrequencySingle]
        :param des_management_function: The des_management_function of this Resource.  # noqa: E501
        :type des_management_function: DESManagementFunctionSingle
        :param drach_optimization_function: The drach_optimization_function of this Resource.  # noqa: E501
        :type drach_optimization_function: DRACHOptimizationFunctionSingle
        :param dmro_function: The dmro_function of this Resource.  # noqa: E501
        :type dmro_function: DMROFunctionSingle
        :param dlbo_function: The dlbo_function of this Resource.  # noqa: E501
        :type dlbo_function: DLBOFunctionSingle
        :param dpci_configuration_function: The dpci_configuration_function of this Resource.  # noqa: E501
        :type dpci_configuration_function: DPCIConfigurationFunctionSingle
        :param cpci_configuration_function: The cpci_configuration_function of this Resource.  # noqa: E501
        :type cpci_configuration_function: CPCIConfigurationFunctionSingle
        :param ces_management_function: The ces_management_function of this Resource.  # noqa: E501
        :type ces_management_function: CESManagementFunctionSingle
        :param configurable5_qi_set: The configurable5_qi_set of this Resource.  # noqa: E501
        :type configurable5_qi_set: List[Configurable5QISetSingle]
        :param rim_rs_global: The rim_rs_global of this Resource.  # noqa: E501
        :type rim_rs_global: RimRSGlobalSingle
        :param dynamic5_qi_set: The dynamic5_qi_set of this Resource.  # noqa: E501
        :type dynamic5_qi_set: List[Dynamic5QISetSingle]
        :param cco_function: The cco_function of this Resource.  # noqa: E501
        :type cco_function: CCOFunctionSingle
        :param gnb_du_function: The gnb_du_function of this Resource.  # noqa: E501
        :type gnb_du_function: List[GnbDuFunctionSingle]
        :param gnb_cu_up_function: The gnb_cu_up_function of this Resource.  # noqa: E501
        :type gnb_cu_up_function: List[GnbCuUpFunctionSingle]
        :param gnb_cu_cp_function: The gnb_cu_cp_function of this Resource.  # noqa: E501
        :type gnb_cu_cp_function: List[GnbCuCpFunctionSingle]
        :param managed_nf_service: The managed_nf_service of this Resource.  # noqa: E501
        :type managed_nf_service: List[ManagedNFServiceSingle]
        :param rrm_policy_ratio: The rrm_policy_ratio of this Resource.  # noqa: E501
        :type rrm_policy_ratio: List[RRMPolicyRatioSingle]
        :param nr_cell_du: The nr_cell_du of this Resource.  # noqa: E501
        :type nr_cell_du: List[NrCellDuSingle]
        :param bwp_multiple: The bwp_multiple of this Resource.  # noqa: E501
        :type bwp_multiple: List[BwpSingle]
        :param nr_sector_carrier_multiple: The nr_sector_carrier_multiple of this Resource.  # noqa: E501
        :type nr_sector_carrier_multiple: List[NrSectorCarrierSingle]
        :param ep_f1_c: The ep_f1_c of this Resource.  # noqa: E501
        :type ep_f1_c: List[EPF1CSingle]
        :param ep_f1_u: The ep_f1_u of this Resource.  # noqa: E501
        :type ep_f1_u: List[EPF1USingle]
        :param operator_du: The operator_du of this Resource.  # noqa: E501
        :type operator_du: List[OperatorDuSingle]
        :param ep_e1: The ep_e1 of this Resource.  # noqa: E501
        :type ep_e1: List[EPE1Single]
        :param ep_xn_u: The ep_xn_u of this Resource.  # noqa: E501
        :type ep_xn_u: List[EPXnUSingle]
        :param ep_ng_u: The ep_ng_u of this Resource.  # noqa: E501
        :type ep_ng_u: List[EPNgUSingle]
        :param ep_x2_u: The ep_x2_u of this Resource.  # noqa: E501
        :type ep_x2_u: List[EPX2USingle]
        :param ep_s1_u: The ep_s1_u of this Resource.  # noqa: E501
        :type ep_s1_u: List[EPS1USingle]
        :param nr_cell_cu: The nr_cell_cu of this Resource.  # noqa: E501
        :type nr_cell_cu: List[NrCellCuSingle]
        :param ep_xn_c: The ep_xn_c of this Resource.  # noqa: E501
        :type ep_xn_c: List[EPXnCSingle]
        :param ep_ng_c: The ep_ng_c of this Resource.  # noqa: E501
        :type ep_ng_c: List[EPNgCSingle]
        :param ep_x2_c: The ep_x2_c of this Resource.  # noqa: E501
        :type ep_x2_c: List[EPX2CSingle]
        :param danr_management_function: The danr_management_function of this Resource.  # noqa: E501
        :type danr_management_function: DANRManagementFunctionSingle
        :param gnb_id: The gnb_id of this Resource.  # noqa: E501
        :type gnb_id: str
        :param gnb_id_length: The gnb_id_length of this Resource.  # noqa: E501
        :type gnb_id_length: int
        :param nr_cell_relation: The nr_cell_relation of this Resource.  # noqa: E501
        :type nr_cell_relation: List[NRCellRelationSingle]
        :param e_utran_cell_relation: The e_utran_cell_relation of this Resource.  # noqa: E501
        :type e_utran_cell_relation: List[EUtranCellRelationSingle]
        :param nr_freq_relation: The nr_freq_relation of this Resource.  # noqa: E501
        :type nr_freq_relation: List[NRFreqRelationSingle]
        :param e_utran_freq_relation: The e_utran_freq_relation of this Resource.  # noqa: E501
        :type e_utran_freq_relation: List[EUtranFreqRelationSingle]
        :param nr_operator_cell_du: The nr_operator_cell_du of this Resource.  # noqa: E501
        :type nr_operator_cell_du: List[NrOperatorCellDuSingle]
        :param cell_local_id: The cell_local_id of this Resource.  # noqa: E501
        :type cell_local_id: int
        :param administrative_state: The administrative_state of this Resource.  # noqa: E501
        :type administrative_state: AdministrativeState
        :param plmn_info_list: The plmn_info_list of this Resource.  # noqa: E501
        :type plmn_info_list: List[PlmnInfo]
        :param nr_tac: The nr_tac of this Resource.  # noqa: E501
        :type nr_tac: int
        :param common_beamforming_function: The common_beamforming_function of this Resource.  # noqa: E501
        :type common_beamforming_function: CommonBeamformingFunctionSingle
        :param beam: The beam of this Resource.  # noqa: E501
        :type beam: List[BeamSingle]
        :param rim_rs_set: The rim_rs_set of this Resource.  # noqa: E501
        :type rim_rs_set: List[RimRSSetSingle]
        :param external_nr_cell_cu: The external_nr_cell_cu of this Resource.  # noqa: E501
        :type external_nr_cell_cu: List[ExternalNrCellCuSingle]
        :param external_eu_tran_cell: The external_eu_tran_cell of this Resource.  # noqa: E501
        :type external_eu_tran_cell: List[ExternalEUTranCellSingle]
        :param external_amf_function: The external_amf_function of this Resource.  # noqa: E501
        :type external_amf_function: List[ExternalAmfFunctionSingle]
        :param external_nrf_function: The external_nrf_function of this Resource.  # noqa: E501
        :type external_nrf_function: List[ExternalNrfFunctionSingle]
        :param external_nssf_function: The external_nssf_function of this Resource.  # noqa: E501
        :type external_nssf_function: List[ExternalNssfFunctionSingle]
        :param amf_set: The amf_set of this Resource.  # noqa: E501
        :type amf_set: List[AmfSetSingle]
        :param amf_region: The amf_region of this Resource.  # noqa: E501
        :type amf_region: List[AmfRegionSingle]
        :param ecm_connection_info: The ecm_connection_info of this Resource.  # noqa: E501
        :type ecm_connection_info: List[EcmConnectionInfoSingle]
        :param amf_function: The amf_function of this Resource.  # noqa: E501
        :type amf_function: List[AmfFunctionSingle]
        :param smf_function: The smf_function of this Resource.  # noqa: E501
        :type smf_function: List[SmfFunctionSingle]
        :param upf_function: The upf_function of this Resource.  # noqa: E501
        :type upf_function: List[UpfFunctionSingle]
        :param n3iwf_function: The n3iwf_function of this Resource.  # noqa: E501
        :type n3iwf_function: List[N3iwfFunctionSingle]
        :param pcf_function: The pcf_function of this Resource.  # noqa: E501
        :type pcf_function: List[PcfFunctionSingle]
        :param ausf_function: The ausf_function of this Resource.  # noqa: E501
        :type ausf_function: List[AusfFunctionSingle]
        :param udm_function: The udm_function of this Resource.  # noqa: E501
        :type udm_function: List[UdmFunctionSingle]
        :param udr_function: The udr_function of this Resource.  # noqa: E501
        :type udr_function: List[UdrFunctionSingle]
        :param udsf_function: The udsf_function of this Resource.  # noqa: E501
        :type udsf_function: List[UdsfFunctionSingle]
        :param nrf_function: The nrf_function of this Resource.  # noqa: E501
        :type nrf_function: List[NrfFunctionSingle]
        :param nssf_function: The nssf_function of this Resource.  # noqa: E501
        :type nssf_function: List[NssfFunctionSingle]
        :param smsf_function: The smsf_function of this Resource.  # noqa: E501
        :type smsf_function: List[SmsfFunctionSingle]
        :param lmf_function: The lmf_function of this Resource.  # noqa: E501
        :type lmf_function: List[LmfFunctionSingle]
        :param ngeir_function: The ngeir_function of this Resource.  # noqa: E501
        :type ngeir_function: List[NgeirFunctionSingle]
        :param sepp_function: The sepp_function of this Resource.  # noqa: E501
        :type sepp_function: List[SeppFunctionSingle]
        :param nwdaf_function: The nwdaf_function of this Resource.  # noqa: E501
        :type nwdaf_function: List[NwdafFunctionSingle]
        :param scp_function: The scp_function of this Resource.  # noqa: E501
        :type scp_function: List[ScpFunctionSingle]
        :param nef_function: The nef_function of this Resource.  # noqa: E501
        :type nef_function: List[NefFunctionSingle]
        :param easdf_function: The easdf_function of this Resource.  # noqa: E501
        :type easdf_function: List[EASDFFunctionSingle]
        :param ep_n2: The ep_n2 of this Resource.  # noqa: E501
        :type ep_n2: List[EPN2Single]
        :param ep_n8: The ep_n8 of this Resource.  # noqa: E501
        :type ep_n8: List[EPN8Single]
        :param ep_n11: The ep_n11 of this Resource.  # noqa: E501
        :type ep_n11: List[EPN11Single]
        :param ep_n12: The ep_n12 of this Resource.  # noqa: E501
        :type ep_n12: List[EPN12Single]
        :param ep_n14: The ep_n14 of this Resource.  # noqa: E501
        :type ep_n14: List[EPN14Single]
        :param ep_n15: The ep_n15 of this Resource.  # noqa: E501
        :type ep_n15: List[EPN15Single]
        :param ep_n17: The ep_n17 of this Resource.  # noqa: E501
        :type ep_n17: List[EPN17Single]
        :param ep_n20: The ep_n20 of this Resource.  # noqa: E501
        :type ep_n20: List[EPN20Single]
        :param ep_n22: The ep_n22 of this Resource.  # noqa: E501
        :type ep_n22: List[EPN22Single]
        :param ep_n26: The ep_n26 of this Resource.  # noqa: E501
        :type ep_n26: List[EPN26Single]
        :param ep_nls: The ep_nls of this Resource.  # noqa: E501
        :type ep_nls: List[EPNLSSingle]
        :param ep_nlg: The ep_nlg of this Resource.  # noqa: E501
        :type ep_nlg: List[EPNLGSingle]
        :param ep_n4: The ep_n4 of this Resource.  # noqa: E501
        :type ep_n4: List[EPN4Single]
        :param ep_n7: The ep_n7 of this Resource.  # noqa: E501
        :type ep_n7: List[EPN7Single]
        :param ep_n10: The ep_n10 of this Resource.  # noqa: E501
        :type ep_n10: List[EPN10Single]
        :param ep_n16: The ep_n16 of this Resource.  # noqa: E501
        :type ep_n16: List[EPN16Single]
        :param ep_s5_c: The ep_s5_c of this Resource.  # noqa: E501
        :type ep_s5_c: List[EPS5CSingle]
        :param five_qi_dscp_mapping_set: The five_qi_dscp_mapping_set of this Resource.  # noqa: E501
        :type five_qi_dscp_mapping_set: FiveQiDscpMappingSetSingle
        :param gtp_u_path_qo_s_monitoring_control: The gtp_u_path_qo_s_monitoring_control of this Resource.  # noqa: E501
        :type gtp_u_path_qo_s_monitoring_control: GtpUPathQoSMonitoringControlSingle
        :param qfqo_s_monitoring_control: The qfqo_s_monitoring_control of this Resource.  # noqa: E501
        :type qfqo_s_monitoring_control: QFQoSMonitoringControlSingle
        :param predefined_pcc_rule_set: The predefined_pcc_rule_set of this Resource.  # noqa: E501
        :type predefined_pcc_rule_set: PredefinedPccRuleSetSingle
        :param ep_n3: The ep_n3 of this Resource.  # noqa: E501
        :type ep_n3: List[EPN3Single]
        :param ep_n6: The ep_n6 of this Resource.  # noqa: E501
        :type ep_n6: List[EPN6Single]
        :param ep_n9: The ep_n9 of this Resource.  # noqa: E501
        :type ep_n9: List[EPN9Single]
        :param ep_s5_u: The ep_s5_u of this Resource.  # noqa: E501
        :type ep_s5_u: List[EPS5USingle]
        :param ep_n5: The ep_n5 of this Resource.  # noqa: E501
        :type ep_n5: List[EPN5Single]
        :param ep_rx: The ep_rx of this Resource.  # noqa: E501
        :type ep_rx: List[EPRxSingle]
        :param ep_n13: The ep_n13 of this Resource.  # noqa: E501
        :type ep_n13: List[EPN13Single]
        :param ep_n27: The ep_n27 of this Resource.  # noqa: E501
        :type ep_n27: List[EPN27Single]
        :param ep_n31: The ep_n31 of this Resource.  # noqa: E501
        :type ep_n31: List[EPN31Single]
        :param ep_n21: The ep_n21 of this Resource.  # noqa: E501
        :type ep_n21: List[EPN21Single]
        :param ep_map_smsc: The ep_map_smsc of this Resource.  # noqa: E501
        :type ep_map_smsc: List[EPMAPSMSCSingle]
        :param ep_n32: The ep_n32 of this Resource.  # noqa: E501
        :type ep_n32: List[EPN32Single]
        :param ep_n33: The ep_n33 of this Resource.  # noqa: E501
        :type ep_n33: List[EPN33Single]
        :param ep_n60: The ep_n60 of this Resource.  # noqa: E501
        :type ep_n60: List[EPN60Single]
        :param ep_npc4: The ep_npc4 of this Resource.  # noqa: E501
        :type ep_npc4: List[EPNpc4Single]
        :param ep_npc6: The ep_npc6 of this Resource.  # noqa: E501
        :type ep_npc6: List[EPNpc6Single]
        :param ep_npc7: The ep_npc7 of this Resource.  # noqa: E501
        :type ep_npc7: List[EPNpc7Single]
        :param ep_npc8: The ep_npc8 of this Resource.  # noqa: E501
        :type ep_npc8: List[EPNpc8Single]
        :param ep_n88: The ep_n88 of this Resource.  # noqa: E501
        :type ep_n88: List[EPN88Single]
        :param network_slice: The network_slice of this Resource.  # noqa: E501
        :type network_slice: List[NetworkSliceSingle]
        :param network_slice_subnet: The network_slice_subnet of this Resource.  # noqa: E501
        :type network_slice_subnet: List[NetworkSliceSubnetSingle]
        :param ep_transport: The ep_transport of this Resource.  # noqa: E501
        :type ep_transport: List[EPTransportSingle]
        :param network_slice_subnet_provider_capabilities: The network_slice_subnet_provider_capabilities of this Resource.  # noqa: E501
        :type network_slice_subnet_provider_capabilities: List[NetworkSliceSubnetProviderCapabilitiesSingle]
        :param feasibility_check_and_reservation_job: The feasibility_check_and_reservation_job of this Resource.  # noqa: E501
        :type feasibility_check_and_reservation_job: List[FeasibilityCheckAndReservationJobSingle]
        :param assurance_goal: The assurance_goal of this Resource.  # noqa: E501
        :type assurance_goal: List[AssuranceGoalSingle]
        :param assurance_closed_control_loop: The assurance_closed_control_loop of this Resource.  # noqa: E501
        :type assurance_closed_control_loop: List[AssuranceClosedControlLoopSingle]
        :param intent: The intent of this Resource.  # noqa: E501
        :type intent: List[IntentSingle]
        :param user_label: The user_label of this Resource.  # noqa: E501
        :type user_label: str
        :param intent_expectations: The intent_expectations of this Resource.  # noqa: E501
        :type intent_expectations: List[IntentSingleAllOfIntentExpectationsInner]
        :param intent_contexts: The intent_contexts of this Resource.  # noqa: E501
        :type intent_contexts: List[IntentContext]
        :param intent_fulfilment_info: The intent_fulfilment_info of this Resource.  # noqa: E501
        :type intent_fulfilment_info: FulfilmentInfo
        """
        self.openapi_types = {
            'id': str,
            'object_class': str,
            'object_instance': str,
            'attributes': AssuranceReportSingleAllOfAttributes,
            'vs_data_container': List[VsDataContainerSingle],
            'mns_agent': List[MnsAgentSingle],
            'files': List[FilesSingle],
            'heartbeat_control': HeartbeatControlSingle,
            'mns_info': List[MnsInfoSingle],
            'mns_label': str,
            'mns_type': str,
            'mns_version': str,
            'mns_address': str,
            'mns_scope': List[str],
            'sub_network': List[SubNetworkSingle],
            'managed_element': List[ManagedElementSingle],
            'management_node': List[ManagementNodeSingle],
            'me_context': List[MeContextSingle],
            'perf_metric_job': List[PerfMetricJobSingle],
            'threshold_monitor': List[ThresholdMonitorSingle],
            'trace_job': List[TraceJobSingle],
            'management_data_collection': List[ManagementDataCollectionSingle],
            'ntf_subscription_control': List[NtfSubscriptionControlSingle],
            'alarm_list': AlarmListSingle,
            'file_download_job': List[FileDownloadJobSingle],
            'mns_registry': MnsRegistrySingle,
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
            'cco_function': CCOFunctionSingle,
            'gnb_du_function': List[GnbDuFunctionSingle],
            'gnb_cu_up_function': List[GnbCuUpFunctionSingle],
            'gnb_cu_cp_function': List[GnbCuCpFunctionSingle],
            'managed_nf_service': List[ManagedNFServiceSingle],
            'rrm_policy_ratio': List[RRMPolicyRatioSingle],
            'nr_cell_du': List[NrCellDuSingle],
            'bwp_multiple': List[BwpSingle],
            'nr_sector_carrier_multiple': List[NrSectorCarrierSingle],
            'ep_f1_c': List[EPF1CSingle],
            'ep_f1_u': List[EPF1USingle],
            'operator_du': List[OperatorDuSingle],
            'ep_e1': List[EPE1Single],
            'ep_xn_u': List[EPXnUSingle],
            'ep_ng_u': List[EPNgUSingle],
            'ep_x2_u': List[EPX2USingle],
            'ep_s1_u': List[EPS1USingle],
            'nr_cell_cu': List[NrCellCuSingle],
            'ep_xn_c': List[EPXnCSingle],
            'ep_ng_c': List[EPNgCSingle],
            'ep_x2_c': List[EPX2CSingle],
            'danr_management_function': DANRManagementFunctionSingle,
            'gnb_id': str,
            'gnb_id_length': int,
            'nr_cell_relation': List[NRCellRelationSingle],
            'e_utran_cell_relation': List[EUtranCellRelationSingle],
            'nr_freq_relation': List[NRFreqRelationSingle],
            'e_utran_freq_relation': List[EUtranFreqRelationSingle],
            'nr_operator_cell_du': List[NrOperatorCellDuSingle],
            'cell_local_id': int,
            'administrative_state': AdministrativeState,
            'plmn_info_list': List[PlmnInfo],
            'nr_tac': int,
            'common_beamforming_function': CommonBeamformingFunctionSingle,
            'beam': List[BeamSingle],
            'rim_rs_set': List[RimRSSetSingle],
            'external_nr_cell_cu': List[ExternalNrCellCuSingle],
            'external_eu_tran_cell': List[ExternalEUTranCellSingle],
            'external_amf_function': List[ExternalAmfFunctionSingle],
            'external_nrf_function': List[ExternalNrfFunctionSingle],
            'external_nssf_function': List[ExternalNssfFunctionSingle],
            'amf_set': List[AmfSetSingle],
            'amf_region': List[AmfRegionSingle],
            'ecm_connection_info': List[EcmConnectionInfoSingle],
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
            'easdf_function': List[EASDFFunctionSingle],
            'ep_n2': List[EPN2Single],
            'ep_n8': List[EPN8Single],
            'ep_n11': List[EPN11Single],
            'ep_n12': List[EPN12Single],
            'ep_n14': List[EPN14Single],
            'ep_n15': List[EPN15Single],
            'ep_n17': List[EPN17Single],
            'ep_n20': List[EPN20Single],
            'ep_n22': List[EPN22Single],
            'ep_n26': List[EPN26Single],
            'ep_nls': List[EPNLSSingle],
            'ep_nlg': List[EPNLGSingle],
            'ep_n4': List[EPN4Single],
            'ep_n7': List[EPN7Single],
            'ep_n10': List[EPN10Single],
            'ep_n16': List[EPN16Single],
            'ep_s5_c': List[EPS5CSingle],
            'five_qi_dscp_mapping_set': FiveQiDscpMappingSetSingle,
            'gtp_u_path_qo_s_monitoring_control': GtpUPathQoSMonitoringControlSingle,
            'qfqo_s_monitoring_control': QFQoSMonitoringControlSingle,
            'predefined_pcc_rule_set': PredefinedPccRuleSetSingle,
            'ep_n3': List[EPN3Single],
            'ep_n6': List[EPN6Single],
            'ep_n9': List[EPN9Single],
            'ep_s5_u': List[EPS5USingle],
            'ep_n5': List[EPN5Single],
            'ep_rx': List[EPRxSingle],
            'ep_n13': List[EPN13Single],
            'ep_n27': List[EPN27Single],
            'ep_n31': List[EPN31Single],
            'ep_n21': List[EPN21Single],
            'ep_map_smsc': List[EPMAPSMSCSingle],
            'ep_n32': List[EPN32Single],
            'ep_n33': List[EPN33Single],
            'ep_n60': List[EPN60Single],
            'ep_npc4': List[EPNpc4Single],
            'ep_npc6': List[EPNpc6Single],
            'ep_npc7': List[EPNpc7Single],
            'ep_npc8': List[EPNpc8Single],
            'ep_n88': List[EPN88Single],
            'network_slice': List[NetworkSliceSingle],
            'network_slice_subnet': List[NetworkSliceSubnetSingle],
            'ep_transport': List[EPTransportSingle],
            'network_slice_subnet_provider_capabilities': List[NetworkSliceSubnetProviderCapabilitiesSingle],
            'feasibility_check_and_reservation_job': List[FeasibilityCheckAndReservationJobSingle],
            'assurance_goal': List[AssuranceGoalSingle],
            'assurance_closed_control_loop': List[AssuranceClosedControlLoopSingle],
            'intent': List[IntentSingle],
            'user_label': str,
            'intent_expectations': List[IntentSingleAllOfIntentExpectationsInner],
            'intent_contexts': List[IntentContext],
            'intent_fulfilment_info': FulfilmentInfo
        }

        self.attribute_map = {
            'id': 'id',
            'object_class': 'objectClass',
            'object_instance': 'objectInstance',
            'attributes': 'attributes',
            'vs_data_container': 'VsDataContainer',
            'mns_agent': 'MnsAgent',
            'files': 'Files',
            'heartbeat_control': 'HeartbeatControl',
            'mns_info': 'MnsInfo',
            'mns_label': 'mnsLabel',
            'mns_type': 'mnsType',
            'mns_version': 'mnsVersion',
            'mns_address': 'mnsAddress',
            'mns_scope': 'mnsScope',
            'sub_network': 'SubNetwork',
            'managed_element': 'ManagedElement',
            'management_node': 'ManagementNode',
            'me_context': 'MeContext',
            'perf_metric_job': 'PerfMetricJob',
            'threshold_monitor': 'ThresholdMonitor',
            'trace_job': 'TraceJob',
            'management_data_collection': 'ManagementDataCollection',
            'ntf_subscription_control': 'NtfSubscriptionControl',
            'alarm_list': 'AlarmList',
            'file_download_job': 'FileDownloadJob',
            'mns_registry': 'MnsRegistry',
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
            'cco_function': 'CCOFunction',
            'gnb_du_function': 'GnbDuFunction',
            'gnb_cu_up_function': 'GnbCuUpFunction',
            'gnb_cu_cp_function': 'GnbCuCpFunction',
            'managed_nf_service': 'ManagedNFService',
            'rrm_policy_ratio': 'RRMPolicyRatio',
            'nr_cell_du': 'NrCellDu',
            'bwp_multiple': 'Bwp-Multiple',
            'nr_sector_carrier_multiple': 'NrSectorCarrier-Multiple',
            'ep_f1_c': 'EP_F1C',
            'ep_f1_u': 'EP_F1U',
            'operator_du': 'OperatorDU',
            'ep_e1': 'EP_E1',
            'ep_xn_u': 'EP_XnU',
            'ep_ng_u': 'EP_NgU',
            'ep_x2_u': 'EP_X2U',
            'ep_s1_u': 'EP_S1U',
            'nr_cell_cu': 'NrCellCu',
            'ep_xn_c': 'EP_XnC',
            'ep_ng_c': 'EP_NgC',
            'ep_x2_c': 'EP_X2C',
            'danr_management_function': 'DANRManagementFunction',
            'gnb_id': 'gnbId',
            'gnb_id_length': 'gnbIdLength',
            'nr_cell_relation': 'NRCellRelation',
            'e_utran_cell_relation': 'EUtranCellRelation',
            'nr_freq_relation': 'NRFreqRelation',
            'e_utran_freq_relation': 'EUtranFreqRelation',
            'nr_operator_cell_du': 'NrOperatorCellDu',
            'cell_local_id': 'cellLocalId',
            'administrative_state': 'administrativeState',
            'plmn_info_list': 'plmnInfoList',
            'nr_tac': 'nrTac',
            'common_beamforming_function': 'CommonBeamformingFunction',
            'beam': 'Beam',
            'rim_rs_set': 'RimRSSet',
            'external_nr_cell_cu': 'ExternalNrCellCu',
            'external_eu_tran_cell': 'ExternalEUTranCell',
            'external_amf_function': 'ExternalAmfFunction',
            'external_nrf_function': 'ExternalNrfFunction',
            'external_nssf_function': 'ExternalNssfFunction',
            'amf_set': 'AmfSet',
            'amf_region': 'AmfRegion',
            'ecm_connection_info': 'EcmConnectionInfo',
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
            'easdf_function': 'EASDFFunction',
            'ep_n2': 'EP_N2',
            'ep_n8': 'EP_N8',
            'ep_n11': 'EP_N11',
            'ep_n12': 'EP_N12',
            'ep_n14': 'EP_N14',
            'ep_n15': 'EP_N15',
            'ep_n17': 'EP_N17',
            'ep_n20': 'EP_N20',
            'ep_n22': 'EP_N22',
            'ep_n26': 'EP_N26',
            'ep_nls': 'EP_NLS',
            'ep_nlg': 'EP_NLG',
            'ep_n4': 'EP_N4',
            'ep_n7': 'EP_N7',
            'ep_n10': 'EP_N10',
            'ep_n16': 'EP_N16',
            'ep_s5_c': 'EP_S5C',
            'five_qi_dscp_mapping_set': 'FiveQiDscpMappingSet',
            'gtp_u_path_qo_s_monitoring_control': 'GtpUPathQoSMonitoringControl',
            'qfqo_s_monitoring_control': 'QFQoSMonitoringControl',
            'predefined_pcc_rule_set': 'PredefinedPccRuleSet',
            'ep_n3': 'EP_N3',
            'ep_n6': 'EP_N6',
            'ep_n9': 'EP_N9',
            'ep_s5_u': 'EP_S5U',
            'ep_n5': 'EP_N5',
            'ep_rx': 'EP_Rx',
            'ep_n13': 'EP_N13',
            'ep_n27': 'EP_N27',
            'ep_n31': 'EP_N31',
            'ep_n21': 'EP_N21',
            'ep_map_smsc': 'EP_MAP_SMSC',
            'ep_n32': 'EP_N32',
            'ep_n33': 'EP_N33',
            'ep_n60': 'EP_N60',
            'ep_npc4': 'EP_Npc4',
            'ep_npc6': 'EP_Npc6',
            'ep_npc7': 'EP_Npc7',
            'ep_npc8': 'EP_Npc8',
            'ep_n88': 'EP_N88',
            'network_slice': 'NetworkSlice',
            'network_slice_subnet': 'NetworkSliceSubnet',
            'ep_transport': 'EP_Transport',
            'network_slice_subnet_provider_capabilities': 'NetworkSliceSubnetProviderCapabilities',
            'feasibility_check_and_reservation_job': 'FeasibilityCheckAndReservationJob',
            'assurance_goal': 'AssuranceGoal',
            'assurance_closed_control_loop': 'AssuranceClosedControlLoop',
            'intent': 'Intent',
            'user_label': 'userLabel',
            'intent_expectations': 'intentExpectations',
            'intent_contexts': 'intentContexts',
            'intent_fulfilment_info': 'intentFulfilmentInfo'
        }

        self._id = id
        self._object_class = object_class
        self._object_instance = object_instance
        self._attributes = attributes
        self._vs_data_container = vs_data_container
        self._mns_agent = mns_agent
        self._files = files
        self._heartbeat_control = heartbeat_control
        self._mns_info = mns_info
        self._mns_label = mns_label
        self._mns_type = mns_type
        self._mns_version = mns_version
        self._mns_address = mns_address
        self._mns_scope = mns_scope
        self._sub_network = sub_network
        self._managed_element = managed_element
        self._management_node = management_node
        self._me_context = me_context
        self._perf_metric_job = perf_metric_job
        self._threshold_monitor = threshold_monitor
        self._trace_job = trace_job
        self._management_data_collection = management_data_collection
        self._ntf_subscription_control = ntf_subscription_control
        self._alarm_list = alarm_list
        self._file_download_job = file_download_job
        self._mns_registry = mns_registry
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
        self._gnb_du_function = gnb_du_function
        self._gnb_cu_up_function = gnb_cu_up_function
        self._gnb_cu_cp_function = gnb_cu_cp_function
        self._managed_nf_service = managed_nf_service
        self._rrm_policy_ratio = rrm_policy_ratio
        self._nr_cell_du = nr_cell_du
        self._bwp_multiple = bwp_multiple
        self._nr_sector_carrier_multiple = nr_sector_carrier_multiple
        self._ep_f1_c = ep_f1_c
        self._ep_f1_u = ep_f1_u
        self._operator_du = operator_du
        self._ep_e1 = ep_e1
        self._ep_xn_u = ep_xn_u
        self._ep_ng_u = ep_ng_u
        self._ep_x2_u = ep_x2_u
        self._ep_s1_u = ep_s1_u
        self._nr_cell_cu = nr_cell_cu
        self._ep_xn_c = ep_xn_c
        self._ep_ng_c = ep_ng_c
        self._ep_x2_c = ep_x2_c
        self._danr_management_function = danr_management_function
        self._gnb_id = gnb_id
        self._gnb_id_length = gnb_id_length
        self._nr_cell_relation = nr_cell_relation
        self._e_utran_cell_relation = e_utran_cell_relation
        self._nr_freq_relation = nr_freq_relation
        self._e_utran_freq_relation = e_utran_freq_relation
        self._nr_operator_cell_du = nr_operator_cell_du
        self._cell_local_id = cell_local_id
        self._administrative_state = administrative_state
        self._plmn_info_list = plmn_info_list
        self._nr_tac = nr_tac
        self._common_beamforming_function = common_beamforming_function
        self._beam = beam
        self._rim_rs_set = rim_rs_set
        self._external_nr_cell_cu = external_nr_cell_cu
        self._external_eu_tran_cell = external_eu_tran_cell
        self._external_amf_function = external_amf_function
        self._external_nrf_function = external_nrf_function
        self._external_nssf_function = external_nssf_function
        self._amf_set = amf_set
        self._amf_region = amf_region
        self._ecm_connection_info = ecm_connection_info
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
        self._easdf_function = easdf_function
        self._ep_n2 = ep_n2
        self._ep_n8 = ep_n8
        self._ep_n11 = ep_n11
        self._ep_n12 = ep_n12
        self._ep_n14 = ep_n14
        self._ep_n15 = ep_n15
        self._ep_n17 = ep_n17
        self._ep_n20 = ep_n20
        self._ep_n22 = ep_n22
        self._ep_n26 = ep_n26
        self._ep_nls = ep_nls
        self._ep_nlg = ep_nlg
        self._ep_n4 = ep_n4
        self._ep_n7 = ep_n7
        self._ep_n10 = ep_n10
        self._ep_n16 = ep_n16
        self._ep_s5_c = ep_s5_c
        self._five_qi_dscp_mapping_set = five_qi_dscp_mapping_set
        self._gtp_u_path_qo_s_monitoring_control = gtp_u_path_qo_s_monitoring_control
        self._qfqo_s_monitoring_control = qfqo_s_monitoring_control
        self._predefined_pcc_rule_set = predefined_pcc_rule_set
        self._ep_n3 = ep_n3
        self._ep_n6 = ep_n6
        self._ep_n9 = ep_n9
        self._ep_s5_u = ep_s5_u
        self._ep_n5 = ep_n5
        self._ep_rx = ep_rx
        self._ep_n13 = ep_n13
        self._ep_n27 = ep_n27
        self._ep_n31 = ep_n31
        self._ep_n21 = ep_n21
        self._ep_map_smsc = ep_map_smsc
        self._ep_n32 = ep_n32
        self._ep_n33 = ep_n33
        self._ep_n60 = ep_n60
        self._ep_npc4 = ep_npc4
        self._ep_npc6 = ep_npc6
        self._ep_npc7 = ep_npc7
        self._ep_npc8 = ep_npc8
        self._ep_n88 = ep_n88
        self._network_slice = network_slice
        self._network_slice_subnet = network_slice_subnet
        self._ep_transport = ep_transport
        self._network_slice_subnet_provider_capabilities = network_slice_subnet_provider_capabilities
        self._feasibility_check_and_reservation_job = feasibility_check_and_reservation_job
        self._assurance_goal = assurance_goal
        self._assurance_closed_control_loop = assurance_closed_control_loop
        self._intent = intent
        self._user_label = user_label
        self._intent_expectations = intent_expectations
        self._intent_contexts = intent_contexts
        self._intent_fulfilment_info = intent_fulfilment_info

    @classmethod
    def from_dict(cls, dikt) -> 'Resource':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Resource of this Resource.  # noqa: E501
        :rtype: Resource
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Resource.


        :return: The id of this Resource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Resource.


        :param id: The id of this Resource.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def object_class(self):
        """Gets the object_class of this Resource.


        :return: The object_class of this Resource.
        :rtype: str
        """
        return self._object_class

    @object_class.setter
    def object_class(self, object_class):
        """Sets the object_class of this Resource.


        :param object_class: The object_class of this Resource.
        :type object_class: str
        """

        self._object_class = object_class

    @property
    def object_instance(self):
        """Gets the object_instance of this Resource.


        :return: The object_instance of this Resource.
        :rtype: str
        """
        return self._object_instance

    @object_instance.setter
    def object_instance(self, object_instance):
        """Sets the object_instance of this Resource.


        :param object_instance: The object_instance of this Resource.
        :type object_instance: str
        """

        self._object_instance = object_instance

    @property
    def attributes(self):
        """Gets the attributes of this Resource.


        :return: The attributes of this Resource.
        :rtype: AssuranceReportSingleAllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Resource.


        :param attributes: The attributes of this Resource.
        :type attributes: AssuranceReportSingleAllOfAttributes
        """

        self._attributes = attributes

    @property
    def vs_data_container(self):
        """Gets the vs_data_container of this Resource.


        :return: The vs_data_container of this Resource.
        :rtype: List[VsDataContainerSingle]
        """
        return self._vs_data_container

    @vs_data_container.setter
    def vs_data_container(self, vs_data_container):
        """Sets the vs_data_container of this Resource.


        :param vs_data_container: The vs_data_container of this Resource.
        :type vs_data_container: List[VsDataContainerSingle]
        """

        self._vs_data_container = vs_data_container

    @property
    def mns_agent(self):
        """Gets the mns_agent of this Resource.


        :return: The mns_agent of this Resource.
        :rtype: List[MnsAgentSingle]
        """
        return self._mns_agent

    @mns_agent.setter
    def mns_agent(self, mns_agent):
        """Sets the mns_agent of this Resource.


        :param mns_agent: The mns_agent of this Resource.
        :type mns_agent: List[MnsAgentSingle]
        """

        self._mns_agent = mns_agent

    @property
    def files(self):
        """Gets the files of this Resource.


        :return: The files of this Resource.
        :rtype: List[FilesSingle]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this Resource.


        :param files: The files of this Resource.
        :type files: List[FilesSingle]
        """

        self._files = files

    @property
    def heartbeat_control(self):
        """Gets the heartbeat_control of this Resource.


        :return: The heartbeat_control of this Resource.
        :rtype: HeartbeatControlSingle
        """
        return self._heartbeat_control

    @heartbeat_control.setter
    def heartbeat_control(self, heartbeat_control):
        """Sets the heartbeat_control of this Resource.


        :param heartbeat_control: The heartbeat_control of this Resource.
        :type heartbeat_control: HeartbeatControlSingle
        """

        self._heartbeat_control = heartbeat_control

    @property
    def mns_info(self):
        """Gets the mns_info of this Resource.


        :return: The mns_info of this Resource.
        :rtype: List[MnsInfoSingle]
        """
        return self._mns_info

    @mns_info.setter
    def mns_info(self, mns_info):
        """Sets the mns_info of this Resource.


        :param mns_info: The mns_info of this Resource.
        :type mns_info: List[MnsInfoSingle]
        """

        self._mns_info = mns_info

    @property
    def mns_label(self):
        """Gets the mns_label of this Resource.


        :return: The mns_label of this Resource.
        :rtype: str
        """
        return self._mns_label

    @mns_label.setter
    def mns_label(self, mns_label):
        """Sets the mns_label of this Resource.


        :param mns_label: The mns_label of this Resource.
        :type mns_label: str
        """

        self._mns_label = mns_label

    @property
    def mns_type(self):
        """Gets the mns_type of this Resource.


        :return: The mns_type of this Resource.
        :rtype: str
        """
        return self._mns_type

    @mns_type.setter
    def mns_type(self, mns_type):
        """Sets the mns_type of this Resource.


        :param mns_type: The mns_type of this Resource.
        :type mns_type: str
        """
        allowed_values = ["ProvMnS", "FaultSupervisionMnS", "StreamingDataReportingMnS", "FileDataReportingMnS"]  # noqa: E501
        if mns_type not in allowed_values:
            raise ValueError(
                "Invalid value for `mns_type` ({0}), must be one of {1}"
                .format(mns_type, allowed_values)
            )

        self._mns_type = mns_type

    @property
    def mns_version(self):
        """Gets the mns_version of this Resource.


        :return: The mns_version of this Resource.
        :rtype: str
        """
        return self._mns_version

    @mns_version.setter
    def mns_version(self, mns_version):
        """Sets the mns_version of this Resource.


        :param mns_version: The mns_version of this Resource.
        :type mns_version: str
        """

        self._mns_version = mns_version

    @property
    def mns_address(self):
        """Gets the mns_address of this Resource.


        :return: The mns_address of this Resource.
        :rtype: str
        """
        return self._mns_address

    @mns_address.setter
    def mns_address(self, mns_address):
        """Sets the mns_address of this Resource.


        :param mns_address: The mns_address of this Resource.
        :type mns_address: str
        """

        self._mns_address = mns_address

    @property
    def mns_scope(self):
        """Gets the mns_scope of this Resource.

        List of the managed object instances that can be accessed using the MnS. If a complete SubNetwork can be accessed using the MnS, this attribute may contain the DN of the SubNetwork instead of the DNs of the individual managed entities within the SubNetwork.  # noqa: E501

        :return: The mns_scope of this Resource.
        :rtype: List[str]
        """
        return self._mns_scope

    @mns_scope.setter
    def mns_scope(self, mns_scope):
        """Sets the mns_scope of this Resource.

        List of the managed object instances that can be accessed using the MnS. If a complete SubNetwork can be accessed using the MnS, this attribute may contain the DN of the SubNetwork instead of the DNs of the individual managed entities within the SubNetwork.  # noqa: E501

        :param mns_scope: The mns_scope of this Resource.
        :type mns_scope: List[str]
        """

        self._mns_scope = mns_scope

    @property
    def sub_network(self):
        """Gets the sub_network of this Resource.


        :return: The sub_network of this Resource.
        :rtype: List[SubNetworkSingle]
        """
        return self._sub_network

    @sub_network.setter
    def sub_network(self, sub_network):
        """Sets the sub_network of this Resource.


        :param sub_network: The sub_network of this Resource.
        :type sub_network: List[SubNetworkSingle]
        """

        self._sub_network = sub_network

    @property
    def managed_element(self):
        """Gets the managed_element of this Resource.


        :return: The managed_element of this Resource.
        :rtype: List[ManagedElementSingle]
        """
        return self._managed_element

    @managed_element.setter
    def managed_element(self, managed_element):
        """Sets the managed_element of this Resource.


        :param managed_element: The managed_element of this Resource.
        :type managed_element: List[ManagedElementSingle]
        """

        self._managed_element = managed_element

    @property
    def management_node(self):
        """Gets the management_node of this Resource.


        :return: The management_node of this Resource.
        :rtype: List[ManagementNodeSingle]
        """
        return self._management_node

    @management_node.setter
    def management_node(self, management_node):
        """Sets the management_node of this Resource.


        :param management_node: The management_node of this Resource.
        :type management_node: List[ManagementNodeSingle]
        """

        self._management_node = management_node

    @property
    def me_context(self):
        """Gets the me_context of this Resource.


        :return: The me_context of this Resource.
        :rtype: List[MeContextSingle]
        """
        return self._me_context

    @me_context.setter
    def me_context(self, me_context):
        """Sets the me_context of this Resource.


        :param me_context: The me_context of this Resource.
        :type me_context: List[MeContextSingle]
        """

        self._me_context = me_context

    @property
    def perf_metric_job(self):
        """Gets the perf_metric_job of this Resource.


        :return: The perf_metric_job of this Resource.
        :rtype: List[PerfMetricJobSingle]
        """
        return self._perf_metric_job

    @perf_metric_job.setter
    def perf_metric_job(self, perf_metric_job):
        """Sets the perf_metric_job of this Resource.


        :param perf_metric_job: The perf_metric_job of this Resource.
        :type perf_metric_job: List[PerfMetricJobSingle]
        """

        self._perf_metric_job = perf_metric_job

    @property
    def threshold_monitor(self):
        """Gets the threshold_monitor of this Resource.


        :return: The threshold_monitor of this Resource.
        :rtype: List[ThresholdMonitorSingle]
        """
        return self._threshold_monitor

    @threshold_monitor.setter
    def threshold_monitor(self, threshold_monitor):
        """Sets the threshold_monitor of this Resource.


        :param threshold_monitor: The threshold_monitor of this Resource.
        :type threshold_monitor: List[ThresholdMonitorSingle]
        """

        self._threshold_monitor = threshold_monitor

    @property
    def trace_job(self):
        """Gets the trace_job of this Resource.


        :return: The trace_job of this Resource.
        :rtype: List[TraceJobSingle]
        """
        return self._trace_job

    @trace_job.setter
    def trace_job(self, trace_job):
        """Sets the trace_job of this Resource.


        :param trace_job: The trace_job of this Resource.
        :type trace_job: List[TraceJobSingle]
        """

        self._trace_job = trace_job

    @property
    def management_data_collection(self):
        """Gets the management_data_collection of this Resource.


        :return: The management_data_collection of this Resource.
        :rtype: List[ManagementDataCollectionSingle]
        """
        return self._management_data_collection

    @management_data_collection.setter
    def management_data_collection(self, management_data_collection):
        """Sets the management_data_collection of this Resource.


        :param management_data_collection: The management_data_collection of this Resource.
        :type management_data_collection: List[ManagementDataCollectionSingle]
        """

        self._management_data_collection = management_data_collection

    @property
    def ntf_subscription_control(self):
        """Gets the ntf_subscription_control of this Resource.


        :return: The ntf_subscription_control of this Resource.
        :rtype: List[NtfSubscriptionControlSingle]
        """
        return self._ntf_subscription_control

    @ntf_subscription_control.setter
    def ntf_subscription_control(self, ntf_subscription_control):
        """Sets the ntf_subscription_control of this Resource.


        :param ntf_subscription_control: The ntf_subscription_control of this Resource.
        :type ntf_subscription_control: List[NtfSubscriptionControlSingle]
        """

        self._ntf_subscription_control = ntf_subscription_control

    @property
    def alarm_list(self):
        """Gets the alarm_list of this Resource.


        :return: The alarm_list of this Resource.
        :rtype: AlarmListSingle
        """
        return self._alarm_list

    @alarm_list.setter
    def alarm_list(self, alarm_list):
        """Sets the alarm_list of this Resource.


        :param alarm_list: The alarm_list of this Resource.
        :type alarm_list: AlarmListSingle
        """

        self._alarm_list = alarm_list

    @property
    def file_download_job(self):
        """Gets the file_download_job of this Resource.


        :return: The file_download_job of this Resource.
        :rtype: List[FileDownloadJobSingle]
        """
        return self._file_download_job

    @file_download_job.setter
    def file_download_job(self, file_download_job):
        """Sets the file_download_job of this Resource.


        :param file_download_job: The file_download_job of this Resource.
        :type file_download_job: List[FileDownloadJobSingle]
        """

        self._file_download_job = file_download_job

    @property
    def mns_registry(self):
        """Gets the mns_registry of this Resource.


        :return: The mns_registry of this Resource.
        :rtype: MnsRegistrySingle
        """
        return self._mns_registry

    @mns_registry.setter
    def mns_registry(self, mns_registry):
        """Sets the mns_registry of this Resource.


        :param mns_registry: The mns_registry of this Resource.
        :type mns_registry: MnsRegistrySingle
        """

        self._mns_registry = mns_registry

    @property
    def nr_frequency(self):
        """Gets the nr_frequency of this Resource.


        :return: The nr_frequency of this Resource.
        :rtype: List[NRFrequencySingle]
        """
        return self._nr_frequency

    @nr_frequency.setter
    def nr_frequency(self, nr_frequency):
        """Sets the nr_frequency of this Resource.


        :param nr_frequency: The nr_frequency of this Resource.
        :type nr_frequency: List[NRFrequencySingle]
        """
        if nr_frequency is not None and len(nr_frequency) < 1:
            raise ValueError("Invalid value for `nr_frequency`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._nr_frequency = nr_frequency

    @property
    def external_gnb_cu_cp_function(self):
        """Gets the external_gnb_cu_cp_function of this Resource.


        :return: The external_gnb_cu_cp_function of this Resource.
        :rtype: List[ExternalGnbCuCpFunctionSingle]
        """
        return self._external_gnb_cu_cp_function

    @external_gnb_cu_cp_function.setter
    def external_gnb_cu_cp_function(self, external_gnb_cu_cp_function):
        """Sets the external_gnb_cu_cp_function of this Resource.


        :param external_gnb_cu_cp_function: The external_gnb_cu_cp_function of this Resource.
        :type external_gnb_cu_cp_function: List[ExternalGnbCuCpFunctionSingle]
        """

        self._external_gnb_cu_cp_function = external_gnb_cu_cp_function

    @property
    def external_enb_function(self):
        """Gets the external_enb_function of this Resource.


        :return: The external_enb_function of this Resource.
        :rtype: List[ExternalENBFunctionSingle]
        """
        return self._external_enb_function

    @external_enb_function.setter
    def external_enb_function(self, external_enb_function):
        """Sets the external_enb_function of this Resource.


        :param external_enb_function: The external_enb_function of this Resource.
        :type external_enb_function: List[ExternalENBFunctionSingle]
        """

        self._external_enb_function = external_enb_function

    @property
    def e_utran_frequency(self):
        """Gets the e_utran_frequency of this Resource.


        :return: The e_utran_frequency of this Resource.
        :rtype: List[EUtranFrequencySingle]
        """
        return self._e_utran_frequency

    @e_utran_frequency.setter
    def e_utran_frequency(self, e_utran_frequency):
        """Sets the e_utran_frequency of this Resource.


        :param e_utran_frequency: The e_utran_frequency of this Resource.
        :type e_utran_frequency: List[EUtranFrequencySingle]
        """
        if e_utran_frequency is not None and len(e_utran_frequency) < 1:
            raise ValueError("Invalid value for `e_utran_frequency`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._e_utran_frequency = e_utran_frequency

    @property
    def des_management_function(self):
        """Gets the des_management_function of this Resource.


        :return: The des_management_function of this Resource.
        :rtype: DESManagementFunctionSingle
        """
        return self._des_management_function

    @des_management_function.setter
    def des_management_function(self, des_management_function):
        """Sets the des_management_function of this Resource.


        :param des_management_function: The des_management_function of this Resource.
        :type des_management_function: DESManagementFunctionSingle
        """

        self._des_management_function = des_management_function

    @property
    def drach_optimization_function(self):
        """Gets the drach_optimization_function of this Resource.


        :return: The drach_optimization_function of this Resource.
        :rtype: DRACHOptimizationFunctionSingle
        """
        return self._drach_optimization_function

    @drach_optimization_function.setter
    def drach_optimization_function(self, drach_optimization_function):
        """Sets the drach_optimization_function of this Resource.


        :param drach_optimization_function: The drach_optimization_function of this Resource.
        :type drach_optimization_function: DRACHOptimizationFunctionSingle
        """

        self._drach_optimization_function = drach_optimization_function

    @property
    def dmro_function(self):
        """Gets the dmro_function of this Resource.


        :return: The dmro_function of this Resource.
        :rtype: DMROFunctionSingle
        """
        return self._dmro_function

    @dmro_function.setter
    def dmro_function(self, dmro_function):
        """Sets the dmro_function of this Resource.


        :param dmro_function: The dmro_function of this Resource.
        :type dmro_function: DMROFunctionSingle
        """

        self._dmro_function = dmro_function

    @property
    def dlbo_function(self):
        """Gets the dlbo_function of this Resource.


        :return: The dlbo_function of this Resource.
        :rtype: DLBOFunctionSingle
        """
        return self._dlbo_function

    @dlbo_function.setter
    def dlbo_function(self, dlbo_function):
        """Sets the dlbo_function of this Resource.


        :param dlbo_function: The dlbo_function of this Resource.
        :type dlbo_function: DLBOFunctionSingle
        """

        self._dlbo_function = dlbo_function

    @property
    def dpci_configuration_function(self):
        """Gets the dpci_configuration_function of this Resource.


        :return: The dpci_configuration_function of this Resource.
        :rtype: DPCIConfigurationFunctionSingle
        """
        return self._dpci_configuration_function

    @dpci_configuration_function.setter
    def dpci_configuration_function(self, dpci_configuration_function):
        """Sets the dpci_configuration_function of this Resource.


        :param dpci_configuration_function: The dpci_configuration_function of this Resource.
        :type dpci_configuration_function: DPCIConfigurationFunctionSingle
        """

        self._dpci_configuration_function = dpci_configuration_function

    @property
    def cpci_configuration_function(self):
        """Gets the cpci_configuration_function of this Resource.


        :return: The cpci_configuration_function of this Resource.
        :rtype: CPCIConfigurationFunctionSingle
        """
        return self._cpci_configuration_function

    @cpci_configuration_function.setter
    def cpci_configuration_function(self, cpci_configuration_function):
        """Sets the cpci_configuration_function of this Resource.


        :param cpci_configuration_function: The cpci_configuration_function of this Resource.
        :type cpci_configuration_function: CPCIConfigurationFunctionSingle
        """

        self._cpci_configuration_function = cpci_configuration_function

    @property
    def ces_management_function(self):
        """Gets the ces_management_function of this Resource.


        :return: The ces_management_function of this Resource.
        :rtype: CESManagementFunctionSingle
        """
        return self._ces_management_function

    @ces_management_function.setter
    def ces_management_function(self, ces_management_function):
        """Sets the ces_management_function of this Resource.


        :param ces_management_function: The ces_management_function of this Resource.
        :type ces_management_function: CESManagementFunctionSingle
        """

        self._ces_management_function = ces_management_function

    @property
    def configurable5_qi_set(self):
        """Gets the configurable5_qi_set of this Resource.


        :return: The configurable5_qi_set of this Resource.
        :rtype: List[Configurable5QISetSingle]
        """
        return self._configurable5_qi_set

    @configurable5_qi_set.setter
    def configurable5_qi_set(self, configurable5_qi_set):
        """Sets the configurable5_qi_set of this Resource.


        :param configurable5_qi_set: The configurable5_qi_set of this Resource.
        :type configurable5_qi_set: List[Configurable5QISetSingle]
        """

        self._configurable5_qi_set = configurable5_qi_set

    @property
    def rim_rs_global(self):
        """Gets the rim_rs_global of this Resource.


        :return: The rim_rs_global of this Resource.
        :rtype: RimRSGlobalSingle
        """
        return self._rim_rs_global

    @rim_rs_global.setter
    def rim_rs_global(self, rim_rs_global):
        """Sets the rim_rs_global of this Resource.


        :param rim_rs_global: The rim_rs_global of this Resource.
        :type rim_rs_global: RimRSGlobalSingle
        """

        self._rim_rs_global = rim_rs_global

    @property
    def dynamic5_qi_set(self):
        """Gets the dynamic5_qi_set of this Resource.


        :return: The dynamic5_qi_set of this Resource.
        :rtype: List[Dynamic5QISetSingle]
        """
        return self._dynamic5_qi_set

    @dynamic5_qi_set.setter
    def dynamic5_qi_set(self, dynamic5_qi_set):
        """Sets the dynamic5_qi_set of this Resource.


        :param dynamic5_qi_set: The dynamic5_qi_set of this Resource.
        :type dynamic5_qi_set: List[Dynamic5QISetSingle]
        """

        self._dynamic5_qi_set = dynamic5_qi_set

    @property
    def cco_function(self):
        """Gets the cco_function of this Resource.


        :return: The cco_function of this Resource.
        :rtype: CCOFunctionSingle
        """
        return self._cco_function

    @cco_function.setter
    def cco_function(self, cco_function):
        """Sets the cco_function of this Resource.


        :param cco_function: The cco_function of this Resource.
        :type cco_function: CCOFunctionSingle
        """

        self._cco_function = cco_function

    @property
    def gnb_du_function(self):
        """Gets the gnb_du_function of this Resource.


        :return: The gnb_du_function of this Resource.
        :rtype: List[GnbDuFunctionSingle]
        """
        return self._gnb_du_function

    @gnb_du_function.setter
    def gnb_du_function(self, gnb_du_function):
        """Sets the gnb_du_function of this Resource.


        :param gnb_du_function: The gnb_du_function of this Resource.
        :type gnb_du_function: List[GnbDuFunctionSingle]
        """

        self._gnb_du_function = gnb_du_function

    @property
    def gnb_cu_up_function(self):
        """Gets the gnb_cu_up_function of this Resource.


        :return: The gnb_cu_up_function of this Resource.
        :rtype: List[GnbCuUpFunctionSingle]
        """
        return self._gnb_cu_up_function

    @gnb_cu_up_function.setter
    def gnb_cu_up_function(self, gnb_cu_up_function):
        """Sets the gnb_cu_up_function of this Resource.


        :param gnb_cu_up_function: The gnb_cu_up_function of this Resource.
        :type gnb_cu_up_function: List[GnbCuUpFunctionSingle]
        """

        self._gnb_cu_up_function = gnb_cu_up_function

    @property
    def gnb_cu_cp_function(self):
        """Gets the gnb_cu_cp_function of this Resource.


        :return: The gnb_cu_cp_function of this Resource.
        :rtype: List[GnbCuCpFunctionSingle]
        """
        return self._gnb_cu_cp_function

    @gnb_cu_cp_function.setter
    def gnb_cu_cp_function(self, gnb_cu_cp_function):
        """Sets the gnb_cu_cp_function of this Resource.


        :param gnb_cu_cp_function: The gnb_cu_cp_function of this Resource.
        :type gnb_cu_cp_function: List[GnbCuCpFunctionSingle]
        """

        self._gnb_cu_cp_function = gnb_cu_cp_function

    @property
    def managed_nf_service(self):
        """Gets the managed_nf_service of this Resource.


        :return: The managed_nf_service of this Resource.
        :rtype: List[ManagedNFServiceSingle]
        """
        return self._managed_nf_service

    @managed_nf_service.setter
    def managed_nf_service(self, managed_nf_service):
        """Sets the managed_nf_service of this Resource.


        :param managed_nf_service: The managed_nf_service of this Resource.
        :type managed_nf_service: List[ManagedNFServiceSingle]
        """

        self._managed_nf_service = managed_nf_service

    @property
    def rrm_policy_ratio(self):
        """Gets the rrm_policy_ratio of this Resource.


        :return: The rrm_policy_ratio of this Resource.
        :rtype: List[RRMPolicyRatioSingle]
        """
        return self._rrm_policy_ratio

    @rrm_policy_ratio.setter
    def rrm_policy_ratio(self, rrm_policy_ratio):
        """Sets the rrm_policy_ratio of this Resource.


        :param rrm_policy_ratio: The rrm_policy_ratio of this Resource.
        :type rrm_policy_ratio: List[RRMPolicyRatioSingle]
        """

        self._rrm_policy_ratio = rrm_policy_ratio

    @property
    def nr_cell_du(self):
        """Gets the nr_cell_du of this Resource.


        :return: The nr_cell_du of this Resource.
        :rtype: List[NrCellDuSingle]
        """
        return self._nr_cell_du

    @nr_cell_du.setter
    def nr_cell_du(self, nr_cell_du):
        """Sets the nr_cell_du of this Resource.


        :param nr_cell_du: The nr_cell_du of this Resource.
        :type nr_cell_du: List[NrCellDuSingle]
        """

        self._nr_cell_du = nr_cell_du

    @property
    def bwp_multiple(self):
        """Gets the bwp_multiple of this Resource.


        :return: The bwp_multiple of this Resource.
        :rtype: List[BwpSingle]
        """
        return self._bwp_multiple

    @bwp_multiple.setter
    def bwp_multiple(self, bwp_multiple):
        """Sets the bwp_multiple of this Resource.


        :param bwp_multiple: The bwp_multiple of this Resource.
        :type bwp_multiple: List[BwpSingle]
        """

        self._bwp_multiple = bwp_multiple

    @property
    def nr_sector_carrier_multiple(self):
        """Gets the nr_sector_carrier_multiple of this Resource.


        :return: The nr_sector_carrier_multiple of this Resource.
        :rtype: List[NrSectorCarrierSingle]
        """
        return self._nr_sector_carrier_multiple

    @nr_sector_carrier_multiple.setter
    def nr_sector_carrier_multiple(self, nr_sector_carrier_multiple):
        """Sets the nr_sector_carrier_multiple of this Resource.


        :param nr_sector_carrier_multiple: The nr_sector_carrier_multiple of this Resource.
        :type nr_sector_carrier_multiple: List[NrSectorCarrierSingle]
        """

        self._nr_sector_carrier_multiple = nr_sector_carrier_multiple

    @property
    def ep_f1_c(self):
        """Gets the ep_f1_c of this Resource.


        :return: The ep_f1_c of this Resource.
        :rtype: List[EPF1CSingle]
        """
        return self._ep_f1_c

    @ep_f1_c.setter
    def ep_f1_c(self, ep_f1_c):
        """Sets the ep_f1_c of this Resource.


        :param ep_f1_c: The ep_f1_c of this Resource.
        :type ep_f1_c: List[EPF1CSingle]
        """

        self._ep_f1_c = ep_f1_c

    @property
    def ep_f1_u(self):
        """Gets the ep_f1_u of this Resource.


        :return: The ep_f1_u of this Resource.
        :rtype: List[EPF1USingle]
        """
        return self._ep_f1_u

    @ep_f1_u.setter
    def ep_f1_u(self, ep_f1_u):
        """Sets the ep_f1_u of this Resource.


        :param ep_f1_u: The ep_f1_u of this Resource.
        :type ep_f1_u: List[EPF1USingle]
        """

        self._ep_f1_u = ep_f1_u

    @property
    def operator_du(self):
        """Gets the operator_du of this Resource.


        :return: The operator_du of this Resource.
        :rtype: List[OperatorDuSingle]
        """
        return self._operator_du

    @operator_du.setter
    def operator_du(self, operator_du):
        """Sets the operator_du of this Resource.


        :param operator_du: The operator_du of this Resource.
        :type operator_du: List[OperatorDuSingle]
        """

        self._operator_du = operator_du

    @property
    def ep_e1(self):
        """Gets the ep_e1 of this Resource.


        :return: The ep_e1 of this Resource.
        :rtype: List[EPE1Single]
        """
        return self._ep_e1

    @ep_e1.setter
    def ep_e1(self, ep_e1):
        """Sets the ep_e1 of this Resource.


        :param ep_e1: The ep_e1 of this Resource.
        :type ep_e1: List[EPE1Single]
        """

        self._ep_e1 = ep_e1

    @property
    def ep_xn_u(self):
        """Gets the ep_xn_u of this Resource.


        :return: The ep_xn_u of this Resource.
        :rtype: List[EPXnUSingle]
        """
        return self._ep_xn_u

    @ep_xn_u.setter
    def ep_xn_u(self, ep_xn_u):
        """Sets the ep_xn_u of this Resource.


        :param ep_xn_u: The ep_xn_u of this Resource.
        :type ep_xn_u: List[EPXnUSingle]
        """

        self._ep_xn_u = ep_xn_u

    @property
    def ep_ng_u(self):
        """Gets the ep_ng_u of this Resource.


        :return: The ep_ng_u of this Resource.
        :rtype: List[EPNgUSingle]
        """
        return self._ep_ng_u

    @ep_ng_u.setter
    def ep_ng_u(self, ep_ng_u):
        """Sets the ep_ng_u of this Resource.


        :param ep_ng_u: The ep_ng_u of this Resource.
        :type ep_ng_u: List[EPNgUSingle]
        """

        self._ep_ng_u = ep_ng_u

    @property
    def ep_x2_u(self):
        """Gets the ep_x2_u of this Resource.


        :return: The ep_x2_u of this Resource.
        :rtype: List[EPX2USingle]
        """
        return self._ep_x2_u

    @ep_x2_u.setter
    def ep_x2_u(self, ep_x2_u):
        """Sets the ep_x2_u of this Resource.


        :param ep_x2_u: The ep_x2_u of this Resource.
        :type ep_x2_u: List[EPX2USingle]
        """

        self._ep_x2_u = ep_x2_u

    @property
    def ep_s1_u(self):
        """Gets the ep_s1_u of this Resource.


        :return: The ep_s1_u of this Resource.
        :rtype: List[EPS1USingle]
        """
        return self._ep_s1_u

    @ep_s1_u.setter
    def ep_s1_u(self, ep_s1_u):
        """Sets the ep_s1_u of this Resource.


        :param ep_s1_u: The ep_s1_u of this Resource.
        :type ep_s1_u: List[EPS1USingle]
        """

        self._ep_s1_u = ep_s1_u

    @property
    def nr_cell_cu(self):
        """Gets the nr_cell_cu of this Resource.


        :return: The nr_cell_cu of this Resource.
        :rtype: List[NrCellCuSingle]
        """
        return self._nr_cell_cu

    @nr_cell_cu.setter
    def nr_cell_cu(self, nr_cell_cu):
        """Sets the nr_cell_cu of this Resource.


        :param nr_cell_cu: The nr_cell_cu of this Resource.
        :type nr_cell_cu: List[NrCellCuSingle]
        """

        self._nr_cell_cu = nr_cell_cu

    @property
    def ep_xn_c(self):
        """Gets the ep_xn_c of this Resource.


        :return: The ep_xn_c of this Resource.
        :rtype: List[EPXnCSingle]
        """
        return self._ep_xn_c

    @ep_xn_c.setter
    def ep_xn_c(self, ep_xn_c):
        """Sets the ep_xn_c of this Resource.


        :param ep_xn_c: The ep_xn_c of this Resource.
        :type ep_xn_c: List[EPXnCSingle]
        """

        self._ep_xn_c = ep_xn_c

    @property
    def ep_ng_c(self):
        """Gets the ep_ng_c of this Resource.


        :return: The ep_ng_c of this Resource.
        :rtype: List[EPNgCSingle]
        """
        return self._ep_ng_c

    @ep_ng_c.setter
    def ep_ng_c(self, ep_ng_c):
        """Sets the ep_ng_c of this Resource.


        :param ep_ng_c: The ep_ng_c of this Resource.
        :type ep_ng_c: List[EPNgCSingle]
        """

        self._ep_ng_c = ep_ng_c

    @property
    def ep_x2_c(self):
        """Gets the ep_x2_c of this Resource.


        :return: The ep_x2_c of this Resource.
        :rtype: List[EPX2CSingle]
        """
        return self._ep_x2_c

    @ep_x2_c.setter
    def ep_x2_c(self, ep_x2_c):
        """Sets the ep_x2_c of this Resource.


        :param ep_x2_c: The ep_x2_c of this Resource.
        :type ep_x2_c: List[EPX2CSingle]
        """

        self._ep_x2_c = ep_x2_c

    @property
    def danr_management_function(self):
        """Gets the danr_management_function of this Resource.


        :return: The danr_management_function of this Resource.
        :rtype: DANRManagementFunctionSingle
        """
        return self._danr_management_function

    @danr_management_function.setter
    def danr_management_function(self, danr_management_function):
        """Sets the danr_management_function of this Resource.


        :param danr_management_function: The danr_management_function of this Resource.
        :type danr_management_function: DANRManagementFunctionSingle
        """

        self._danr_management_function = danr_management_function

    @property
    def gnb_id(self):
        """Gets the gnb_id of this Resource.


        :return: The gnb_id of this Resource.
        :rtype: str
        """
        return self._gnb_id

    @gnb_id.setter
    def gnb_id(self, gnb_id):
        """Sets the gnb_id of this Resource.


        :param gnb_id: The gnb_id of this Resource.
        :type gnb_id: str
        """

        self._gnb_id = gnb_id

    @property
    def gnb_id_length(self):
        """Gets the gnb_id_length of this Resource.


        :return: The gnb_id_length of this Resource.
        :rtype: int
        """
        return self._gnb_id_length

    @gnb_id_length.setter
    def gnb_id_length(self, gnb_id_length):
        """Sets the gnb_id_length of this Resource.


        :param gnb_id_length: The gnb_id_length of this Resource.
        :type gnb_id_length: int
        """
        if gnb_id_length is not None and gnb_id_length > 32:  # noqa: E501
            raise ValueError("Invalid value for `gnb_id_length`, must be a value less than or equal to `32`")  # noqa: E501
        if gnb_id_length is not None and gnb_id_length < 22:  # noqa: E501
            raise ValueError("Invalid value for `gnb_id_length`, must be a value greater than or equal to `22`")  # noqa: E501

        self._gnb_id_length = gnb_id_length

    @property
    def nr_cell_relation(self):
        """Gets the nr_cell_relation of this Resource.


        :return: The nr_cell_relation of this Resource.
        :rtype: List[NRCellRelationSingle]
        """
        return self._nr_cell_relation

    @nr_cell_relation.setter
    def nr_cell_relation(self, nr_cell_relation):
        """Sets the nr_cell_relation of this Resource.


        :param nr_cell_relation: The nr_cell_relation of this Resource.
        :type nr_cell_relation: List[NRCellRelationSingle]
        """

        self._nr_cell_relation = nr_cell_relation

    @property
    def e_utran_cell_relation(self):
        """Gets the e_utran_cell_relation of this Resource.


        :return: The e_utran_cell_relation of this Resource.
        :rtype: List[EUtranCellRelationSingle]
        """
        return self._e_utran_cell_relation

    @e_utran_cell_relation.setter
    def e_utran_cell_relation(self, e_utran_cell_relation):
        """Sets the e_utran_cell_relation of this Resource.


        :param e_utran_cell_relation: The e_utran_cell_relation of this Resource.
        :type e_utran_cell_relation: List[EUtranCellRelationSingle]
        """

        self._e_utran_cell_relation = e_utran_cell_relation

    @property
    def nr_freq_relation(self):
        """Gets the nr_freq_relation of this Resource.


        :return: The nr_freq_relation of this Resource.
        :rtype: List[NRFreqRelationSingle]
        """
        return self._nr_freq_relation

    @nr_freq_relation.setter
    def nr_freq_relation(self, nr_freq_relation):
        """Sets the nr_freq_relation of this Resource.


        :param nr_freq_relation: The nr_freq_relation of this Resource.
        :type nr_freq_relation: List[NRFreqRelationSingle]
        """

        self._nr_freq_relation = nr_freq_relation

    @property
    def e_utran_freq_relation(self):
        """Gets the e_utran_freq_relation of this Resource.


        :return: The e_utran_freq_relation of this Resource.
        :rtype: List[EUtranFreqRelationSingle]
        """
        return self._e_utran_freq_relation

    @e_utran_freq_relation.setter
    def e_utran_freq_relation(self, e_utran_freq_relation):
        """Sets the e_utran_freq_relation of this Resource.


        :param e_utran_freq_relation: The e_utran_freq_relation of this Resource.
        :type e_utran_freq_relation: List[EUtranFreqRelationSingle]
        """

        self._e_utran_freq_relation = e_utran_freq_relation

    @property
    def nr_operator_cell_du(self):
        """Gets the nr_operator_cell_du of this Resource.


        :return: The nr_operator_cell_du of this Resource.
        :rtype: List[NrOperatorCellDuSingle]
        """
        return self._nr_operator_cell_du

    @nr_operator_cell_du.setter
    def nr_operator_cell_du(self, nr_operator_cell_du):
        """Sets the nr_operator_cell_du of this Resource.


        :param nr_operator_cell_du: The nr_operator_cell_du of this Resource.
        :type nr_operator_cell_du: List[NrOperatorCellDuSingle]
        """

        self._nr_operator_cell_du = nr_operator_cell_du

    @property
    def cell_local_id(self):
        """Gets the cell_local_id of this Resource.


        :return: The cell_local_id of this Resource.
        :rtype: int
        """
        return self._cell_local_id

    @cell_local_id.setter
    def cell_local_id(self, cell_local_id):
        """Sets the cell_local_id of this Resource.


        :param cell_local_id: The cell_local_id of this Resource.
        :type cell_local_id: int
        """

        self._cell_local_id = cell_local_id

    @property
    def administrative_state(self):
        """Gets the administrative_state of this Resource.


        :return: The administrative_state of this Resource.
        :rtype: AdministrativeState
        """
        return self._administrative_state

    @administrative_state.setter
    def administrative_state(self, administrative_state):
        """Sets the administrative_state of this Resource.


        :param administrative_state: The administrative_state of this Resource.
        :type administrative_state: AdministrativeState
        """

        self._administrative_state = administrative_state

    @property
    def plmn_info_list(self):
        """Gets the plmn_info_list of this Resource.


        :return: The plmn_info_list of this Resource.
        :rtype: List[PlmnInfo]
        """
        return self._plmn_info_list

    @plmn_info_list.setter
    def plmn_info_list(self, plmn_info_list):
        """Sets the plmn_info_list of this Resource.


        :param plmn_info_list: The plmn_info_list of this Resource.
        :type plmn_info_list: List[PlmnInfo]
        """

        self._plmn_info_list = plmn_info_list

    @property
    def nr_tac(self):
        """Gets the nr_tac of this Resource.


        :return: The nr_tac of this Resource.
        :rtype: int
        """
        return self._nr_tac

    @nr_tac.setter
    def nr_tac(self, nr_tac):
        """Sets the nr_tac of this Resource.


        :param nr_tac: The nr_tac of this Resource.
        :type nr_tac: int
        """
        if nr_tac is not None and nr_tac > 16777215:  # noqa: E501
            raise ValueError("Invalid value for `nr_tac`, must be a value less than or equal to `16777215`")  # noqa: E501

        self._nr_tac = nr_tac

    @property
    def common_beamforming_function(self):
        """Gets the common_beamforming_function of this Resource.


        :return: The common_beamforming_function of this Resource.
        :rtype: CommonBeamformingFunctionSingle
        """
        return self._common_beamforming_function

    @common_beamforming_function.setter
    def common_beamforming_function(self, common_beamforming_function):
        """Sets the common_beamforming_function of this Resource.


        :param common_beamforming_function: The common_beamforming_function of this Resource.
        :type common_beamforming_function: CommonBeamformingFunctionSingle
        """

        self._common_beamforming_function = common_beamforming_function

    @property
    def beam(self):
        """Gets the beam of this Resource.


        :return: The beam of this Resource.
        :rtype: List[BeamSingle]
        """
        return self._beam

    @beam.setter
    def beam(self, beam):
        """Sets the beam of this Resource.


        :param beam: The beam of this Resource.
        :type beam: List[BeamSingle]
        """

        self._beam = beam

    @property
    def rim_rs_set(self):
        """Gets the rim_rs_set of this Resource.


        :return: The rim_rs_set of this Resource.
        :rtype: List[RimRSSetSingle]
        """
        return self._rim_rs_set

    @rim_rs_set.setter
    def rim_rs_set(self, rim_rs_set):
        """Sets the rim_rs_set of this Resource.


        :param rim_rs_set: The rim_rs_set of this Resource.
        :type rim_rs_set: List[RimRSSetSingle]
        """

        self._rim_rs_set = rim_rs_set

    @property
    def external_nr_cell_cu(self):
        """Gets the external_nr_cell_cu of this Resource.


        :return: The external_nr_cell_cu of this Resource.
        :rtype: List[ExternalNrCellCuSingle]
        """
        return self._external_nr_cell_cu

    @external_nr_cell_cu.setter
    def external_nr_cell_cu(self, external_nr_cell_cu):
        """Sets the external_nr_cell_cu of this Resource.


        :param external_nr_cell_cu: The external_nr_cell_cu of this Resource.
        :type external_nr_cell_cu: List[ExternalNrCellCuSingle]
        """

        self._external_nr_cell_cu = external_nr_cell_cu

    @property
    def external_eu_tran_cell(self):
        """Gets the external_eu_tran_cell of this Resource.


        :return: The external_eu_tran_cell of this Resource.
        :rtype: List[ExternalEUTranCellSingle]
        """
        return self._external_eu_tran_cell

    @external_eu_tran_cell.setter
    def external_eu_tran_cell(self, external_eu_tran_cell):
        """Sets the external_eu_tran_cell of this Resource.


        :param external_eu_tran_cell: The external_eu_tran_cell of this Resource.
        :type external_eu_tran_cell: List[ExternalEUTranCellSingle]
        """

        self._external_eu_tran_cell = external_eu_tran_cell

    @property
    def external_amf_function(self):
        """Gets the external_amf_function of this Resource.


        :return: The external_amf_function of this Resource.
        :rtype: List[ExternalAmfFunctionSingle]
        """
        return self._external_amf_function

    @external_amf_function.setter
    def external_amf_function(self, external_amf_function):
        """Sets the external_amf_function of this Resource.


        :param external_amf_function: The external_amf_function of this Resource.
        :type external_amf_function: List[ExternalAmfFunctionSingle]
        """

        self._external_amf_function = external_amf_function

    @property
    def external_nrf_function(self):
        """Gets the external_nrf_function of this Resource.


        :return: The external_nrf_function of this Resource.
        :rtype: List[ExternalNrfFunctionSingle]
        """
        return self._external_nrf_function

    @external_nrf_function.setter
    def external_nrf_function(self, external_nrf_function):
        """Sets the external_nrf_function of this Resource.


        :param external_nrf_function: The external_nrf_function of this Resource.
        :type external_nrf_function: List[ExternalNrfFunctionSingle]
        """

        self._external_nrf_function = external_nrf_function

    @property
    def external_nssf_function(self):
        """Gets the external_nssf_function of this Resource.


        :return: The external_nssf_function of this Resource.
        :rtype: List[ExternalNssfFunctionSingle]
        """
        return self._external_nssf_function

    @external_nssf_function.setter
    def external_nssf_function(self, external_nssf_function):
        """Sets the external_nssf_function of this Resource.


        :param external_nssf_function: The external_nssf_function of this Resource.
        :type external_nssf_function: List[ExternalNssfFunctionSingle]
        """

        self._external_nssf_function = external_nssf_function

    @property
    def amf_set(self):
        """Gets the amf_set of this Resource.


        :return: The amf_set of this Resource.
        :rtype: List[AmfSetSingle]
        """
        return self._amf_set

    @amf_set.setter
    def amf_set(self, amf_set):
        """Sets the amf_set of this Resource.


        :param amf_set: The amf_set of this Resource.
        :type amf_set: List[AmfSetSingle]
        """

        self._amf_set = amf_set

    @property
    def amf_region(self):
        """Gets the amf_region of this Resource.


        :return: The amf_region of this Resource.
        :rtype: List[AmfRegionSingle]
        """
        return self._amf_region

    @amf_region.setter
    def amf_region(self, amf_region):
        """Sets the amf_region of this Resource.


        :param amf_region: The amf_region of this Resource.
        :type amf_region: List[AmfRegionSingle]
        """

        self._amf_region = amf_region

    @property
    def ecm_connection_info(self):
        """Gets the ecm_connection_info of this Resource.


        :return: The ecm_connection_info of this Resource.
        :rtype: List[EcmConnectionInfoSingle]
        """
        return self._ecm_connection_info

    @ecm_connection_info.setter
    def ecm_connection_info(self, ecm_connection_info):
        """Sets the ecm_connection_info of this Resource.


        :param ecm_connection_info: The ecm_connection_info of this Resource.
        :type ecm_connection_info: List[EcmConnectionInfoSingle]
        """

        self._ecm_connection_info = ecm_connection_info

    @property
    def amf_function(self):
        """Gets the amf_function of this Resource.


        :return: The amf_function of this Resource.
        :rtype: List[AmfFunctionSingle]
        """
        return self._amf_function

    @amf_function.setter
    def amf_function(self, amf_function):
        """Sets the amf_function of this Resource.


        :param amf_function: The amf_function of this Resource.
        :type amf_function: List[AmfFunctionSingle]
        """

        self._amf_function = amf_function

    @property
    def smf_function(self):
        """Gets the smf_function of this Resource.


        :return: The smf_function of this Resource.
        :rtype: List[SmfFunctionSingle]
        """
        return self._smf_function

    @smf_function.setter
    def smf_function(self, smf_function):
        """Sets the smf_function of this Resource.


        :param smf_function: The smf_function of this Resource.
        :type smf_function: List[SmfFunctionSingle]
        """

        self._smf_function = smf_function

    @property
    def upf_function(self):
        """Gets the upf_function of this Resource.


        :return: The upf_function of this Resource.
        :rtype: List[UpfFunctionSingle]
        """
        return self._upf_function

    @upf_function.setter
    def upf_function(self, upf_function):
        """Sets the upf_function of this Resource.


        :param upf_function: The upf_function of this Resource.
        :type upf_function: List[UpfFunctionSingle]
        """

        self._upf_function = upf_function

    @property
    def n3iwf_function(self):
        """Gets the n3iwf_function of this Resource.


        :return: The n3iwf_function of this Resource.
        :rtype: List[N3iwfFunctionSingle]
        """
        return self._n3iwf_function

    @n3iwf_function.setter
    def n3iwf_function(self, n3iwf_function):
        """Sets the n3iwf_function of this Resource.


        :param n3iwf_function: The n3iwf_function of this Resource.
        :type n3iwf_function: List[N3iwfFunctionSingle]
        """

        self._n3iwf_function = n3iwf_function

    @property
    def pcf_function(self):
        """Gets the pcf_function of this Resource.


        :return: The pcf_function of this Resource.
        :rtype: List[PcfFunctionSingle]
        """
        return self._pcf_function

    @pcf_function.setter
    def pcf_function(self, pcf_function):
        """Sets the pcf_function of this Resource.


        :param pcf_function: The pcf_function of this Resource.
        :type pcf_function: List[PcfFunctionSingle]
        """

        self._pcf_function = pcf_function

    @property
    def ausf_function(self):
        """Gets the ausf_function of this Resource.


        :return: The ausf_function of this Resource.
        :rtype: List[AusfFunctionSingle]
        """
        return self._ausf_function

    @ausf_function.setter
    def ausf_function(self, ausf_function):
        """Sets the ausf_function of this Resource.


        :param ausf_function: The ausf_function of this Resource.
        :type ausf_function: List[AusfFunctionSingle]
        """

        self._ausf_function = ausf_function

    @property
    def udm_function(self):
        """Gets the udm_function of this Resource.


        :return: The udm_function of this Resource.
        :rtype: List[UdmFunctionSingle]
        """
        return self._udm_function

    @udm_function.setter
    def udm_function(self, udm_function):
        """Sets the udm_function of this Resource.


        :param udm_function: The udm_function of this Resource.
        :type udm_function: List[UdmFunctionSingle]
        """

        self._udm_function = udm_function

    @property
    def udr_function(self):
        """Gets the udr_function of this Resource.


        :return: The udr_function of this Resource.
        :rtype: List[UdrFunctionSingle]
        """
        return self._udr_function

    @udr_function.setter
    def udr_function(self, udr_function):
        """Sets the udr_function of this Resource.


        :param udr_function: The udr_function of this Resource.
        :type udr_function: List[UdrFunctionSingle]
        """

        self._udr_function = udr_function

    @property
    def udsf_function(self):
        """Gets the udsf_function of this Resource.


        :return: The udsf_function of this Resource.
        :rtype: List[UdsfFunctionSingle]
        """
        return self._udsf_function

    @udsf_function.setter
    def udsf_function(self, udsf_function):
        """Sets the udsf_function of this Resource.


        :param udsf_function: The udsf_function of this Resource.
        :type udsf_function: List[UdsfFunctionSingle]
        """

        self._udsf_function = udsf_function

    @property
    def nrf_function(self):
        """Gets the nrf_function of this Resource.


        :return: The nrf_function of this Resource.
        :rtype: List[NrfFunctionSingle]
        """
        return self._nrf_function

    @nrf_function.setter
    def nrf_function(self, nrf_function):
        """Sets the nrf_function of this Resource.


        :param nrf_function: The nrf_function of this Resource.
        :type nrf_function: List[NrfFunctionSingle]
        """

        self._nrf_function = nrf_function

    @property
    def nssf_function(self):
        """Gets the nssf_function of this Resource.


        :return: The nssf_function of this Resource.
        :rtype: List[NssfFunctionSingle]
        """
        return self._nssf_function

    @nssf_function.setter
    def nssf_function(self, nssf_function):
        """Sets the nssf_function of this Resource.


        :param nssf_function: The nssf_function of this Resource.
        :type nssf_function: List[NssfFunctionSingle]
        """

        self._nssf_function = nssf_function

    @property
    def smsf_function(self):
        """Gets the smsf_function of this Resource.


        :return: The smsf_function of this Resource.
        :rtype: List[SmsfFunctionSingle]
        """
        return self._smsf_function

    @smsf_function.setter
    def smsf_function(self, smsf_function):
        """Sets the smsf_function of this Resource.


        :param smsf_function: The smsf_function of this Resource.
        :type smsf_function: List[SmsfFunctionSingle]
        """

        self._smsf_function = smsf_function

    @property
    def lmf_function(self):
        """Gets the lmf_function of this Resource.


        :return: The lmf_function of this Resource.
        :rtype: List[LmfFunctionSingle]
        """
        return self._lmf_function

    @lmf_function.setter
    def lmf_function(self, lmf_function):
        """Sets the lmf_function of this Resource.


        :param lmf_function: The lmf_function of this Resource.
        :type lmf_function: List[LmfFunctionSingle]
        """

        self._lmf_function = lmf_function

    @property
    def ngeir_function(self):
        """Gets the ngeir_function of this Resource.


        :return: The ngeir_function of this Resource.
        :rtype: List[NgeirFunctionSingle]
        """
        return self._ngeir_function

    @ngeir_function.setter
    def ngeir_function(self, ngeir_function):
        """Sets the ngeir_function of this Resource.


        :param ngeir_function: The ngeir_function of this Resource.
        :type ngeir_function: List[NgeirFunctionSingle]
        """

        self._ngeir_function = ngeir_function

    @property
    def sepp_function(self):
        """Gets the sepp_function of this Resource.


        :return: The sepp_function of this Resource.
        :rtype: List[SeppFunctionSingle]
        """
        return self._sepp_function

    @sepp_function.setter
    def sepp_function(self, sepp_function):
        """Sets the sepp_function of this Resource.


        :param sepp_function: The sepp_function of this Resource.
        :type sepp_function: List[SeppFunctionSingle]
        """

        self._sepp_function = sepp_function

    @property
    def nwdaf_function(self):
        """Gets the nwdaf_function of this Resource.


        :return: The nwdaf_function of this Resource.
        :rtype: List[NwdafFunctionSingle]
        """
        return self._nwdaf_function

    @nwdaf_function.setter
    def nwdaf_function(self, nwdaf_function):
        """Sets the nwdaf_function of this Resource.


        :param nwdaf_function: The nwdaf_function of this Resource.
        :type nwdaf_function: List[NwdafFunctionSingle]
        """

        self._nwdaf_function = nwdaf_function

    @property
    def scp_function(self):
        """Gets the scp_function of this Resource.


        :return: The scp_function of this Resource.
        :rtype: List[ScpFunctionSingle]
        """
        return self._scp_function

    @scp_function.setter
    def scp_function(self, scp_function):
        """Sets the scp_function of this Resource.


        :param scp_function: The scp_function of this Resource.
        :type scp_function: List[ScpFunctionSingle]
        """

        self._scp_function = scp_function

    @property
    def nef_function(self):
        """Gets the nef_function of this Resource.


        :return: The nef_function of this Resource.
        :rtype: List[NefFunctionSingle]
        """
        return self._nef_function

    @nef_function.setter
    def nef_function(self, nef_function):
        """Sets the nef_function of this Resource.


        :param nef_function: The nef_function of this Resource.
        :type nef_function: List[NefFunctionSingle]
        """

        self._nef_function = nef_function

    @property
    def easdf_function(self):
        """Gets the easdf_function of this Resource.


        :return: The easdf_function of this Resource.
        :rtype: List[EASDFFunctionSingle]
        """
        return self._easdf_function

    @easdf_function.setter
    def easdf_function(self, easdf_function):
        """Sets the easdf_function of this Resource.


        :param easdf_function: The easdf_function of this Resource.
        :type easdf_function: List[EASDFFunctionSingle]
        """

        self._easdf_function = easdf_function

    @property
    def ep_n2(self):
        """Gets the ep_n2 of this Resource.


        :return: The ep_n2 of this Resource.
        :rtype: List[EPN2Single]
        """
        return self._ep_n2

    @ep_n2.setter
    def ep_n2(self, ep_n2):
        """Sets the ep_n2 of this Resource.


        :param ep_n2: The ep_n2 of this Resource.
        :type ep_n2: List[EPN2Single]
        """

        self._ep_n2 = ep_n2

    @property
    def ep_n8(self):
        """Gets the ep_n8 of this Resource.


        :return: The ep_n8 of this Resource.
        :rtype: List[EPN8Single]
        """
        return self._ep_n8

    @ep_n8.setter
    def ep_n8(self, ep_n8):
        """Sets the ep_n8 of this Resource.


        :param ep_n8: The ep_n8 of this Resource.
        :type ep_n8: List[EPN8Single]
        """

        self._ep_n8 = ep_n8

    @property
    def ep_n11(self):
        """Gets the ep_n11 of this Resource.


        :return: The ep_n11 of this Resource.
        :rtype: List[EPN11Single]
        """
        return self._ep_n11

    @ep_n11.setter
    def ep_n11(self, ep_n11):
        """Sets the ep_n11 of this Resource.


        :param ep_n11: The ep_n11 of this Resource.
        :type ep_n11: List[EPN11Single]
        """

        self._ep_n11 = ep_n11

    @property
    def ep_n12(self):
        """Gets the ep_n12 of this Resource.


        :return: The ep_n12 of this Resource.
        :rtype: List[EPN12Single]
        """
        return self._ep_n12

    @ep_n12.setter
    def ep_n12(self, ep_n12):
        """Sets the ep_n12 of this Resource.


        :param ep_n12: The ep_n12 of this Resource.
        :type ep_n12: List[EPN12Single]
        """

        self._ep_n12 = ep_n12

    @property
    def ep_n14(self):
        """Gets the ep_n14 of this Resource.


        :return: The ep_n14 of this Resource.
        :rtype: List[EPN14Single]
        """
        return self._ep_n14

    @ep_n14.setter
    def ep_n14(self, ep_n14):
        """Sets the ep_n14 of this Resource.


        :param ep_n14: The ep_n14 of this Resource.
        :type ep_n14: List[EPN14Single]
        """

        self._ep_n14 = ep_n14

    @property
    def ep_n15(self):
        """Gets the ep_n15 of this Resource.


        :return: The ep_n15 of this Resource.
        :rtype: List[EPN15Single]
        """
        return self._ep_n15

    @ep_n15.setter
    def ep_n15(self, ep_n15):
        """Sets the ep_n15 of this Resource.


        :param ep_n15: The ep_n15 of this Resource.
        :type ep_n15: List[EPN15Single]
        """

        self._ep_n15 = ep_n15

    @property
    def ep_n17(self):
        """Gets the ep_n17 of this Resource.


        :return: The ep_n17 of this Resource.
        :rtype: List[EPN17Single]
        """
        return self._ep_n17

    @ep_n17.setter
    def ep_n17(self, ep_n17):
        """Sets the ep_n17 of this Resource.


        :param ep_n17: The ep_n17 of this Resource.
        :type ep_n17: List[EPN17Single]
        """

        self._ep_n17 = ep_n17

    @property
    def ep_n20(self):
        """Gets the ep_n20 of this Resource.


        :return: The ep_n20 of this Resource.
        :rtype: List[EPN20Single]
        """
        return self._ep_n20

    @ep_n20.setter
    def ep_n20(self, ep_n20):
        """Sets the ep_n20 of this Resource.


        :param ep_n20: The ep_n20 of this Resource.
        :type ep_n20: List[EPN20Single]
        """

        self._ep_n20 = ep_n20

    @property
    def ep_n22(self):
        """Gets the ep_n22 of this Resource.


        :return: The ep_n22 of this Resource.
        :rtype: List[EPN22Single]
        """
        return self._ep_n22

    @ep_n22.setter
    def ep_n22(self, ep_n22):
        """Sets the ep_n22 of this Resource.


        :param ep_n22: The ep_n22 of this Resource.
        :type ep_n22: List[EPN22Single]
        """

        self._ep_n22 = ep_n22

    @property
    def ep_n26(self):
        """Gets the ep_n26 of this Resource.


        :return: The ep_n26 of this Resource.
        :rtype: List[EPN26Single]
        """
        return self._ep_n26

    @ep_n26.setter
    def ep_n26(self, ep_n26):
        """Sets the ep_n26 of this Resource.


        :param ep_n26: The ep_n26 of this Resource.
        :type ep_n26: List[EPN26Single]
        """

        self._ep_n26 = ep_n26

    @property
    def ep_nls(self):
        """Gets the ep_nls of this Resource.


        :return: The ep_nls of this Resource.
        :rtype: List[EPNLSSingle]
        """
        return self._ep_nls

    @ep_nls.setter
    def ep_nls(self, ep_nls):
        """Sets the ep_nls of this Resource.


        :param ep_nls: The ep_nls of this Resource.
        :type ep_nls: List[EPNLSSingle]
        """

        self._ep_nls = ep_nls

    @property
    def ep_nlg(self):
        """Gets the ep_nlg of this Resource.


        :return: The ep_nlg of this Resource.
        :rtype: List[EPNLGSingle]
        """
        return self._ep_nlg

    @ep_nlg.setter
    def ep_nlg(self, ep_nlg):
        """Sets the ep_nlg of this Resource.


        :param ep_nlg: The ep_nlg of this Resource.
        :type ep_nlg: List[EPNLGSingle]
        """

        self._ep_nlg = ep_nlg

    @property
    def ep_n4(self):
        """Gets the ep_n4 of this Resource.


        :return: The ep_n4 of this Resource.
        :rtype: List[EPN4Single]
        """
        return self._ep_n4

    @ep_n4.setter
    def ep_n4(self, ep_n4):
        """Sets the ep_n4 of this Resource.


        :param ep_n4: The ep_n4 of this Resource.
        :type ep_n4: List[EPN4Single]
        """

        self._ep_n4 = ep_n4

    @property
    def ep_n7(self):
        """Gets the ep_n7 of this Resource.


        :return: The ep_n7 of this Resource.
        :rtype: List[EPN7Single]
        """
        return self._ep_n7

    @ep_n7.setter
    def ep_n7(self, ep_n7):
        """Sets the ep_n7 of this Resource.


        :param ep_n7: The ep_n7 of this Resource.
        :type ep_n7: List[EPN7Single]
        """

        self._ep_n7 = ep_n7

    @property
    def ep_n10(self):
        """Gets the ep_n10 of this Resource.


        :return: The ep_n10 of this Resource.
        :rtype: List[EPN10Single]
        """
        return self._ep_n10

    @ep_n10.setter
    def ep_n10(self, ep_n10):
        """Sets the ep_n10 of this Resource.


        :param ep_n10: The ep_n10 of this Resource.
        :type ep_n10: List[EPN10Single]
        """

        self._ep_n10 = ep_n10

    @property
    def ep_n16(self):
        """Gets the ep_n16 of this Resource.


        :return: The ep_n16 of this Resource.
        :rtype: List[EPN16Single]
        """
        return self._ep_n16

    @ep_n16.setter
    def ep_n16(self, ep_n16):
        """Sets the ep_n16 of this Resource.


        :param ep_n16: The ep_n16 of this Resource.
        :type ep_n16: List[EPN16Single]
        """

        self._ep_n16 = ep_n16

    @property
    def ep_s5_c(self):
        """Gets the ep_s5_c of this Resource.


        :return: The ep_s5_c of this Resource.
        :rtype: List[EPS5CSingle]
        """
        return self._ep_s5_c

    @ep_s5_c.setter
    def ep_s5_c(self, ep_s5_c):
        """Sets the ep_s5_c of this Resource.


        :param ep_s5_c: The ep_s5_c of this Resource.
        :type ep_s5_c: List[EPS5CSingle]
        """

        self._ep_s5_c = ep_s5_c

    @property
    def five_qi_dscp_mapping_set(self):
        """Gets the five_qi_dscp_mapping_set of this Resource.


        :return: The five_qi_dscp_mapping_set of this Resource.
        :rtype: FiveQiDscpMappingSetSingle
        """
        return self._five_qi_dscp_mapping_set

    @five_qi_dscp_mapping_set.setter
    def five_qi_dscp_mapping_set(self, five_qi_dscp_mapping_set):
        """Sets the five_qi_dscp_mapping_set of this Resource.


        :param five_qi_dscp_mapping_set: The five_qi_dscp_mapping_set of this Resource.
        :type five_qi_dscp_mapping_set: FiveQiDscpMappingSetSingle
        """

        self._five_qi_dscp_mapping_set = five_qi_dscp_mapping_set

    @property
    def gtp_u_path_qo_s_monitoring_control(self):
        """Gets the gtp_u_path_qo_s_monitoring_control of this Resource.


        :return: The gtp_u_path_qo_s_monitoring_control of this Resource.
        :rtype: GtpUPathQoSMonitoringControlSingle
        """
        return self._gtp_u_path_qo_s_monitoring_control

    @gtp_u_path_qo_s_monitoring_control.setter
    def gtp_u_path_qo_s_monitoring_control(self, gtp_u_path_qo_s_monitoring_control):
        """Sets the gtp_u_path_qo_s_monitoring_control of this Resource.


        :param gtp_u_path_qo_s_monitoring_control: The gtp_u_path_qo_s_monitoring_control of this Resource.
        :type gtp_u_path_qo_s_monitoring_control: GtpUPathQoSMonitoringControlSingle
        """

        self._gtp_u_path_qo_s_monitoring_control = gtp_u_path_qo_s_monitoring_control

    @property
    def qfqo_s_monitoring_control(self):
        """Gets the qfqo_s_monitoring_control of this Resource.


        :return: The qfqo_s_monitoring_control of this Resource.
        :rtype: QFQoSMonitoringControlSingle
        """
        return self._qfqo_s_monitoring_control

    @qfqo_s_monitoring_control.setter
    def qfqo_s_monitoring_control(self, qfqo_s_monitoring_control):
        """Sets the qfqo_s_monitoring_control of this Resource.


        :param qfqo_s_monitoring_control: The qfqo_s_monitoring_control of this Resource.
        :type qfqo_s_monitoring_control: QFQoSMonitoringControlSingle
        """

        self._qfqo_s_monitoring_control = qfqo_s_monitoring_control

    @property
    def predefined_pcc_rule_set(self):
        """Gets the predefined_pcc_rule_set of this Resource.


        :return: The predefined_pcc_rule_set of this Resource.
        :rtype: PredefinedPccRuleSetSingle
        """
        return self._predefined_pcc_rule_set

    @predefined_pcc_rule_set.setter
    def predefined_pcc_rule_set(self, predefined_pcc_rule_set):
        """Sets the predefined_pcc_rule_set of this Resource.


        :param predefined_pcc_rule_set: The predefined_pcc_rule_set of this Resource.
        :type predefined_pcc_rule_set: PredefinedPccRuleSetSingle
        """

        self._predefined_pcc_rule_set = predefined_pcc_rule_set

    @property
    def ep_n3(self):
        """Gets the ep_n3 of this Resource.


        :return: The ep_n3 of this Resource.
        :rtype: List[EPN3Single]
        """
        return self._ep_n3

    @ep_n3.setter
    def ep_n3(self, ep_n3):
        """Sets the ep_n3 of this Resource.


        :param ep_n3: The ep_n3 of this Resource.
        :type ep_n3: List[EPN3Single]
        """

        self._ep_n3 = ep_n3

    @property
    def ep_n6(self):
        """Gets the ep_n6 of this Resource.


        :return: The ep_n6 of this Resource.
        :rtype: List[EPN6Single]
        """
        return self._ep_n6

    @ep_n6.setter
    def ep_n6(self, ep_n6):
        """Sets the ep_n6 of this Resource.


        :param ep_n6: The ep_n6 of this Resource.
        :type ep_n6: List[EPN6Single]
        """

        self._ep_n6 = ep_n6

    @property
    def ep_n9(self):
        """Gets the ep_n9 of this Resource.


        :return: The ep_n9 of this Resource.
        :rtype: List[EPN9Single]
        """
        return self._ep_n9

    @ep_n9.setter
    def ep_n9(self, ep_n9):
        """Sets the ep_n9 of this Resource.


        :param ep_n9: The ep_n9 of this Resource.
        :type ep_n9: List[EPN9Single]
        """

        self._ep_n9 = ep_n9

    @property
    def ep_s5_u(self):
        """Gets the ep_s5_u of this Resource.


        :return: The ep_s5_u of this Resource.
        :rtype: List[EPS5USingle]
        """
        return self._ep_s5_u

    @ep_s5_u.setter
    def ep_s5_u(self, ep_s5_u):
        """Sets the ep_s5_u of this Resource.


        :param ep_s5_u: The ep_s5_u of this Resource.
        :type ep_s5_u: List[EPS5USingle]
        """

        self._ep_s5_u = ep_s5_u

    @property
    def ep_n5(self):
        """Gets the ep_n5 of this Resource.


        :return: The ep_n5 of this Resource.
        :rtype: List[EPN5Single]
        """
        return self._ep_n5

    @ep_n5.setter
    def ep_n5(self, ep_n5):
        """Sets the ep_n5 of this Resource.


        :param ep_n5: The ep_n5 of this Resource.
        :type ep_n5: List[EPN5Single]
        """

        self._ep_n5 = ep_n5

    @property
    def ep_rx(self):
        """Gets the ep_rx of this Resource.


        :return: The ep_rx of this Resource.
        :rtype: List[EPRxSingle]
        """
        return self._ep_rx

    @ep_rx.setter
    def ep_rx(self, ep_rx):
        """Sets the ep_rx of this Resource.


        :param ep_rx: The ep_rx of this Resource.
        :type ep_rx: List[EPRxSingle]
        """

        self._ep_rx = ep_rx

    @property
    def ep_n13(self):
        """Gets the ep_n13 of this Resource.


        :return: The ep_n13 of this Resource.
        :rtype: List[EPN13Single]
        """
        return self._ep_n13

    @ep_n13.setter
    def ep_n13(self, ep_n13):
        """Sets the ep_n13 of this Resource.


        :param ep_n13: The ep_n13 of this Resource.
        :type ep_n13: List[EPN13Single]
        """

        self._ep_n13 = ep_n13

    @property
    def ep_n27(self):
        """Gets the ep_n27 of this Resource.


        :return: The ep_n27 of this Resource.
        :rtype: List[EPN27Single]
        """
        return self._ep_n27

    @ep_n27.setter
    def ep_n27(self, ep_n27):
        """Sets the ep_n27 of this Resource.


        :param ep_n27: The ep_n27 of this Resource.
        :type ep_n27: List[EPN27Single]
        """

        self._ep_n27 = ep_n27

    @property
    def ep_n31(self):
        """Gets the ep_n31 of this Resource.


        :return: The ep_n31 of this Resource.
        :rtype: List[EPN31Single]
        """
        return self._ep_n31

    @ep_n31.setter
    def ep_n31(self, ep_n31):
        """Sets the ep_n31 of this Resource.


        :param ep_n31: The ep_n31 of this Resource.
        :type ep_n31: List[EPN31Single]
        """

        self._ep_n31 = ep_n31

    @property
    def ep_n21(self):
        """Gets the ep_n21 of this Resource.


        :return: The ep_n21 of this Resource.
        :rtype: List[EPN21Single]
        """
        return self._ep_n21

    @ep_n21.setter
    def ep_n21(self, ep_n21):
        """Sets the ep_n21 of this Resource.


        :param ep_n21: The ep_n21 of this Resource.
        :type ep_n21: List[EPN21Single]
        """

        self._ep_n21 = ep_n21

    @property
    def ep_map_smsc(self):
        """Gets the ep_map_smsc of this Resource.


        :return: The ep_map_smsc of this Resource.
        :rtype: List[EPMAPSMSCSingle]
        """
        return self._ep_map_smsc

    @ep_map_smsc.setter
    def ep_map_smsc(self, ep_map_smsc):
        """Sets the ep_map_smsc of this Resource.


        :param ep_map_smsc: The ep_map_smsc of this Resource.
        :type ep_map_smsc: List[EPMAPSMSCSingle]
        """

        self._ep_map_smsc = ep_map_smsc

    @property
    def ep_n32(self):
        """Gets the ep_n32 of this Resource.


        :return: The ep_n32 of this Resource.
        :rtype: List[EPN32Single]
        """
        return self._ep_n32

    @ep_n32.setter
    def ep_n32(self, ep_n32):
        """Sets the ep_n32 of this Resource.


        :param ep_n32: The ep_n32 of this Resource.
        :type ep_n32: List[EPN32Single]
        """

        self._ep_n32 = ep_n32

    @property
    def ep_n33(self):
        """Gets the ep_n33 of this Resource.


        :return: The ep_n33 of this Resource.
        :rtype: List[EPN33Single]
        """
        return self._ep_n33

    @ep_n33.setter
    def ep_n33(self, ep_n33):
        """Sets the ep_n33 of this Resource.


        :param ep_n33: The ep_n33 of this Resource.
        :type ep_n33: List[EPN33Single]
        """

        self._ep_n33 = ep_n33

    @property
    def ep_n60(self):
        """Gets the ep_n60 of this Resource.


        :return: The ep_n60 of this Resource.
        :rtype: List[EPN60Single]
        """
        return self._ep_n60

    @ep_n60.setter
    def ep_n60(self, ep_n60):
        """Sets the ep_n60 of this Resource.


        :param ep_n60: The ep_n60 of this Resource.
        :type ep_n60: List[EPN60Single]
        """

        self._ep_n60 = ep_n60

    @property
    def ep_npc4(self):
        """Gets the ep_npc4 of this Resource.


        :return: The ep_npc4 of this Resource.
        :rtype: List[EPNpc4Single]
        """
        return self._ep_npc4

    @ep_npc4.setter
    def ep_npc4(self, ep_npc4):
        """Sets the ep_npc4 of this Resource.


        :param ep_npc4: The ep_npc4 of this Resource.
        :type ep_npc4: List[EPNpc4Single]
        """

        self._ep_npc4 = ep_npc4

    @property
    def ep_npc6(self):
        """Gets the ep_npc6 of this Resource.


        :return: The ep_npc6 of this Resource.
        :rtype: List[EPNpc6Single]
        """
        return self._ep_npc6

    @ep_npc6.setter
    def ep_npc6(self, ep_npc6):
        """Sets the ep_npc6 of this Resource.


        :param ep_npc6: The ep_npc6 of this Resource.
        :type ep_npc6: List[EPNpc6Single]
        """

        self._ep_npc6 = ep_npc6

    @property
    def ep_npc7(self):
        """Gets the ep_npc7 of this Resource.


        :return: The ep_npc7 of this Resource.
        :rtype: List[EPNpc7Single]
        """
        return self._ep_npc7

    @ep_npc7.setter
    def ep_npc7(self, ep_npc7):
        """Sets the ep_npc7 of this Resource.


        :param ep_npc7: The ep_npc7 of this Resource.
        :type ep_npc7: List[EPNpc7Single]
        """

        self._ep_npc7 = ep_npc7

    @property
    def ep_npc8(self):
        """Gets the ep_npc8 of this Resource.


        :return: The ep_npc8 of this Resource.
        :rtype: List[EPNpc8Single]
        """
        return self._ep_npc8

    @ep_npc8.setter
    def ep_npc8(self, ep_npc8):
        """Sets the ep_npc8 of this Resource.


        :param ep_npc8: The ep_npc8 of this Resource.
        :type ep_npc8: List[EPNpc8Single]
        """

        self._ep_npc8 = ep_npc8

    @property
    def ep_n88(self):
        """Gets the ep_n88 of this Resource.


        :return: The ep_n88 of this Resource.
        :rtype: List[EPN88Single]
        """
        return self._ep_n88

    @ep_n88.setter
    def ep_n88(self, ep_n88):
        """Sets the ep_n88 of this Resource.


        :param ep_n88: The ep_n88 of this Resource.
        :type ep_n88: List[EPN88Single]
        """

        self._ep_n88 = ep_n88

    @property
    def network_slice(self):
        """Gets the network_slice of this Resource.


        :return: The network_slice of this Resource.
        :rtype: List[NetworkSliceSingle]
        """
        return self._network_slice

    @network_slice.setter
    def network_slice(self, network_slice):
        """Sets the network_slice of this Resource.


        :param network_slice: The network_slice of this Resource.
        :type network_slice: List[NetworkSliceSingle]
        """

        self._network_slice = network_slice

    @property
    def network_slice_subnet(self):
        """Gets the network_slice_subnet of this Resource.


        :return: The network_slice_subnet of this Resource.
        :rtype: List[NetworkSliceSubnetSingle]
        """
        return self._network_slice_subnet

    @network_slice_subnet.setter
    def network_slice_subnet(self, network_slice_subnet):
        """Sets the network_slice_subnet of this Resource.


        :param network_slice_subnet: The network_slice_subnet of this Resource.
        :type network_slice_subnet: List[NetworkSliceSubnetSingle]
        """

        self._network_slice_subnet = network_slice_subnet

    @property
    def ep_transport(self):
        """Gets the ep_transport of this Resource.


        :return: The ep_transport of this Resource.
        :rtype: List[EPTransportSingle]
        """
        return self._ep_transport

    @ep_transport.setter
    def ep_transport(self, ep_transport):
        """Sets the ep_transport of this Resource.


        :param ep_transport: The ep_transport of this Resource.
        :type ep_transport: List[EPTransportSingle]
        """

        self._ep_transport = ep_transport

    @property
    def network_slice_subnet_provider_capabilities(self):
        """Gets the network_slice_subnet_provider_capabilities of this Resource.


        :return: The network_slice_subnet_provider_capabilities of this Resource.
        :rtype: List[NetworkSliceSubnetProviderCapabilitiesSingle]
        """
        return self._network_slice_subnet_provider_capabilities

    @network_slice_subnet_provider_capabilities.setter
    def network_slice_subnet_provider_capabilities(self, network_slice_subnet_provider_capabilities):
        """Sets the network_slice_subnet_provider_capabilities of this Resource.


        :param network_slice_subnet_provider_capabilities: The network_slice_subnet_provider_capabilities of this Resource.
        :type network_slice_subnet_provider_capabilities: List[NetworkSliceSubnetProviderCapabilitiesSingle]
        """

        self._network_slice_subnet_provider_capabilities = network_slice_subnet_provider_capabilities

    @property
    def feasibility_check_and_reservation_job(self):
        """Gets the feasibility_check_and_reservation_job of this Resource.


        :return: The feasibility_check_and_reservation_job of this Resource.
        :rtype: List[FeasibilityCheckAndReservationJobSingle]
        """
        return self._feasibility_check_and_reservation_job

    @feasibility_check_and_reservation_job.setter
    def feasibility_check_and_reservation_job(self, feasibility_check_and_reservation_job):
        """Sets the feasibility_check_and_reservation_job of this Resource.


        :param feasibility_check_and_reservation_job: The feasibility_check_and_reservation_job of this Resource.
        :type feasibility_check_and_reservation_job: List[FeasibilityCheckAndReservationJobSingle]
        """

        self._feasibility_check_and_reservation_job = feasibility_check_and_reservation_job

    @property
    def assurance_goal(self):
        """Gets the assurance_goal of this Resource.


        :return: The assurance_goal of this Resource.
        :rtype: List[AssuranceGoalSingle]
        """
        return self._assurance_goal

    @assurance_goal.setter
    def assurance_goal(self, assurance_goal):
        """Sets the assurance_goal of this Resource.


        :param assurance_goal: The assurance_goal of this Resource.
        :type assurance_goal: List[AssuranceGoalSingle]
        """

        self._assurance_goal = assurance_goal

    @property
    def assurance_closed_control_loop(self):
        """Gets the assurance_closed_control_loop of this Resource.


        :return: The assurance_closed_control_loop of this Resource.
        :rtype: List[AssuranceClosedControlLoopSingle]
        """
        return self._assurance_closed_control_loop

    @assurance_closed_control_loop.setter
    def assurance_closed_control_loop(self, assurance_closed_control_loop):
        """Sets the assurance_closed_control_loop of this Resource.


        :param assurance_closed_control_loop: The assurance_closed_control_loop of this Resource.
        :type assurance_closed_control_loop: List[AssuranceClosedControlLoopSingle]
        """

        self._assurance_closed_control_loop = assurance_closed_control_loop

    @property
    def intent(self):
        """Gets the intent of this Resource.


        :return: The intent of this Resource.
        :rtype: List[IntentSingle]
        """
        return self._intent

    @intent.setter
    def intent(self, intent):
        """Sets the intent of this Resource.


        :param intent: The intent of this Resource.
        :type intent: List[IntentSingle]
        """

        self._intent = intent

    @property
    def user_label(self):
        """Gets the user_label of this Resource.


        :return: The user_label of this Resource.
        :rtype: str
        """
        return self._user_label

    @user_label.setter
    def user_label(self, user_label):
        """Sets the user_label of this Resource.


        :param user_label: The user_label of this Resource.
        :type user_label: str
        """

        self._user_label = user_label

    @property
    def intent_expectations(self):
        """Gets the intent_expectations of this Resource.


        :return: The intent_expectations of this Resource.
        :rtype: List[IntentSingleAllOfIntentExpectationsInner]
        """
        return self._intent_expectations

    @intent_expectations.setter
    def intent_expectations(self, intent_expectations):
        """Sets the intent_expectations of this Resource.


        :param intent_expectations: The intent_expectations of this Resource.
        :type intent_expectations: List[IntentSingleAllOfIntentExpectationsInner]
        """

        self._intent_expectations = intent_expectations

    @property
    def intent_contexts(self):
        """Gets the intent_contexts of this Resource.


        :return: The intent_contexts of this Resource.
        :rtype: List[IntentContext]
        """
        return self._intent_contexts

    @intent_contexts.setter
    def intent_contexts(self, intent_contexts):
        """Sets the intent_contexts of this Resource.


        :param intent_contexts: The intent_contexts of this Resource.
        :type intent_contexts: List[IntentContext]
        """

        self._intent_contexts = intent_contexts

    @property
    def intent_fulfilment_info(self):
        """Gets the intent_fulfilment_info of this Resource.


        :return: The intent_fulfilment_info of this Resource.
        :rtype: FulfilmentInfo
        """
        return self._intent_fulfilment_info

    @intent_fulfilment_info.setter
    def intent_fulfilment_info(self, intent_fulfilment_info):
        """Sets the intent_fulfilment_info of this Resource.


        :param intent_fulfilment_info: The intent_fulfilment_info of this Resource.
        :type intent_fulfilment_info: FulfilmentInfo
        """

        self._intent_fulfilment_info = intent_fulfilment_info
