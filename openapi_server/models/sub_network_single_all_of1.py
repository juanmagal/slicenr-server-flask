# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.cco_function_single import CCOFunctionSingle
from openapi_server.models.ces_management_function_single import CESManagementFunctionSingle
from openapi_server.models.cpci_configuration_function_single import CPCIConfigurationFunctionSingle
from openapi_server.models.configurable5_qi_set_single import Configurable5QISetSingle
from openapi_server.models.des_management_function_single import DESManagementFunctionSingle
from openapi_server.models.dlbo_function_single import DLBOFunctionSingle
from openapi_server.models.dmro_function_single import DMROFunctionSingle
from openapi_server.models.dpci_configuration_function_single import DPCIConfigurationFunctionSingle
from openapi_server.models.drach_optimization_function_single import DRACHOptimizationFunctionSingle
from openapi_server.models.dynamic5_qi_set_single import Dynamic5QISetSingle
from openapi_server.models.e_utran_frequency_single import EUtranFrequencySingle
from openapi_server.models.external_enb_function_single import ExternalENBFunctionSingle
from openapi_server.models.external_gnb_cu_cp_function_single import ExternalGnbCuCpFunctionSingle
from openapi_server.models.managed_element_single import ManagedElementSingle
from openapi_server.models.nr_frequency_single import NRFrequencySingle
from openapi_server.models.rim_rs_global_single import RimRSGlobalSingle
from openapi_server.models.sub_network_single import SubNetworkSingle
from openapi_server import util

from openapi_server.models.cco_function_single import CCOFunctionSingle  # noqa: E501
from openapi_server.models.ces_management_function_single import CESManagementFunctionSingle  # noqa: E501
from openapi_server.models.configurable5_qi_set_single import Configurable5QISetSingle  # noqa: E501
from openapi_server.models.cpci_configuration_function_single import CPCIConfigurationFunctionSingle  # noqa: E501
from openapi_server.models.des_management_function_single import DESManagementFunctionSingle  # noqa: E501
from openapi_server.models.dlbo_function_single import DLBOFunctionSingle  # noqa: E501
from openapi_server.models.dmro_function_single import DMROFunctionSingle  # noqa: E501
from openapi_server.models.dpci_configuration_function_single import DPCIConfigurationFunctionSingle  # noqa: E501
from openapi_server.models.drach_optimization_function_single import DRACHOptimizationFunctionSingle  # noqa: E501
from openapi_server.models.dynamic5_qi_set_single import Dynamic5QISetSingle  # noqa: E501
from openapi_server.models.e_utran_frequency_single import EUtranFrequencySingle  # noqa: E501
from openapi_server.models.external_enb_function_single import ExternalENBFunctionSingle  # noqa: E501
from openapi_server.models.external_gnb_cu_cp_function_single import ExternalGnbCuCpFunctionSingle  # noqa: E501
from openapi_server.models.managed_element_single import ManagedElementSingle  # noqa: E501
from openapi_server.models.nr_frequency_single import NRFrequencySingle  # noqa: E501
from openapi_server.models.rim_rs_global_single import RimRSGlobalSingle  # noqa: E501
from openapi_server.models.sub_network_single import SubNetworkSingle  # noqa: E501

