# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.tx_direction import TxDirection
from openapi_server import util

from openapi_server.models.tx_direction import TxDirection  # noqa: E501

class NrSectorCarrierSingleAllOfAttributesAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, tx_direction=None, configured_max_tx_power=None, arfcn_dl=None, arfcn_ul=None, b_s_channel_bw_dl=None, b_s_channel_bw_ul=None, sector_equipment_function_ref=None):  # noqa: E501
        """NrSectorCarrierSingleAllOfAttributesAllOf - a model defined in OpenAPI

        :param tx_direction: The tx_direction of this NrSectorCarrierSingleAllOfAttributesAllOf.  # noqa: E501
        :type tx_direction: TxDirection
        :param configured_max_tx_power: The configured_max_tx_power of this NrSectorCarrierSingleAllOfAttributesAllOf.  # noqa: E501
        :type configured_max_tx_power: int
        :param arfcn_dl: The arfcn_dl of this NrSectorCarrierSingleAllOfAttributesAllOf.  # noqa: E501
        :type arfcn_dl: int
        :param arfcn_ul: The arfcn_ul of this NrSectorCarrierSingleAllOfAttributesAllOf.  # noqa: E501
        :type arfcn_ul: int
        :param b_s_channel_bw_dl: The b_s_channel_bw_dl of this NrSectorCarrierSingleAllOfAttributesAllOf.  # noqa: E501
        :type b_s_channel_bw_dl: int
        :param b_s_channel_bw_ul: The b_s_channel_bw_ul of this NrSectorCarrierSingleAllOfAttributesAllOf.  # noqa: E501
        :type b_s_channel_bw_ul: int
        :param sector_equipment_function_ref: The sector_equipment_function_ref of this NrSectorCarrierSingleAllOfAttributesAllOf.  # noqa: E501
        :type sector_equipment_function_ref: str
        """
        self.openapi_types = {
            'tx_direction': TxDirection,
            'configured_max_tx_power': int,
            'arfcn_dl': int,
            'arfcn_ul': int,
            'b_s_channel_bw_dl': int,
            'b_s_channel_bw_ul': int,
            'sector_equipment_function_ref': str
        }

        self.attribute_map = {
            'tx_direction': 'txDirection',
            'configured_max_tx_power': 'configuredMaxTxPower',
            'arfcn_dl': 'arfcnDL',
            'arfcn_ul': 'arfcnUL',
            'b_s_channel_bw_dl': 'bSChannelBwDL',
            'b_s_channel_bw_ul': 'bSChannelBwUL',
            'sector_equipment_function_ref': 'sectorEquipmentFunctionRef'
        }

        self._tx_direction = tx_direction
        self._configured_max_tx_power = configured_max_tx_power
        self._arfcn_dl = arfcn_dl
        self._arfcn_ul = arfcn_ul
        self._b_s_channel_bw_dl = b_s_channel_bw_dl
        self._b_s_channel_bw_ul = b_s_channel_bw_ul
        self._sector_equipment_function_ref = sector_equipment_function_ref

    @classmethod
    def from_dict(cls, dikt) -> 'NrSectorCarrierSingleAllOfAttributesAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NrSectorCarrier_Single_allOf_attributes_allOf of this NrSectorCarrierSingleAllOfAttributesAllOf.  # noqa: E501
        :rtype: NrSectorCarrierSingleAllOfAttributesAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def tx_direction(self):
        """Gets the tx_direction of this NrSectorCarrierSingleAllOfAttributesAllOf.


        :return: The tx_direction of this NrSectorCarrierSingleAllOfAttributesAllOf.
        :rtype: TxDirection
        """
        return self._tx_direction

    @tx_direction.setter
    def tx_direction(self, tx_direction):
        """Sets the tx_direction of this NrSectorCarrierSingleAllOfAttributesAllOf.


        :param tx_direction: The tx_direction of this NrSectorCarrierSingleAllOfAttributesAllOf.
        :type tx_direction: TxDirection
        """

        self._tx_direction = tx_direction

    @property
    def configured_max_tx_power(self):
        """Gets the configured_max_tx_power of this NrSectorCarrierSingleAllOfAttributesAllOf.


        :return: The configured_max_tx_power of this NrSectorCarrierSingleAllOfAttributesAllOf.
        :rtype: int
        """
        return self._configured_max_tx_power

    @configured_max_tx_power.setter
    def configured_max_tx_power(self, configured_max_tx_power):
        """Sets the configured_max_tx_power of this NrSectorCarrierSingleAllOfAttributesAllOf.


        :param configured_max_tx_power: The configured_max_tx_power of this NrSectorCarrierSingleAllOfAttributesAllOf.
        :type configured_max_tx_power: int
        """

        self._configured_max_tx_power = configured_max_tx_power

    @property
    def arfcn_dl(self):
        """Gets the arfcn_dl of this NrSectorCarrierSingleAllOfAttributesAllOf.


        :return: The arfcn_dl of this NrSectorCarrierSingleAllOfAttributesAllOf.
        :rtype: int
        """
        return self._arfcn_dl

    @arfcn_dl.setter
    def arfcn_dl(self, arfcn_dl):
        """Sets the arfcn_dl of this NrSectorCarrierSingleAllOfAttributesAllOf.


        :param arfcn_dl: The arfcn_dl of this NrSectorCarrierSingleAllOfAttributesAllOf.
        :type arfcn_dl: int
        """

        self._arfcn_dl = arfcn_dl

    @property
    def arfcn_ul(self):
        """Gets the arfcn_ul of this NrSectorCarrierSingleAllOfAttributesAllOf.


        :return: The arfcn_ul of this NrSectorCarrierSingleAllOfAttributesAllOf.
        :rtype: int
        """
        return self._arfcn_ul

    @arfcn_ul.setter
    def arfcn_ul(self, arfcn_ul):
        """Sets the arfcn_ul of this NrSectorCarrierSingleAllOfAttributesAllOf.


        :param arfcn_ul: The arfcn_ul of this NrSectorCarrierSingleAllOfAttributesAllOf.
        :type arfcn_ul: int
        """

        self._arfcn_ul = arfcn_ul

    @property
    def b_s_channel_bw_dl(self):
        """Gets the b_s_channel_bw_dl of this NrSectorCarrierSingleAllOfAttributesAllOf.


        :return: The b_s_channel_bw_dl of this NrSectorCarrierSingleAllOfAttributesAllOf.
        :rtype: int
        """
        return self._b_s_channel_bw_dl

    @b_s_channel_bw_dl.setter
    def b_s_channel_bw_dl(self, b_s_channel_bw_dl):
        """Sets the b_s_channel_bw_dl of this NrSectorCarrierSingleAllOfAttributesAllOf.


        :param b_s_channel_bw_dl: The b_s_channel_bw_dl of this NrSectorCarrierSingleAllOfAttributesAllOf.
        :type b_s_channel_bw_dl: int
        """

        self._b_s_channel_bw_dl = b_s_channel_bw_dl

    @property
    def b_s_channel_bw_ul(self):
        """Gets the b_s_channel_bw_ul of this NrSectorCarrierSingleAllOfAttributesAllOf.


        :return: The b_s_channel_bw_ul of this NrSectorCarrierSingleAllOfAttributesAllOf.
        :rtype: int
        """
        return self._b_s_channel_bw_ul

    @b_s_channel_bw_ul.setter
    def b_s_channel_bw_ul(self, b_s_channel_bw_ul):
        """Sets the b_s_channel_bw_ul of this NrSectorCarrierSingleAllOfAttributesAllOf.


        :param b_s_channel_bw_ul: The b_s_channel_bw_ul of this NrSectorCarrierSingleAllOfAttributesAllOf.
        :type b_s_channel_bw_ul: int
        """

        self._b_s_channel_bw_ul = b_s_channel_bw_ul

    @property
    def sector_equipment_function_ref(self):
        """Gets the sector_equipment_function_ref of this NrSectorCarrierSingleAllOfAttributesAllOf.


        :return: The sector_equipment_function_ref of this NrSectorCarrierSingleAllOfAttributesAllOf.
        :rtype: str
        """
        return self._sector_equipment_function_ref

    @sector_equipment_function_ref.setter
    def sector_equipment_function_ref(self, sector_equipment_function_ref):
        """Sets the sector_equipment_function_ref of this NrSectorCarrierSingleAllOfAttributesAllOf.


        :param sector_equipment_function_ref: The sector_equipment_function_ref of this NrSectorCarrierSingleAllOfAttributesAllOf.
        :type sector_equipment_function_ref: str
        """

        self._sector_equipment_function_ref = sector_equipment_function_ref