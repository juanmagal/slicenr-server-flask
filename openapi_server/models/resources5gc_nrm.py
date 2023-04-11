# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.alarm_list_single import AlarmListSingle
from openapi_server.models.amf_function_single import AmfFunctionSingle
from openapi_server.models.amf_region_single import AmfRegionSingle
from openapi_server.models.amf_set_single import AmfSetSingle
from openapi_server.models.ausf_function_single import AusfFunctionSingle
from openapi_server.models.configurable5_qi_set_single import Configurable5QISetSingle
from openapi_server.models.ddnmf_function_single import DDNMFFunctionSingle
from openapi_server.models.dynamic5_qi_set_single import Dynamic5QISetSingle
from openapi_server.models.easdf_function_single import EASDFFunctionSingle
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
from openapi_server.models.ep_npc4_single import EPNpc4Single
from openapi_server.models.ep_npc6_single import EPNpc6Single
from openapi_server.models.ep_npc7_single import EPNpc7Single
from openapi_server.models.ep_npc8_single import EPNpc8Single
from openapi_server.models.eprx_single import EPRxSingle
from openapi_server.models.eps5_c_single import EPS5CSingle
from openapi_server.models.eps5_u_single import EPS5USingle
from openapi_server.models.ecm_connection_info_single import EcmConnectionInfoSingle
from openapi_server.models.ecm_connection_info_single_all_of_attributes import EcmConnectionInfoSingleAllOfAttributes
from openapi_server.models.external_amf_function_single import ExternalAmfFunctionSingle
from openapi_server.models.external_nrf_function_single import ExternalNrfFunctionSingle
from openapi_server.models.external_nssf_function_single import ExternalNssfFunctionSingle
from openapi_server.models.external_sepp_function_single import ExternalSeppFunctionSingle
from openapi_server.models.file_download_job_single import FileDownloadJobSingle
from openapi_server.models.files_single import FilesSingle
from openapi_server.models.five_qi_dscp_mapping_set_single import FiveQiDscpMappingSetSingle
from openapi_server.models.gtp_u_path_qo_s_monitoring_control_single import GtpUPathQoSMonitoringControlSingle
from openapi_server.models.lmf_function_single import LmfFunctionSingle
from openapi_server.models.managed_element_single import ManagedElementSingle
from openapi_server.models.managed_element_single1 import ManagedElementSingle1
from openapi_server.models.managed_nf_service_single import ManagedNFServiceSingle
from openapi_server.models.management_data_collection_single import ManagementDataCollectionSingle
from openapi_server.models.management_node_single import ManagementNodeSingle
from openapi_server.models.me_context_single import MeContextSingle
from openapi_server.models.mns_agent_single import MnsAgentSingle
from openapi_server.models.mns_registry_single import MnsRegistrySingle
from openapi_server.models.n3iwf_function_single import N3iwfFunctionSingle
from openapi_server.models.nef_function_single import NefFunctionSingle
from openapi_server.models.ngeir_function_single import NgeirFunctionSingle
from openapi_server.models.nrf_function_single import NrfFunctionSingle
from openapi_server.models.nsacf_function_single import NsacfFunctionSingle
from openapi_server.models.nssf_function_single import NssfFunctionSingle
from openapi_server.models.ntf_subscription_control_single import NtfSubscriptionControlSingle
from openapi_server.models.nwdaf_function_single import NwdafFunctionSingle
from openapi_server.models.pcf_function_single import PcfFunctionSingle
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle
from openapi_server.models.predefined_pcc_rule_set_single import PredefinedPccRuleSetSingle
from openapi_server.models.prov_mn_s import ProvMnS
from openapi_server.models.qfqo_s_monitoring_control_single import QFQoSMonitoringControlSingle
from openapi_server.models.scp_function_single import ScpFunctionSingle
from openapi_server.models.sepp_function_single import SeppFunctionSingle
from openapi_server.models.smf_function_single import SmfFunctionSingle
from openapi_server.models.smsf_function_single import SmsfFunctionSingle
from openapi_server.models.sub_network_single import SubNetworkSingle
from openapi_server.models.sub_network_single1 import SubNetworkSingle1
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
from openapi_server.models.amf_region_single import AmfRegionSingle  # noqa: E501
from openapi_server.models.amf_set_single import AmfSetSingle  # noqa: E501
from openapi_server.models.ausf_function_single import AusfFunctionSingle  # noqa: E501
from openapi_server.models.configurable5_qi_set_single import Configurable5QISetSingle  # noqa: E501
from openapi_server.models.ddnmf_function_single import DDNMFFunctionSingle  # noqa: E501
from openapi_server.models.dynamic5_qi_set_single import Dynamic5QISetSingle  # noqa: E501
from openapi_server.models.easdf_function_single import EASDFFunctionSingle  # noqa: E501
from openapi_server.models.ecm_connection_info_single import EcmConnectionInfoSingle  # noqa: E501
from openapi_server.models.ecm_connection_info_single_all_of_attributes import EcmConnectionInfoSingleAllOfAttributes  # noqa: E501
from openapi_server.models.ep_npc4_single import EPNpc4Single  # noqa: E501
from openapi_server.models.ep_npc6_single import EPNpc6Single  # noqa: E501
from openapi_server.models.ep_npc7_single import EPNpc7Single  # noqa: E501
from openapi_server.models.ep_npc8_single import EPNpc8Single  # noqa: E501
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
from openapi_server.models.epnlg_single import EPNLGSingle  # noqa: E501
from openapi_server.models.epnls_single import EPNLSSingle  # noqa: E501
from openapi_server.models.eprx_single import EPRxSingle  # noqa: E501
from openapi_server.models.eps5_c_single import EPS5CSingle  # noqa: E501
from openapi_server.models.eps5_u_single import EPS5USingle  # noqa: E501
from openapi_server.models.external_amf_function_single import ExternalAmfFunctionSingle  # noqa: E501
from openapi_server.models.external_nrf_function_single import ExternalNrfFunctionSingle  # noqa: E501
from openapi_server.models.external_nssf_function_single import ExternalNssfFunctionSingle  # noqa: E501
from openapi_server.models.external_sepp_function_single import ExternalSeppFunctionSingle  # noqa: E501
from openapi_server.models.file_download_job_single import FileDownloadJobSingle  # noqa: E501
from openapi_server.models.files_single import FilesSingle  # noqa: E501
from openapi_server.models.five_qi_dscp_mapping_set_single import FiveQiDscpMappingSetSingle  # noqa: E501
from openapi_server.models.gtp_u_path_qo_s_monitoring_control_single import GtpUPathQoSMonitoringControlSingle  # noqa: E501
from openapi_server.models.lmf_function_single import LmfFunctionSingle  # noqa: E501
from openapi_server.models.managed_element_single import ManagedElementSingle  # noqa: E501
from openapi_server.models.managed_element_single1 import ManagedElementSingle1  # noqa: E501
from openapi_server.models.managed_nf_service_single import ManagedNFServiceSingle  # noqa: E501
from openapi_server.models.management_data_collection_single import ManagementDataCollectionSingle  # noqa: E501
from openapi_server.models.management_node_single import ManagementNodeSingle  # noqa: E501
from openapi_server.models.me_context_single import MeContextSingle  # noqa: E501
from openapi_server.models.mns_agent_single import MnsAgentSingle  # noqa: E501
from openapi_server.models.mns_registry_single import MnsRegistrySingle  # noqa: E501
from openapi_server.models.n3iwf_function_single import N3iwfFunctionSingle  # noqa: E501
from openapi_server.models.nef_function_single import NefFunctionSingle  # noqa: E501
from openapi_server.models.ngeir_function_single import NgeirFunctionSingle  # noqa: E501
from openapi_server.models.nrf_function_single import NrfFunctionSingle  # noqa: E501
from openapi_server.models.nsacf_function_single import NsacfFunctionSingle  # noqa: E501
from openapi_server.models.nssf_function_single import NssfFunctionSingle  # noqa: E501
from openapi_server.models.ntf_subscription_control_single import NtfSubscriptionControlSingle  # noqa: E501
from openapi_server.models.nwdaf_function_single import NwdafFunctionSingle  # noqa: E501
from openapi_server.models.pcf_function_single import PcfFunctionSingle  # noqa: E501
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle  # noqa: E501
from openapi_server.models.predefined_pcc_rule_set_single import PredefinedPccRuleSetSingle  # noqa: E501
from openapi_server.models.prov_mn_s import ProvMnS  # noqa: E501
from openapi_server.models.qfqo_s_monitoring_control_single import QFQoSMonitoringControlSingle  # noqa: E501
from openapi_server.models.scp_function_single import ScpFunctionSingle  # noqa: E501
from openapi_server.models.sepp_function_single import SeppFunctionSingle  # noqa: E501
from openapi_server.models.smf_function_single import SmfFunctionSingle  # noqa: E501
from openapi_server.models.smsf_function_single import SmsfFunctionSingle  # noqa: E501
from openapi_server.models.sub_network_single import SubNetworkSingle  # noqa: E501
from openapi_server.models.sub_network_single1 import SubNetworkSingle1  # noqa: E501
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle  # noqa: E501
from openapi_server.models.trace_job_single import TraceJobSingle  # noqa: E501
from openapi_server.models.udm_function_single import UdmFunctionSingle  # noqa: E501
from openapi_server.models.udr_function_single import UdrFunctionSingle  # noqa: E501
from openapi_server.models.udsf_function_single import UdsfFunctionSingle  # noqa: E501
from openapi_server.models.upf_function_single import UpfFunctionSingle  # noqa: E501
from openapi_server.models.vs_data_container_single import VsDataContainerSingle  # noqa: E501

