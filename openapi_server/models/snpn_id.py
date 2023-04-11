# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
import re
from openapi_server import util

import re  # noqa: E501

class SnpnId(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, mcc=None, mnc=None, nid=None):  # noqa: E501
        """SnpnId - a model defined in OpenAPI

        :param mcc: The mcc of this SnpnId.  # noqa: E501
        :type mcc: str
        :param mnc: The mnc of this SnpnId.  # noqa: E501
        :type mnc: str
        :param nid: The nid of this SnpnId.  # noqa: E501
        :type nid: str
        """
        self.openapi_types = {
            'mcc': str,
            'mnc': str,
            'nid': str
        }

        self.attribute_map = {
            'mcc': 'mcc',
            'mnc': 'mnc',
            'nid': 'nid'
        }

        self._mcc = mcc
        self._mnc = mnc
        self._nid = nid

    @classmethod
    def from_dict(cls, dikt) -> 'SnpnId':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SnpnId of this SnpnId.  # noqa: E501
        :rtype: SnpnId
        """
        return util.deserialize_model(dikt, cls)

    @property
    def mcc(self):
        """Gets the mcc of this SnpnId.


        :return: The mcc of this SnpnId.
        :rtype: str
        """
        return self._mcc

    @mcc.setter
    def mcc(self, mcc):
        """Sets the mcc of this SnpnId.


        :param mcc: The mcc of this SnpnId.
        :type mcc: str
        """
        if mcc is not None and not re.search(r'^[0-9]{3}$', mcc):  # noqa: E501
            raise ValueError("Invalid value for `mcc`, must be a follow pattern or equal to `/^[0-9]{3}$/`")  # noqa: E501

        self._mcc = mcc

    @property
    def mnc(self):
        """Gets the mnc of this SnpnId.


        :return: The mnc of this SnpnId.
        :rtype: str
        """
        return self._mnc

    @mnc.setter
    def mnc(self, mnc):
        """Sets the mnc of this SnpnId.


        :param mnc: The mnc of this SnpnId.
        :type mnc: str
        """
        if mnc is not None and not re.search(r'^[0-9]{2,3}$', mnc):  # noqa: E501
            raise ValueError("Invalid value for `mnc`, must be a follow pattern or equal to `/^[0-9]{2,3}$/`")  # noqa: E501

        self._mnc = mnc

    @property
    def nid(self):
        """Gets the nid of this SnpnId.


        :return: The nid of this SnpnId.
        :rtype: str
        """
        return self._nid

    @nid.setter
    def nid(self, nid):
        """Sets the nid of this SnpnId.


        :param nid: The nid of this SnpnId.
        :type nid: str
        """

        self._nid = nid
