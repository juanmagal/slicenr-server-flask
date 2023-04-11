# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.delay_tolerance import DelayTolerance
from openapi_server.models.deterministic_comm import DeterministicComm
from openapi_server.models.mobility_level import MobilityLevel
from openapi_server.models.positioning_ran_subnet import PositioningRANSubnet
from openapi_server.models.sharing_level import SharingLevel
from openapi_server.models.slice_simultaneous_use import SliceSimultaneousUse
from openapi_server.models.synchronicity_ran_subnet import SynchronicityRANSubnet
from openapi_server.models.term_density import TermDensity
from openapi_server.models.xl_thpt import XLThpt
from openapi_server import util

from openapi_server.models.delay_tolerance import DelayTolerance  # noqa: E501
from openapi_server.models.deterministic_comm import DeterministicComm  # noqa: E501
from openapi_server.models.mobility_level import MobilityLevel  # noqa: E501
from openapi_server.models.positioning_ran_subnet import PositioningRANSubnet  # noqa: E501
from openapi_server.models.sharing_level import SharingLevel  # noqa: E501
from openapi_server.models.slice_simultaneous_use import SliceSimultaneousUse  # noqa: E501
from openapi_server.models.synchronicity_ran_subnet import SynchronicityRANSubnet  # noqa: E501
from openapi_server.models.term_density import TermDensity  # noqa: E501
from openapi_server.models.xl_thpt import XLThpt  # noqa: E501

