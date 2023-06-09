# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.c_son_pci_list import CSonPciList
from openapi_server import util

from openapi_server.models.c_son_pci_list import CSonPciList  # noqa: E501

class CPCIConfigurationFunctionSingleAllOfAttributes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, c_pci_configuration_control=None, c_son_pci_list=None):  # noqa: E501
        """CPCIConfigurationFunctionSingleAllOfAttributes - a model defined in OpenAPI

        :param c_pci_configuration_control: The c_pci_configuration_control of this CPCIConfigurationFunctionSingleAllOfAttributes.  # noqa: E501
        :type c_pci_configuration_control: bool
        :param c_son_pci_list: The c_son_pci_list of this CPCIConfigurationFunctionSingleAllOfAttributes.  # noqa: E501
        :type c_son_pci_list: CSonPciList
        """
        self.openapi_types = {
            'c_pci_configuration_control': bool,
            'c_son_pci_list': CSonPciList
        }

        self.attribute_map = {
            'c_pci_configuration_control': 'cPciConfigurationControl',
            'c_son_pci_list': 'cSonPciList'
        }

        self._c_pci_configuration_control = c_pci_configuration_control
        self._c_son_pci_list = c_son_pci_list

    @classmethod
    def from_dict(cls, dikt) -> 'CPCIConfigurationFunctionSingleAllOfAttributes':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CPCIConfigurationFunction_Single_allOf_attributes of this CPCIConfigurationFunctionSingleAllOfAttributes.  # noqa: E501
        :rtype: CPCIConfigurationFunctionSingleAllOfAttributes
        """
        return util.deserialize_model(dikt, cls)

    @property
    def c_pci_configuration_control(self):
        """Gets the c_pci_configuration_control of this CPCIConfigurationFunctionSingleAllOfAttributes.


        :return: The c_pci_configuration_control of this CPCIConfigurationFunctionSingleAllOfAttributes.
        :rtype: bool
        """
        return self._c_pci_configuration_control

    @c_pci_configuration_control.setter
    def c_pci_configuration_control(self, c_pci_configuration_control):
        """Sets the c_pci_configuration_control of this CPCIConfigurationFunctionSingleAllOfAttributes.


        :param c_pci_configuration_control: The c_pci_configuration_control of this CPCIConfigurationFunctionSingleAllOfAttributes.
        :type c_pci_configuration_control: bool
        """

        self._c_pci_configuration_control = c_pci_configuration_control

    @property
    def c_son_pci_list(self):
        """Gets the c_son_pci_list of this CPCIConfigurationFunctionSingleAllOfAttributes.


        :return: The c_son_pci_list of this CPCIConfigurationFunctionSingleAllOfAttributes.
        :rtype: CSonPciList
        """
        return self._c_son_pci_list

    @c_son_pci_list.setter
    def c_son_pci_list(self, c_son_pci_list):
        """Sets the c_son_pci_list of this CPCIConfigurationFunctionSingleAllOfAttributes.


        :param c_son_pci_list: The c_son_pci_list of this CPCIConfigurationFunctionSingleAllOfAttributes.
        :type c_son_pci_list: CSonPciList
        """

        self._c_son_pci_list = c_son_pci_list