class Resources5gcNrm(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, sub_network=None, managed_element=None, id=None, object_class=None, object_instance=None, vs_data_container=None, attributes=None, management_node=None, mns_agent=None, me_context=None, perf_metric_job=None, threshold_monitor=None, trace_job=None, management_data_collection=None, ntf_subscription_control=None, alarm_list=None, file_download_job=None, files=None, mns_registry=None, external_amf_function=None, external_nrf_function=None, external_nssf_function=None, amf_set=None, amf_region=None, configurable5_qi_set=None, dynamic5_qi_set=None, ecm_connection_info=None, amf_function=None, smf_function=None, upf_function=None, n3iwf_function=None, pcf_function=None, ausf_function=None, udm_function=None, udr_function=None, udsf_function=None, nrf_function=None, nssf_function=None, smsf_function=None, lmf_function=None, ngeir_function=None, sepp_function=None, nwdaf_function=None, scp_function=None, nef_function=None, easdf_function=None, managed_nf_service=None, ep_n2=None, ep_n8=None, ep_n11=None, ep_n12=None, ep_n14=None, ep_n15=None, ep_n17=None, ep_n20=None, ep_n22=None, ep_n26=None, ep_nls=None, ep_nlg=None, ep_n4=None, ep_n7=None, ep_n10=None, ep_n16=None, ep_s5_c=None, five_qi_dscp_mapping_set=None, gtp_u_path_qo_s_monitoring_control=None, qfqo_s_monitoring_control=None, predefined_pcc_rule_set=None, ep_n3=None, ep_n6=None, ep_n9=None, ep_s5_u=None, ep_n5=None, ep_rx=None, ep_n13=None, ep_n27=None, ep_n31=None, ep_n21=None, ep_map_smsc=None, ep_n32=None, ep_n33=None, ep_n60=None, ep_npc4=None, ep_npc6=None, ep_npc7=None, ep_npc8=None, ep_n88=None):  # noqa: E501
        """Resources5gcNrm - a model defined in OpenAPI

        :param sub_network: The sub_network of this Resources5gcNrm.  # noqa: E501
        :type sub_network: List[SubNetworkSingle]
        :param managed_element: The managed_element of this Resources5gcNrm.  # noqa: E501
        :type managed_element: List[ManagedElementSingle]
        :param id: The id of this Resources5gcNrm.  # noqa: E501
        :type id: str
        :param object_class: The object_class of this Resources5gcNrm.  # noqa: E501
        :type object_class: str
        :param object_instance: The object_instance of this Resources5gcNrm.  # noqa: E501
        :type object_instance: str
        :param vs_data_container: The vs_data_container of this Resources5gcNrm.  # noqa: E501
        :type vs_data_container: List[VsDataContainerSingle]
        :param attributes: The attributes of this Resources5gcNrm.  # noqa: E501
        :type attributes: EcmConnectionInfoSingleAllOfAttributes
        :param management_node: The management_node of this Resources5gcNrm.  # noqa: E501
        :type management_node: List[ManagementNodeSingle]
        :param mns_agent: The mns_agent of this Resources5gcNrm.  # noqa: E501
        :type mns_agent: List[MnsAgentSingle]
        :param me_context: The me_context of this Resources5gcNrm.  # noqa: E501
        :type me_context: List[MeContextSingle]
        :param perf_metric_job: The perf_metric_job of this Resources5gcNrm.  # noqa: E501
        :type perf_metric_job: List[PerfMetricJobSingle]
        :param threshold_monitor: The threshold_monitor of this Resources5gcNrm.  # noqa: E501
        :type threshold_monitor: List[ThresholdMonitorSingle]
        :param trace_job: The trace_job of this Resources5gcNrm.  # noqa: E501
        :type trace_job: List[TraceJobSingle]
        :param management_data_collection: The management_data_collection of this Resources5gcNrm.  # noqa: E501
        :type management_data_collection: List[ManagementDataCollectionSingle]
        :param ntf_subscription_control: The ntf_subscription_control of this Resources5gcNrm.  # noqa: E501
        :type ntf_subscription_control: List[NtfSubscriptionControlSingle]
        :param alarm_list: The alarm_list of this Resources5gcNrm.  # noqa: E501
        :type alarm_list: AlarmListSingle
        :param file_download_job: The file_download_job of this Resources5gcNrm.  # noqa: E501
        :type file_download_job: List[FileDownloadJobSingle]
        :param files: The files of this Resources5gcNrm.  # noqa: E501
        :type files: List[FilesSingle]
        :param mns_registry: The mns_registry of this Resources5gcNrm.  # noqa: E501
        :type mns_registry: MnsRegistrySingle
        :param external_amf_function: The external_amf_function of this Resources5gcNrm.  # noqa: E501
        :type external_amf_function: List[ExternalAmfFunctionSingle]
        :param external_nrf_function: The external_nrf_function of this Resources5gcNrm.  # noqa: E501
        :type external_nrf_function: List[ExternalNrfFunctionSingle]
        :param external_nssf_function: The external_nssf_function of this Resources5gcNrm.  # noqa: E501
        :type external_nssf_function: List[ExternalNssfFunctionSingle]
        :param amf_set: The amf_set of this Resources5gcNrm.  # noqa: E501
        :type amf_set: List[AmfSetSingle]
        :param amf_region: The amf_region of this Resources5gcNrm.  # noqa: E501
        :type amf_region: List[AmfRegionSingle]
        :param configurable5_qi_set: The configurable5_qi_set of this Resources5gcNrm.  # noqa: E501
        :type configurable5_qi_set: List[Configurable5QISetSingle]
        :param dynamic5_qi_set: The dynamic5_qi_set of this Resources5gcNrm.  # noqa: E501
        :type dynamic5_qi_set: List[Dynamic5QISetSingle]
        :param ecm_connection_info: The ecm_connection_info of this Resources5gcNrm.  # noqa: E501
        :type ecm_connection_info: List[EcmConnectionInfoSingle]
        :param amf_function: The amf_function of this Resources5gcNrm.  # noqa: E501
        :type amf_function: List[AmfFunctionSingle]
        :param smf_function: The smf_function of this Resources5gcNrm.  # noqa: E501
        :type smf_function: List[SmfFunctionSingle]
        :param upf_function: The upf_function of this Resources5gcNrm.  # noqa: E501
        :type upf_function: List[UpfFunctionSingle]
        :param n3iwf_function: The n3iwf_function of this Resources5gcNrm.  # noqa: E501
        :type n3iwf_function: List[N3iwfFunctionSingle]
        :param pcf_function: The pcf_function of this Resources5gcNrm.  # noqa: E501
        :type pcf_function: List[PcfFunctionSingle]
        :param ausf_function: The ausf_function of this Resources5gcNrm.  # noqa: E501
        :type ausf_function: List[AusfFunctionSingle]
        :param udm_function: The udm_function of this Resources5gcNrm.  # noqa: E501
        :type udm_function: List[UdmFunctionSingle]
        :param udr_function: The udr_function of this Resources5gcNrm.  # noqa: E501
        :type udr_function: List[UdrFunctionSingle]
        :param udsf_function: The udsf_function of this Resources5gcNrm.  # noqa: E501
        :type udsf_function: List[UdsfFunctionSingle]
        :param nrf_function: The nrf_function of this Resources5gcNrm.  # noqa: E501
        :type nrf_function: List[NrfFunctionSingle]
        :param nssf_function: The nssf_function of this Resources5gcNrm.  # noqa: E501
        :type nssf_function: List[NssfFunctionSingle]
        :param smsf_function: The smsf_function of this Resources5gcNrm.  # noqa: E501
        :type smsf_function: List[SmsfFunctionSingle]
        :param lmf_function: The lmf_function of this Resources5gcNrm.  # noqa: E501
        :type lmf_function: List[LmfFunctionSingle]
        :param ngeir_function: The ngeir_function of this Resources5gcNrm.  # noqa: E501
        :type ngeir_function: List[NgeirFunctionSingle]
        :param sepp_function: The sepp_function of this Resources5gcNrm.  # noqa: E501
        :type sepp_function: List[SeppFunctionSingle]
        :param nwdaf_function: The nwdaf_function of this Resources5gcNrm.  # noqa: E501
        :type nwdaf_function: List[NwdafFunctionSingle]
        :param scp_function: The scp_function of this Resources5gcNrm.  # noqa: E501
        :type scp_function: List[ScpFunctionSingle]
        :param nef_function: The nef_function of this Resources5gcNrm.  # noqa: E501
        :type nef_function: List[NefFunctionSingle]
        :param easdf_function: The easdf_function of this Resources5gcNrm.  # noqa: E501
        :type easdf_function: List[EASDFFunctionSingle]
        :param managed_nf_service: The managed_nf_service of this Resources5gcNrm.  # noqa: E501
        :type managed_nf_service: List[ManagedNFServiceSingle]
        :param ep_n2: The ep_n2 of this Resources5gcNrm.  # noqa: E501
        :type ep_n2: List[EPN2Single]
        :param ep_n8: The ep_n8 of this Resources5gcNrm.  # noqa: E501
        :type ep_n8: List[EPN8Single]
        :param ep_n11: The ep_n11 of this Resources5gcNrm.  # noqa: E501
        :type ep_n11: List[EPN11Single]
        :param ep_n12: The ep_n12 of this Resources5gcNrm.  # noqa: E501
        :type ep_n12: List[EPN12Single]
        :param ep_n14: The ep_n14 of this Resources5gcNrm.  # noqa: E501
        :type ep_n14: List[EPN14Single]
        :param ep_n15: The ep_n15 of this Resources5gcNrm.  # noqa: E501
        :type ep_n15: List[EPN15Single]
        :param ep_n17: The ep_n17 of this Resources5gcNrm.  # noqa: E501
        :type ep_n17: List[EPN17Single]
        :param ep_n20: The ep_n20 of this Resources5gcNrm.  # noqa: E501
        :type ep_n20: List[EPN20Single]
        :param ep_n22: The ep_n22 of this Resources5gcNrm.  # noqa: E501
        :type ep_n22: List[EPN22Single]
        :param ep_n26: The ep_n26 of this Resources5gcNrm.  # noqa: E501
        :type ep_n26: List[EPN26Single]
        :param ep_nls: The ep_nls of this Resources5gcNrm.  # noqa: E501
        :type ep_nls: List[EPNLSSingle]
        :param ep_nlg: The ep_nlg of this Resources5gcNrm.  # noqa: E501
        :type ep_nlg: List[EPNLGSingle]
        :param ep_n4: The ep_n4 of this Resources5gcNrm.  # noqa: E501
        :type ep_n4: List[EPN4Single]
        :param ep_n7: The ep_n7 of this Resources5gcNrm.  # noqa: E501
        :type ep_n7: List[EPN7Single]
        :param ep_n10: The ep_n10 of this Resources5gcNrm.  # noqa: E501
        :type ep_n10: List[EPN10Single]
        :param ep_n16: The ep_n16 of this Resources5gcNrm.  # noqa: E501
        :type ep_n16: List[EPN16Single]
        :param ep_s5_c: The ep_s5_c of this Resources5gcNrm.  # noqa: E501
        :type ep_s5_c: List[EPS5CSingle]
        :param five_qi_dscp_mapping_set: The five_qi_dscp_mapping_set of this Resources5gcNrm.  # noqa: E501
        :type five_qi_dscp_mapping_set: FiveQiDscpMappingSetSingle
        :param gtp_u_path_qo_s_monitoring_control: The gtp_u_path_qo_s_monitoring_control of this Resources5gcNrm.  # noqa: E501
        :type gtp_u_path_qo_s_monitoring_control: GtpUPathQoSMonitoringControlSingle
        :param qfqo_s_monitoring_control: The qfqo_s_monitoring_control of this Resources5gcNrm.  # noqa: E501
        :type qfqo_s_monitoring_control: QFQoSMonitoringControlSingle
        :param predefined_pcc_rule_set: The predefined_pcc_rule_set of this Resources5gcNrm.  # noqa: E501
        :type predefined_pcc_rule_set: PredefinedPccRuleSetSingle
        :param ep_n3: The ep_n3 of this Resources5gcNrm.  # noqa: E501
        :type ep_n3: List[EPN3Single]
        :param ep_n6: The ep_n6 of this Resources5gcNrm.  # noqa: E501
        :type ep_n6: List[EPN6Single]
        :param ep_n9: The ep_n9 of this Resources5gcNrm.  # noqa: E501
        :type ep_n9: List[EPN9Single]
        :param ep_s5_u: The ep_s5_u of this Resources5gcNrm.  # noqa: E501
        :type ep_s5_u: List[EPS5USingle]
        :param ep_n5: The ep_n5 of this Resources5gcNrm.  # noqa: E501
        :type ep_n5: List[EPN5Single]
        :param ep_rx: The ep_rx of this Resources5gcNrm.  # noqa: E501
        :type ep_rx: List[EPRxSingle]
        :param ep_n13: The ep_n13 of this Resources5gcNrm.  # noqa: E501
        :type ep_n13: List[EPN13Single]
        :param ep_n27: The ep_n27 of this Resources5gcNrm.  # noqa: E501
        :type ep_n27: List[EPN27Single]
        :param ep_n31: The ep_n31 of this Resources5gcNrm.  # noqa: E501
        :type ep_n31: List[EPN31Single]
        :param ep_n21: The ep_n21 of this Resources5gcNrm.  # noqa: E501
        :type ep_n21: List[EPN21Single]
        :param ep_map_smsc: The ep_map_smsc of this Resources5gcNrm.  # noqa: E501
        :type ep_map_smsc: List[EPMAPSMSCSingle]
        :param ep_n32: The ep_n32 of this Resources5gcNrm.  # noqa: E501
        :type ep_n32: List[EPN32Single]
        :param ep_n33: The ep_n33 of this Resources5gcNrm.  # noqa: E501
        :type ep_n33: List[EPN33Single]
        :param ep_n60: The ep_n60 of this Resources5gcNrm.  # noqa: E501
        :type ep_n60: List[EPN60Single]
        :param ep_npc4: The ep_npc4 of this Resources5gcNrm.  # noqa: E501
        :type ep_npc4: List[EPNpc4Single]
        :param ep_npc6: The ep_npc6 of this Resources5gcNrm.  # noqa: E501
        :type ep_npc6: List[EPNpc6Single]
        :param ep_npc7: The ep_npc7 of this Resources5gcNrm.  # noqa: E501
        :type ep_npc7: List[EPNpc7Single]
        :param ep_npc8: The ep_npc8 of this Resources5gcNrm.  # noqa: E501
        :type ep_npc8: List[EPNpc8Single]
        :param ep_n88: The ep_n88 of this Resources5gcNrm.  # noqa: E501
        :type ep_n88: List[EPN88Single]
        """
        self.openapi_types = {
            'sub_network': List[SubNetworkSingle],
            'managed_element': List[ManagedElementSingle],
            'id': str,
            'object_class': str,
            'object_instance': str,
            'vs_data_container': List[VsDataContainerSingle],
            'attributes': EcmConnectionInfoSingleAllOfAttributes,
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
            'external_amf_function': List[ExternalAmfFunctionSingle],
            'external_nrf_function': List[ExternalNrfFunctionSingle],
            'external_nssf_function': List[ExternalNssfFunctionSingle],
            'amf_set': List[AmfSetSingle],
            'amf_region': List[AmfRegionSingle],
            'configurable5_qi_set': List[Configurable5QISetSingle],
            'dynamic5_qi_set': List[Dynamic5QISetSingle],
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
            'managed_nf_service': List[ManagedNFServiceSingle],
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
            'ep_n88': List[EPN88Single]
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
            'external_amf_function': 'ExternalAmfFunction',
            'external_nrf_function': 'ExternalNrfFunction',
            'external_nssf_function': 'ExternalNssfFunction',
            'amf_set': 'AmfSet',
            'amf_region': 'AmfRegion',
            'configurable5_qi_set': 'Configurable5QISet',
            'dynamic5_qi_set': 'Dynamic5QISet',
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
            'managed_nf_service': 'ManagedNFService',
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
            'ep_n88': 'EP_N88'
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
        self._external_amf_function = external_amf_function
        self._external_nrf_function = external_nrf_function
        self._external_nssf_function = external_nssf_function
        self._amf_set = amf_set
        self._amf_region = amf_region
        self._configurable5_qi_set = configurable5_qi_set
        self._dynamic5_qi_set = dynamic5_qi_set
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
        self._managed_nf_service = managed_nf_service
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

    @classmethod
    def from_dict(cls, dikt) -> 'Resources5gcNrm':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The resources-5gcNrm of this Resources5gcNrm.  # noqa: E501
        :rtype: Resources5gcNrm
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sub_network(self):
        """Gets the sub_network of this Resources5gcNrm.


        :return: The sub_network of this Resources5gcNrm.
        :rtype: List[SubNetworkSingle]
        """
        return self._sub_network

    @sub_network.setter
    def sub_network(self, sub_network):
        """Sets the sub_network of this Resources5gcNrm.


        :param sub_network: The sub_network of this Resources5gcNrm.
        :type sub_network: List[SubNetworkSingle]
        """

        self._sub_network = sub_network

    @property
    def managed_element(self):
        """Gets the managed_element of this Resources5gcNrm.


        :return: The managed_element of this Resources5gcNrm.
        :rtype: List[ManagedElementSingle]
        """
        return self._managed_element

    @managed_element.setter
    def managed_element(self, managed_element):
        """Sets the managed_element of this Resources5gcNrm.


        :param managed_element: The managed_element of this Resources5gcNrm.
        :type managed_element: List[ManagedElementSingle]
        """

        self._managed_element = managed_element

    @property
    def id(self):
        """Gets the id of this Resources5gcNrm.


        :return: The id of this Resources5gcNrm.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Resources5gcNrm.


        :param id: The id of this Resources5gcNrm.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def object_class(self):
        """Gets the object_class of this Resources5gcNrm.


        :return: The object_class of this Resources5gcNrm.
        :rtype: str
        """
        return self._object_class

    @object_class.setter
    def object_class(self, object_class):
        """Sets the object_class of this Resources5gcNrm.


        :param object_class: The object_class of this Resources5gcNrm.
        :type object_class: str
        """

        self._object_class = object_class

    @property
    def object_instance(self):
        """Gets the object_instance of this Resources5gcNrm.


        :return: The object_instance of this Resources5gcNrm.
        :rtype: str
        """
        return self._object_instance

    @object_instance.setter
    def object_instance(self, object_instance):
        """Sets the object_instance of this Resources5gcNrm.


        :param object_instance: The object_instance of this Resources5gcNrm.
        :type object_instance: str
        """

        self._object_instance = object_instance

    @property
    def vs_data_container(self):
        """Gets the vs_data_container of this Resources5gcNrm.


        :return: The vs_data_container of this Resources5gcNrm.
        :rtype: List[VsDataContainerSingle]
        """
        return self._vs_data_container

    @vs_data_container.setter
    def vs_data_container(self, vs_data_container):
        """Sets the vs_data_container of this Resources5gcNrm.


        :param vs_data_container: The vs_data_container of this Resources5gcNrm.
        :type vs_data_container: List[VsDataContainerSingle]
        """

        self._vs_data_container = vs_data_container

    @property
    def attributes(self):
        """Gets the attributes of this Resources5gcNrm.


        :return: The attributes of this Resources5gcNrm.
        :rtype: EcmConnectionInfoSingleAllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Resources5gcNrm.


        :param attributes: The attributes of this Resources5gcNrm.
        :type attributes: EcmConnectionInfoSingleAllOfAttributes
        """

        self._attributes = attributes

    @property
    def management_node(self):
        """Gets the management_node of this Resources5gcNrm.


        :return: The management_node of this Resources5gcNrm.
        :rtype: List[ManagementNodeSingle]
        """
        return self._management_node

    @management_node.setter
    def management_node(self, management_node):
        """Sets the management_node of this Resources5gcNrm.


        :param management_node: The management_node of this Resources5gcNrm.
        :type management_node: List[ManagementNodeSingle]
        """

        self._management_node = management_node

    @property
    def mns_agent(self):
        """Gets the mns_agent of this Resources5gcNrm.


        :return: The mns_agent of this Resources5gcNrm.
        :rtype: List[MnsAgentSingle]
        """
        return self._mns_agent

    @mns_agent.setter
    def mns_agent(self, mns_agent):
        """Sets the mns_agent of this Resources5gcNrm.


        :param mns_agent: The mns_agent of this Resources5gcNrm.
        :type mns_agent: List[MnsAgentSingle]
        """

        self._mns_agent = mns_agent

    @property
    def me_context(self):
        """Gets the me_context of this Resources5gcNrm.


        :return: The me_context of this Resources5gcNrm.
        :rtype: List[MeContextSingle]
        """
        return self._me_context

    @me_context.setter
    def me_context(self, me_context):
        """Sets the me_context of this Resources5gcNrm.


        :param me_context: The me_context of this Resources5gcNrm.
        :type me_context: List[MeContextSingle]
        """

        self._me_context = me_context

    @property
    def perf_metric_job(self):
        """Gets the perf_metric_job of this Resources5gcNrm.


        :return: The perf_metric_job of this Resources5gcNrm.
        :rtype: List[PerfMetricJobSingle]
        """
        return self._perf_metric_job

    @perf_metric_job.setter
    def perf_metric_job(self, perf_metric_job):
        """Sets the perf_metric_job of this Resources5gcNrm.


        :param perf_metric_job: The perf_metric_job of this Resources5gcNrm.
        :type perf_metric_job: List[PerfMetricJobSingle]
        """

        self._perf_metric_job = perf_metric_job

    @property
    def threshold_monitor(self):
        """Gets the threshold_monitor of this Resources5gcNrm.


        :return: The threshold_monitor of this Resources5gcNrm.
        :rtype: List[ThresholdMonitorSingle]
        """
        return self._threshold_monitor

    @threshold_monitor.setter
    def threshold_monitor(self, threshold_monitor):
        """Sets the threshold_monitor of this Resources5gcNrm.


        :param threshold_monitor: The threshold_monitor of this Resources5gcNrm.
        :type threshold_monitor: List[ThresholdMonitorSingle]
        """

        self._threshold_monitor = threshold_monitor

    @property
    def trace_job(self):
        """Gets the trace_job of this Resources5gcNrm.


        :return: The trace_job of this Resources5gcNrm.
        :rtype: List[TraceJobSingle]
        """
        return self._trace_job

    @trace_job.setter
    def trace_job(self, trace_job):
        """Sets the trace_job of this Resources5gcNrm.


        :param trace_job: The trace_job of this Resources5gcNrm.
        :type trace_job: List[TraceJobSingle]
        """

        self._trace_job = trace_job

    @property
    def management_data_collection(self):
        """Gets the management_data_collection of this Resources5gcNrm.


        :return: The management_data_collection of this Resources5gcNrm.
        :rtype: List[ManagementDataCollectionSingle]
        """
        return self._management_data_collection

    @management_data_collection.setter
    def management_data_collection(self, management_data_collection):
        """Sets the management_data_collection of this Resources5gcNrm.


        :param management_data_collection: The management_data_collection of this Resources5gcNrm.
        :type management_data_collection: List[ManagementDataCollectionSingle]
        """

        self._management_data_collection = management_data_collection

    @property
    def ntf_subscription_control(self):
        """Gets the ntf_subscription_control of this Resources5gcNrm.


        :return: The ntf_subscription_control of this Resources5gcNrm.
        :rtype: List[NtfSubscriptionControlSingle]
        """
        return self._ntf_subscription_control

    @ntf_subscription_control.setter
    def ntf_subscription_control(self, ntf_subscription_control):
        """Sets the ntf_subscription_control of this Resources5gcNrm.


        :param ntf_subscription_control: The ntf_subscription_control of this Resources5gcNrm.
        :type ntf_subscription_control: List[NtfSubscriptionControlSingle]
        """

        self._ntf_subscription_control = ntf_subscription_control

    @property
    def alarm_list(self):
        """Gets the alarm_list of this Resources5gcNrm.


        :return: The alarm_list of this Resources5gcNrm.
        :rtype: AlarmListSingle
        """
        return self._alarm_list

    @alarm_list.setter
    def alarm_list(self, alarm_list):
        """Sets the alarm_list of this Resources5gcNrm.


        :param alarm_list: The alarm_list of this Resources5gcNrm.
        :type alarm_list: AlarmListSingle
        """

        self._alarm_list = alarm_list

    @property
    def file_download_job(self):
        """Gets the file_download_job of this Resources5gcNrm.


        :return: The file_download_job of this Resources5gcNrm.
        :rtype: List[FileDownloadJobSingle]
        """
        return self._file_download_job

    @file_download_job.setter
    def file_download_job(self, file_download_job):
        """Sets the file_download_job of this Resources5gcNrm.


        :param file_download_job: The file_download_job of this Resources5gcNrm.
        :type file_download_job: List[FileDownloadJobSingle]
        """

        self._file_download_job = file_download_job

    @property
    def files(self):
        """Gets the files of this Resources5gcNrm.


        :return: The files of this Resources5gcNrm.
        :rtype: List[FilesSingle]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this Resources5gcNrm.


        :param files: The files of this Resources5gcNrm.
        :type files: List[FilesSingle]
        """

        self._files = files

    @property
    def mns_registry(self):
        """Gets the mns_registry of this Resources5gcNrm.


        :return: The mns_registry of this Resources5gcNrm.
        :rtype: MnsRegistrySingle
        """
        return self._mns_registry

    @mns_registry.setter
    def mns_registry(self, mns_registry):
        """Sets the mns_registry of this Resources5gcNrm.


        :param mns_registry: The mns_registry of this Resources5gcNrm.
        :type mns_registry: MnsRegistrySingle
        """

        self._mns_registry = mns_registry

    @property
    def external_amf_function(self):
        """Gets the external_amf_function of this Resources5gcNrm.


        :return: The external_amf_function of this Resources5gcNrm.
        :rtype: List[ExternalAmfFunctionSingle]
        """
        return self._external_amf_function

    @external_amf_function.setter
    def external_amf_function(self, external_amf_function):
        """Sets the external_amf_function of this Resources5gcNrm.


        :param external_amf_function: The external_amf_function of this Resources5gcNrm.
        :type external_amf_function: List[ExternalAmfFunctionSingle]
        """

        self._external_amf_function = external_amf_function

    @property
    def external_nrf_function(self):
        """Gets the external_nrf_function of this Resources5gcNrm.


        :return: The external_nrf_function of this Resources5gcNrm.
        :rtype: List[ExternalNrfFunctionSingle]
        """
        return self._external_nrf_function

    @external_nrf_function.setter
    def external_nrf_function(self, external_nrf_function):
        """Sets the external_nrf_function of this Resources5gcNrm.


        :param external_nrf_function: The external_nrf_function of this Resources5gcNrm.
        :type external_nrf_function: List[ExternalNrfFunctionSingle]
        """

        self._external_nrf_function = external_nrf_function

    @property
    def external_nssf_function(self):
        """Gets the external_nssf_function of this Resources5gcNrm.


        :return: The external_nssf_function of this Resources5gcNrm.
        :rtype: List[ExternalNssfFunctionSingle]
        """
        return self._external_nssf_function

    @external_nssf_function.setter
    def external_nssf_function(self, external_nssf_function):
        """Sets the external_nssf_function of this Resources5gcNrm.


        :param external_nssf_function: The external_nssf_function of this Resources5gcNrm.
        :type external_nssf_function: List[ExternalNssfFunctionSingle]
        """

        self._external_nssf_function = external_nssf_function

    @property
    def amf_set(self):
        """Gets the amf_set of this Resources5gcNrm.


        :return: The amf_set of this Resources5gcNrm.
        :rtype: List[AmfSetSingle]
        """
        return self._amf_set

    @amf_set.setter
    def amf_set(self, amf_set):
        """Sets the amf_set of this Resources5gcNrm.


        :param amf_set: The amf_set of this Resources5gcNrm.
        :type amf_set: List[AmfSetSingle]
        """

        self._amf_set = amf_set

    @property
    def amf_region(self):
        """Gets the amf_region of this Resources5gcNrm.


        :return: The amf_region of this Resources5gcNrm.
        :rtype: List[AmfRegionSingle]
        """
        return self._amf_region

    @amf_region.setter
    def amf_region(self, amf_region):
        """Sets the amf_region of this Resources5gcNrm.


        :param amf_region: The amf_region of this Resources5gcNrm.
        :type amf_region: List[AmfRegionSingle]
        """

        self._amf_region = amf_region

    @property
    def configurable5_qi_set(self):
        """Gets the configurable5_qi_set of this Resources5gcNrm.


        :return: The configurable5_qi_set of this Resources5gcNrm.
        :rtype: List[Configurable5QISetSingle]
        """
        return self._configurable5_qi_set

    @configurable5_qi_set.setter
    def configurable5_qi_set(self, configurable5_qi_set):
        """Sets the configurable5_qi_set of this Resources5gcNrm.


        :param configurable5_qi_set: The configurable5_qi_set of this Resources5gcNrm.
        :type configurable5_qi_set: List[Configurable5QISetSingle]
        """

        self._configurable5_qi_set = configurable5_qi_set

    @property
    def dynamic5_qi_set(self):
        """Gets the dynamic5_qi_set of this Resources5gcNrm.


        :return: The dynamic5_qi_set of this Resources5gcNrm.
        :rtype: List[Dynamic5QISetSingle]
        """
        return self._dynamic5_qi_set

    @dynamic5_qi_set.setter
    def dynamic5_qi_set(self, dynamic5_qi_set):
        """Sets the dynamic5_qi_set of this Resources5gcNrm.


        :param dynamic5_qi_set: The dynamic5_qi_set of this Resources5gcNrm.
        :type dynamic5_qi_set: List[Dynamic5QISetSingle]
        """

        self._dynamic5_qi_set = dynamic5_qi_set

    @property
    def ecm_connection_info(self):
        """Gets the ecm_connection_info of this Resources5gcNrm.


        :return: The ecm_connection_info of this Resources5gcNrm.
        :rtype: List[EcmConnectionInfoSingle]
        """
        return self._ecm_connection_info

    @ecm_connection_info.setter
    def ecm_connection_info(self, ecm_connection_info):
        """Sets the ecm_connection_info of this Resources5gcNrm.


        :param ecm_connection_info: The ecm_connection_info of this Resources5gcNrm.
        :type ecm_connection_info: List[EcmConnectionInfoSingle]
        """

        self._ecm_connection_info = ecm_connection_info

    @property
    def amf_function(self):
        """Gets the amf_function of this Resources5gcNrm.


        :return: The amf_function of this Resources5gcNrm.
        :rtype: List[AmfFunctionSingle]
        """
        return self._amf_function

    @amf_function.setter
    def amf_function(self, amf_function):
        """Sets the amf_function of this Resources5gcNrm.


        :param amf_function: The amf_function of this Resources5gcNrm.
        :type amf_function: List[AmfFunctionSingle]
        """

        self._amf_function = amf_function

    @property
    def smf_function(self):
        """Gets the smf_function of this Resources5gcNrm.


        :return: The smf_function of this Resources5gcNrm.
        :rtype: List[SmfFunctionSingle]
        """
        return self._smf_function

    @smf_function.setter
    def smf_function(self, smf_function):
        """Sets the smf_function of this Resources5gcNrm.


        :param smf_function: The smf_function of this Resources5gcNrm.
        :type smf_function: List[SmfFunctionSingle]
        """

        self._smf_function = smf_function

    @property
    def upf_function(self):
        """Gets the upf_function of this Resources5gcNrm.


        :return: The upf_function of this Resources5gcNrm.
        :rtype: List[UpfFunctionSingle]
        """
        return self._upf_function

    @upf_function.setter
    def upf_function(self, upf_function):
        """Sets the upf_function of this Resources5gcNrm.


        :param upf_function: The upf_function of this Resources5gcNrm.
        :type upf_function: List[UpfFunctionSingle]
        """

        self._upf_function = upf_function

    @property
    def n3iwf_function(self):
        """Gets the n3iwf_function of this Resources5gcNrm.


        :return: The n3iwf_function of this Resources5gcNrm.
        :rtype: List[N3iwfFunctionSingle]
        """
        return self._n3iwf_function

    @n3iwf_function.setter
    def n3iwf_function(self, n3iwf_function):
        """Sets the n3iwf_function of this Resources5gcNrm.


        :param n3iwf_function: The n3iwf_function of this Resources5gcNrm.
        :type n3iwf_function: List[N3iwfFunctionSingle]
        """

        self._n3iwf_function = n3iwf_function

    @property
    def pcf_function(self):
        """Gets the pcf_function of this Resources5gcNrm.


        :return: The pcf_function of this Resources5gcNrm.
        :rtype: List[PcfFunctionSingle]
        """
        return self._pcf_function

    @pcf_function.setter
    def pcf_function(self, pcf_function):
        """Sets the pcf_function of this Resources5gcNrm.


        :param pcf_function: The pcf_function of this Resources5gcNrm.
        :type pcf_function: List[PcfFunctionSingle]
        """

        self._pcf_function = pcf_function

    @property
    def ausf_function(self):
        """Gets the ausf_function of this Resources5gcNrm.


        :return: The ausf_function of this Resources5gcNrm.
        :rtype: List[AusfFunctionSingle]
        """
        return self._ausf_function

    @ausf_function.setter
    def ausf_function(self, ausf_function):
        """Sets the ausf_function of this Resources5gcNrm.


        :param ausf_function: The ausf_function of this Resources5gcNrm.
        :type ausf_function: List[AusfFunctionSingle]
        """

        self._ausf_function = ausf_function

    @property
    def udm_function(self):
        """Gets the udm_function of this Resources5gcNrm.


        :return: The udm_function of this Resources5gcNrm.
        :rtype: List[UdmFunctionSingle]
        """
        return self._udm_function

    @udm_function.setter
    def udm_function(self, udm_function):
        """Sets the udm_function of this Resources5gcNrm.


        :param udm_function: The udm_function of this Resources5gcNrm.
        :type udm_function: List[UdmFunctionSingle]
        """

        self._udm_function = udm_function

    @property
    def udr_function(self):
        """Gets the udr_function of this Resources5gcNrm.


        :return: The udr_function of this Resources5gcNrm.
        :rtype: List[UdrFunctionSingle]
        """
        return self._udr_function

    @udr_function.setter
    def udr_function(self, udr_function):
        """Sets the udr_function of this Resources5gcNrm.


        :param udr_function: The udr_function of this Resources5gcNrm.
        :type udr_function: List[UdrFunctionSingle]
        """

        self._udr_function = udr_function

    @property
    def udsf_function(self):
        """Gets the udsf_function of this Resources5gcNrm.


        :return: The udsf_function of this Resources5gcNrm.
        :rtype: List[UdsfFunctionSingle]
        """
        return self._udsf_function

    @udsf_function.setter
    def udsf_function(self, udsf_function):
        """Sets the udsf_function of this Resources5gcNrm.


        :param udsf_function: The udsf_function of this Resources5gcNrm.
        :type udsf_function: List[UdsfFunctionSingle]
        """

        self._udsf_function = udsf_function

    @property
    def nrf_function(self):
        """Gets the nrf_function of this Resources5gcNrm.


        :return: The nrf_function of this Resources5gcNrm.
        :rtype: List[NrfFunctionSingle]
        """
        return self._nrf_function

    @nrf_function.setter
    def nrf_function(self, nrf_function):
        """Sets the nrf_function of this Resources5gcNrm.


        :param nrf_function: The nrf_function of this Resources5gcNrm.
        :type nrf_function: List[NrfFunctionSingle]
        """

        self._nrf_function = nrf_function

    @property
    def nssf_function(self):
        """Gets the nssf_function of this Resources5gcNrm.


        :return: The nssf_function of this Resources5gcNrm.
        :rtype: List[NssfFunctionSingle]
        """
        return self._nssf_function

    @nssf_function.setter
    def nssf_function(self, nssf_function):
        """Sets the nssf_function of this Resources5gcNrm.


        :param nssf_function: The nssf_function of this Resources5gcNrm.
        :type nssf_function: List[NssfFunctionSingle]
        """

        self._nssf_function = nssf_function

    @property
    def smsf_function(self):
        """Gets the smsf_function of this Resources5gcNrm.


        :return: The smsf_function of this Resources5gcNrm.
        :rtype: List[SmsfFunctionSingle]
        """
        return self._smsf_function

    @smsf_function.setter
    def smsf_function(self, smsf_function):
        """Sets the smsf_function of this Resources5gcNrm.


        :param smsf_function: The smsf_function of this Resources5gcNrm.
        :type smsf_function: List[SmsfFunctionSingle]
        """

        self._smsf_function = smsf_function

    @property
    def lmf_function(self):
        """Gets the lmf_function of this Resources5gcNrm.


        :return: The lmf_function of this Resources5gcNrm.
        :rtype: List[LmfFunctionSingle]
        """
        return self._lmf_function

    @lmf_function.setter
    def lmf_function(self, lmf_function):
        """Sets the lmf_function of this Resources5gcNrm.


        :param lmf_function: The lmf_function of this Resources5gcNrm.
        :type lmf_function: List[LmfFunctionSingle]
        """

        self._lmf_function = lmf_function

    @property
    def ngeir_function(self):
        """Gets the ngeir_function of this Resources5gcNrm.


        :return: The ngeir_function of this Resources5gcNrm.
        :rtype: List[NgeirFunctionSingle]
        """
        return self._ngeir_function

    @ngeir_function.setter
    def ngeir_function(self, ngeir_function):
        """Sets the ngeir_function of this Resources5gcNrm.


        :param ngeir_function: The ngeir_function of this Resources5gcNrm.
        :type ngeir_function: List[NgeirFunctionSingle]
        """

        self._ngeir_function = ngeir_function

    @property
    def sepp_function(self):
        """Gets the sepp_function of this Resources5gcNrm.


        :return: The sepp_function of this Resources5gcNrm.
        :rtype: List[SeppFunctionSingle]
        """
        return self._sepp_function

    @sepp_function.setter
    def sepp_function(self, sepp_function):
        """Sets the sepp_function of this Resources5gcNrm.


        :param sepp_function: The sepp_function of this Resources5gcNrm.
        :type sepp_function: List[SeppFunctionSingle]
        """

        self._sepp_function = sepp_function

    @property
    def nwdaf_function(self):
        """Gets the nwdaf_function of this Resources5gcNrm.


        :return: The nwdaf_function of this Resources5gcNrm.
        :rtype: List[NwdafFunctionSingle]
        """
        return self._nwdaf_function

    @nwdaf_function.setter
    def nwdaf_function(self, nwdaf_function):
        """Sets the nwdaf_function of this Resources5gcNrm.


        :param nwdaf_function: The nwdaf_function of this Resources5gcNrm.
        :type nwdaf_function: List[NwdafFunctionSingle]
        """

        self._nwdaf_function = nwdaf_function

    @property
    def scp_function(self):
        """Gets the scp_function of this Resources5gcNrm.


        :return: The scp_function of this Resources5gcNrm.
        :rtype: List[ScpFunctionSingle]
        """
        return self._scp_function

    @scp_function.setter
    def scp_function(self, scp_function):
        """Sets the scp_function of this Resources5gcNrm.


        :param scp_function: The scp_function of this Resources5gcNrm.
        :type scp_function: List[ScpFunctionSingle]
        """

        self._scp_function = scp_function

    @property
    def nef_function(self):
        """Gets the nef_function of this Resources5gcNrm.


        :return: The nef_function of this Resources5gcNrm.
        :rtype: List[NefFunctionSingle]
        """
        return self._nef_function

    @nef_function.setter
    def nef_function(self, nef_function):
        """Sets the nef_function of this Resources5gcNrm.


        :param nef_function: The nef_function of this Resources5gcNrm.
        :type nef_function: List[NefFunctionSingle]
        """

        self._nef_function = nef_function

    @property
    def easdf_function(self):
        """Gets the easdf_function of this Resources5gcNrm.


        :return: The easdf_function of this Resources5gcNrm.
        :rtype: List[EASDFFunctionSingle]
        """
        return self._easdf_function

    @easdf_function.setter
    def easdf_function(self, easdf_function):
        """Sets the easdf_function of this Resources5gcNrm.


        :param easdf_function: The easdf_function of this Resources5gcNrm.
        :type easdf_function: List[EASDFFunctionSingle]
        """

        self._easdf_function = easdf_function

    @property
    def managed_nf_service(self):
        """Gets the managed_nf_service of this Resources5gcNrm.


        :return: The managed_nf_service of this Resources5gcNrm.
        :rtype: List[ManagedNFServiceSingle]
        """
        return self._managed_nf_service

    @managed_nf_service.setter
    def managed_nf_service(self, managed_nf_service):
        """Sets the managed_nf_service of this Resources5gcNrm.


        :param managed_nf_service: The managed_nf_service of this Resources5gcNrm.
        :type managed_nf_service: List[ManagedNFServiceSingle]
        """

        self._managed_nf_service = managed_nf_service

    @property
    def ep_n2(self):
        """Gets the ep_n2 of this Resources5gcNrm.


        :return: The ep_n2 of this Resources5gcNrm.
        :rtype: List[EPN2Single]
        """
        return self._ep_n2

    @ep_n2.setter
    def ep_n2(self, ep_n2):
        """Sets the ep_n2 of this Resources5gcNrm.


        :param ep_n2: The ep_n2 of this Resources5gcNrm.
        :type ep_n2: List[EPN2Single]
        """

        self._ep_n2 = ep_n2

    @property
    def ep_n8(self):
        """Gets the ep_n8 of this Resources5gcNrm.


        :return: The ep_n8 of this Resources5gcNrm.
        :rtype: List[EPN8Single]
        """
        return self._ep_n8

    @ep_n8.setter
    def ep_n8(self, ep_n8):
        """Sets the ep_n8 of this Resources5gcNrm.


        :param ep_n8: The ep_n8 of this Resources5gcNrm.
        :type ep_n8: List[EPN8Single]
        """

        self._ep_n8 = ep_n8

    @property
    def ep_n11(self):
        """Gets the ep_n11 of this Resources5gcNrm.


        :return: The ep_n11 of this Resources5gcNrm.
        :rtype: List[EPN11Single]
        """
        return self._ep_n11

    @ep_n11.setter
    def ep_n11(self, ep_n11):
        """Sets the ep_n11 of this Resources5gcNrm.


        :param ep_n11: The ep_n11 of this Resources5gcNrm.
        :type ep_n11: List[EPN11Single]
        """

        self._ep_n11 = ep_n11

    @property
    def ep_n12(self):
        """Gets the ep_n12 of this Resources5gcNrm.


        :return: The ep_n12 of this Resources5gcNrm.
        :rtype: List[EPN12Single]
        """
        return self._ep_n12

    @ep_n12.setter
    def ep_n12(self, ep_n12):
        """Sets the ep_n12 of this Resources5gcNrm.


        :param ep_n12: The ep_n12 of this Resources5gcNrm.
        :type ep_n12: List[EPN12Single]
        """

        self._ep_n12 = ep_n12

    @property
    def ep_n14(self):
        """Gets the ep_n14 of this Resources5gcNrm.


        :return: The ep_n14 of this Resources5gcNrm.
        :rtype: List[EPN14Single]
        """
        return self._ep_n14

    @ep_n14.setter
    def ep_n14(self, ep_n14):
        """Sets the ep_n14 of this Resources5gcNrm.


        :param ep_n14: The ep_n14 of this Resources5gcNrm.
        :type ep_n14: List[EPN14Single]
        """

        self._ep_n14 = ep_n14

    @property
    def ep_n15(self):
        """Gets the ep_n15 of this Resources5gcNrm.


        :return: The ep_n15 of this Resources5gcNrm.
        :rtype: List[EPN15Single]
        """
        return self._ep_n15

    @ep_n15.setter
    def ep_n15(self, ep_n15):
        """Sets the ep_n15 of this Resources5gcNrm.


        :param ep_n15: The ep_n15 of this Resources5gcNrm.
        :type ep_n15: List[EPN15Single]
        """

        self._ep_n15 = ep_n15

    @property
    def ep_n17(self):
        """Gets the ep_n17 of this Resources5gcNrm.


        :return: The ep_n17 of this Resources5gcNrm.
        :rtype: List[EPN17Single]
        """
        return self._ep_n17

    @ep_n17.setter
    def ep_n17(self, ep_n17):
        """Sets the ep_n17 of this Resources5gcNrm.


        :param ep_n17: The ep_n17 of this Resources5gcNrm.
        :type ep_n17: List[EPN17Single]
        """

        self._ep_n17 = ep_n17

    @property
    def ep_n20(self):
        """Gets the ep_n20 of this Resources5gcNrm.


        :return: The ep_n20 of this Resources5gcNrm.
        :rtype: List[EPN20Single]
        """
        return self._ep_n20

    @ep_n20.setter
    def ep_n20(self, ep_n20):
        """Sets the ep_n20 of this Resources5gcNrm.


        :param ep_n20: The ep_n20 of this Resources5gcNrm.
        :type ep_n20: List[EPN20Single]
        """

        self._ep_n20 = ep_n20

    @property
    def ep_n22(self):
        """Gets the ep_n22 of this Resources5gcNrm.


        :return: The ep_n22 of this Resources5gcNrm.
        :rtype: List[EPN22Single]
        """
        return self._ep_n22

    @ep_n22.setter
    def ep_n22(self, ep_n22):
        """Sets the ep_n22 of this Resources5gcNrm.


        :param ep_n22: The ep_n22 of this Resources5gcNrm.
        :type ep_n22: List[EPN22Single]
        """

        self._ep_n22 = ep_n22

    @property
    def ep_n26(self):
        """Gets the ep_n26 of this Resources5gcNrm.


        :return: The ep_n26 of this Resources5gcNrm.
        :rtype: List[EPN26Single]
        """
        return self._ep_n26

    @ep_n26.setter
    def ep_n26(self, ep_n26):
        """Sets the ep_n26 of this Resources5gcNrm.


        :param ep_n26: The ep_n26 of this Resources5gcNrm.
        :type ep_n26: List[EPN26Single]
        """

        self._ep_n26 = ep_n26

    @property
    def ep_nls(self):
        """Gets the ep_nls of this Resources5gcNrm.


        :return: The ep_nls of this Resources5gcNrm.
        :rtype: List[EPNLSSingle]
        """
        return self._ep_nls

    @ep_nls.setter
    def ep_nls(self, ep_nls):
        """Sets the ep_nls of this Resources5gcNrm.


        :param ep_nls: The ep_nls of this Resources5gcNrm.
        :type ep_nls: List[EPNLSSingle]
        """

        self._ep_nls = ep_nls

    @property
    def ep_nlg(self):
        """Gets the ep_nlg of this Resources5gcNrm.


        :return: The ep_nlg of this Resources5gcNrm.
        :rtype: List[EPNLGSingle]
        """
        return self._ep_nlg

    @ep_nlg.setter
    def ep_nlg(self, ep_nlg):
        """Sets the ep_nlg of this Resources5gcNrm.


        :param ep_nlg: The ep_nlg of this Resources5gcNrm.
        :type ep_nlg: List[EPNLGSingle]
        """

        self._ep_nlg = ep_nlg

    @property
    def ep_n4(self):
        """Gets the ep_n4 of this Resources5gcNrm.


        :return: The ep_n4 of this Resources5gcNrm.
        :rtype: List[EPN4Single]
        """
        return self._ep_n4

    @ep_n4.setter
    def ep_n4(self, ep_n4):
        """Sets the ep_n4 of this Resources5gcNrm.


        :param ep_n4: The ep_n4 of this Resources5gcNrm.
        :type ep_n4: List[EPN4Single]
        """

        self._ep_n4 = ep_n4

    @property
    def ep_n7(self):
        """Gets the ep_n7 of this Resources5gcNrm.


        :return: The ep_n7 of this Resources5gcNrm.
        :rtype: List[EPN7Single]
        """
        return self._ep_n7

    @ep_n7.setter
    def ep_n7(self, ep_n7):
        """Sets the ep_n7 of this Resources5gcNrm.


        :param ep_n7: The ep_n7 of this Resources5gcNrm.
        :type ep_n7: List[EPN7Single]
        """

        self._ep_n7 = ep_n7

    @property
    def ep_n10(self):
        """Gets the ep_n10 of this Resources5gcNrm.


        :return: The ep_n10 of this Resources5gcNrm.
        :rtype: List[EPN10Single]
        """
        return self._ep_n10

    @ep_n10.setter
    def ep_n10(self, ep_n10):
        """Sets the ep_n10 of this Resources5gcNrm.


        :param ep_n10: The ep_n10 of this Resources5gcNrm.
        :type ep_n10: List[EPN10Single]
        """

        self._ep_n10 = ep_n10

    @property
    def ep_n16(self):
        """Gets the ep_n16 of this Resources5gcNrm.


        :return: The ep_n16 of this Resources5gcNrm.
        :rtype: List[EPN16Single]
        """
        return self._ep_n16

    @ep_n16.setter
    def ep_n16(self, ep_n16):
        """Sets the ep_n16 of this Resources5gcNrm.


        :param ep_n16: The ep_n16 of this Resources5gcNrm.
        :type ep_n16: List[EPN16Single]
        """

        self._ep_n16 = ep_n16

    @property
    def ep_s5_c(self):
        """Gets the ep_s5_c of this Resources5gcNrm.


        :return: The ep_s5_c of this Resources5gcNrm.
        :rtype: List[EPS5CSingle]
        """
        return self._ep_s5_c

    @ep_s5_c.setter
    def ep_s5_c(self, ep_s5_c):
        """Sets the ep_s5_c of this Resources5gcNrm.


        :param ep_s5_c: The ep_s5_c of this Resources5gcNrm.
        :type ep_s5_c: List[EPS5CSingle]
        """

        self._ep_s5_c = ep_s5_c

    @property
    def five_qi_dscp_mapping_set(self):
        """Gets the five_qi_dscp_mapping_set of this Resources5gcNrm.


        :return: The five_qi_dscp_mapping_set of this Resources5gcNrm.
        :rtype: FiveQiDscpMappingSetSingle
        """
        return self._five_qi_dscp_mapping_set

    @five_qi_dscp_mapping_set.setter
    def five_qi_dscp_mapping_set(self, five_qi_dscp_mapping_set):
        """Sets the five_qi_dscp_mapping_set of this Resources5gcNrm.


        :param five_qi_dscp_mapping_set: The five_qi_dscp_mapping_set of this Resources5gcNrm.
        :type five_qi_dscp_mapping_set: FiveQiDscpMappingSetSingle
        """

        self._five_qi_dscp_mapping_set = five_qi_dscp_mapping_set

    @property
    def gtp_u_path_qo_s_monitoring_control(self):
        """Gets the gtp_u_path_qo_s_monitoring_control of this Resources5gcNrm.


        :return: The gtp_u_path_qo_s_monitoring_control of this Resources5gcNrm.
        :rtype: GtpUPathQoSMonitoringControlSingle
        """
        return self._gtp_u_path_qo_s_monitoring_control

    @gtp_u_path_qo_s_monitoring_control.setter
    def gtp_u_path_qo_s_monitoring_control(self, gtp_u_path_qo_s_monitoring_control):
        """Sets the gtp_u_path_qo_s_monitoring_control of this Resources5gcNrm.


        :param gtp_u_path_qo_s_monitoring_control: The gtp_u_path_qo_s_monitoring_control of this Resources5gcNrm.
        :type gtp_u_path_qo_s_monitoring_control: GtpUPathQoSMonitoringControlSingle
        """

        self._gtp_u_path_qo_s_monitoring_control = gtp_u_path_qo_s_monitoring_control

    @property
    def qfqo_s_monitoring_control(self):
        """Gets the qfqo_s_monitoring_control of this Resources5gcNrm.


        :return: The qfqo_s_monitoring_control of this Resources5gcNrm.
        :rtype: QFQoSMonitoringControlSingle
        """
        return self._qfqo_s_monitoring_control

    @qfqo_s_monitoring_control.setter
    def qfqo_s_monitoring_control(self, qfqo_s_monitoring_control):
        """Sets the qfqo_s_monitoring_control of this Resources5gcNrm.


        :param qfqo_s_monitoring_control: The qfqo_s_monitoring_control of this Resources5gcNrm.
        :type qfqo_s_monitoring_control: QFQoSMonitoringControlSingle
        """

        self._qfqo_s_monitoring_control = qfqo_s_monitoring_control

    @property
    def predefined_pcc_rule_set(self):
        """Gets the predefined_pcc_rule_set of this Resources5gcNrm.


        :return: The predefined_pcc_rule_set of this Resources5gcNrm.
        :rtype: PredefinedPccRuleSetSingle
        """
        return self._predefined_pcc_rule_set

    @predefined_pcc_rule_set.setter
    def predefined_pcc_rule_set(self, predefined_pcc_rule_set):
        """Sets the predefined_pcc_rule_set of this Resources5gcNrm.


        :param predefined_pcc_rule_set: The predefined_pcc_rule_set of this Resources5gcNrm.
        :type predefined_pcc_rule_set: PredefinedPccRuleSetSingle
        """

        self._predefined_pcc_rule_set = predefined_pcc_rule_set

    @property
    def ep_n3(self):
        """Gets the ep_n3 of this Resources5gcNrm.


        :return: The ep_n3 of this Resources5gcNrm.
        :rtype: List[EPN3Single]
        """
        return self._ep_n3

    @ep_n3.setter
    def ep_n3(self, ep_n3):
        """Sets the ep_n3 of this Resources5gcNrm.


        :param ep_n3: The ep_n3 of this Resources5gcNrm.
        :type ep_n3: List[EPN3Single]
        """

        self._ep_n3 = ep_n3

    @property
    def ep_n6(self):
        """Gets the ep_n6 of this Resources5gcNrm.


        :return: The ep_n6 of this Resources5gcNrm.
        :rtype: List[EPN6Single]
        """
        return self._ep_n6

    @ep_n6.setter
    def ep_n6(self, ep_n6):
        """Sets the ep_n6 of this Resources5gcNrm.


        :param ep_n6: The ep_n6 of this Resources5gcNrm.
        :type ep_n6: List[EPN6Single]
        """

        self._ep_n6 = ep_n6

    @property
    def ep_n9(self):
        """Gets the ep_n9 of this Resources5gcNrm.


        :return: The ep_n9 of this Resources5gcNrm.
        :rtype: List[EPN9Single]
        """
        return self._ep_n9

    @ep_n9.setter
    def ep_n9(self, ep_n9):
        """Sets the ep_n9 of this Resources5gcNrm.


        :param ep_n9: The ep_n9 of this Resources5gcNrm.
        :type ep_n9: List[EPN9Single]
        """

        self._ep_n9 = ep_n9

    @property
    def ep_s5_u(self):
        """Gets the ep_s5_u of this Resources5gcNrm.


        :return: The ep_s5_u of this Resources5gcNrm.
        :rtype: List[EPS5USingle]
        """
        return self._ep_s5_u

    @ep_s5_u.setter
    def ep_s5_u(self, ep_s5_u):
        """Sets the ep_s5_u of this Resources5gcNrm.


        :param ep_s5_u: The ep_s5_u of this Resources5gcNrm.
        :type ep_s5_u: List[EPS5USingle]
        """

        self._ep_s5_u = ep_s5_u

    @property
    def ep_n5(self):
        """Gets the ep_n5 of this Resources5gcNrm.


        :return: The ep_n5 of this Resources5gcNrm.
        :rtype: List[EPN5Single]
        """
        return self._ep_n5

    @ep_n5.setter
    def ep_n5(self, ep_n5):
        """Sets the ep_n5 of this Resources5gcNrm.


        :param ep_n5: The ep_n5 of this Resources5gcNrm.
        :type ep_n5: List[EPN5Single]
        """

        self._ep_n5 = ep_n5

    @property
    def ep_rx(self):
        """Gets the ep_rx of this Resources5gcNrm.


        :return: The ep_rx of this Resources5gcNrm.
        :rtype: List[EPRxSingle]
        """
        return self._ep_rx

    @ep_rx.setter
    def ep_rx(self, ep_rx):
        """Sets the ep_rx of this Resources5gcNrm.


        :param ep_rx: The ep_rx of this Resources5gcNrm.
        :type ep_rx: List[EPRxSingle]
        """

        self._ep_rx = ep_rx

    @property
    def ep_n13(self):
        """Gets the ep_n13 of this Resources5gcNrm.


        :return: The ep_n13 of this Resources5gcNrm.
        :rtype: List[EPN13Single]
        """
        return self._ep_n13

    @ep_n13.setter
    def ep_n13(self, ep_n13):
        """Sets the ep_n13 of this Resources5gcNrm.


        :param ep_n13: The ep_n13 of this Resources5gcNrm.
        :type ep_n13: List[EPN13Single]
        """

        self._ep_n13 = ep_n13

    @property
    def ep_n27(self):
        """Gets the ep_n27 of this Resources5gcNrm.


        :return: The ep_n27 of this Resources5gcNrm.
        :rtype: List[EPN27Single]
        """
        return self._ep_n27

    @ep_n27.setter
    def ep_n27(self, ep_n27):
        """Sets the ep_n27 of this Resources5gcNrm.


        :param ep_n27: The ep_n27 of this Resources5gcNrm.
        :type ep_n27: List[EPN27Single]
        """

        self._ep_n27 = ep_n27

    @property
    def ep_n31(self):
        """Gets the ep_n31 of this Resources5gcNrm.


        :return: The ep_n31 of this Resources5gcNrm.
        :rtype: List[EPN31Single]
        """
        return self._ep_n31

    @ep_n31.setter
    def ep_n31(self, ep_n31):
        """Sets the ep_n31 of this Resources5gcNrm.


        :param ep_n31: The ep_n31 of this Resources5gcNrm.
        :type ep_n31: List[EPN31Single]
        """

        self._ep_n31 = ep_n31

    @property
    def ep_n21(self):
        """Gets the ep_n21 of this Resources5gcNrm.


        :return: The ep_n21 of this Resources5gcNrm.
        :rtype: List[EPN21Single]
        """
        return self._ep_n21

    @ep_n21.setter
    def ep_n21(self, ep_n21):
        """Sets the ep_n21 of this Resources5gcNrm.


        :param ep_n21: The ep_n21 of this Resources5gcNrm.
        :type ep_n21: List[EPN21Single]
        """

        self._ep_n21 = ep_n21

    @property
    def ep_map_smsc(self):
        """Gets the ep_map_smsc of this Resources5gcNrm.


        :return: The ep_map_smsc of this Resources5gcNrm.
        :rtype: List[EPMAPSMSCSingle]
        """
        return self._ep_map_smsc

    @ep_map_smsc.setter
    def ep_map_smsc(self, ep_map_smsc):
        """Sets the ep_map_smsc of this Resources5gcNrm.


        :param ep_map_smsc: The ep_map_smsc of this Resources5gcNrm.
        :type ep_map_smsc: List[EPMAPSMSCSingle]
        """

        self._ep_map_smsc = ep_map_smsc

    @property
    def ep_n32(self):
        """Gets the ep_n32 of this Resources5gcNrm.


        :return: The ep_n32 of this Resources5gcNrm.
        :rtype: List[EPN32Single]
        """
        return self._ep_n32

    @ep_n32.setter
    def ep_n32(self, ep_n32):
        """Sets the ep_n32 of this Resources5gcNrm.


        :param ep_n32: The ep_n32 of this Resources5gcNrm.
        :type ep_n32: List[EPN32Single]
        """

        self._ep_n32 = ep_n32

    @property
    def ep_n33(self):
        """Gets the ep_n33 of this Resources5gcNrm.


        :return: The ep_n33 of this Resources5gcNrm.
        :rtype: List[EPN33Single]
        """
        return self._ep_n33

    @ep_n33.setter
    def ep_n33(self, ep_n33):
        """Sets the ep_n33 of this Resources5gcNrm.


        :param ep_n33: The ep_n33 of this Resources5gcNrm.
        :type ep_n33: List[EPN33Single]
        """

        self._ep_n33 = ep_n33

    @property
    def ep_n60(self):
        """Gets the ep_n60 of this Resources5gcNrm.


        :return: The ep_n60 of this Resources5gcNrm.
        :rtype: List[EPN60Single]
        """
        return self._ep_n60

    @ep_n60.setter
    def ep_n60(self, ep_n60):
        """Sets the ep_n60 of this Resources5gcNrm.


        :param ep_n60: The ep_n60 of this Resources5gcNrm.
        :type ep_n60: List[EPN60Single]
        """

        self._ep_n60 = ep_n60

    @property
    def ep_npc4(self):
        """Gets the ep_npc4 of this Resources5gcNrm.


        :return: The ep_npc4 of this Resources5gcNrm.
        :rtype: List[EPNpc4Single]
        """
        return self._ep_npc4

    @ep_npc4.setter
    def ep_npc4(self, ep_npc4):
        """Sets the ep_npc4 of this Resources5gcNrm.


        :param ep_npc4: The ep_npc4 of this Resources5gcNrm.
        :type ep_npc4: List[EPNpc4Single]
        """

        self._ep_npc4 = ep_npc4

    @property
    def ep_npc6(self):
        """Gets the ep_npc6 of this Resources5gcNrm.


        :return: The ep_npc6 of this Resources5gcNrm.
        :rtype: List[EPNpc6Single]
        """
        return self._ep_npc6

    @ep_npc6.setter
    def ep_npc6(self, ep_npc6):
        """Sets the ep_npc6 of this Resources5gcNrm.


        :param ep_npc6: The ep_npc6 of this Resources5gcNrm.
        :type ep_npc6: List[EPNpc6Single]
        """

        self._ep_npc6 = ep_npc6

    @property
    def ep_npc7(self):
        """Gets the ep_npc7 of this Resources5gcNrm.


        :return: The ep_npc7 of this Resources5gcNrm.
        :rtype: List[EPNpc7Single]
        """
        return self._ep_npc7

    @ep_npc7.setter
    def ep_npc7(self, ep_npc7):
        """Sets the ep_npc7 of this Resources5gcNrm.


        :param ep_npc7: The ep_npc7 of this Resources5gcNrm.
        :type ep_npc7: List[EPNpc7Single]
        """

        self._ep_npc7 = ep_npc7

    @property
    def ep_npc8(self):
        """Gets the ep_npc8 of this Resources5gcNrm.


        :return: The ep_npc8 of this Resources5gcNrm.
        :rtype: List[EPNpc8Single]
        """
        return self._ep_npc8

    @ep_npc8.setter
    def ep_npc8(self, ep_npc8):
        """Sets the ep_npc8 of this Resources5gcNrm.


        :param ep_npc8: The ep_npc8 of this Resources5gcNrm.
        :type ep_npc8: List[EPNpc8Single]
        """

        self._ep_npc8 = ep_npc8

    @property
    def ep_n88(self):
        """Gets the ep_n88 of this Resources5gcNrm.


        :return: The ep_n88 of this Resources5gcNrm.
        :rtype: List[EPN88Single]
        """
        return self._ep_n88

    @ep_n88.setter
    def ep_n88(self, ep_n88):
        """Sets the ep_n88 of this Resources5gcNrm.


        :param ep_n88: The ep_n88 of this Resources5gcNrm.
        :type ep_n88: List[EPN88Single]
        """

        self._ep_n88 = ep_n88