class RANSliceSubnetProfile(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, coverage_area_ta_list=None, d_l_latency=None, u_l_latency=None, u_e_mobility_level=None, resource_sharing_level=None, max_numberof_ues=None, activity_factor=None, d_l_thpt_per_slice_subnet=None, d_l_thpt_per_ue=None, u_l_thpt_per_slice_subnet=None, u_l_thpt_per_ue=None, u_e_speed=None, reliability=None, s_st=None, d_l_max_pkt_size=None, u_l_max_pkt_size=None, n_r_operating_bands=None, delay_tolerance=None, positioning=None, slice_simultaneous_use=None, energy_efficiency=None, term_density=None, survival_time=None, synchronicity=None, d_l_deterministic_comm=None, u_l_deterministic_comm=None):  # noqa: E501
        """RANSliceSubnetProfile - a model defined in OpenAPI

        :param coverage_area_ta_list: The coverage_area_ta_list of this RANSliceSubnetProfile.  # noqa: E501
        :type coverage_area_ta_list: List[int]
        :param d_l_latency: The d_l_latency of this RANSliceSubnetProfile.  # noqa: E501
        :type d_l_latency: float
        :param u_l_latency: The u_l_latency of this RANSliceSubnetProfile.  # noqa: E501
        :type u_l_latency: float
        :param u_e_mobility_level: The u_e_mobility_level of this RANSliceSubnetProfile.  # noqa: E501
        :type u_e_mobility_level: MobilityLevel
        :param resource_sharing_level: The resource_sharing_level of this RANSliceSubnetProfile.  # noqa: E501
        :type resource_sharing_level: SharingLevel
        :param max_numberof_ues: The max_numberof_ues of this RANSliceSubnetProfile.  # noqa: E501
        :type max_numberof_ues: int
        :param activity_factor: The activity_factor of this RANSliceSubnetProfile.  # noqa: E501
        :type activity_factor: int
        :param d_l_thpt_per_slice_subnet: The d_l_thpt_per_slice_subnet of this RANSliceSubnetProfile.  # noqa: E501
        :type d_l_thpt_per_slice_subnet: XLThpt
        :param d_l_thpt_per_ue: The d_l_thpt_per_ue of this RANSliceSubnetProfile.  # noqa: E501
        :type d_l_thpt_per_ue: XLThpt
        :param u_l_thpt_per_slice_subnet: The u_l_thpt_per_slice_subnet of this RANSliceSubnetProfile.  # noqa: E501
        :type u_l_thpt_per_slice_subnet: XLThpt
        :param u_l_thpt_per_ue: The u_l_thpt_per_ue of this RANSliceSubnetProfile.  # noqa: E501
        :type u_l_thpt_per_ue: XLThpt
        :param u_e_speed: The u_e_speed of this RANSliceSubnetProfile.  # noqa: E501
        :type u_e_speed: int
        :param reliability: The reliability of this RANSliceSubnetProfile.  # noqa: E501
        :type reliability: float
        :param s_st: The s_st of this RANSliceSubnetProfile.  # noqa: E501
        :type s_st: int
        :param d_l_max_pkt_size: The d_l_max_pkt_size of this RANSliceSubnetProfile.  # noqa: E501
        :type d_l_max_pkt_size: int
        :param u_l_max_pkt_size: The u_l_max_pkt_size of this RANSliceSubnetProfile.  # noqa: E501
        :type u_l_max_pkt_size: int
        :param n_r_operating_bands: The n_r_operating_bands of this RANSliceSubnetProfile.  # noqa: E501
        :type n_r_operating_bands: str
        :param delay_tolerance: The delay_tolerance of this RANSliceSubnetProfile.  # noqa: E501
        :type delay_tolerance: DelayTolerance
        :param positioning: The positioning of this RANSliceSubnetProfile.  # noqa: E501
        :type positioning: PositioningRANSubnet
        :param slice_simultaneous_use: The slice_simultaneous_use of this RANSliceSubnetProfile.  # noqa: E501
        :type slice_simultaneous_use: SliceSimultaneousUse
        :param energy_efficiency: The energy_efficiency of this RANSliceSubnetProfile.  # noqa: E501
        :type energy_efficiency: float
        :param term_density: The term_density of this RANSliceSubnetProfile.  # noqa: E501
        :type term_density: TermDensity
        :param survival_time: The survival_time of this RANSliceSubnetProfile.  # noqa: E501
        :type survival_time: float
        :param synchronicity: The synchronicity of this RANSliceSubnetProfile.  # noqa: E501
        :type synchronicity: SynchronicityRANSubnet
        :param d_l_deterministic_comm: The d_l_deterministic_comm of this RANSliceSubnetProfile.  # noqa: E501
        :type d_l_deterministic_comm: DeterministicComm
        :param u_l_deterministic_comm: The u_l_deterministic_comm of this RANSliceSubnetProfile.  # noqa: E501
        :type u_l_deterministic_comm: DeterministicComm
        """
        self.openapi_types = {
            'coverage_area_ta_list': List[int],
            'd_l_latency': float,
            'u_l_latency': float,
            'u_e_mobility_level': MobilityLevel,
            'resource_sharing_level': SharingLevel,
            'max_numberof_ues': int,
            'activity_factor': int,
            'd_l_thpt_per_slice_subnet': XLThpt,
            'd_l_thpt_per_ue': XLThpt,
            'u_l_thpt_per_slice_subnet': XLThpt,
            'u_l_thpt_per_ue': XLThpt,
            'u_e_speed': int,
            'reliability': float,
            's_st': int,
            'd_l_max_pkt_size': int,
            'u_l_max_pkt_size': int,
            'n_r_operating_bands': str,
            'delay_tolerance': DelayTolerance,
            'positioning': PositioningRANSubnet,
            'slice_simultaneous_use': SliceSimultaneousUse,
            'energy_efficiency': float,
            'term_density': TermDensity,
            'survival_time': float,
            'synchronicity': SynchronicityRANSubnet,
            'd_l_deterministic_comm': DeterministicComm,
            'u_l_deterministic_comm': DeterministicComm
        }

        self.attribute_map = {
            'coverage_area_ta_list': 'coverageAreaTAList',
            'd_l_latency': 'dLLatency',
            'u_l_latency': 'uLLatency',
            'u_e_mobility_level': 'uEMobilityLevel',
            'resource_sharing_level': 'resourceSharingLevel',
            'max_numberof_ues': 'maxNumberofUEs',
            'activity_factor': 'activityFactor',
            'd_l_thpt_per_slice_subnet': 'dLThptPerSliceSubnet',
            'd_l_thpt_per_ue': 'dLThptPerUE',
            'u_l_thpt_per_slice_subnet': 'uLThptPerSliceSubnet',
            'u_l_thpt_per_ue': 'uLThptPerUE',
            'u_e_speed': 'uESpeed',
            'reliability': 'reliability',
            's_st': 'sST',
            'd_l_max_pkt_size': 'dLMaxPktSize',
            'u_l_max_pkt_size': 'uLMaxPktSize',
            'n_r_operating_bands': 'nROperatingBands',
            'delay_tolerance': 'delayTolerance',
            'positioning': 'positioning',
            'slice_simultaneous_use': 'sliceSimultaneousUse',
            'energy_efficiency': 'energyEfficiency',
            'term_density': 'termDensity',
            'survival_time': 'survivalTime',
            'synchronicity': 'synchronicity',
            'd_l_deterministic_comm': 'dLDeterministicComm',
            'u_l_deterministic_comm': 'uLDeterministicComm'
        }

        self._coverage_area_ta_list = coverage_area_ta_list
        self._d_l_latency = d_l_latency
        self._u_l_latency = u_l_latency
        self._u_e_mobility_level = u_e_mobility_level
        self._resource_sharing_level = resource_sharing_level
        self._max_numberof_ues = max_numberof_ues
        self._activity_factor = activity_factor
        self._d_l_thpt_per_slice_subnet = d_l_thpt_per_slice_subnet
        self._d_l_thpt_per_ue = d_l_thpt_per_ue
        self._u_l_thpt_per_slice_subnet = u_l_thpt_per_slice_subnet
        self._u_l_thpt_per_ue = u_l_thpt_per_ue
        self._u_e_speed = u_e_speed
        self._reliability = reliability
        self._s_st = s_st
        self._d_l_max_pkt_size = d_l_max_pkt_size
        self._u_l_max_pkt_size = u_l_max_pkt_size
        self._n_r_operating_bands = n_r_operating_bands
        self._delay_tolerance = delay_tolerance
        self._positioning = positioning
        self._slice_simultaneous_use = slice_simultaneous_use
        self._energy_efficiency = energy_efficiency
        self._term_density = term_density
        self._survival_time = survival_time
        self._synchronicity = synchronicity
        self._d_l_deterministic_comm = d_l_deterministic_comm
        self._u_l_deterministic_comm = u_l_deterministic_comm

    @classmethod
    def from_dict(cls, dikt) -> 'RANSliceSubnetProfile':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RANSliceSubnetProfile of this RANSliceSubnetProfile.  # noqa: E501
        :rtype: RANSliceSubnetProfile
        """
        return util.deserialize_model(dikt, cls)

    @property
    def coverage_area_ta_list(self):
        """Gets the coverage_area_ta_list of this RANSliceSubnetProfile.


        :return: The coverage_area_ta_list of this RANSliceSubnetProfile.
        :rtype: List[int]
        """
        return self._coverage_area_ta_list

    @coverage_area_ta_list.setter
    def coverage_area_ta_list(self, coverage_area_ta_list):
        """Sets the coverage_area_ta_list of this RANSliceSubnetProfile.


        :param coverage_area_ta_list: The coverage_area_ta_list of this RANSliceSubnetProfile.
        :type coverage_area_ta_list: List[int]
        """

        self._coverage_area_ta_list = coverage_area_ta_list

    @property
    def d_l_latency(self):
        """Gets the d_l_latency of this RANSliceSubnetProfile.


        :return: The d_l_latency of this RANSliceSubnetProfile.
        :rtype: float
        """
        return self._d_l_latency

    @d_l_latency.setter
    def d_l_latency(self, d_l_latency):
        """Sets the d_l_latency of this RANSliceSubnetProfile.


        :param d_l_latency: The d_l_latency of this RANSliceSubnetProfile.
        :type d_l_latency: float
        """

        self._d_l_latency = d_l_latency

    @property
    def u_l_latency(self):
        """Gets the u_l_latency of this RANSliceSubnetProfile.


        :return: The u_l_latency of this RANSliceSubnetProfile.
        :rtype: float
        """
        return self._u_l_latency

    @u_l_latency.setter
    def u_l_latency(self, u_l_latency):
        """Sets the u_l_latency of this RANSliceSubnetProfile.


        :param u_l_latency: The u_l_latency of this RANSliceSubnetProfile.
        :type u_l_latency: float
        """

        self._u_l_latency = u_l_latency

    @property
    def u_e_mobility_level(self):
        """Gets the u_e_mobility_level of this RANSliceSubnetProfile.


        :return: The u_e_mobility_level of this RANSliceSubnetProfile.
        :rtype: MobilityLevel
        """
        return self._u_e_mobility_level

    @u_e_mobility_level.setter
    def u_e_mobility_level(self, u_e_mobility_level):
        """Sets the u_e_mobility_level of this RANSliceSubnetProfile.


        :param u_e_mobility_level: The u_e_mobility_level of this RANSliceSubnetProfile.
        :type u_e_mobility_level: MobilityLevel
        """

        self._u_e_mobility_level = u_e_mobility_level

    @property
    def resource_sharing_level(self):
        """Gets the resource_sharing_level of this RANSliceSubnetProfile.


        :return: The resource_sharing_level of this RANSliceSubnetProfile.
        :rtype: SharingLevel
        """
        return self._resource_sharing_level

    @resource_sharing_level.setter
    def resource_sharing_level(self, resource_sharing_level):
        """Sets the resource_sharing_level of this RANSliceSubnetProfile.


        :param resource_sharing_level: The resource_sharing_level of this RANSliceSubnetProfile.
        :type resource_sharing_level: SharingLevel
        """

        self._resource_sharing_level = resource_sharing_level

    @property
    def max_numberof_ues(self):
        """Gets the max_numberof_ues of this RANSliceSubnetProfile.


        :return: The max_numberof_ues of this RANSliceSubnetProfile.
        :rtype: int
        """
        return self._max_numberof_ues

    @max_numberof_ues.setter
    def max_numberof_ues(self, max_numberof_ues):
        """Sets the max_numberof_ues of this RANSliceSubnetProfile.


        :param max_numberof_ues: The max_numberof_ues of this RANSliceSubnetProfile.
        :type max_numberof_ues: int
        """

        self._max_numberof_ues = max_numberof_ues

    @property
    def activity_factor(self):
        """Gets the activity_factor of this RANSliceSubnetProfile.


        :return: The activity_factor of this RANSliceSubnetProfile.
        :rtype: int
        """
        return self._activity_factor

    @activity_factor.setter
    def activity_factor(self, activity_factor):
        """Sets the activity_factor of this RANSliceSubnetProfile.


        :param activity_factor: The activity_factor of this RANSliceSubnetProfile.
        :type activity_factor: int
        """

        self._activity_factor = activity_factor

    @property
    def d_l_thpt_per_slice_subnet(self):
        """Gets the d_l_thpt_per_slice_subnet of this RANSliceSubnetProfile.


        :return: The d_l_thpt_per_slice_subnet of this RANSliceSubnetProfile.
        :rtype: XLThpt
        """
        return self._d_l_thpt_per_slice_subnet

    @d_l_thpt_per_slice_subnet.setter
    def d_l_thpt_per_slice_subnet(self, d_l_thpt_per_slice_subnet):
        """Sets the d_l_thpt_per_slice_subnet of this RANSliceSubnetProfile.


        :param d_l_thpt_per_slice_subnet: The d_l_thpt_per_slice_subnet of this RANSliceSubnetProfile.
        :type d_l_thpt_per_slice_subnet: XLThpt
        """

        self._d_l_thpt_per_slice_subnet = d_l_thpt_per_slice_subnet

    @property
    def d_l_thpt_per_ue(self):
        """Gets the d_l_thpt_per_ue of this RANSliceSubnetProfile.


        :return: The d_l_thpt_per_ue of this RANSliceSubnetProfile.
        :rtype: XLThpt
        """
        return self._d_l_thpt_per_ue

    @d_l_thpt_per_ue.setter
    def d_l_thpt_per_ue(self, d_l_thpt_per_ue):
        """Sets the d_l_thpt_per_ue of this RANSliceSubnetProfile.


        :param d_l_thpt_per_ue: The d_l_thpt_per_ue of this RANSliceSubnetProfile.
        :type d_l_thpt_per_ue: XLThpt
        """

        self._d_l_thpt_per_ue = d_l_thpt_per_ue

    @property
    def u_l_thpt_per_slice_subnet(self):
        """Gets the u_l_thpt_per_slice_subnet of this RANSliceSubnetProfile.


        :return: The u_l_thpt_per_slice_subnet of this RANSliceSubnetProfile.
        :rtype: XLThpt
        """
        return self._u_l_thpt_per_slice_subnet

    @u_l_thpt_per_slice_subnet.setter
    def u_l_thpt_per_slice_subnet(self, u_l_thpt_per_slice_subnet):
        """Sets the u_l_thpt_per_slice_subnet of this RANSliceSubnetProfile.


        :param u_l_thpt_per_slice_subnet: The u_l_thpt_per_slice_subnet of this RANSliceSubnetProfile.
        :type u_l_thpt_per_slice_subnet: XLThpt
        """

        self._u_l_thpt_per_slice_subnet = u_l_thpt_per_slice_subnet

    @property
    def u_l_thpt_per_ue(self):
        """Gets the u_l_thpt_per_ue of this RANSliceSubnetProfile.


        :return: The u_l_thpt_per_ue of this RANSliceSubnetProfile.
        :rtype: XLThpt
        """
        return self._u_l_thpt_per_ue

    @u_l_thpt_per_ue.setter
    def u_l_thpt_per_ue(self, u_l_thpt_per_ue):
        """Sets the u_l_thpt_per_ue of this RANSliceSubnetProfile.


        :param u_l_thpt_per_ue: The u_l_thpt_per_ue of this RANSliceSubnetProfile.
        :type u_l_thpt_per_ue: XLThpt
        """

        self._u_l_thpt_per_ue = u_l_thpt_per_ue

    @property
    def u_e_speed(self):
        """Gets the u_e_speed of this RANSliceSubnetProfile.


        :return: The u_e_speed of this RANSliceSubnetProfile.
        :rtype: int
        """
        return self._u_e_speed

    @u_e_speed.setter
    def u_e_speed(self, u_e_speed):
        """Sets the u_e_speed of this RANSliceSubnetProfile.


        :param u_e_speed: The u_e_speed of this RANSliceSubnetProfile.
        :type u_e_speed: int
        """

        self._u_e_speed = u_e_speed

    @property
    def reliability(self):
        """Gets the reliability of this RANSliceSubnetProfile.


        :return: The reliability of this RANSliceSubnetProfile.
        :rtype: float
        """
        return self._reliability

    @reliability.setter
    def reliability(self, reliability):
        """Sets the reliability of this RANSliceSubnetProfile.


        :param reliability: The reliability of this RANSliceSubnetProfile.
        :type reliability: float
        """

        self._reliability = reliability

    @property
    def s_st(self):
        """Gets the s_st of this RANSliceSubnetProfile.


        :return: The s_st of this RANSliceSubnetProfile.
        :rtype: int
        """
        return self._s_st

    @s_st.setter
    def s_st(self, s_st):
        """Sets the s_st of this RANSliceSubnetProfile.


        :param s_st: The s_st of this RANSliceSubnetProfile.
        :type s_st: int
        """
        if s_st is not None and s_st > 255:  # noqa: E501
            raise ValueError("Invalid value for `s_st`, must be a value less than or equal to `255`")  # noqa: E501

        self._s_st = s_st

    @property
    def d_l_max_pkt_size(self):
        """Gets the d_l_max_pkt_size of this RANSliceSubnetProfile.


        :return: The d_l_max_pkt_size of this RANSliceSubnetProfile.
        :rtype: int
        """
        return self._d_l_max_pkt_size

    @d_l_max_pkt_size.setter
    def d_l_max_pkt_size(self, d_l_max_pkt_size):
        """Sets the d_l_max_pkt_size of this RANSliceSubnetProfile.


        :param d_l_max_pkt_size: The d_l_max_pkt_size of this RANSliceSubnetProfile.
        :type d_l_max_pkt_size: int
        """

        self._d_l_max_pkt_size = d_l_max_pkt_size

    @property
    def u_l_max_pkt_size(self):
        """Gets the u_l_max_pkt_size of this RANSliceSubnetProfile.


        :return: The u_l_max_pkt_size of this RANSliceSubnetProfile.
        :rtype: int
        """
        return self._u_l_max_pkt_size

    @u_l_max_pkt_size.setter
    def u_l_max_pkt_size(self, u_l_max_pkt_size):
        """Sets the u_l_max_pkt_size of this RANSliceSubnetProfile.


        :param u_l_max_pkt_size: The u_l_max_pkt_size of this RANSliceSubnetProfile.
        :type u_l_max_pkt_size: int
        """

        self._u_l_max_pkt_size = u_l_max_pkt_size

    @property
    def n_r_operating_bands(self):
        """Gets the n_r_operating_bands of this RANSliceSubnetProfile.


        :return: The n_r_operating_bands of this RANSliceSubnetProfile.
        :rtype: str
        """
        return self._n_r_operating_bands

    @n_r_operating_bands.setter
    def n_r_operating_bands(self, n_r_operating_bands):
        """Sets the n_r_operating_bands of this RANSliceSubnetProfile.


        :param n_r_operating_bands: The n_r_operating_bands of this RANSliceSubnetProfile.
        :type n_r_operating_bands: str
        """

        self._n_r_operating_bands = n_r_operating_bands

    @property
    def delay_tolerance(self):
        """Gets the delay_tolerance of this RANSliceSubnetProfile.


        :return: The delay_tolerance of this RANSliceSubnetProfile.
        :rtype: DelayTolerance
        """
        return self._delay_tolerance

    @delay_tolerance.setter
    def delay_tolerance(self, delay_tolerance):
        """Sets the delay_tolerance of this RANSliceSubnetProfile.


        :param delay_tolerance: The delay_tolerance of this RANSliceSubnetProfile.
        :type delay_tolerance: DelayTolerance
        """

        self._delay_tolerance = delay_tolerance

    @property
    def positioning(self):
        """Gets the positioning of this RANSliceSubnetProfile.


        :return: The positioning of this RANSliceSubnetProfile.
        :rtype: PositioningRANSubnet
        """
        return self._positioning

    @positioning.setter
    def positioning(self, positioning):
        """Sets the positioning of this RANSliceSubnetProfile.


        :param positioning: The positioning of this RANSliceSubnetProfile.
        :type positioning: PositioningRANSubnet
        """

        self._positioning = positioning

    @property
    def slice_simultaneous_use(self):
        """Gets the slice_simultaneous_use of this RANSliceSubnetProfile.


        :return: The slice_simultaneous_use of this RANSliceSubnetProfile.
        :rtype: SliceSimultaneousUse
        """
        return self._slice_simultaneous_use

    @slice_simultaneous_use.setter
    def slice_simultaneous_use(self, slice_simultaneous_use):
        """Sets the slice_simultaneous_use of this RANSliceSubnetProfile.


        :param slice_simultaneous_use: The slice_simultaneous_use of this RANSliceSubnetProfile.
        :type slice_simultaneous_use: SliceSimultaneousUse
        """

        self._slice_simultaneous_use = slice_simultaneous_use

    @property
    def energy_efficiency(self):
        """Gets the energy_efficiency of this RANSliceSubnetProfile.


        :return: The energy_efficiency of this RANSliceSubnetProfile.
        :rtype: float
        """
        return self._energy_efficiency

    @energy_efficiency.setter
    def energy_efficiency(self, energy_efficiency):
        """Sets the energy_efficiency of this RANSliceSubnetProfile.


        :param energy_efficiency: The energy_efficiency of this RANSliceSubnetProfile.
        :type energy_efficiency: float
        """

        self._energy_efficiency = energy_efficiency

    @property
    def term_density(self):
        """Gets the term_density of this RANSliceSubnetProfile.


        :return: The term_density of this RANSliceSubnetProfile.
        :rtype: TermDensity
        """
        return self._term_density

    @term_density.setter
    def term_density(self, term_density):
        """Sets the term_density of this RANSliceSubnetProfile.


        :param term_density: The term_density of this RANSliceSubnetProfile.
        :type term_density: TermDensity
        """

        self._term_density = term_density

    @property
    def survival_time(self):
        """Gets the survival_time of this RANSliceSubnetProfile.


        :return: The survival_time of this RANSliceSubnetProfile.
        :rtype: float
        """
        return self._survival_time

    @survival_time.setter
    def survival_time(self, survival_time):
        """Sets the survival_time of this RANSliceSubnetProfile.


        :param survival_time: The survival_time of this RANSliceSubnetProfile.
        :type survival_time: float
        """

        self._survival_time = survival_time

    @property
    def synchronicity(self):
        """Gets the synchronicity of this RANSliceSubnetProfile.


        :return: The synchronicity of this RANSliceSubnetProfile.
        :rtype: SynchronicityRANSubnet
        """
        return self._synchronicity

    @synchronicity.setter
    def synchronicity(self, synchronicity):
        """Sets the synchronicity of this RANSliceSubnetProfile.


        :param synchronicity: The synchronicity of this RANSliceSubnetProfile.
        :type synchronicity: SynchronicityRANSubnet
        """

        self._synchronicity = synchronicity

    @property
    def d_l_deterministic_comm(self):
        """Gets the d_l_deterministic_comm of this RANSliceSubnetProfile.


        :return: The d_l_deterministic_comm of this RANSliceSubnetProfile.
        :rtype: DeterministicComm
        """
        return self._d_l_deterministic_comm

    @d_l_deterministic_comm.setter
    def d_l_deterministic_comm(self, d_l_deterministic_comm):
        """Sets the d_l_deterministic_comm of this RANSliceSubnetProfile.


        :param d_l_deterministic_comm: The d_l_deterministic_comm of this RANSliceSubnetProfile.
        :type d_l_deterministic_comm: DeterministicComm
        """

        self._d_l_deterministic_comm = d_l_deterministic_comm

    @property
    def u_l_deterministic_comm(self):
        """Gets the u_l_deterministic_comm of this RANSliceSubnetProfile.


        :return: The u_l_deterministic_comm of this RANSliceSubnetProfile.
        :rtype: DeterministicComm
        """
        return self._u_l_deterministic_comm

    @u_l_deterministic_comm.setter
    def u_l_deterministic_comm(self, u_l_deterministic_comm):
        """Sets the u_l_deterministic_comm of this RANSliceSubnetProfile.


        :param u_l_deterministic_comm: The u_l_deterministic_comm of this RANSliceSubnetProfile.
        :type u_l_deterministic_comm: DeterministicComm
        """

        self._u_l_deterministic_comm = u_l_deterministic_comm