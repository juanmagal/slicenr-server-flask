# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.ipv6_addr1 import Ipv6Addr1
import re
from openapi_server import util

from openapi_server.models.ipv6_addr1 import Ipv6Addr1  # noqa: E501
import re  # noqa: E501

class RouteInformation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ipv4_addr=None, ipv6_addr=None, port_number=None):  # noqa: E501
        """RouteInformation - a model defined in OpenAPI

        :param ipv4_addr: The ipv4_addr of this RouteInformation.  # noqa: E501
        :type ipv4_addr: str
        :param ipv6_addr: The ipv6_addr of this RouteInformation.  # noqa: E501
        :type ipv6_addr: Ipv6Addr1
        :param port_number: The port_number of this RouteInformation.  # noqa: E501
        :type port_number: int
        """
        self.openapi_types = {
            'ipv4_addr': str,
            'ipv6_addr': Ipv6Addr1,
            'port_number': int
        }

        self.attribute_map = {
            'ipv4_addr': 'ipv4Addr',
            'ipv6_addr': 'ipv6Addr',
            'port_number': 'portNumber'
        }

        self._ipv4_addr = ipv4_addr
        self._ipv6_addr = ipv6_addr
        self._port_number = port_number

    @classmethod
    def from_dict(cls, dikt) -> 'RouteInformation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RouteInformation of this RouteInformation.  # noqa: E501
        :rtype: RouteInformation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ipv4_addr(self):
        """Gets the ipv4_addr of this RouteInformation.

        String identifying a IPv4 address formatted in the 'dotted decimal' notation as defined in RFC 1166.   # noqa: E501

        :return: The ipv4_addr of this RouteInformation.
        :rtype: str
        """
        return self._ipv4_addr

    @ipv4_addr.setter
    def ipv4_addr(self, ipv4_addr):
        """Sets the ipv4_addr of this RouteInformation.

        String identifying a IPv4 address formatted in the 'dotted decimal' notation as defined in RFC 1166.   # noqa: E501

        :param ipv4_addr: The ipv4_addr of this RouteInformation.
        :type ipv4_addr: str
        """
        if ipv4_addr is not None and not re.search(r'^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$', ipv4_addr):  # noqa: E501
            raise ValueError("Invalid value for `ipv4_addr`, must be a follow pattern or equal to `/^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$/`")  # noqa: E501

        self._ipv4_addr = ipv4_addr

    @property
    def ipv6_addr(self):
        """Gets the ipv6_addr of this RouteInformation.


        :return: The ipv6_addr of this RouteInformation.
        :rtype: Ipv6Addr1
        """
        return self._ipv6_addr

    @ipv6_addr.setter
    def ipv6_addr(self, ipv6_addr):
        """Sets the ipv6_addr of this RouteInformation.


        :param ipv6_addr: The ipv6_addr of this RouteInformation.
        :type ipv6_addr: Ipv6Addr1
        """

        self._ipv6_addr = ipv6_addr

    @property
    def port_number(self):
        """Gets the port_number of this RouteInformation.

        Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.  # noqa: E501

        :return: The port_number of this RouteInformation.
        :rtype: int
        """
        return self._port_number

    @port_number.setter
    def port_number(self, port_number):
        """Sets the port_number of this RouteInformation.

        Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.  # noqa: E501

        :param port_number: The port_number of this RouteInformation.
        :type port_number: int
        """
        if port_number is None:
            raise ValueError("Invalid value for `port_number`, must not be `None`")  # noqa: E501
        if port_number is not None and port_number < 0:  # noqa: E501
            raise ValueError("Invalid value for `port_number`, must be a value greater than or equal to `0`")  # noqa: E501

        self._port_number = port_number
