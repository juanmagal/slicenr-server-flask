# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.af_sig_protocol import AfSigProtocol
from openapi_server.models.condition_data import ConditionData
from openapi_server.models.flow_information import FlowInformation
from openapi_server.models.qos_data import QosData
from openapi_server.models.traffic_control_data import TrafficControlData
from openapi_server.models.tscai_input_container import TscaiInputContainer
from openapi_server import util

from openapi_server.models.af_sig_protocol import AfSigProtocol  # noqa: E501
from openapi_server.models.condition_data import ConditionData  # noqa: E501
from openapi_server.models.flow_information import FlowInformation  # noqa: E501
from openapi_server.models.qos_data import QosData  # noqa: E501
from openapi_server.models.traffic_control_data import TrafficControlData  # noqa: E501
from openapi_server.models.tscai_input_container import TscaiInputContainer  # noqa: E501

class PccRule(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pcc_rule_id=None, flow_info_list=None, application_id=None, app_descriptor=None, content_version=None, precedence=None, af_sig_protocol=None, is_app_relocatable=None, is_ue_addr_preserved=None, qos_data=None, alt_qos_params=None, traffic_control_data=None, condition_data=None, tscai_input_dl=None, tscai_input_ul=None):  # noqa: E501
        """PccRule - a model defined in OpenAPI

        :param pcc_rule_id: The pcc_rule_id of this PccRule.  # noqa: E501
        :type pcc_rule_id: str
        :param flow_info_list: The flow_info_list of this PccRule.  # noqa: E501
        :type flow_info_list: List[FlowInformation]
        :param application_id: The application_id of this PccRule.  # noqa: E501
        :type application_id: str
        :param app_descriptor: The app_descriptor of this PccRule.  # noqa: E501
        :type app_descriptor: str
        :param content_version: The content_version of this PccRule.  # noqa: E501
        :type content_version: int
        :param precedence: The precedence of this PccRule.  # noqa: E501
        :type precedence: int
        :param af_sig_protocol: The af_sig_protocol of this PccRule.  # noqa: E501
        :type af_sig_protocol: AfSigProtocol
        :param is_app_relocatable: The is_app_relocatable of this PccRule.  # noqa: E501
        :type is_app_relocatable: bool
        :param is_ue_addr_preserved: The is_ue_addr_preserved of this PccRule.  # noqa: E501
        :type is_ue_addr_preserved: bool
        :param qos_data: The qos_data of this PccRule.  # noqa: E501
        :type qos_data: List[List]
        :param alt_qos_params: The alt_qos_params of this PccRule.  # noqa: E501
        :type alt_qos_params: List[List]
        :param traffic_control_data: The traffic_control_data of this PccRule.  # noqa: E501
        :type traffic_control_data: List[List]
        :param condition_data: The condition_data of this PccRule.  # noqa: E501
        :type condition_data: ConditionData
        :param tscai_input_dl: The tscai_input_dl of this PccRule.  # noqa: E501
        :type tscai_input_dl: TscaiInputContainer
        :param tscai_input_ul: The tscai_input_ul of this PccRule.  # noqa: E501
        :type tscai_input_ul: TscaiInputContainer
        """
        self.openapi_types = {
            'pcc_rule_id': str,
            'flow_info_list': List[FlowInformation],
            'application_id': str,
            'app_descriptor': str,
            'content_version': int,
            'precedence': int,
            'af_sig_protocol': AfSigProtocol,
            'is_app_relocatable': bool,
            'is_ue_addr_preserved': bool,
            'qos_data': List[List],
            'alt_qos_params': List[List],
            'traffic_control_data': List[List],
            'condition_data': ConditionData,
            'tscai_input_dl': TscaiInputContainer,
            'tscai_input_ul': TscaiInputContainer
        }

        self.attribute_map = {
            'pcc_rule_id': 'pccRuleId',
            'flow_info_list': 'flowInfoList',
            'application_id': 'applicationId',
            'app_descriptor': 'appDescriptor',
            'content_version': 'contentVersion',
            'precedence': 'precedence',
            'af_sig_protocol': 'afSigProtocol',
            'is_app_relocatable': 'isAppRelocatable',
            'is_ue_addr_preserved': 'isUeAddrPreserved',
            'qos_data': 'qosData',
            'alt_qos_params': 'altQosParams',
            'traffic_control_data': 'trafficControlData',
            'condition_data': 'conditionData',
            'tscai_input_dl': 'tscaiInputDl',
            'tscai_input_ul': 'tscaiInputUl'
        }

        self._pcc_rule_id = pcc_rule_id
        self._flow_info_list = flow_info_list
        self._application_id = application_id
        self._app_descriptor = app_descriptor
        self._content_version = content_version
        self._precedence = precedence
        self._af_sig_protocol = af_sig_protocol
        self._is_app_relocatable = is_app_relocatable
        self._is_ue_addr_preserved = is_ue_addr_preserved
        self._qos_data = qos_data
        self._alt_qos_params = alt_qos_params
        self._traffic_control_data = traffic_control_data
        self._condition_data = condition_data
        self._tscai_input_dl = tscai_input_dl
        self._tscai_input_ul = tscai_input_ul

    @classmethod
    def from_dict(cls, dikt) -> 'PccRule':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PccRule of this PccRule.  # noqa: E501
        :rtype: PccRule
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pcc_rule_id(self):
        """Gets the pcc_rule_id of this PccRule.

        Univocally identifies the PCC rule within a PDU session.  # noqa: E501

        :return: The pcc_rule_id of this PccRule.
        :rtype: str
        """
        return self._pcc_rule_id

    @pcc_rule_id.setter
    def pcc_rule_id(self, pcc_rule_id):
        """Sets the pcc_rule_id of this PccRule.

        Univocally identifies the PCC rule within a PDU session.  # noqa: E501

        :param pcc_rule_id: The pcc_rule_id of this PccRule.
        :type pcc_rule_id: str
        """

        self._pcc_rule_id = pcc_rule_id

    @property
    def flow_info_list(self):
        """Gets the flow_info_list of this PccRule.


        :return: The flow_info_list of this PccRule.
        :rtype: List[FlowInformation]
        """
        return self._flow_info_list

    @flow_info_list.setter
    def flow_info_list(self, flow_info_list):
        """Sets the flow_info_list of this PccRule.


        :param flow_info_list: The flow_info_list of this PccRule.
        :type flow_info_list: List[FlowInformation]
        """

        self._flow_info_list = flow_info_list

    @property
    def application_id(self):
        """Gets the application_id of this PccRule.


        :return: The application_id of this PccRule.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this PccRule.


        :param application_id: The application_id of this PccRule.
        :type application_id: str
        """

        self._application_id = application_id

    @property
    def app_descriptor(self):
        """Gets the app_descriptor of this PccRule.

        string with format 'bytes' as defined in OpenAPI  # noqa: E501

        :return: The app_descriptor of this PccRule.
        :rtype: str
        """
        return self._app_descriptor

    @app_descriptor.setter
    def app_descriptor(self, app_descriptor):
        """Sets the app_descriptor of this PccRule.

        string with format 'bytes' as defined in OpenAPI  # noqa: E501

        :param app_descriptor: The app_descriptor of this PccRule.
        :type app_descriptor: str
        """

        self._app_descriptor = app_descriptor

    @property
    def content_version(self):
        """Gets the content_version of this PccRule.

        Represents the content version of some content.  # noqa: E501

        :return: The content_version of this PccRule.
        :rtype: int
        """
        return self._content_version

    @content_version.setter
    def content_version(self, content_version):
        """Sets the content_version of this PccRule.

        Represents the content version of some content.  # noqa: E501

        :param content_version: The content_version of this PccRule.
        :type content_version: int
        """

        self._content_version = content_version

    @property
    def precedence(self):
        """Gets the precedence of this PccRule.

        Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.  # noqa: E501

        :return: The precedence of this PccRule.
        :rtype: int
        """
        return self._precedence

    @precedence.setter
    def precedence(self, precedence):
        """Sets the precedence of this PccRule.

        Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.  # noqa: E501

        :param precedence: The precedence of this PccRule.
        :type precedence: int
        """
        if precedence is not None and precedence < 0:  # noqa: E501
            raise ValueError("Invalid value for `precedence`, must be a value greater than or equal to `0`")  # noqa: E501

        self._precedence = precedence

    @property
    def af_sig_protocol(self):
        """Gets the af_sig_protocol of this PccRule.


        :return: The af_sig_protocol of this PccRule.
        :rtype: AfSigProtocol
        """
        return self._af_sig_protocol

    @af_sig_protocol.setter
    def af_sig_protocol(self, af_sig_protocol):
        """Sets the af_sig_protocol of this PccRule.


        :param af_sig_protocol: The af_sig_protocol of this PccRule.
        :type af_sig_protocol: AfSigProtocol
        """

        self._af_sig_protocol = af_sig_protocol

    @property
    def is_app_relocatable(self):
        """Gets the is_app_relocatable of this PccRule.


        :return: The is_app_relocatable of this PccRule.
        :rtype: bool
        """
        return self._is_app_relocatable

    @is_app_relocatable.setter
    def is_app_relocatable(self, is_app_relocatable):
        """Sets the is_app_relocatable of this PccRule.


        :param is_app_relocatable: The is_app_relocatable of this PccRule.
        :type is_app_relocatable: bool
        """

        self._is_app_relocatable = is_app_relocatable

    @property
    def is_ue_addr_preserved(self):
        """Gets the is_ue_addr_preserved of this PccRule.


        :return: The is_ue_addr_preserved of this PccRule.
        :rtype: bool
        """
        return self._is_ue_addr_preserved

    @is_ue_addr_preserved.setter
    def is_ue_addr_preserved(self, is_ue_addr_preserved):
        """Sets the is_ue_addr_preserved of this PccRule.


        :param is_ue_addr_preserved: The is_ue_addr_preserved of this PccRule.
        :type is_ue_addr_preserved: bool
        """

        self._is_ue_addr_preserved = is_ue_addr_preserved

    @property
    def qos_data(self):
        """Gets the qos_data of this PccRule.


        :return: The qos_data of this PccRule.
        :rtype: List[List]
        """
        return self._qos_data

    @qos_data.setter
    def qos_data(self, qos_data):
        """Sets the qos_data of this PccRule.


        :param qos_data: The qos_data of this PccRule.
        :type qos_data: List[List]
        """

        self._qos_data = qos_data

    @property
    def alt_qos_params(self):
        """Gets the alt_qos_params of this PccRule.


        :return: The alt_qos_params of this PccRule.
        :rtype: List[List]
        """
        return self._alt_qos_params

    @alt_qos_params.setter
    def alt_qos_params(self, alt_qos_params):
        """Sets the alt_qos_params of this PccRule.


        :param alt_qos_params: The alt_qos_params of this PccRule.
        :type alt_qos_params: List[List]
        """

        self._alt_qos_params = alt_qos_params

    @property
    def traffic_control_data(self):
        """Gets the traffic_control_data of this PccRule.


        :return: The traffic_control_data of this PccRule.
        :rtype: List[List]
        """
        return self._traffic_control_data

    @traffic_control_data.setter
    def traffic_control_data(self, traffic_control_data):
        """Sets the traffic_control_data of this PccRule.


        :param traffic_control_data: The traffic_control_data of this PccRule.
        :type traffic_control_data: List[List]
        """

        self._traffic_control_data = traffic_control_data

    @property
    def condition_data(self):
        """Gets the condition_data of this PccRule.


        :return: The condition_data of this PccRule.
        :rtype: ConditionData
        """
        return self._condition_data

    @condition_data.setter
    def condition_data(self, condition_data):
        """Sets the condition_data of this PccRule.


        :param condition_data: The condition_data of this PccRule.
        :type condition_data: ConditionData
        """

        self._condition_data = condition_data

    @property
    def tscai_input_dl(self):
        """Gets the tscai_input_dl of this PccRule.


        :return: The tscai_input_dl of this PccRule.
        :rtype: TscaiInputContainer
        """
        return self._tscai_input_dl

    @tscai_input_dl.setter
    def tscai_input_dl(self, tscai_input_dl):
        """Sets the tscai_input_dl of this PccRule.


        :param tscai_input_dl: The tscai_input_dl of this PccRule.
        :type tscai_input_dl: TscaiInputContainer
        """

        self._tscai_input_dl = tscai_input_dl

    @property
    def tscai_input_ul(self):
        """Gets the tscai_input_ul of this PccRule.


        :return: The tscai_input_ul of this PccRule.
        :rtype: TscaiInputContainer
        """
        return self._tscai_input_ul

    @tscai_input_ul.setter
    def tscai_input_ul(self, tscai_input_ul):
        """Sets the tscai_input_ul of this PccRule.


        :param tscai_input_ul: The tscai_input_ul of this PccRule.
        :type tscai_input_ul: TscaiInputContainer
        """

        self._tscai_input_ul = tscai_input_ul