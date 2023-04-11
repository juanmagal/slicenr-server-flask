# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.administrative_state import AdministrativeState
from openapi_server.models.alarm_list_single import AlarmListSingle
from openapi_server.models.beam_single import BeamSingle
from openapi_server.models.bwp_single import BwpSingle
from openapi_server.models.cco_function_single import CCOFunctionSingle
from openapi_server.models.cco_overshoot_coverage_parameters_single import CCOOvershootCoverageParametersSingle
from openapi_server.models.cco_parameters_attr_all_of_attributes import CCOParametersAttrAllOfAttributes
from openapi_server.models.cco_pilot_pollution_parameters_single import CCOPilotPollutionParametersSingle
from openapi_server.models.cco_weak_coverage_parameters_single import CCOWeakCoverageParametersSingle
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
from openapi_server.models.epe1_single import EPE1Single
from openapi_server.models.epf1_c_single import EPF1CSingle
from openapi_server.models.epf1_u_single import EPF1USingle
from openapi_server.models.epng_c_single import EPNgCSingle
from openapi_server.models.epng_u_single import EPNgUSingle
from openapi_server.models.eps1_u_single import EPS1USingle
from openapi_server.models.epx2_c_single import EPX2CSingle
from openapi_server.models.epx2_u_single import EPX2USingle
from openapi_server.models.epxn_c_single import EPXnCSingle
from openapi_server.models.epxn_u_single import EPXnUSingle
from openapi_server.models.e_utran_cell_relation_single import EUtranCellRelationSingle
from openapi_server.models.e_utran_freq_relation_single import EUtranFreqRelationSingle
from openapi_server.models.e_utran_frequency_single import EUtranFrequencySingle
from openapi_server.models.external_enb_function_single import ExternalENBFunctionSingle
from openapi_server.models.external_eu_tran_cell_single import ExternalEUTranCellSingle
from openapi_server.models.external_gnb_cu_cp_function_single import ExternalGnbCuCpFunctionSingle
from openapi_server.models.external_gnb_cu_up_function_single import ExternalGnbCuUpFunctionSingle
from openapi_server.models.external_gnb_du_function_single import ExternalGnbDuFunctionSingle
from openapi_server.models.external_nr_cell_cu_single import ExternalNrCellCuSingle
from openapi_server.models.file_download_job_single import FileDownloadJobSingle
from openapi_server.models.files_single import FilesSingle
from openapi_server.models.gnb_cu_cp_function_single import GnbCuCpFunctionSingle
from openapi_server.models.gnb_cu_up_function_single import GnbCuUpFunctionSingle
from openapi_server.models.gnb_du_function_single import GnbDuFunctionSingle
from openapi_server.models.managed_element_single import ManagedElementSingle
from openapi_server.models.managed_nf_service_single import ManagedNFServiceSingle
from openapi_server.models.management_data_collection_single import ManagementDataCollectionSingle
from openapi_server.models.management_node_single import ManagementNodeSingle
from openapi_server.models.me_context_single import MeContextSingle
from openapi_server.models.mn_s import MnS
from openapi_server.models.mns_agent_single import MnsAgentSingle
from openapi_server.models.mns_registry_single import MnsRegistrySingle
from openapi_server.models.nr_cell_relation_single import NRCellRelationSingle
from openapi_server.models.nr_freq_relation_single import NRFreqRelationSingle
from openapi_server.models.nr_frequency_single import NRFrequencySingle
from openapi_server.models.nr_cell_cu_single import NrCellCuSingle
from openapi_server.models.nr_cell_du_single import NrCellDuSingle
from openapi_server.models.nr_operator_cell_du_single import NrOperatorCellDuSingle
from openapi_server.models.nr_sector_carrier_single import NrSectorCarrierSingle
from openapi_server.models.ntf_subscription_control_single import NtfSubscriptionControlSingle
from openapi_server.models.operator_du_single import OperatorDuSingle
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle
from openapi_server.models.plmn_info import PlmnInfo
from openapi_server.models.rrm_policy_ratio_single import RRMPolicyRatioSingle
from openapi_server.models.rim_rs_global_single import RimRSGlobalSingle
from openapi_server.models.rim_rs_set_single import RimRSSetSingle
from openapi_server.models.sub_network_single import SubNetworkSingle
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle
from openapi_server.models.trace_job_single import TraceJobSingle
from openapi_server.models.vs_data_container_single import VsDataContainerSingle
from openapi_server import util

from openapi_server.models.administrative_state import AdministrativeState  # noqa: E501
from openapi_server.models.alarm_list_single import AlarmListSingle  # noqa: E501
from openapi_server.models.beam_single import BeamSingle  # noqa: E501
from openapi_server.models.bwp_single import BwpSingle  # noqa: E501
from openapi_server.models.cco_function_single import CCOFunctionSingle  # noqa: E501
from openapi_server.models.cco_overshoot_coverage_parameters_single import CCOOvershootCoverageParametersSingle  # noqa: E501
from openapi_server.models.cco_parameters_attr_all_of_attributes import CCOParametersAttrAllOfAttributes  # noqa: E501
from openapi_server.models.cco_pilot_pollution_parameters_single import CCOPilotPollutionParametersSingle  # noqa: E501
from openapi_server.models.cco_weak_coverage_parameters_single import CCOWeakCoverageParametersSingle  # noqa: E501
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
from openapi_server.models.epe1_single import EPE1Single  # noqa: E501
from openapi_server.models.epf1_c_single import EPF1CSingle  # noqa: E501
from openapi_server.models.epf1_u_single import EPF1USingle  # noqa: E501
from openapi_server.models.epng_c_single import EPNgCSingle  # noqa: E501
from openapi_server.models.epng_u_single import EPNgUSingle  # noqa: E501
from openapi_server.models.eps1_u_single import EPS1USingle  # noqa: E501
from openapi_server.models.epx2_c_single import EPX2CSingle  # noqa: E501
from openapi_server.models.epx2_u_single import EPX2USingle  # noqa: E501
from openapi_server.models.epxn_c_single import EPXnCSingle  # noqa: E501
from openapi_server.models.epxn_u_single import EPXnUSingle  # noqa: E501
from openapi_server.models.external_enb_function_single import ExternalENBFunctionSingle  # noqa: E501
from openapi_server.models.external_eu_tran_cell_single import ExternalEUTranCellSingle  # noqa: E501
from openapi_server.models.external_gnb_cu_cp_function_single import ExternalGnbCuCpFunctionSingle  # noqa: E501
from openapi_server.models.external_gnb_cu_up_function_single import ExternalGnbCuUpFunctionSingle  # noqa: E501
from openapi_server.models.external_gnb_du_function_single import ExternalGnbDuFunctionSingle  # noqa: E501
from openapi_server.models.external_nr_cell_cu_single import ExternalNrCellCuSingle  # noqa: E501
from openapi_server.models.file_download_job_single import FileDownloadJobSingle  # noqa: E501
from openapi_server.models.files_single import FilesSingle  # noqa: E501
from openapi_server.models.gnb_cu_cp_function_single import GnbCuCpFunctionSingle  # noqa: E501
from openapi_server.models.gnb_cu_up_function_single import GnbCuUpFunctionSingle  # noqa: E501
from openapi_server.models.gnb_du_function_single import GnbDuFunctionSingle  # noqa: E501
from openapi_server.models.managed_element_single import ManagedElementSingle  # noqa: E501
from openapi_server.models.managed_nf_service_single import ManagedNFServiceSingle  # noqa: E501
from openapi_server.models.management_data_collection_single import ManagementDataCollectionSingle  # noqa: E501
from openapi_server.models.management_node_single import ManagementNodeSingle  # noqa: E501
from openapi_server.models.me_context_single import MeContextSingle  # noqa: E501
from openapi_server.models.mn_s import MnS  # noqa: E501
from openapi_server.models.mns_agent_single import MnsAgentSingle  # noqa: E501
from openapi_server.models.mns_registry_single import MnsRegistrySingle  # noqa: E501
from openapi_server.models.nr_cell_cu_single import NrCellCuSingle  # noqa: E501
from openapi_server.models.nr_cell_du_single import NrCellDuSingle  # noqa: E501
from openapi_server.models.nr_cell_relation_single import NRCellRelationSingle  # noqa: E501
from openapi_server.models.nr_freq_relation_single import NRFreqRelationSingle  # noqa: E501
from openapi_server.models.nr_frequency_single import NRFrequencySingle  # noqa: E501
from openapi_server.models.nr_operator_cell_du_single import NrOperatorCellDuSingle  # noqa: E501
from openapi_server.models.nr_sector_carrier_single import NrSectorCarrierSingle  # noqa: E501
from openapi_server.models.ntf_subscription_control_single import NtfSubscriptionControlSingle  # noqa: E501
from openapi_server.models.operator_du_single import OperatorDuSingle  # noqa: E501
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle  # noqa: E501
from openapi_server.models.plmn_info import PlmnInfo  # noqa: E501
from openapi_server.models.rim_rs_global_single import RimRSGlobalSingle  # noqa: E501
from openapi_server.models.rim_rs_set_single import RimRSSetSingle  # noqa: E501
from openapi_server.models.rrm_policy_ratio_single import RRMPolicyRatioSingle  # noqa: E501
from openapi_server.models.sub_network_single import SubNetworkSingle  # noqa: E501
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle  # noqa: E501
from openapi_server.models.trace_job_single import TraceJobSingle  # noqa: E501
from openapi_server.models.vs_data_container_single import VsDataContainerSingle  # noqa: E501

