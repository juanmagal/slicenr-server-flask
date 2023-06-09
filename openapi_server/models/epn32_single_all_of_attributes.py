# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.host_addr import HostAddr
from openapi_server.models.plmn_id import PlmnId
from openapi_server.models.supported_perf_metric_group import SupportedPerfMetricGroup
from openapi_server import util

from openapi_server.models.host_addr import HostAddr  # noqa: E501
from openapi_server.models.plmn_id import PlmnId  # noqa: E501
from openapi_server.models.supported_perf_metric_group import SupportedPerfMetricGroup  # noqa: E501

class EPN32SingleAllOfAttributes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, user_label=None, far_end_entity=None, supported_perf_metric_groups=None, remote_plmn_id=None, remote_sepp_address=None, remote_sepp_id=None, n32c_paras=None, n32f_policy=None, with_ipx=None):  # noqa: E501
        """EPN32SingleAllOfAttributes - a model defined in OpenAPI

        :param user_label: The user_label of this EPN32SingleAllOfAttributes.  # noqa: E501
        :type user_label: str
        :param far_end_entity: The far_end_entity of this EPN32SingleAllOfAttributes.  # noqa: E501
        :type far_end_entity: str
        :param supported_perf_metric_groups: The supported_perf_metric_groups of this EPN32SingleAllOfAttributes.  # noqa: E501
        :type supported_perf_metric_groups: List[SupportedPerfMetricGroup]
        :param remote_plmn_id: The remote_plmn_id of this EPN32SingleAllOfAttributes.  # noqa: E501
        :type remote_plmn_id: PlmnId
        :param remote_sepp_address: The remote_sepp_address of this EPN32SingleAllOfAttributes.  # noqa: E501
        :type remote_sepp_address: HostAddr
        :param remote_sepp_id: The remote_sepp_id of this EPN32SingleAllOfAttributes.  # noqa: E501
        :type remote_sepp_id: int
        :param n32c_paras: The n32c_paras of this EPN32SingleAllOfAttributes.  # noqa: E501
        :type n32c_paras: str
        :param n32f_policy: The n32f_policy of this EPN32SingleAllOfAttributes.  # noqa: E501
        :type n32f_policy: str
        :param with_ipx: The with_ipx of this EPN32SingleAllOfAttributes.  # noqa: E501
        :type with_ipx: bool
        """
        self.openapi_types = {
            'user_label': str,
            'far_end_entity': str,
            'supported_perf_metric_groups': List[SupportedPerfMetricGroup],
            'remote_plmn_id': PlmnId,
            'remote_sepp_address': HostAddr,
            'remote_sepp_id': int,
            'n32c_paras': str,
            'n32f_policy': str,
            'with_ipx': bool
        }

        self.attribute_map = {
            'user_label': 'userLabel',
            'far_end_entity': 'farEndEntity',
            'supported_perf_metric_groups': 'supportedPerfMetricGroups',
            'remote_plmn_id': 'remotePlmnId',
            'remote_sepp_address': 'remoteSeppAddress',
            'remote_sepp_id': 'remoteSeppId',
            'n32c_paras': 'n32cParas',
            'n32f_policy': 'n32fPolicy',
            'with_ipx': 'withIPX'
        }

        self._user_label = user_label
        self._far_end_entity = far_end_entity
        self._supported_perf_metric_groups = supported_perf_metric_groups
        self._remote_plmn_id = remote_plmn_id
        self._remote_sepp_address = remote_sepp_address
        self._remote_sepp_id = remote_sepp_id
        self._n32c_paras = n32c_paras
        self._n32f_policy = n32f_policy
        self._with_ipx = with_ipx

    @classmethod
    def from_dict(cls, dikt) -> 'EPN32SingleAllOfAttributes':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EP_N32_Single_allOf_attributes of this EPN32SingleAllOfAttributes.  # noqa: E501
        :rtype: EPN32SingleAllOfAttributes
        """
        return util.deserialize_model(dikt, cls)

    @property
    def user_label(self):
        """Gets the user_label of this EPN32SingleAllOfAttributes.


        :return: The user_label of this EPN32SingleAllOfAttributes.
        :rtype: str
        """
        return self._user_label

    @user_label.setter
    def user_label(self, user_label):
        """Sets the user_label of this EPN32SingleAllOfAttributes.


        :param user_label: The user_label of this EPN32SingleAllOfAttributes.
        :type user_label: str
        """

        self._user_label = user_label

    @property
    def far_end_entity(self):
        """Gets the far_end_entity of this EPN32SingleAllOfAttributes.


        :return: The far_end_entity of this EPN32SingleAllOfAttributes.
        :rtype: str
        """
        return self._far_end_entity

    @far_end_entity.setter
    def far_end_entity(self, far_end_entity):
        """Sets the far_end_entity of this EPN32SingleAllOfAttributes.


        :param far_end_entity: The far_end_entity of this EPN32SingleAllOfAttributes.
        :type far_end_entity: str
        """

        self._far_end_entity = far_end_entity

    @property
    def supported_perf_metric_groups(self):
        """Gets the supported_perf_metric_groups of this EPN32SingleAllOfAttributes.


        :return: The supported_perf_metric_groups of this EPN32SingleAllOfAttributes.
        :rtype: List[SupportedPerfMetricGroup]
        """
        return self._supported_perf_metric_groups

    @supported_perf_metric_groups.setter
    def supported_perf_metric_groups(self, supported_perf_metric_groups):
        """Sets the supported_perf_metric_groups of this EPN32SingleAllOfAttributes.


        :param supported_perf_metric_groups: The supported_perf_metric_groups of this EPN32SingleAllOfAttributes.
        :type supported_perf_metric_groups: List[SupportedPerfMetricGroup]
        """

        self._supported_perf_metric_groups = supported_perf_metric_groups

    @property
    def remote_plmn_id(self):
        """Gets the remote_plmn_id of this EPN32SingleAllOfAttributes.


        :return: The remote_plmn_id of this EPN32SingleAllOfAttributes.
        :rtype: PlmnId
        """
        return self._remote_plmn_id

    @remote_plmn_id.setter
    def remote_plmn_id(self, remote_plmn_id):
        """Sets the remote_plmn_id of this EPN32SingleAllOfAttributes.


        :param remote_plmn_id: The remote_plmn_id of this EPN32SingleAllOfAttributes.
        :type remote_plmn_id: PlmnId
        """

        self._remote_plmn_id = remote_plmn_id

    @property
    def remote_sepp_address(self):
        """Gets the remote_sepp_address of this EPN32SingleAllOfAttributes.


        :return: The remote_sepp_address of this EPN32SingleAllOfAttributes.
        :rtype: HostAddr
        """
        return self._remote_sepp_address

    @remote_sepp_address.setter
    def remote_sepp_address(self, remote_sepp_address):
        """Sets the remote_sepp_address of this EPN32SingleAllOfAttributes.


        :param remote_sepp_address: The remote_sepp_address of this EPN32SingleAllOfAttributes.
        :type remote_sepp_address: HostAddr
        """

        self._remote_sepp_address = remote_sepp_address

    @property
    def remote_sepp_id(self):
        """Gets the remote_sepp_id of this EPN32SingleAllOfAttributes.


        :return: The remote_sepp_id of this EPN32SingleAllOfAttributes.
        :rtype: int
        """
        return self._remote_sepp_id

    @remote_sepp_id.setter
    def remote_sepp_id(self, remote_sepp_id):
        """Sets the remote_sepp_id of this EPN32SingleAllOfAttributes.


        :param remote_sepp_id: The remote_sepp_id of this EPN32SingleAllOfAttributes.
        :type remote_sepp_id: int
        """

        self._remote_sepp_id = remote_sepp_id

    @property
    def n32c_paras(self):
        """Gets the n32c_paras of this EPN32SingleAllOfAttributes.


        :return: The n32c_paras of this EPN32SingleAllOfAttributes.
        :rtype: str
        """
        return self._n32c_paras

    @n32c_paras.setter
    def n32c_paras(self, n32c_paras):
        """Sets the n32c_paras of this EPN32SingleAllOfAttributes.


        :param n32c_paras: The n32c_paras of this EPN32SingleAllOfAttributes.
        :type n32c_paras: str
        """

        self._n32c_paras = n32c_paras

    @property
    def n32f_policy(self):
        """Gets the n32f_policy of this EPN32SingleAllOfAttributes.


        :return: The n32f_policy of this EPN32SingleAllOfAttributes.
        :rtype: str
        """
        return self._n32f_policy

    @n32f_policy.setter
    def n32f_policy(self, n32f_policy):
        """Sets the n32f_policy of this EPN32SingleAllOfAttributes.


        :param n32f_policy: The n32f_policy of this EPN32SingleAllOfAttributes.
        :type n32f_policy: str
        """

        self._n32f_policy = n32f_policy

    @property
    def with_ipx(self):
        """Gets the with_ipx of this EPN32SingleAllOfAttributes.


        :return: The with_ipx of this EPN32SingleAllOfAttributes.
        :rtype: bool
        """
        return self._with_ipx

    @with_ipx.setter
    def with_ipx(self, with_ipx):
        """Sets the with_ipx of this EPN32SingleAllOfAttributes.


        :param with_ipx: The with_ipx of this EPN32SingleAllOfAttributes.
        :type with_ipx: bool
        """

        self._with_ipx = with_ipx
