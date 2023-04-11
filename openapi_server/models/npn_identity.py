# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.plmn_id import PlmnId
from openapi_server import util

from openapi_server.models.plmn_id import PlmnId  # noqa: E501

class NpnIdentity(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, plmn_id=None, cagid_list=None, nid_list=None):  # noqa: E501
        """NpnIdentity - a model defined in OpenAPI

        :param plmn_id: The plmn_id of this NpnIdentity.  # noqa: E501
        :type plmn_id: PlmnId
        :param cagid_list: The cagid_list of this NpnIdentity.  # noqa: E501
        :type cagid_list: str
        :param nid_list: The nid_list of this NpnIdentity.  # noqa: E501
        :type nid_list: str
        """
        self.openapi_types = {
            'plmn_id': PlmnId,
            'cagid_list': str,
            'nid_list': str
        }

        self.attribute_map = {
            'plmn_id': 'plmnId',
            'cagid_list': 'cagidList',
            'nid_list': 'nidList'
        }

        self._plmn_id = plmn_id
        self._cagid_list = cagid_list
        self._nid_list = nid_list

    @classmethod
    def from_dict(cls, dikt) -> 'NpnIdentity':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NpnIdentity of this NpnIdentity.  # noqa: E501
        :rtype: NpnIdentity
        """
        return util.deserialize_model(dikt, cls)

    @property
    def plmn_id(self):
        """Gets the plmn_id of this NpnIdentity.


        :return: The plmn_id of this NpnIdentity.
        :rtype: PlmnId
        """
        return self._plmn_id

    @plmn_id.setter
    def plmn_id(self, plmn_id):
        """Sets the plmn_id of this NpnIdentity.


        :param plmn_id: The plmn_id of this NpnIdentity.
        :type plmn_id: PlmnId
        """

        self._plmn_id = plmn_id

    @property
    def cagid_list(self):
        """Gets the cagid_list of this NpnIdentity.


        :return: The cagid_list of this NpnIdentity.
        :rtype: str
        """
        return self._cagid_list

    @cagid_list.setter
    def cagid_list(self, cagid_list):
        """Sets the cagid_list of this NpnIdentity.


        :param cagid_list: The cagid_list of this NpnIdentity.
        :type cagid_list: str
        """

        self._cagid_list = cagid_list

    @property
    def nid_list(self):
        """Gets the nid_list of this NpnIdentity.


        :return: The nid_list of this NpnIdentity.
        :rtype: str
        """
        return self._nid_list

    @nid_list.setter
    def nid_list(self, nid_list):
        """Sets the nid_list of this NpnIdentity.


        :param nid_list: The nid_list of this NpnIdentity.
        :type nid_list: str
        """

        self._nid_list = nid_list