class SubNetworkSingleAllOf1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, sub_network=None, managed_element=None, nr_frequency=None, external_gnb_cu_cp_function=None, external_enb_function=None, e_utran_frequency=None, des_management_function=None, drach_optimization_function=None, dmro_function=None, dlbo_function=None, dpci_configuration_function=None, cpci_configuration_function=None, ces_management_function=None, configurable5_qi_set=None, rim_rs_global=None, dynamic5_qi_set=None, cco_function=None):  # noqa: E501
        """SubNetworkSingleAllOf1 - a model defined in OpenAPI

        :param sub_network: The sub_network of this SubNetworkSingleAllOf1.  # noqa: E501
        :type sub_network: List[SubNetworkSingle]
        :param managed_element: The managed_element of this SubNetworkSingleAllOf1.  # noqa: E501
        :type managed_element: List[ManagedElementSingle]
        :param nr_frequency: The nr_frequency of this SubNetworkSingleAllOf1.  # noqa: E501
        :type nr_frequency: List[NRFrequencySingle]
        :param external_gnb_cu_cp_function: The external_gnb_cu_cp_function of this SubNetworkSingleAllOf1.  # noqa: E501
        :type external_gnb_cu_cp_function: List[ExternalGnbCuCpFunctionSingle]
        :param external_enb_function: The external_enb_function of this SubNetworkSingleAllOf1.  # noqa: E501
        :type external_enb_function: List[ExternalENBFunctionSingle]
        :param e_utran_frequency: The e_utran_frequency of this SubNetworkSingleAllOf1.  # noqa: E501
        :type e_utran_frequency: List[EUtranFrequencySingle]
        :param des_management_function: The des_management_function of this SubNetworkSingleAllOf1.  # noqa: E501
        :type des_management_function: DESManagementFunctionSingle
        :param drach_optimization_function: The drach_optimization_function of this SubNetworkSingleAllOf1.  # noqa: E501
        :type drach_optimization_function: DRACHOptimizationFunctionSingle
        :param dmro_function: The dmro_function of this SubNetworkSingleAllOf1.  # noqa: E501
        :type dmro_function: DMROFunctionSingle
        :param dlbo_function: The dlbo_function of this SubNetworkSingleAllOf1.  # noqa: E501
        :type dlbo_function: DLBOFunctionSingle
        :param dpci_configuration_function: The dpci_configuration_function of this SubNetworkSingleAllOf1.  # noqa: E501
        :type dpci_configuration_function: DPCIConfigurationFunctionSingle
        :param cpci_configuration_function: The cpci_configuration_function of this SubNetworkSingleAllOf1.  # noqa: E501
        :type cpci_configuration_function: CPCIConfigurationFunctionSingle
        :param ces_management_function: The ces_management_function of this SubNetworkSingleAllOf1.  # noqa: E501
        :type ces_management_function: CESManagementFunctionSingle
        :param configurable5_qi_set: The configurable5_qi_set of this SubNetworkSingleAllOf1.  # noqa: E501
        :type configurable5_qi_set: List[Configurable5QISetSingle]
        :param rim_rs_global: The rim_rs_global of this SubNetworkSingleAllOf1.  # noqa: E501
        :type rim_rs_global: RimRSGlobalSingle
        :param dynamic5_qi_set: The dynamic5_qi_set of this SubNetworkSingleAllOf1.  # noqa: E501
        :type dynamic5_qi_set: List[Dynamic5QISetSingle]
        :param cco_function: The cco_function of this SubNetworkSingleAllOf1.  # noqa: E501
        :type cco_function: CCOFunctionSingle
        """
        self.openapi_types = {
            'sub_network': List[SubNetworkSingle],
            'managed_element': List[ManagedElementSingle],
            'nr_frequency': List[NRFrequencySingle],
            'external_gnb_cu_cp_function': List[ExternalGnbCuCpFunctionSingle],
            'external_enb_function': List[ExternalENBFunctionSingle],
            'e_utran_frequency': List[EUtranFrequencySingle],
            'des_management_function': DESManagementFunctionSingle,
            'drach_optimization_function': DRACHOptimizationFunctionSingle,
            'dmro_function': DMROFunctionSingle,
            'dlbo_function': DLBOFunctionSingle,
            'dpci_configuration_function': DPCIConfigurationFunctionSingle,
            'cpci_configuration_function': CPCIConfigurationFunctionSingle,
            'ces_management_function': CESManagementFunctionSingle,
            'configurable5_qi_set': List[Configurable5QISetSingle],
            'rim_rs_global': RimRSGlobalSingle,
            'dynamic5_qi_set': List[Dynamic5QISetSingle],
            'cco_function': CCOFunctionSingle
        }

        self.attribute_map = {
            'sub_network': 'SubNetwork',
            'managed_element': 'ManagedElement',
            'nr_frequency': 'NRFrequency',
            'external_gnb_cu_cp_function': 'ExternalGnbCuCpFunction',
            'external_enb_function': 'ExternalENBFunction',
            'e_utran_frequency': 'EUtranFrequency',
            'des_management_function': 'DESManagementFunction',
            'drach_optimization_function': 'DRACHOptimizationFunction',
            'dmro_function': 'DMROFunction',
            'dlbo_function': 'DLBOFunction',
            'dpci_configuration_function': 'DPCIConfigurationFunction',
            'cpci_configuration_function': 'CPCIConfigurationFunction',
            'ces_management_function': 'CESManagementFunction',
            'configurable5_qi_set': 'Configurable5QISet',
            'rim_rs_global': 'RimRSGlobal',
            'dynamic5_qi_set': 'Dynamic5QISet',
            'cco_function': 'CCOFunction'
        }

        self._sub_network = sub_network
        self._managed_element = managed_element
        self._nr_frequency = nr_frequency
        self._external_gnb_cu_cp_function = external_gnb_cu_cp_function
        self._external_enb_function = external_enb_function
        self._e_utran_frequency = e_utran_frequency
        self._des_management_function = des_management_function
        self._drach_optimization_function = drach_optimization_function
        self._dmro_function = dmro_function
        self._dlbo_function = dlbo_function
        self._dpci_configuration_function = dpci_configuration_function
        self._cpci_configuration_function = cpci_configuration_function
        self._ces_management_function = ces_management_function
        self._configurable5_qi_set = configurable5_qi_set
        self._rim_rs_global = rim_rs_global
        self._dynamic5_qi_set = dynamic5_qi_set
        self._cco_function = cco_function

    @classmethod
    def from_dict(cls, dikt) -> 'SubNetworkSingleAllOf1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SubNetwork_Single_allOf_1 of this SubNetworkSingleAllOf1.  # noqa: E501
        :rtype: SubNetworkSingleAllOf1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sub_network(self):
        """Gets the sub_network of this SubNetworkSingleAllOf1.


        :return: The sub_network of this SubNetworkSingleAllOf1.
        :rtype: List[SubNetworkSingle]
        """
        return self._sub_network

    @sub_network.setter
    def sub_network(self, sub_network):
        """Sets the sub_network of this SubNetworkSingleAllOf1.


        :param sub_network: The sub_network of this SubNetworkSingleAllOf1.
        :type sub_network: List[SubNetworkSingle]
        """

        self._sub_network = sub_network

    @property
    def managed_element(self):
        """Gets the managed_element of this SubNetworkSingleAllOf1.


        :return: The managed_element of this SubNetworkSingleAllOf1.
        :rtype: List[ManagedElementSingle]
        """
        return self._managed_element

    @managed_element.setter
    def managed_element(self, managed_element):
        """Sets the managed_element of this SubNetworkSingleAllOf1.


        :param managed_element: The managed_element of this SubNetworkSingleAllOf1.
        :type managed_element: List[ManagedElementSingle]
        """

        self._managed_element = managed_element

    @property
    def nr_frequency(self):
        """Gets the nr_frequency of this SubNetworkSingleAllOf1.


        :return: The nr_frequency of this SubNetworkSingleAllOf1.
        :rtype: List[NRFrequencySingle]
        """
        return self._nr_frequency

    @nr_frequency.setter
    def nr_frequency(self, nr_frequency):
        """Sets the nr_frequency of this SubNetworkSingleAllOf1.


        :param nr_frequency: The nr_frequency of this SubNetworkSingleAllOf1.
        :type nr_frequency: List[NRFrequencySingle]
        """
        if nr_frequency is not None and len(nr_frequency) < 1:
            raise ValueError("Invalid value for `nr_frequency`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._nr_frequency = nr_frequency

    @property
    def external_gnb_cu_cp_function(self):
        """Gets the external_gnb_cu_cp_function of this SubNetworkSingleAllOf1.


        :return: The external_gnb_cu_cp_function of this SubNetworkSingleAllOf1.
        :rtype: List[ExternalGnbCuCpFunctionSingle]
        """
        return self._external_gnb_cu_cp_function

    @external_gnb_cu_cp_function.setter
    def external_gnb_cu_cp_function(self, external_gnb_cu_cp_function):
        """Sets the external_gnb_cu_cp_function of this SubNetworkSingleAllOf1.


        :param external_gnb_cu_cp_function: The external_gnb_cu_cp_function of this SubNetworkSingleAllOf1.
        :type external_gnb_cu_cp_function: List[ExternalGnbCuCpFunctionSingle]
        """

        self._external_gnb_cu_cp_function = external_gnb_cu_cp_function

    @property
    def external_enb_function(self):
        """Gets the external_enb_function of this SubNetworkSingleAllOf1.


        :return: The external_enb_function of this SubNetworkSingleAllOf1.
        :rtype: List[ExternalENBFunctionSingle]
        """
        return self._external_enb_function

    @external_enb_function.setter
    def external_enb_function(self, external_enb_function):
        """Sets the external_enb_function of this SubNetworkSingleAllOf1.


        :param external_enb_function: The external_enb_function of this SubNetworkSingleAllOf1.
        :type external_enb_function: List[ExternalENBFunctionSingle]
        """

        self._external_enb_function = external_enb_function

    @property
    def e_utran_frequency(self):
        """Gets the e_utran_frequency of this SubNetworkSingleAllOf1.


        :return: The e_utran_frequency of this SubNetworkSingleAllOf1.
        :rtype: List[EUtranFrequencySingle]
        """
        return self._e_utran_frequency

    @e_utran_frequency.setter
    def e_utran_frequency(self, e_utran_frequency):
        """Sets the e_utran_frequency of this SubNetworkSingleAllOf1.


        :param e_utran_frequency: The e_utran_frequency of this SubNetworkSingleAllOf1.
        :type e_utran_frequency: List[EUtranFrequencySingle]
        """
        if e_utran_frequency is not None and len(e_utran_frequency) < 1:
            raise ValueError("Invalid value for `e_utran_frequency`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._e_utran_frequency = e_utran_frequency

    @property
    def des_management_function(self):
        """Gets the des_management_function of this SubNetworkSingleAllOf1.


        :return: The des_management_function of this SubNetworkSingleAllOf1.
        :rtype: DESManagementFunctionSingle
        """
        return self._des_management_function

    @des_management_function.setter
    def des_management_function(self, des_management_function):
        """Sets the des_management_function of this SubNetworkSingleAllOf1.


        :param des_management_function: The des_management_function of this SubNetworkSingleAllOf1.
        :type des_management_function: DESManagementFunctionSingle
        """

        self._des_management_function = des_management_function

    @property
    def drach_optimization_function(self):
        """Gets the drach_optimization_function of this SubNetworkSingleAllOf1.


        :return: The drach_optimization_function of this SubNetworkSingleAllOf1.
        :rtype: DRACHOptimizationFunctionSingle
        """
        return self._drach_optimization_function

    @drach_optimization_function.setter
    def drach_optimization_function(self, drach_optimization_function):
        """Sets the drach_optimization_function of this SubNetworkSingleAllOf1.


        :param drach_optimization_function: The drach_optimization_function of this SubNetworkSingleAllOf1.
        :type drach_optimization_function: DRACHOptimizationFunctionSingle
        """

        self._drach_optimization_function = drach_optimization_function

    @property
    def dmro_function(self):
        """Gets the dmro_function of this SubNetworkSingleAllOf1.


        :return: The dmro_function of this SubNetworkSingleAllOf1.
        :rtype: DMROFunctionSingle
        """
        return self._dmro_function

    @dmro_function.setter
    def dmro_function(self, dmro_function):
        """Sets the dmro_function of this SubNetworkSingleAllOf1.


        :param dmro_function: The dmro_function of this SubNetworkSingleAllOf1.
        :type dmro_function: DMROFunctionSingle
        """

        self._dmro_function = dmro_function

    @property
    def dlbo_function(self):
        """Gets the dlbo_function of this SubNetworkSingleAllOf1.


        :return: The dlbo_function of this SubNetworkSingleAllOf1.
        :rtype: DLBOFunctionSingle
        """
        return self._dlbo_function

    @dlbo_function.setter
    def dlbo_function(self, dlbo_function):
        """Sets the dlbo_function of this SubNetworkSingleAllOf1.


        :param dlbo_function: The dlbo_function of this SubNetworkSingleAllOf1.
        :type dlbo_function: DLBOFunctionSingle
        """

        self._dlbo_function = dlbo_function

    @property
    def dpci_configuration_function(self):
        """Gets the dpci_configuration_function of this SubNetworkSingleAllOf1.


        :return: The dpci_configuration_function of this SubNetworkSingleAllOf1.
        :rtype: DPCIConfigurationFunctionSingle
        """
        return self._dpci_configuration_function

    @dpci_configuration_function.setter
    def dpci_configuration_function(self, dpci_configuration_function):
        """Sets the dpci_configuration_function of this SubNetworkSingleAllOf1.


        :param dpci_configuration_function: The dpci_configuration_function of this SubNetworkSingleAllOf1.
        :type dpci_configuration_function: DPCIConfigurationFunctionSingle
        """

        self._dpci_configuration_function = dpci_configuration_function

    @property
    def cpci_configuration_function(self):
        """Gets the cpci_configuration_function of this SubNetworkSingleAllOf1.


        :return: The cpci_configuration_function of this SubNetworkSingleAllOf1.
        :rtype: CPCIConfigurationFunctionSingle
        """
        return self._cpci_configuration_function

    @cpci_configuration_function.setter
    def cpci_configuration_function(self, cpci_configuration_function):
        """Sets the cpci_configuration_function of this SubNetworkSingleAllOf1.


        :param cpci_configuration_function: The cpci_configuration_function of this SubNetworkSingleAllOf1.
        :type cpci_configuration_function: CPCIConfigurationFunctionSingle
        """

        self._cpci_configuration_function = cpci_configuration_function

    @property
    def ces_management_function(self):
        """Gets the ces_management_function of this SubNetworkSingleAllOf1.


        :return: The ces_management_function of this SubNetworkSingleAllOf1.
        :rtype: CESManagementFunctionSingle
        """
        return self._ces_management_function

    @ces_management_function.setter
    def ces_management_function(self, ces_management_function):
        """Sets the ces_management_function of this SubNetworkSingleAllOf1.


        :param ces_management_function: The ces_management_function of this SubNetworkSingleAllOf1.
        :type ces_management_function: CESManagementFunctionSingle
        """

        self._ces_management_function = ces_management_function

    @property
    def configurable5_qi_set(self):
        """Gets the configurable5_qi_set of this SubNetworkSingleAllOf1.


        :return: The configurable5_qi_set of this SubNetworkSingleAllOf1.
        :rtype: List[Configurable5QISetSingle]
        """
        return self._configurable5_qi_set

    @configurable5_qi_set.setter
    def configurable5_qi_set(self, configurable5_qi_set):
        """Sets the configurable5_qi_set of this SubNetworkSingleAllOf1.


        :param configurable5_qi_set: The configurable5_qi_set of this SubNetworkSingleAllOf1.
        :type configurable5_qi_set: List[Configurable5QISetSingle]
        """

        self._configurable5_qi_set = configurable5_qi_set

    @property
    def rim_rs_global(self):
        """Gets the rim_rs_global of this SubNetworkSingleAllOf1.


        :return: The rim_rs_global of this SubNetworkSingleAllOf1.
        :rtype: RimRSGlobalSingle
        """
        return self._rim_rs_global

    @rim_rs_global.setter
    def rim_rs_global(self, rim_rs_global):
        """Sets the rim_rs_global of this SubNetworkSingleAllOf1.


        :param rim_rs_global: The rim_rs_global of this SubNetworkSingleAllOf1.
        :type rim_rs_global: RimRSGlobalSingle
        """

        self._rim_rs_global = rim_rs_global

    @property
    def dynamic5_qi_set(self):
        """Gets the dynamic5_qi_set of this SubNetworkSingleAllOf1.


        :return: The dynamic5_qi_set of this SubNetworkSingleAllOf1.
        :rtype: List[Dynamic5QISetSingle]
        """
        return self._dynamic5_qi_set

    @dynamic5_qi_set.setter
    def dynamic5_qi_set(self, dynamic5_qi_set):
        """Sets the dynamic5_qi_set of this SubNetworkSingleAllOf1.


        :param dynamic5_qi_set: The dynamic5_qi_set of this SubNetworkSingleAllOf1.
        :type dynamic5_qi_set: List[Dynamic5QISetSingle]
        """

        self._dynamic5_qi_set = dynamic5_qi_set

    @property
    def cco_function(self):
        """Gets the cco_function of this SubNetworkSingleAllOf1.


        :return: The cco_function of this SubNetworkSingleAllOf1.
        :rtype: CCOFunctionSingle
        """
        return self._cco_function

    @cco_function.setter
    def cco_function(self, cco_function):
        """Sets the cco_function of this SubNetworkSingleAllOf1.


        :param cco_function: The cco_function of this SubNetworkSingleAllOf1.
        :type cco_function: CCOFunctionSingle
        """

        self._cco_function = cco_function
