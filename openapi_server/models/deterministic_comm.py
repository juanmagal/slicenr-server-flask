# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.serv_attr_com import ServAttrCom
from openapi_server.models.support import Support
from openapi_server import util

from openapi_server.models.serv_attr_com import ServAttrCom  # noqa: E501
from openapi_server.models.support import Support  # noqa: E501

class DeterministicComm(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, serv_attr_com=None, availability=None, periodicity_list=None):  # noqa: E501
        """DeterministicComm - a model defined in OpenAPI

        :param serv_attr_com: The serv_attr_com of this DeterministicComm.  # noqa: E501
        :type serv_attr_com: ServAttrCom
        :param availability: The availability of this DeterministicComm.  # noqa: E501
        :type availability: Support
        :param periodicity_list: The periodicity_list of this DeterministicComm.  # noqa: E501
        :type periodicity_list: List[int]
        """
        self.openapi_types = {
            'serv_attr_com': ServAttrCom,
            'availability': Support,
            'periodicity_list': List[int]
        }

        self.attribute_map = {
            'serv_attr_com': 'servAttrCom',
            'availability': 'availability',
            'periodicity_list': 'periodicityList'
        }

        self._serv_attr_com = serv_attr_com
        self._availability = availability
        self._periodicity_list = periodicity_list

    @classmethod
    def from_dict(cls, dikt) -> 'DeterministicComm':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DeterministicComm of this DeterministicComm.  # noqa: E501
        :rtype: DeterministicComm
        """
        return util.deserialize_model(dikt, cls)

    @property
    def serv_attr_com(self):
        """Gets the serv_attr_com of this DeterministicComm.


        :return: The serv_attr_com of this DeterministicComm.
        :rtype: ServAttrCom
        """
        return self._serv_attr_com

    @serv_attr_com.setter
    def serv_attr_com(self, serv_attr_com):
        """Sets the serv_attr_com of this DeterministicComm.


        :param serv_attr_com: The serv_attr_com of this DeterministicComm.
        :type serv_attr_com: ServAttrCom
        """

        self._serv_attr_com = serv_attr_com

    @property
    def availability(self):
        """Gets the availability of this DeterministicComm.


        :return: The availability of this DeterministicComm.
        :rtype: Support
        """
        return self._availability

    @availability.setter
    def availability(self, availability):
        """Sets the availability of this DeterministicComm.


        :param availability: The availability of this DeterministicComm.
        :type availability: Support
        """

        self._availability = availability

    @property
    def periodicity_list(self):
        """Gets the periodicity_list of this DeterministicComm.


        :return: The periodicity_list of this DeterministicComm.
        :rtype: List[int]
        """
        return self._periodicity_list

    @periodicity_list.setter
    def periodicity_list(self, periodicity_list):
        """Sets the periodicity_list of this DeterministicComm.


        :param periodicity_list: The periodicity_list of this DeterministicComm.
        :type periodicity_list: List[int]
        """

        self._periodicity_list = periodicity_list