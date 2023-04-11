# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.ces_management_function_single import CESManagementFunctionSingle
from openapi_server.models.cpci_configuration_function_single import CPCIConfigurationFunctionSingle
from openapi_server.models.configurable5_qi_set_single import Configurable5QISetSingle
from openapi_server.models.des_management_function_single import DESManagementFunctionSingle
from openapi_server.models.dlbo_function_single import DLBOFunctionSingle
from openapi_server.models.dmro_function_single import DMROFunctionSingle
from openapi_server.models.dpci_configuration_function_single import DPCIConfigurationFunctionSingle
from openapi_server.models.drach_optimization_function_single import DRACHOptimizationFunctionSingle
from openapi_server.models.dynamic5_qi_set_single import Dynamic5QISetSingle
from openapi_server.models.gnb_cu_cp_function_single import GnbCuCpFunctionSingle
from openapi_server.models.gnb_cu_up_function_single import GnbCuUpFunctionSingle
from openapi_server.models.gnb_du_function_single import GnbDuFunctionSingle
from openapi_server import util

from openapi_server.models.ces_management_function_single import CESManagementFunctionSingle  # noqa: E501
from openapi_server.models.configurable5_qi_set_single import Configurable5QISetSingle  # noqa: E501
from openapi_server.models.cpci_configuration_function_single import CPCIConfigurationFunctionSingle  # noqa: E501
from openapi_server.models.des_management_function_single import DESManagementFunctionSingle  # noqa: E501
from openapi_server.models.dlbo_function_single import DLBOFunctionSingle  # noqa: E501
from openapi_server.models.dmro_function_single import DMROFunctionSingle  # noqa: E501
from openapi_server.models.dpci_configuration_function_single import DPCIConfigurationFunctionSingle  # noqa: E501
from openapi_server.models.drach_optimization_function_single import DRACHOptimizationFunctionSingle  # noqa: E501
from openapi_server.models.dynamic5_qi_set_single import Dynamic5QISetSingle  # noqa: E501
from openapi_server.models.gnb_cu_cp_function_single import GnbCuCpFunctionSingle  # noqa: E501
from openapi_server.models.gnb_cu_up_function_single import GnbCuUpFunctionSingle  # noqa: E501
from openapi_server.models.gnb_du_function_single import GnbDuFunctionSingle  # noqa: E501

