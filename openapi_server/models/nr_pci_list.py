# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class NRPciList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, nr_pci=None):  # noqa: E501
        """NRPciList - a model defined in OpenAPI

        :param nr_pci: The nr_pci of this NRPciList.  # noqa: E501
        :type nr_pci: int
        """
        self.openapi_types = {
            'nr_pci': int
        }

        self.attribute_map = {
            'nr_pci': 'NRPci'
        }

        self._nr_pci = nr_pci

    @classmethod
    def from_dict(cls, dikt) -> 'NRPciList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NRPciList of this NRPciList.  # noqa: E501
        :rtype: NRPciList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nr_pci(self):
        """Gets the nr_pci of this NRPciList.


        :return: The nr_pci of this NRPciList.
        :rtype: int
        """
        return self._nr_pci

    @nr_pci.setter
    def nr_pci(self, nr_pci):
        """Sets the nr_pci of this NRPciList.


        :param nr_pci: The nr_pci of this NRPciList.
        :type nr_pci: int
        """

        self._nr_pci = nr_pci
