# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
import re
from openapi_server import util

import re  # noqa: E501

class PlmnId1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, mcc=None, mnc=None):  # noqa: E501
        """PlmnId1 - a model defined in OpenAPI

        :param mcc: The mcc of this PlmnId1.  # noqa: E501
        :type mcc: str
        :param mnc: The mnc of this PlmnId1.  # noqa: E501
        :type mnc: str
        """
        self.openapi_types = {
            'mcc': str,
            'mnc': str
        }

        self.attribute_map = {
            'mcc': 'mcc',
            'mnc': 'mnc'
        }

        self._mcc = mcc
        self._mnc = mnc

    @classmethod
    def from_dict(cls, dikt) -> 'PlmnId1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PlmnId_1 of this PlmnId1.  # noqa: E501
        :rtype: PlmnId1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def mcc(self):
        """Gets the mcc of this PlmnId1.


        :return: The mcc of this PlmnId1.
        :rtype: str
        """
        return self._mcc

    @mcc.setter
    def mcc(self, mcc):
        """Sets the mcc of this PlmnId1.


        :param mcc: The mcc of this PlmnId1.
        :type mcc: str
        """
        if mcc is not None and not re.search(r'^[0-9]{3}$', mcc):  # noqa: E501
            raise ValueError("Invalid value for `mcc`, must be a follow pattern or equal to `/^[0-9]{3}$/`")  # noqa: E501

        self._mcc = mcc

    @property
    def mnc(self):
        """Gets the mnc of this PlmnId1.


        :return: The mnc of this PlmnId1.
        :rtype: str
        """
        return self._mnc

    @mnc.setter
    def mnc(self, mnc):
        """Sets the mnc of this PlmnId1.


        :param mnc: The mnc of this PlmnId1.
        :type mnc: str
        """
        if mnc is not None and not re.search(r'^[0-9]{2,3}$', mnc):  # noqa: E501
            raise ValueError("Invalid value for `mnc`, must be a follow pattern or equal to `/^[0-9]{2,3}$/`")  # noqa: E501

        self._mnc = mnc