class ManagedElementSingleAllOf1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, gnb_du_function=None, gnb_cu_up_function=None, gnb_cu_cp_function=None, des_management_function=None, drach_optimization_function=None, dmro_function=None, dlbo_function=None, dpci_configuration_function=None, cpci_configuration_function=None, ces_management_function=None, configurable5_qi_set=None, dynamic5_qi_set=None):  # noqa: E501
        """ManagedElementSingleAllOf1 - a model defined in OpenAPI

        :param gnb_du_function: The gnb_du_function of this ManagedElementSingleAllOf1.  # noqa: E501
        :type gnb_du_function: List[GnbDuFunctionSingle]
        :param gnb_cu_up_function: The gnb_cu_up_function of this ManagedElementSingleAllOf1.  # noqa: E501
        :type gnb_cu_up_function: List[GnbCuUpFunctionSingle]
        :param gnb_cu_cp_function: The gnb_cu_cp_function of this ManagedElementSingleAllOf1.  # noqa: E501
        :type gnb_cu_cp_function: List[GnbCuCpFunctionSingle]
        :param des_management_function: The des_management_function of this ManagedElementSingleAllOf1.  # noqa: E501
        :type des_management_function: DESManagementFunctionSingle
        :param drach_optimization_function: The drach_optimization_function of this ManagedElementSingleAllOf1.  # noqa: E501
        :type drach_optimization_function: DRACHOptimizationFunctionSingle
        :param dmro_function: The dmro_function of this ManagedElementSingleAllOf1.  # noqa: E501
        :type dmro_function: DMROFunctionSingle
        :param dlbo_function: The dlbo_function of this ManagedElementSingleAllOf1.  # noqa: E501
        :type dlbo_function: DLBOFunctionSingle
        :param dpci_configuration_function: The dpci_configuration_function of this ManagedElementSingleAllOf1.  # noqa: E501
        :type dpci_configuration_function: DPCIConfigurationFunctionSingle
        :param cpci_configuration_function: The cpci_configuration_function of this ManagedElementSingleAllOf1.  # noqa: E501
        :type cpci_configuration_function: CPCIConfigurationFunctionSingle
        :param ces_management_function: The ces_management_function of this ManagedElementSingleAllOf1.  # noqa: E501
        :type ces_management_function: CESManagementFunctionSingle
        :param configurable5_qi_set: The configurable5_qi_set of this ManagedElementSingleAllOf1.  # noqa: E501
        :type configurable5_qi_set: List[Configurable5QISetSingle]
        :param dynamic5_qi_set: The dynamic5_qi_set of this ManagedElementSingleAllOf1.  # noqa: E501
        :type dynamic5_qi_set: List[Dynamic5QISetSingle]
        """
        self.openapi_types = {
            'gnb_du_function': List[GnbDuFunctionSingle],
            'gnb_cu_up_function': List[GnbCuUpFunctionSingle],
            'gnb_cu_cp_function': List[GnbCuCpFunctionSingle],
            'des_management_function': DESManagementFunctionSingle,
            'drach_optimization_function': DRACHOptimizationFunctionSingle,
            'dmro_function': DMROFunctionSingle,
            'dlbo_function': DLBOFunctionSingle,
            'dpci_configuration_function': DPCIConfigurationFunctionSingle,
            'cpci_configuration_function': CPCIConfigurationFunctionSingle,
            'ces_management_function': CESManagementFunctionSingle,
            'configurable5_qi_set': List[Configurable5QISetSingle],
            'dynamic5_qi_set': List[Dynamic5QISetSingle]
        }

        self.attribute_map = {
            'gnb_du_function': 'GnbDuFunction',
            'gnb_cu_up_function': 'GnbCuUpFunction',
            'gnb_cu_cp_function': 'GnbCuCpFunction',
            'des_management_function': 'DESManagementFunction',
            'drach_optimization_function': 'DRACHOptimizationFunction',
            'dmro_function': 'DMROFunction',
            'dlbo_function': 'DLBOFunction',
            'dpci_configuration_function': 'DPCIConfigurationFunction',
            'cpci_configuration_function': 'CPCIConfigurationFunction',
            'ces_management_function': 'CESManagementFunction',
            'configurable5_qi_set': 'Configurable5QISet',
            'dynamic5_qi_set': 'Dynamic5QISet'
        }

        self._gnb_du_function = gnb_du_function
        self._gnb_cu_up_function = gnb_cu_up_function
        self._gnb_cu_cp_function = gnb_cu_cp_function
        self._des_management_function = des_management_function
        self._drach_optimization_function = drach_optimization_function
        self._dmro_function = dmro_function
        self._dlbo_function = dlbo_function
        self._dpci_configuration_function = dpci_configuration_function
        self._cpci_configuration_function = cpci_configuration_function
        self._ces_management_function = ces_management_function
        self._configurable5_qi_set = configurable5_qi_set
        self._dynamic5_qi_set = dynamic5_qi_set

    @classmethod
    def from_dict(cls, dikt) -> 'ManagedElementSingleAllOf1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ManagedElement_Single_allOf_1 of this ManagedElementSingleAllOf1.  # noqa: E501
        :rtype: ManagedElementSingleAllOf1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def gnb_du_function(self):
        """Gets the gnb_du_function of this ManagedElementSingleAllOf1.


        :return: The gnb_du_function of this ManagedElementSingleAllOf1.
        :rtype: List[GnbDuFunctionSingle]
        """
        return self._gnb_du_function

    @gnb_du_function.setter
    def gnb_du_function(self, gnb_du_function):
        """Sets the gnb_du_function of this ManagedElementSingleAllOf1.


        :param gnb_du_function: The gnb_du_function of this ManagedElementSingleAllOf1.
        :type gnb_du_function: List[GnbDuFunctionSingle]
        """

        self._gnb_du_function = gnb_du_function

    @property
    def gnb_cu_up_function(self):
        """Gets the gnb_cu_up_function of this ManagedElementSingleAllOf1.


        :return: The gnb_cu_up_function of this ManagedElementSingleAllOf1.
        :rtype: List[GnbCuUpFunctionSingle]
        """
        return self._gnb_cu_up_function

    @gnb_cu_up_function.setter
    def gnb_cu_up_function(self, gnb_cu_up_function):
        """Sets the gnb_cu_up_function of this ManagedElementSingleAllOf1.


        :param gnb_cu_up_function: The gnb_cu_up_function of this ManagedElementSingleAllOf1.
        :type gnb_cu_up_function: List[GnbCuUpFunctionSingle]
        """

        self._gnb_cu_up_function = gnb_cu_up_function

    @property
    def gnb_cu_cp_function(self):
        """Gets the gnb_cu_cp_function of this ManagedElementSingleAllOf1.


        :return: The gnb_cu_cp_function of this ManagedElementSingleAllOf1.
        :rtype: List[GnbCuCpFunctionSingle]
        """
        return self._gnb_cu_cp_function

    @gnb_cu_cp_function.setter
    def gnb_cu_cp_function(self, gnb_cu_cp_function):
        """Sets the gnb_cu_cp_function of this ManagedElementSingleAllOf1.


        :param gnb_cu_cp_function: The gnb_cu_cp_function of this ManagedElementSingleAllOf1.
        :type gnb_cu_cp_function: List[GnbCuCpFunctionSingle]
        """

        self._gnb_cu_cp_function = gnb_cu_cp_function

    @property
    def des_management_function(self):
        """Gets the des_management_function of this ManagedElementSingleAllOf1.


        :return: The des_management_function of this ManagedElementSingleAllOf1.
        :rtype: DESManagementFunctionSingle
        """
        return self._des_management_function

    @des_management_function.setter
    def des_management_function(self, des_management_function):
        """Sets the des_management_function of this ManagedElementSingleAllOf1.


        :param des_management_function: The des_management_function of this ManagedElementSingleAllOf1.
        :type des_management_function: DESManagementFunctionSingle
        """

        self._des_management_function = des_management_function

    @property
    def drach_optimization_function(self):
        """Gets the drach_optimization_function of this ManagedElementSingleAllOf1.


        :return: The drach_optimization_function of this ManagedElementSingleAllOf1.
        :rtype: DRACHOptimizationFunctionSingle
        """
        return self._drach_optimization_function

    @drach_optimization_function.setter
    def drach_optimization_function(self, drach_optimization_function):
        """Sets the drach_optimization_function of this ManagedElementSingleAllOf1.


        :param drach_optimization_function: The drach_optimization_function of this ManagedElementSingleAllOf1.
        :type drach_optimization_function: DRACHOptimizationFunctionSingle
        """

        self._drach_optimization_function = drach_optimization_function

    @property
    def dmro_function(self):
        """Gets the dmro_function of this ManagedElementSingleAllOf1.


        :return: The dmro_function of this ManagedElementSingleAllOf1.
        :rtype: DMROFunctionSingle
        """
        return self._dmro_function

    @dmro_function.setter
    def dmro_function(self, dmro_function):
        """Sets the dmro_function of this ManagedElementSingleAllOf1.


        :param dmro_function: The dmro_function of this ManagedElementSingleAllOf1.
        :type dmro_function: DMROFunctionSingle
        """

        self._dmro_function = dmro_function

    @property
    def dlbo_function(self):
        """Gets the dlbo_function of this ManagedElementSingleAllOf1.


        :return: The dlbo_function of this ManagedElementSingleAllOf1.
        :rtype: DLBOFunctionSingle
        """
        return self._dlbo_function

    @dlbo_function.setter
    def dlbo_function(self, dlbo_function):
        """Sets the dlbo_function of this ManagedElementSingleAllOf1.


        :param dlbo_function: The dlbo_function of this ManagedElementSingleAllOf1.
        :type dlbo_function: DLBOFunctionSingle
        """

        self._dlbo_function = dlbo_function

    @property
    def dpci_configuration_function(self):
        """Gets the dpci_configuration_function of this ManagedElementSingleAllOf1.


        :return: The dpci_configuration_function of this ManagedElementSingleAllOf1.
        :rtype: DPCIConfigurationFunctionSingle
        """
        return self._dpci_configuration_function

    @dpci_configuration_function.setter
    def dpci_configuration_function(self, dpci_configuration_function):
        """Sets the dpci_configuration_function of this ManagedElementSingleAllOf1.


        :param dpci_configuration_function: The dpci_configuration_function of this ManagedElementSingleAllOf1.
        :type dpci_configuration_function: DPCIConfigurationFunctionSingle
        """

        self._dpci_configuration_function = dpci_configuration_function

    @property
    def cpci_configuration_function(self):
        """Gets the cpci_configuration_function of this ManagedElementSingleAllOf1.


        :return: The cpci_configuration_function of this ManagedElementSingleAllOf1.
        :rtype: CPCIConfigurationFunctionSingle
        """
        return self._cpci_configuration_function

    @cpci_configuration_function.setter
    def cpci_configuration_function(self, cpci_configuration_function):
        """Sets the cpci_configuration_function of this ManagedElementSingleAllOf1.


        :param cpci_configuration_function: The cpci_configuration_function of this ManagedElementSingleAllOf1.
        :type cpci_configuration_function: CPCIConfigurationFunctionSingle
        """

        self._cpci_configuration_function = cpci_configuration_function

    @property
    def ces_management_function(self):
        """Gets the ces_management_function of this ManagedElementSingleAllOf1.


        :return: The ces_management_function of this ManagedElementSingleAllOf1.
        :rtype: CESManagementFunctionSingle
        """
        return self._ces_management_function

    @ces_management_function.setter
    def ces_management_function(self, ces_management_function):
        """Sets the ces_management_function of this ManagedElementSingleAllOf1.


        :param ces_management_function: The ces_management_function of this ManagedElementSingleAllOf1.
        :type ces_management_function: CESManagementFunctionSingle
        """

        self._ces_management_function = ces_management_function

    @property
    def configurable5_qi_set(self):
        """Gets the configurable5_qi_set of this ManagedElementSingleAllOf1.


        :return: The configurable5_qi_set of this ManagedElementSingleAllOf1.
        :rtype: List[Configurable5QISetSingle]
        """
        return self._configurable5_qi_set

    @configurable5_qi_set.setter
    def configurable5_qi_set(self, configurable5_qi_set):
        """Sets the configurable5_qi_set of this ManagedElementSingleAllOf1.


        :param configurable5_qi_set: The configurable5_qi_set of this ManagedElementSingleAllOf1.
        :type configurable5_qi_set: List[Configurable5QISetSingle]
        """

        self._configurable5_qi_set = configurable5_qi_set

    @property
    def dynamic5_qi_set(self):
        """Gets the dynamic5_qi_set of this ManagedElementSingleAllOf1.


        :return: The dynamic5_qi_set of this ManagedElementSingleAllOf1.
        :rtype: List[Dynamic5QISetSingle]
        """
        return self._dynamic5_qi_set

    @dynamic5_qi_set.setter
    def dynamic5_qi_set(self, dynamic5_qi_set):
        """Sets the dynamic5_qi_set of this ManagedElementSingleAllOf1.


        :param dynamic5_qi_set: The dynamic5_qi_set of this ManagedElementSingleAllOf1.
        :type dynamic5_qi_set: List[Dynamic5QISetSingle]
        """

        self._dynamic5_qi_set = dynamic5_qi_set