class ResourcesNrNrm(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, sub_network=None, managed_element=None, id=None, object_class=None, object_instance=None, vs_data_container=None, attributes=None, management_node=None, mns_agent=None, me_context=None, perf_metric_job=None, threshold_monitor=None, trace_job=None, management_data_collection=None, ntf_subscription_control=None, alarm_list=None, file_download_job=None, files=None, mns_registry=None, nr_frequency=None, external_gnb_cu_cp_function=None, external_enb_function=None, e_utran_frequency=None, des_management_function=None, drach_optimization_function=None, dmro_function=None, dlbo_function=None, dpci_configuration_function=None, cpci_configuration_function=None, ces_management_function=None, configurable5_qi_set=None, rim_rs_global=None, dynamic5_qi_set=None, cco_function=None, gnb_du_function=None, gnb_cu_up_function=None, gnb_cu_cp_function=None, managed_nf_service=None, rrm_policy_ratio=None, nr_cell_du=None, bwp_multiple=None, nr_sector_carrier_multiple=None, ep_f1_c=None, ep_f1_u=None, operator_du=None, ep_e1=None, ep_xn_u=None, ep_ng_u=None, ep_x2_u=None, ep_s1_u=None, nr_cell_cu=None, ep_xn_c=None, ep_ng_c=None, ep_x2_c=None, danr_management_function=None, gnb_id=None, gnb_id_length=None, nr_cell_relation=None, e_utran_cell_relation=None, nr_freq_relation=None, e_utran_freq_relation=None, nr_operator_cell_du=None, cell_local_id=None, administrative_state=None, plmn_info_list=None, nr_tac=None, common_beamforming_function=None, beam=None, rim_rs_set=None, external_nr_cell_cu=None, external_eu_tran_cell=None):  # noqa: E501
        """ResourcesNrNrm - a model defined in OpenAPI

        :param sub_network: The sub_network of this ResourcesNrNrm.  # noqa: E501
        :type sub_network: List[SubNetworkSingle]
        :param managed_element: The managed_element of this ResourcesNrNrm.  # noqa: E501
        :type managed_element: List[ManagedElementSingle]
        :param id: The id of this ResourcesNrNrm.  # noqa: E501
        :type id: str
        :param object_class: The object_class of this ResourcesNrNrm.  # noqa: E501
        :type object_class: str
        :param object_instance: The object_instance of this ResourcesNrNrm.  # noqa: E501
        :type object_instance: str
        :param vs_data_container: The vs_data_container of this ResourcesNrNrm.  # noqa: E501
        :type vs_data_container: List[VsDataContainerSingle]
        :param attributes: The attributes of this ResourcesNrNrm.  # noqa: E501
        :type attributes: CCOParametersAttrAllOfAttributes
        :param management_node: The management_node of this ResourcesNrNrm.  # noqa: E501
        :type management_node: List[ManagementNodeSingle]
        :param mns_agent: The mns_agent of this ResourcesNrNrm.  # noqa: E501
        :type mns_agent: List[MnsAgentSingle]
        :param me_context: The me_context of this ResourcesNrNrm.  # noqa: E501
        :type me_context: List[MeContextSingle]
        :param perf_metric_job: The perf_metric_job of this ResourcesNrNrm.  # noqa: E501
        :type perf_metric_job: List[PerfMetricJobSingle]
        :param threshold_monitor: The threshold_monitor of this ResourcesNrNrm.  # noqa: E501
        :type threshold_monitor: List[ThresholdMonitorSingle]
        :param trace_job: The trace_job of this ResourcesNrNrm.  # noqa: E501
        :type trace_job: List[TraceJobSingle]
        :param management_data_collection: The management_data_collection of this ResourcesNrNrm.  # noqa: E501
        :type management_data_collection: List[ManagementDataCollectionSingle]
        :param ntf_subscription_control: The ntf_subscription_control of this ResourcesNrNrm.  # noqa: E501
        :type ntf_subscription_control: List[NtfSubscriptionControlSingle]
        :param alarm_list: The alarm_list of this ResourcesNrNrm.  # noqa: E501
        :type alarm_list: AlarmListSingle
        :param file_download_job: The file_download_job of this ResourcesNrNrm.  # noqa: E501
        :type file_download_job: List[FileDownloadJobSingle]
        :param files: The files of this ResourcesNrNrm.  # noqa: E501
        :type files: List[FilesSingle]
        :param mns_registry: The mns_registry of this ResourcesNrNrm.  # noqa: E501
        :type mns_registry: MnsRegistrySingle
        :param nr_frequency: The nr_frequency of this ResourcesNrNrm.  # noqa: E501
        :type nr_frequency: List[NRFrequencySingle]
        :param external_gnb_cu_cp_function: The external_gnb_cu_cp_function of this ResourcesNrNrm.  # noqa: E501
        :type external_gnb_cu_cp_function: List[ExternalGnbCuCpFunctionSingle]
        :param external_enb_function: The external_enb_function of this ResourcesNrNrm.  # noqa: E501
        :type external_enb_function: List[ExternalENBFunctionSingle]
        :param e_utran_frequency: The e_utran_frequency of this ResourcesNrNrm.  # noqa: E501
        :type e_utran_frequency: List[EUtranFrequencySingle]
        :param des_management_function: The des_management_function of this ResourcesNrNrm.  # noqa: E501
        :type des_management_function: DESManagementFunctionSingle
        :param drach_optimization_function: The drach_optimization_function of this ResourcesNrNrm.  # noqa: E501
        :type drach_optimization_function: DRACHOptimizationFunctionSingle
        :param dmro_function: The dmro_function of this ResourcesNrNrm.  # noqa: E501
        :type dmro_function: DMROFunctionSingle
        :param dlbo_function: The dlbo_function of this ResourcesNrNrm.  # noqa: E501
        :type dlbo_function: DLBOFunctionSingle
        :param dpci_configuration_function: The dpci_configuration_function of this ResourcesNrNrm.  # noqa: E501
        :type dpci_configuration_function: DPCIConfigurationFunctionSingle
        :param cpci_configuration_function: The cpci_configuration_function of this ResourcesNrNrm.  # noqa: E501
        :type cpci_configuration_function: CPCIConfigurationFunctionSingle
        :param ces_management_function: The ces_management_function of this ResourcesNrNrm.  # noqa: E501
        :type ces_management_function: CESManagementFunctionSingle
        :param configurable5_qi_set: The configurable5_qi_set of this ResourcesNrNrm.  # noqa: E501
        :type configurable5_qi_set: List[Configurable5QISetSingle]
        :param rim_rs_global: The rim_rs_global of this ResourcesNrNrm.  # noqa: E501
        :type rim_rs_global: RimRSGlobalSingle
        :param dynamic5_qi_set: The dynamic5_qi_set of this ResourcesNrNrm.  # noqa: E501
        :type dynamic5_qi_set: List[Dynamic5QISetSingle]
        :param cco_function: The cco_function of this ResourcesNrNrm.  # noqa: E501
        :type cco_function: CCOFunctionSingle
        :param gnb_du_function: The gnb_du_function of this ResourcesNrNrm.  # noqa: E501
        :type gnb_du_function: List[GnbDuFunctionSingle]
        :param gnb_cu_up_function: The gnb_cu_up_function of this ResourcesNrNrm.  # noqa: E501
        :type gnb_cu_up_function: List[GnbCuUpFunctionSingle]
        :param gnb_cu_cp_function: The gnb_cu_cp_function of this ResourcesNrNrm.  # noqa: E501
        :type gnb_cu_cp_function: List[GnbCuCpFunctionSingle]
        :param managed_nf_service: The managed_nf_service of this ResourcesNrNrm.  # noqa: E501
        :type managed_nf_service: List[ManagedNFServiceSingle]
        :param rrm_policy_ratio: The rrm_policy_ratio of this ResourcesNrNrm.  # noqa: E501
        :type rrm_policy_ratio: List[RRMPolicyRatioSingle]
        :param nr_cell_du: The nr_cell_du of this ResourcesNrNrm.  # noqa: E501
        :type nr_cell_du: List[NrCellDuSingle]
        :param bwp_multiple: The bwp_multiple of this ResourcesNrNrm.  # noqa: E501
        :type bwp_multiple: List[BwpSingle]
        :param nr_sector_carrier_multiple: The nr_sector_carrier_multiple of this ResourcesNrNrm.  # noqa: E501
        :type nr_sector_carrier_multiple: List[NrSectorCarrierSingle]
        :param ep_f1_c: The ep_f1_c of this ResourcesNrNrm.  # noqa: E501
        :type ep_f1_c: List[EPF1CSingle]
        :param ep_f1_u: The ep_f1_u of this ResourcesNrNrm.  # noqa: E501
        :type ep_f1_u: List[EPF1USingle]
        :param operator_du: The operator_du of this ResourcesNrNrm.  # noqa: E501
        :type operator_du: List[OperatorDuSingle]
        :param ep_e1: The ep_e1 of this ResourcesNrNrm.  # noqa: E501
        :type ep_e1: List[EPE1Single]
        :param ep_xn_u: The ep_xn_u of this ResourcesNrNrm.  # noqa: E501
        :type ep_xn_u: List[EPXnUSingle]
        :param ep_ng_u: The ep_ng_u of this ResourcesNrNrm.  # noqa: E501
        :type ep_ng_u: List[EPNgUSingle]
        :param ep_x2_u: The ep_x2_u of this ResourcesNrNrm.  # noqa: E501
        :type ep_x2_u: List[EPX2USingle]
        :param ep_s1_u: The ep_s1_u of this ResourcesNrNrm.  # noqa: E501
        :type ep_s1_u: List[EPS1USingle]
        :param nr_cell_cu: The nr_cell_cu of this ResourcesNrNrm.  # noqa: E501
        :type nr_cell_cu: List[NrCellCuSingle]
        :param ep_xn_c: The ep_xn_c of this ResourcesNrNrm.  # noqa: E501
        :type ep_xn_c: List[EPXnCSingle]
        :param ep_ng_c: The ep_ng_c of this ResourcesNrNrm.  # noqa: E501
        :type ep_ng_c: List[EPNgCSingle]
        :param ep_x2_c: The ep_x2_c of this ResourcesNrNrm.  # noqa: E501
        :type ep_x2_c: List[EPX2CSingle]
        :param danr_management_function: The danr_management_function of this ResourcesNrNrm.  # noqa: E501
        :type danr_management_function: DANRManagementFunctionSingle
        :param gnb_id: The gnb_id of this ResourcesNrNrm.  # noqa: E501
        :type gnb_id: str
        :param gnb_id_length: The gnb_id_length of this ResourcesNrNrm.  # noqa: E501
        :type gnb_id_length: int
        :param nr_cell_relation: The nr_cell_relation of this ResourcesNrNrm.  # noqa: E501
        :type nr_cell_relation: List[NRCellRelationSingle]
        :param e_utran_cell_relation: The e_utran_cell_relation of this ResourcesNrNrm.  # noqa: E501
        :type e_utran_cell_relation: List[EUtranCellRelationSingle]
        :param nr_freq_relation: The nr_freq_relation of this ResourcesNrNrm.  # noqa: E501
        :type nr_freq_relation: List[NRFreqRelationSingle]
        :param e_utran_freq_relation: The e_utran_freq_relation of this ResourcesNrNrm.  # noqa: E501
        :type e_utran_freq_relation: List[EUtranFreqRelationSingle]
        :param nr_operator_cell_du: The nr_operator_cell_du of this ResourcesNrNrm.  # noqa: E501
        :type nr_operator_cell_du: List[NrOperatorCellDuSingle]
        :param cell_local_id: The cell_local_id of this ResourcesNrNrm.  # noqa: E501
        :type cell_local_id: int
        :param administrative_state: The administrative_state of this ResourcesNrNrm.  # noqa: E501
        :type administrative_state: AdministrativeState
        :param plmn_info_list: The plmn_info_list of this ResourcesNrNrm.  # noqa: E501
        :type plmn_info_list: List[PlmnInfo]
        :param nr_tac: The nr_tac of this ResourcesNrNrm.  # noqa: E501
        :type nr_tac: int
        :param common_beamforming_function: The common_beamforming_function of this ResourcesNrNrm.  # noqa: E501
        :type common_beamforming_function: CommonBeamformingFunctionSingle
        :param beam: The beam of this ResourcesNrNrm.  # noqa: E501
        :type beam: List[BeamSingle]
        :param rim_rs_set: The rim_rs_set of this ResourcesNrNrm.  # noqa: E501
        :type rim_rs_set: List[RimRSSetSingle]
        :param external_nr_cell_cu: The external_nr_cell_cu of this ResourcesNrNrm.  # noqa: E501
        :type external_nr_cell_cu: List[ExternalNrCellCuSingle]
        :param external_eu_tran_cell: The external_eu_tran_cell of this ResourcesNrNrm.  # noqa: E501
        :type external_eu_tran_cell: List[ExternalEUTranCellSingle]
        """
        self.openapi_types = {
            'sub_network': List[SubNetworkSingle],
            'managed_element': List[ManagedElementSingle],
            'id': str,
            'object_class': str,
            'object_instance': str,
            'vs_data_container': List[VsDataContainerSingle],
            'attributes': CCOParametersAttrAllOfAttributes,
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
            'external_eu_tran_cell': List[ExternalEUTranCellSingle]
        }

        self.attribute_map = {
            'sub_network': 'SubNetwork',
            'managed_element': 'ManagedElement',
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
            'external_eu_tran_cell': 'ExternalEUTranCell'
        }

        self._sub_network = sub_network
        self._managed_element = managed_element
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

    @classmethod
    def from_dict(cls, dikt) -> 'ResourcesNrNrm':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The resources-nrNrm of this ResourcesNrNrm.  # noqa: E501
        :rtype: ResourcesNrNrm
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sub_network(self):
        """Gets the sub_network of this ResourcesNrNrm.


        :return: The sub_network of this ResourcesNrNrm.
        :rtype: List[SubNetworkSingle]
        """
        return self._sub_network

    @sub_network.setter
    def sub_network(self, sub_network):
        """Sets the sub_network of this ResourcesNrNrm.


        :param sub_network: The sub_network of this ResourcesNrNrm.
        :type sub_network: List[SubNetworkSingle]
        """

        self._sub_network = sub_network

    @property
    def managed_element(self):
        """Gets the managed_element of this ResourcesNrNrm.


        :return: The managed_element of this ResourcesNrNrm.
        :rtype: List[ManagedElementSingle]
        """
        return self._managed_element

    @managed_element.setter
    def managed_element(self, managed_element):
        """Sets the managed_element of this ResourcesNrNrm.


        :param managed_element: The managed_element of this ResourcesNrNrm.
        :type managed_element: List[ManagedElementSingle]
        """

        self._managed_element = managed_element

    @property
    def id(self):
        """Gets the id of this ResourcesNrNrm.


        :return: The id of this ResourcesNrNrm.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResourcesNrNrm.


        :param id: The id of this ResourcesNrNrm.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def object_class(self):
        """Gets the object_class of this ResourcesNrNrm.


        :return: The object_class of this ResourcesNrNrm.
        :rtype: str
        """
        return self._object_class

    @object_class.setter
    def object_class(self, object_class):
        """Sets the object_class of this ResourcesNrNrm.


        :param object_class: The object_class of this ResourcesNrNrm.
        :type object_class: str
        """

        self._object_class = object_class

    @property
    def object_instance(self):
        """Gets the object_instance of this ResourcesNrNrm.


        :return: The object_instance of this ResourcesNrNrm.
        :rtype: str
        """
        return self._object_instance

    @object_instance.setter
    def object_instance(self, object_instance):
        """Sets the object_instance of this ResourcesNrNrm.


        :param object_instance: The object_instance of this ResourcesNrNrm.
        :type object_instance: str
        """

        self._object_instance = object_instance

    @property
    def vs_data_container(self):
        """Gets the vs_data_container of this ResourcesNrNrm.


        :return: The vs_data_container of this ResourcesNrNrm.
        :rtype: List[VsDataContainerSingle]
        """
        return self._vs_data_container

    @vs_data_container.setter
    def vs_data_container(self, vs_data_container):
        """Sets the vs_data_container of this ResourcesNrNrm.


        :param vs_data_container: The vs_data_container of this ResourcesNrNrm.
        :type vs_data_container: List[VsDataContainerSingle]
        """

        self._vs_data_container = vs_data_container

    @property
    def attributes(self):
        """Gets the attributes of this ResourcesNrNrm.


        :return: The attributes of this ResourcesNrNrm.
        :rtype: CCOParametersAttrAllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this ResourcesNrNrm.


        :param attributes: The attributes of this ResourcesNrNrm.
        :type attributes: CCOParametersAttrAllOfAttributes
        """

        self._attributes = attributes

    @property
    def management_node(self):
        """Gets the management_node of this ResourcesNrNrm.


        :return: The management_node of this ResourcesNrNrm.
        :rtype: List[ManagementNodeSingle]
        """
        return self._management_node

    @management_node.setter
    def management_node(self, management_node):
        """Sets the management_node of this ResourcesNrNrm.


        :param management_node: The management_node of this ResourcesNrNrm.
        :type management_node: List[ManagementNodeSingle]
        """

        self._management_node = management_node

    @property
    def mns_agent(self):
        """Gets the mns_agent of this ResourcesNrNrm.


        :return: The mns_agent of this ResourcesNrNrm.
        :rtype: List[MnsAgentSingle]
        """
        return self._mns_agent

    @mns_agent.setter
    def mns_agent(self, mns_agent):
        """Sets the mns_agent of this ResourcesNrNrm.


        :param mns_agent: The mns_agent of this ResourcesNrNrm.
        :type mns_agent: List[MnsAgentSingle]
        """

        self._mns_agent = mns_agent

    @property
    def me_context(self):
        """Gets the me_context of this ResourcesNrNrm.


        :return: The me_context of this ResourcesNrNrm.
        :rtype: List[MeContextSingle]
        """
        return self._me_context

    @me_context.setter
    def me_context(self, me_context):
        """Sets the me_context of this ResourcesNrNrm.


        :param me_context: The me_context of this ResourcesNrNrm.
        :type me_context: List[MeContextSingle]
        """

        self._me_context = me_context

    @property
    def perf_metric_job(self):
        """Gets the perf_metric_job of this ResourcesNrNrm.


        :return: The perf_metric_job of this ResourcesNrNrm.
        :rtype: List[PerfMetricJobSingle]
        """
        return self._perf_metric_job

    @perf_metric_job.setter
    def perf_metric_job(self, perf_metric_job):
        """Sets the perf_metric_job of this ResourcesNrNrm.


        :param perf_metric_job: The perf_metric_job of this ResourcesNrNrm.
        :type perf_metric_job: List[PerfMetricJobSingle]
        """

        self._perf_metric_job = perf_metric_job

    @property
    def threshold_monitor(self):
        """Gets the threshold_monitor of this ResourcesNrNrm.


        :return: The threshold_monitor of this ResourcesNrNrm.
        :rtype: List[ThresholdMonitorSingle]
        """
        return self._threshold_monitor

    @threshold_monitor.setter
    def threshold_monitor(self, threshold_monitor):
        """Sets the threshold_monitor of this ResourcesNrNrm.


        :param threshold_monitor: The threshold_monitor of this ResourcesNrNrm.
        :type threshold_monitor: List[ThresholdMonitorSingle]
        """

        self._threshold_monitor = threshold_monitor

    @property
    def trace_job(self):
        """Gets the trace_job of this ResourcesNrNrm.


        :return: The trace_job of this ResourcesNrNrm.
        :rtype: List[TraceJobSingle]
        """
        return self._trace_job

    @trace_job.setter
    def trace_job(self, trace_job):
        """Sets the trace_job of this ResourcesNrNrm.


        :param trace_job: The trace_job of this ResourcesNrNrm.
        :type trace_job: List[TraceJobSingle]
        """

        self._trace_job = trace_job

    @property
    def management_data_collection(self):
        """Gets the management_data_collection of this ResourcesNrNrm.


        :return: The management_data_collection of this ResourcesNrNrm.
        :rtype: List[ManagementDataCollectionSingle]
        """
        return self._management_data_collection

    @management_data_collection.setter
    def management_data_collection(self, management_data_collection):
        """Sets the management_data_collection of this ResourcesNrNrm.


        :param management_data_collection: The management_data_collection of this ResourcesNrNrm.
        :type management_data_collection: List[ManagementDataCollectionSingle]
        """

        self._management_data_collection = management_data_collection

    @property
    def ntf_subscription_control(self):
        """Gets the ntf_subscription_control of this ResourcesNrNrm.


        :return: The ntf_subscription_control of this ResourcesNrNrm.
        :rtype: List[NtfSubscriptionControlSingle]
        """
        return self._ntf_subscription_control

    @ntf_subscription_control.setter
    def ntf_subscription_control(self, ntf_subscription_control):
        """Sets the ntf_subscription_control of this ResourcesNrNrm.


        :param ntf_subscription_control: The ntf_subscription_control of this ResourcesNrNrm.
        :type ntf_subscription_control: List[NtfSubscriptionControlSingle]
        """

        self._ntf_subscription_control = ntf_subscription_control

    @property
    def alarm_list(self):
        """Gets the alarm_list of this ResourcesNrNrm.


        :return: The alarm_list of this ResourcesNrNrm.
        :rtype: AlarmListSingle
        """
        return self._alarm_list

    @alarm_list.setter
    def alarm_list(self, alarm_list):
        """Sets the alarm_list of this ResourcesNrNrm.


        :param alarm_list: The alarm_list of this ResourcesNrNrm.
        :type alarm_list: AlarmListSingle
        """

        self._alarm_list = alarm_list

    @property
    def file_download_job(self):
        """Gets the file_download_job of this ResourcesNrNrm.


        :return: The file_download_job of this ResourcesNrNrm.
        :rtype: List[FileDownloadJobSingle]
        """
        return self._file_download_job

    @file_download_job.setter
    def file_download_job(self, file_download_job):
        """Sets the file_download_job of this ResourcesNrNrm.


        :param file_download_job: The file_download_job of this ResourcesNrNrm.
        :type file_download_job: List[FileDownloadJobSingle]
        """

        self._file_download_job = file_download_job

    @property
    def files(self):
        """Gets the files of this ResourcesNrNrm.


        :return: The files of this ResourcesNrNrm.
        :rtype: List[FilesSingle]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this ResourcesNrNrm.


        :param files: The files of this ResourcesNrNrm.
        :type files: List[FilesSingle]
        """

        self._files = files

    @property
    def mns_registry(self):
        """Gets the mns_registry of this ResourcesNrNrm.


        :return: The mns_registry of this ResourcesNrNrm.
        :rtype: MnsRegistrySingle
        """
        return self._mns_registry

    @mns_registry.setter
    def mns_registry(self, mns_registry):
        """Sets the mns_registry of this ResourcesNrNrm.


        :param mns_registry: The mns_registry of this ResourcesNrNrm.
        :type mns_registry: MnsRegistrySingle
        """

        self._mns_registry = mns_registry

    @property
    def nr_frequency(self):
        """Gets the nr_frequency of this ResourcesNrNrm.


        :return: The nr_frequency of this ResourcesNrNrm.
        :rtype: List[NRFrequencySingle]
        """
        return self._nr_frequency

    @nr_frequency.setter
    def nr_frequency(self, nr_frequency):
        """Sets the nr_frequency of this ResourcesNrNrm.


        :param nr_frequency: The nr_frequency of this ResourcesNrNrm.
        :type nr_frequency: List[NRFrequencySingle]
        """
        if nr_frequency is not None and len(nr_frequency) < 1:
            raise ValueError("Invalid value for `nr_frequency`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._nr_frequency = nr_frequency

    @property
    def external_gnb_cu_cp_function(self):
        """Gets the external_gnb_cu_cp_function of this ResourcesNrNrm.


        :return: The external_gnb_cu_cp_function of this ResourcesNrNrm.
        :rtype: List[ExternalGnbCuCpFunctionSingle]
        """
        return self._external_gnb_cu_cp_function

    @external_gnb_cu_cp_function.setter
    def external_gnb_cu_cp_function(self, external_gnb_cu_cp_function):
        """Sets the external_gnb_cu_cp_function of this ResourcesNrNrm.


        :param external_gnb_cu_cp_function: The external_gnb_cu_cp_function of this ResourcesNrNrm.
        :type external_gnb_cu_cp_function: List[ExternalGnbCuCpFunctionSingle]
        """

        self._external_gnb_cu_cp_function = external_gnb_cu_cp_function

    @property
    def external_enb_function(self):
        """Gets the external_enb_function of this ResourcesNrNrm.


        :return: The external_enb_function of this ResourcesNrNrm.
        :rtype: List[ExternalENBFunctionSingle]
        """
        return self._external_enb_function

    @external_enb_function.setter
    def external_enb_function(self, external_enb_function):
        """Sets the external_enb_function of this ResourcesNrNrm.


        :param external_enb_function: The external_enb_function of this ResourcesNrNrm.
        :type external_enb_function: List[ExternalENBFunctionSingle]
        """

        self._external_enb_function = external_enb_function

    @property
    def e_utran_frequency(self):
        """Gets the e_utran_frequency of this ResourcesNrNrm.


        :return: The e_utran_frequency of this ResourcesNrNrm.
        :rtype: List[EUtranFrequencySingle]
        """
        return self._e_utran_frequency

    @e_utran_frequency.setter
    def e_utran_frequency(self, e_utran_frequency):
        """Sets the e_utran_frequency of this ResourcesNrNrm.


        :param e_utran_frequency: The e_utran_frequency of this ResourcesNrNrm.
        :type e_utran_frequency: List[EUtranFrequencySingle]
        """
        if e_utran_frequency is not None and len(e_utran_frequency) < 1:
            raise ValueError("Invalid value for `e_utran_frequency`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._e_utran_frequency = e_utran_frequency

    @property
    def des_management_function(self):
        """Gets the des_management_function of this ResourcesNrNrm.


        :return: The des_management_function of this ResourcesNrNrm.
        :rtype: DESManagementFunctionSingle
        """
        return self._des_management_function

    @des_management_function.setter
    def des_management_function(self, des_management_function):
        """Sets the des_management_function of this ResourcesNrNrm.


        :param des_management_function: The des_management_function of this ResourcesNrNrm.
        :type des_management_function: DESManagementFunctionSingle
        """

        self._des_management_function = des_management_function

    @property
    def drach_optimization_function(self):
        """Gets the drach_optimization_function of this ResourcesNrNrm.


        :return: The drach_optimization_function of this ResourcesNrNrm.
        :rtype: DRACHOptimizationFunctionSingle
        """
        return self._drach_optimization_function

    @drach_optimization_function.setter
    def drach_optimization_function(self, drach_optimization_function):
        """Sets the drach_optimization_function of this ResourcesNrNrm.


        :param drach_optimization_function: The drach_optimization_function of this ResourcesNrNrm.
        :type drach_optimization_function: DRACHOptimizationFunctionSingle
        """

        self._drach_optimization_function = drach_optimization_function

    @property
    def dmro_function(self):
        """Gets the dmro_function of this ResourcesNrNrm.


        :return: The dmro_function of this ResourcesNrNrm.
        :rtype: DMROFunctionSingle
        """
        return self._dmro_function

    @dmro_function.setter
    def dmro_function(self, dmro_function):
        """Sets the dmro_function of this ResourcesNrNrm.


        :param dmro_function: The dmro_function of this ResourcesNrNrm.
        :type dmro_function: DMROFunctionSingle
        """

        self._dmro_function = dmro_function

    @property
    def dlbo_function(self):
        """Gets the dlbo_function of this ResourcesNrNrm.


        :return: The dlbo_function of this ResourcesNrNrm.
        :rtype: DLBOFunctionSingle
        """
        return self._dlbo_function

    @dlbo_function.setter
    def dlbo_function(self, dlbo_function):
        """Sets the dlbo_function of this ResourcesNrNrm.


        :param dlbo_function: The dlbo_function of this ResourcesNrNrm.
        :type dlbo_function: DLBOFunctionSingle
        """

        self._dlbo_function = dlbo_function

    @property
    def dpci_configuration_function(self):
        """Gets the dpci_configuration_function of this ResourcesNrNrm.


        :return: The dpci_configuration_function of this ResourcesNrNrm.
        :rtype: DPCIConfigurationFunctionSingle
        """
        return self._dpci_configuration_function

    @dpci_configuration_function.setter
    def dpci_configuration_function(self, dpci_configuration_function):
        """Sets the dpci_configuration_function of this ResourcesNrNrm.


        :param dpci_configuration_function: The dpci_configuration_function of this ResourcesNrNrm.
        :type dpci_configuration_function: DPCIConfigurationFunctionSingle
        """

        self._dpci_configuration_function = dpci_configuration_function

    @property
    def cpci_configuration_function(self):
        """Gets the cpci_configuration_function of this ResourcesNrNrm.


        :return: The cpci_configuration_function of this ResourcesNrNrm.
        :rtype: CPCIConfigurationFunctionSingle
        """
        return self._cpci_configuration_function

    @cpci_configuration_function.setter
    def cpci_configuration_function(self, cpci_configuration_function):
        """Sets the cpci_configuration_function of this ResourcesNrNrm.


        :param cpci_configuration_function: The cpci_configuration_function of this ResourcesNrNrm.
        :type cpci_configuration_function: CPCIConfigurationFunctionSingle
        """

        self._cpci_configuration_function = cpci_configuration_function

    @property
    def ces_management_function(self):
        """Gets the ces_management_function of this ResourcesNrNrm.


        :return: The ces_management_function of this ResourcesNrNrm.
        :rtype: CESManagementFunctionSingle
        """
        return self._ces_management_function

    @ces_management_function.setter
    def ces_management_function(self, ces_management_function):
        """Sets the ces_management_function of this ResourcesNrNrm.


        :param ces_management_function: The ces_management_function of this ResourcesNrNrm.
        :type ces_management_function: CESManagementFunctionSingle
        """

        self._ces_management_function = ces_management_function

    @property
    def configurable5_qi_set(self):
        """Gets the configurable5_qi_set of this ResourcesNrNrm.


        :return: The configurable5_qi_set of this ResourcesNrNrm.
        :rtype: List[Configurable5QISetSingle]
        """
        return self._configurable5_qi_set

    @configurable5_qi_set.setter
    def configurable5_qi_set(self, configurable5_qi_set):
        """Sets the configurable5_qi_set of this ResourcesNrNrm.


        :param configurable5_qi_set: The configurable5_qi_set of this ResourcesNrNrm.
        :type configurable5_qi_set: List[Configurable5QISetSingle]
        """

        self._configurable5_qi_set = configurable5_qi_set

    @property
    def rim_rs_global(self):
        """Gets the rim_rs_global of this ResourcesNrNrm.


        :return: The rim_rs_global of this ResourcesNrNrm.
        :rtype: RimRSGlobalSingle
        """
        return self._rim_rs_global

    @rim_rs_global.setter
    def rim_rs_global(self, rim_rs_global):
        """Sets the rim_rs_global of this ResourcesNrNrm.


        :param rim_rs_global: The rim_rs_global of this ResourcesNrNrm.
        :type rim_rs_global: RimRSGlobalSingle
        """

        self._rim_rs_global = rim_rs_global

    @property
    def dynamic5_qi_set(self):
        """Gets the dynamic5_qi_set of this ResourcesNrNrm.


        :return: The dynamic5_qi_set of this ResourcesNrNrm.
        :rtype: List[Dynamic5QISetSingle]
        """
        return self._dynamic5_qi_set

    @dynamic5_qi_set.setter
    def dynamic5_qi_set(self, dynamic5_qi_set):
        """Sets the dynamic5_qi_set of this ResourcesNrNrm.


        :param dynamic5_qi_set: The dynamic5_qi_set of this ResourcesNrNrm.
        :type dynamic5_qi_set: List[Dynamic5QISetSingle]
        """

        self._dynamic5_qi_set = dynamic5_qi_set

    @property
    def cco_function(self):
        """Gets the cco_function of this ResourcesNrNrm.


        :return: The cco_function of this ResourcesNrNrm.
        :rtype: CCOFunctionSingle
        """
        return self._cco_function

    @cco_function.setter
    def cco_function(self, cco_function):
        """Sets the cco_function of this ResourcesNrNrm.


        :param cco_function: The cco_function of this ResourcesNrNrm.
        :type cco_function: CCOFunctionSingle
        """

        self._cco_function = cco_function

    @property
    def gnb_du_function(self):
        """Gets the gnb_du_function of this ResourcesNrNrm.


        :return: The gnb_du_function of this ResourcesNrNrm.
        :rtype: List[GnbDuFunctionSingle]
        """
        return self._gnb_du_function

    @gnb_du_function.setter
    def gnb_du_function(self, gnb_du_function):
        """Sets the gnb_du_function of this ResourcesNrNrm.


        :param gnb_du_function: The gnb_du_function of this ResourcesNrNrm.
        :type gnb_du_function: List[GnbDuFunctionSingle]
        """

        self._gnb_du_function = gnb_du_function

    @property
    def gnb_cu_up_function(self):
        """Gets the gnb_cu_up_function of this ResourcesNrNrm.


        :return: The gnb_cu_up_function of this ResourcesNrNrm.
        :rtype: List[GnbCuUpFunctionSingle]
        """
        return self._gnb_cu_up_function

    @gnb_cu_up_function.setter
    def gnb_cu_up_function(self, gnb_cu_up_function):
        """Sets the gnb_cu_up_function of this ResourcesNrNrm.


        :param gnb_cu_up_function: The gnb_cu_up_function of this ResourcesNrNrm.
        :type gnb_cu_up_function: List[GnbCuUpFunctionSingle]
        """

        self._gnb_cu_up_function = gnb_cu_up_function

    @property
    def gnb_cu_cp_function(self):
        """Gets the gnb_cu_cp_function of this ResourcesNrNrm.


        :return: The gnb_cu_cp_function of this ResourcesNrNrm.
        :rtype: List[GnbCuCpFunctionSingle]
        """
        return self._gnb_cu_cp_function

    @gnb_cu_cp_function.setter
    def gnb_cu_cp_function(self, gnb_cu_cp_function):
        """Sets the gnb_cu_cp_function of this ResourcesNrNrm.


        :param gnb_cu_cp_function: The gnb_cu_cp_function of this ResourcesNrNrm.
        :type gnb_cu_cp_function: List[GnbCuCpFunctionSingle]
        """

        self._gnb_cu_cp_function = gnb_cu_cp_function

    @property
    def managed_nf_service(self):
        """Gets the managed_nf_service of this ResourcesNrNrm.


        :return: The managed_nf_service of this ResourcesNrNrm.
        :rtype: List[ManagedNFServiceSingle]
        """
        return self._managed_nf_service

    @managed_nf_service.setter
    def managed_nf_service(self, managed_nf_service):
        """Sets the managed_nf_service of this ResourcesNrNrm.


        :param managed_nf_service: The managed_nf_service of this ResourcesNrNrm.
        :type managed_nf_service: List[ManagedNFServiceSingle]
        """

        self._managed_nf_service = managed_nf_service

    @property
    def rrm_policy_ratio(self):
        """Gets the rrm_policy_ratio of this ResourcesNrNrm.


        :return: The rrm_policy_ratio of this ResourcesNrNrm.
        :rtype: List[RRMPolicyRatioSingle]
        """
        return self._rrm_policy_ratio

    @rrm_policy_ratio.setter
    def rrm_policy_ratio(self, rrm_policy_ratio):
        """Sets the rrm_policy_ratio of this ResourcesNrNrm.


        :param rrm_policy_ratio: The rrm_policy_ratio of this ResourcesNrNrm.
        :type rrm_policy_ratio: List[RRMPolicyRatioSingle]
        """

        self._rrm_policy_ratio = rrm_policy_ratio

    @property
    def nr_cell_du(self):
        """Gets the nr_cell_du of this ResourcesNrNrm.


        :return: The nr_cell_du of this ResourcesNrNrm.
        :rtype: List[NrCellDuSingle]
        """
        return self._nr_cell_du

    @nr_cell_du.setter
    def nr_cell_du(self, nr_cell_du):
        """Sets the nr_cell_du of this ResourcesNrNrm.


        :param nr_cell_du: The nr_cell_du of this ResourcesNrNrm.
        :type nr_cell_du: List[NrCellDuSingle]
        """

        self._nr_cell_du = nr_cell_du

    @property
    def bwp_multiple(self):
        """Gets the bwp_multiple of this ResourcesNrNrm.


        :return: The bwp_multiple of this ResourcesNrNrm.
        :rtype: List[BwpSingle]
        """
        return self._bwp_multiple

    @bwp_multiple.setter
    def bwp_multiple(self, bwp_multiple):
        """Sets the bwp_multiple of this ResourcesNrNrm.


        :param bwp_multiple: The bwp_multiple of this ResourcesNrNrm.
        :type bwp_multiple: List[BwpSingle]
        """

        self._bwp_multiple = bwp_multiple

    @property
    def nr_sector_carrier_multiple(self):
        """Gets the nr_sector_carrier_multiple of this ResourcesNrNrm.


        :return: The nr_sector_carrier_multiple of this ResourcesNrNrm.
        :rtype: List[NrSectorCarrierSingle]
        """
        return self._nr_sector_carrier_multiple

    @nr_sector_carrier_multiple.setter
    def nr_sector_carrier_multiple(self, nr_sector_carrier_multiple):
        """Sets the nr_sector_carrier_multiple of this ResourcesNrNrm.


        :param nr_sector_carrier_multiple: The nr_sector_carrier_multiple of this ResourcesNrNrm.
        :type nr_sector_carrier_multiple: List[NrSectorCarrierSingle]
        """

        self._nr_sector_carrier_multiple = nr_sector_carrier_multiple

    @property
    def ep_f1_c(self):
        """Gets the ep_f1_c of this ResourcesNrNrm.


        :return: The ep_f1_c of this ResourcesNrNrm.
        :rtype: List[EPF1CSingle]
        """
        return self._ep_f1_c

    @ep_f1_c.setter
    def ep_f1_c(self, ep_f1_c):
        """Sets the ep_f1_c of this ResourcesNrNrm.


        :param ep_f1_c: The ep_f1_c of this ResourcesNrNrm.
        :type ep_f1_c: List[EPF1CSingle]
        """

        self._ep_f1_c = ep_f1_c

    @property
    def ep_f1_u(self):
        """Gets the ep_f1_u of this ResourcesNrNrm.


        :return: The ep_f1_u of this ResourcesNrNrm.
        :rtype: List[EPF1USingle]
        """
        return self._ep_f1_u

    @ep_f1_u.setter
    def ep_f1_u(self, ep_f1_u):
        """Sets the ep_f1_u of this ResourcesNrNrm.


        :param ep_f1_u: The ep_f1_u of this ResourcesNrNrm.
        :type ep_f1_u: List[EPF1USingle]
        """

        self._ep_f1_u = ep_f1_u

    @property
    def operator_du(self):
        """Gets the operator_du of this ResourcesNrNrm.


        :return: The operator_du of this ResourcesNrNrm.
        :rtype: List[OperatorDuSingle]
        """
        return self._operator_du

    @operator_du.setter
    def operator_du(self, operator_du):
        """Sets the operator_du of this ResourcesNrNrm.


        :param operator_du: The operator_du of this ResourcesNrNrm.
        :type operator_du: List[OperatorDuSingle]
        """

        self._operator_du = operator_du

    @property
    def ep_e1(self):
        """Gets the ep_e1 of this ResourcesNrNrm.


        :return: The ep_e1 of this ResourcesNrNrm.
        :rtype: List[EPE1Single]
        """
        return self._ep_e1

    @ep_e1.setter
    def ep_e1(self, ep_e1):
        """Sets the ep_e1 of this ResourcesNrNrm.


        :param ep_e1: The ep_e1 of this ResourcesNrNrm.
        :type ep_e1: List[EPE1Single]
        """

        self._ep_e1 = ep_e1

    @property
    def ep_xn_u(self):
        """Gets the ep_xn_u of this ResourcesNrNrm.


        :return: The ep_xn_u of this ResourcesNrNrm.
        :rtype: List[EPXnUSingle]
        """
        return self._ep_xn_u

    @ep_xn_u.setter
    def ep_xn_u(self, ep_xn_u):
        """Sets the ep_xn_u of this ResourcesNrNrm.


        :param ep_xn_u: The ep_xn_u of this ResourcesNrNrm.
        :type ep_xn_u: List[EPXnUSingle]
        """

        self._ep_xn_u = ep_xn_u

    @property
    def ep_ng_u(self):
        """Gets the ep_ng_u of this ResourcesNrNrm.


        :return: The ep_ng_u of this ResourcesNrNrm.
        :rtype: List[EPNgUSingle]
        """
        return self._ep_ng_u

    @ep_ng_u.setter
    def ep_ng_u(self, ep_ng_u):
        """Sets the ep_ng_u of this ResourcesNrNrm.


        :param ep_ng_u: The ep_ng_u of this ResourcesNrNrm.
        :type ep_ng_u: List[EPNgUSingle]
        """

        self._ep_ng_u = ep_ng_u

    @property
    def ep_x2_u(self):
        """Gets the ep_x2_u of this ResourcesNrNrm.


        :return: The ep_x2_u of this ResourcesNrNrm.
        :rtype: List[EPX2USingle]
        """
        return self._ep_x2_u

    @ep_x2_u.setter
    def ep_x2_u(self, ep_x2_u):
        """Sets the ep_x2_u of this ResourcesNrNrm.


        :param ep_x2_u: The ep_x2_u of this ResourcesNrNrm.
        :type ep_x2_u: List[EPX2USingle]
        """

        self._ep_x2_u = ep_x2_u

    @property
    def ep_s1_u(self):
        """Gets the ep_s1_u of this ResourcesNrNrm.


        :return: The ep_s1_u of this ResourcesNrNrm.
        :rtype: List[EPS1USingle]
        """
        return self._ep_s1_u

    @ep_s1_u.setter
    def ep_s1_u(self, ep_s1_u):
        """Sets the ep_s1_u of this ResourcesNrNrm.


        :param ep_s1_u: The ep_s1_u of this ResourcesNrNrm.
        :type ep_s1_u: List[EPS1USingle]
        """

        self._ep_s1_u = ep_s1_u

    @property
    def nr_cell_cu(self):
        """Gets the nr_cell_cu of this ResourcesNrNrm.


        :return: The nr_cell_cu of this ResourcesNrNrm.
        :rtype: List[NrCellCuSingle]
        """
        return self._nr_cell_cu

    @nr_cell_cu.setter
    def nr_cell_cu(self, nr_cell_cu):
        """Sets the nr_cell_cu of this ResourcesNrNrm.


        :param nr_cell_cu: The nr_cell_cu of this ResourcesNrNrm.
        :type nr_cell_cu: List[NrCellCuSingle]
        """

        self._nr_cell_cu = nr_cell_cu

    @property
    def ep_xn_c(self):
        """Gets the ep_xn_c of this ResourcesNrNrm.


        :return: The ep_xn_c of this ResourcesNrNrm.
        :rtype: List[EPXnCSingle]
        """
        return self._ep_xn_c

    @ep_xn_c.setter
    def ep_xn_c(self, ep_xn_c):
        """Sets the ep_xn_c of this ResourcesNrNrm.


        :param ep_xn_c: The ep_xn_c of this ResourcesNrNrm.
        :type ep_xn_c: List[EPXnCSingle]
        """

        self._ep_xn_c = ep_xn_c

    @property
    def ep_ng_c(self):
        """Gets the ep_ng_c of this ResourcesNrNrm.


        :return: The ep_ng_c of this ResourcesNrNrm.
        :rtype: List[EPNgCSingle]
        """
        return self._ep_ng_c

    @ep_ng_c.setter
    def ep_ng_c(self, ep_ng_c):
        """Sets the ep_ng_c of this ResourcesNrNrm.


        :param ep_ng_c: The ep_ng_c of this ResourcesNrNrm.
        :type ep_ng_c: List[EPNgCSingle]
        """

        self._ep_ng_c = ep_ng_c

    @property
    def ep_x2_c(self):
        """Gets the ep_x2_c of this ResourcesNrNrm.


        :return: The ep_x2_c of this ResourcesNrNrm.
        :rtype: List[EPX2CSingle]
        """
        return self._ep_x2_c

    @ep_x2_c.setter
    def ep_x2_c(self, ep_x2_c):
        """Sets the ep_x2_c of this ResourcesNrNrm.


        :param ep_x2_c: The ep_x2_c of this ResourcesNrNrm.
        :type ep_x2_c: List[EPX2CSingle]
        """

        self._ep_x2_c = ep_x2_c

    @property
    def danr_management_function(self):
        """Gets the danr_management_function of this ResourcesNrNrm.


        :return: The danr_management_function of this ResourcesNrNrm.
        :rtype: DANRManagementFunctionSingle
        """
        return self._danr_management_function

    @danr_management_function.setter
    def danr_management_function(self, danr_management_function):
        """Sets the danr_management_function of this ResourcesNrNrm.


        :param danr_management_function: The danr_management_function of this ResourcesNrNrm.
        :type danr_management_function: DANRManagementFunctionSingle
        """

        self._danr_management_function = danr_management_function

    @property
    def gnb_id(self):
        """Gets the gnb_id of this ResourcesNrNrm.


        :return: The gnb_id of this ResourcesNrNrm.
        :rtype: str
        """
        return self._gnb_id

    @gnb_id.setter
    def gnb_id(self, gnb_id):
        """Sets the gnb_id of this ResourcesNrNrm.


        :param gnb_id: The gnb_id of this ResourcesNrNrm.
        :type gnb_id: str
        """

        self._gnb_id = gnb_id

    @property
    def gnb_id_length(self):
        """Gets the gnb_id_length of this ResourcesNrNrm.


        :return: The gnb_id_length of this ResourcesNrNrm.
        :rtype: int
        """
        return self._gnb_id_length

    @gnb_id_length.setter
    def gnb_id_length(self, gnb_id_length):
        """Sets the gnb_id_length of this ResourcesNrNrm.


        :param gnb_id_length: The gnb_id_length of this ResourcesNrNrm.
        :type gnb_id_length: int
        """
        if gnb_id_length is not None and gnb_id_length > 32:  # noqa: E501
            raise ValueError("Invalid value for `gnb_id_length`, must be a value less than or equal to `32`")  # noqa: E501
        if gnb_id_length is not None and gnb_id_length < 22:  # noqa: E501
            raise ValueError("Invalid value for `gnb_id_length`, must be a value greater than or equal to `22`")  # noqa: E501

        self._gnb_id_length = gnb_id_length

    @property
    def nr_cell_relation(self):
        """Gets the nr_cell_relation of this ResourcesNrNrm.


        :return: The nr_cell_relation of this ResourcesNrNrm.
        :rtype: List[NRCellRelationSingle]
        """
        return self._nr_cell_relation

    @nr_cell_relation.setter
    def nr_cell_relation(self, nr_cell_relation):
        """Sets the nr_cell_relation of this ResourcesNrNrm.


        :param nr_cell_relation: The nr_cell_relation of this ResourcesNrNrm.
        :type nr_cell_relation: List[NRCellRelationSingle]
        """

        self._nr_cell_relation = nr_cell_relation

    @property
    def e_utran_cell_relation(self):
        """Gets the e_utran_cell_relation of this ResourcesNrNrm.


        :return: The e_utran_cell_relation of this ResourcesNrNrm.
        :rtype: List[EUtranCellRelationSingle]
        """
        return self._e_utran_cell_relation

    @e_utran_cell_relation.setter
    def e_utran_cell_relation(self, e_utran_cell_relation):
        """Sets the e_utran_cell_relation of this ResourcesNrNrm.


        :param e_utran_cell_relation: The e_utran_cell_relation of this ResourcesNrNrm.
        :type e_utran_cell_relation: List[EUtranCellRelationSingle]
        """

        self._e_utran_cell_relation = e_utran_cell_relation

    @property
    def nr_freq_relation(self):
        """Gets the nr_freq_relation of this ResourcesNrNrm.


        :return: The nr_freq_relation of this ResourcesNrNrm.
        :rtype: List[NRFreqRelationSingle]
        """
        return self._nr_freq_relation

    @nr_freq_relation.setter
    def nr_freq_relation(self, nr_freq_relation):
        """Sets the nr_freq_relation of this ResourcesNrNrm.


        :param nr_freq_relation: The nr_freq_relation of this ResourcesNrNrm.
        :type nr_freq_relation: List[NRFreqRelationSingle]
        """

        self._nr_freq_relation = nr_freq_relation

    @property
    def e_utran_freq_relation(self):
        """Gets the e_utran_freq_relation of this ResourcesNrNrm.


        :return: The e_utran_freq_relation of this ResourcesNrNrm.
        :rtype: List[EUtranFreqRelationSingle]
        """
        return self._e_utran_freq_relation

    @e_utran_freq_relation.setter
    def e_utran_freq_relation(self, e_utran_freq_relation):
        """Sets the e_utran_freq_relation of this ResourcesNrNrm.


        :param e_utran_freq_relation: The e_utran_freq_relation of this ResourcesNrNrm.
        :type e_utran_freq_relation: List[EUtranFreqRelationSingle]
        """

        self._e_utran_freq_relation = e_utran_freq_relation

    @property
    def nr_operator_cell_du(self):
        """Gets the nr_operator_cell_du of this ResourcesNrNrm.


        :return: The nr_operator_cell_du of this ResourcesNrNrm.
        :rtype: List[NrOperatorCellDuSingle]
        """
        return self._nr_operator_cell_du

    @nr_operator_cell_du.setter
    def nr_operator_cell_du(self, nr_operator_cell_du):
        """Sets the nr_operator_cell_du of this ResourcesNrNrm.


        :param nr_operator_cell_du: The nr_operator_cell_du of this ResourcesNrNrm.
        :type nr_operator_cell_du: List[NrOperatorCellDuSingle]
        """

        self._nr_operator_cell_du = nr_operator_cell_du

    @property
    def cell_local_id(self):
        """Gets the cell_local_id of this ResourcesNrNrm.


        :return: The cell_local_id of this ResourcesNrNrm.
        :rtype: int
        """
        return self._cell_local_id

    @cell_local_id.setter
    def cell_local_id(self, cell_local_id):
        """Sets the cell_local_id of this ResourcesNrNrm.


        :param cell_local_id: The cell_local_id of this ResourcesNrNrm.
        :type cell_local_id: int
        """

        self._cell_local_id = cell_local_id

    @property
    def administrative_state(self):
        """Gets the administrative_state of this ResourcesNrNrm.


        :return: The administrative_state of this ResourcesNrNrm.
        :rtype: AdministrativeState
        """
        return self._administrative_state

    @administrative_state.setter
    def administrative_state(self, administrative_state):
        """Sets the administrative_state of this ResourcesNrNrm.


        :param administrative_state: The administrative_state of this ResourcesNrNrm.
        :type administrative_state: AdministrativeState
        """

        self._administrative_state = administrative_state

    @property
    def plmn_info_list(self):
        """Gets the plmn_info_list of this ResourcesNrNrm.


        :return: The plmn_info_list of this ResourcesNrNrm.
        :rtype: List[PlmnInfo]
        """
        return self._plmn_info_list

    @plmn_info_list.setter
    def plmn_info_list(self, plmn_info_list):
        """Sets the plmn_info_list of this ResourcesNrNrm.


        :param plmn_info_list: The plmn_info_list of this ResourcesNrNrm.
        :type plmn_info_list: List[PlmnInfo]
        """

        self._plmn_info_list = plmn_info_list

    @property
    def nr_tac(self):
        """Gets the nr_tac of this ResourcesNrNrm.


        :return: The nr_tac of this ResourcesNrNrm.
        :rtype: int
        """
        return self._nr_tac

    @nr_tac.setter
    def nr_tac(self, nr_tac):
        """Sets the nr_tac of this ResourcesNrNrm.


        :param nr_tac: The nr_tac of this ResourcesNrNrm.
        :type nr_tac: int
        """
        if nr_tac is not None and nr_tac > 16777215:  # noqa: E501
            raise ValueError("Invalid value for `nr_tac`, must be a value less than or equal to `16777215`")  # noqa: E501

        self._nr_tac = nr_tac

    @property
    def common_beamforming_function(self):
        """Gets the common_beamforming_function of this ResourcesNrNrm.


        :return: The common_beamforming_function of this ResourcesNrNrm.
        :rtype: CommonBeamformingFunctionSingle
        """
        return self._common_beamforming_function

    @common_beamforming_function.setter
    def common_beamforming_function(self, common_beamforming_function):
        """Sets the common_beamforming_function of this ResourcesNrNrm.


        :param common_beamforming_function: The common_beamforming_function of this ResourcesNrNrm.
        :type common_beamforming_function: CommonBeamformingFunctionSingle
        """

        self._common_beamforming_function = common_beamforming_function

    @property
    def beam(self):
        """Gets the beam of this ResourcesNrNrm.


        :return: The beam of this ResourcesNrNrm.
        :rtype: List[BeamSingle]
        """
        return self._beam

    @beam.setter
    def beam(self, beam):
        """Sets the beam of this ResourcesNrNrm.


        :param beam: The beam of this ResourcesNrNrm.
        :type beam: List[BeamSingle]
        """

        self._beam = beam

    @property
    def rim_rs_set(self):
        """Gets the rim_rs_set of this ResourcesNrNrm.


        :return: The rim_rs_set of this ResourcesNrNrm.
        :rtype: List[RimRSSetSingle]
        """
        return self._rim_rs_set

    @rim_rs_set.setter
    def rim_rs_set(self, rim_rs_set):
        """Sets the rim_rs_set of this ResourcesNrNrm.


        :param rim_rs_set: The rim_rs_set of this ResourcesNrNrm.
        :type rim_rs_set: List[RimRSSetSingle]
        """

        self._rim_rs_set = rim_rs_set

    @property
    def external_nr_cell_cu(self):
        """Gets the external_nr_cell_cu of this ResourcesNrNrm.


        :return: The external_nr_cell_cu of this ResourcesNrNrm.
        :rtype: List[ExternalNrCellCuSingle]
        """
        return self._external_nr_cell_cu

    @external_nr_cell_cu.setter
    def external_nr_cell_cu(self, external_nr_cell_cu):
        """Sets the external_nr_cell_cu of this ResourcesNrNrm.


        :param external_nr_cell_cu: The external_nr_cell_cu of this ResourcesNrNrm.
        :type external_nr_cell_cu: List[ExternalNrCellCuSingle]
        """

        self._external_nr_cell_cu = external_nr_cell_cu

    @property
    def external_eu_tran_cell(self):
        """Gets the external_eu_tran_cell of this ResourcesNrNrm.


        :return: The external_eu_tran_cell of this ResourcesNrNrm.
        :rtype: List[ExternalEUTranCellSingle]
        """
        return self._external_eu_tran_cell

    @external_eu_tran_cell.setter
    def external_eu_tran_cell(self, external_eu_tran_cell):
        """Sets the external_eu_tran_cell of this ResourcesNrNrm.


        :param external_eu_tran_cell: The external_eu_tran_cell of this ResourcesNrNrm.
        :type external_eu_tran_cell: List[ExternalEUTranCellSingle]
        """

        self._external_eu_tran_cell = external_eu_tran_cell
