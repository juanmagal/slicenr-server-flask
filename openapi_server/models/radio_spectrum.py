# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.serv_attr_com import ServAttrCom
from openapi_server import util

from openapi_server.models.serv_attr_com import ServAttrCom  # noqa: E501

class RadioSpectrum(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, serv_attr_com=None, n_r_operating_bands=None):  # noqa: E501
        """RadioSpectrum - a model defined in OpenAPI

        :param serv_attr_com: The serv_attr_com of this RadioSpectrum.  # noqa: E501
        :type serv_attr_com: ServAttrCom
        :param n_r_operating_bands: The n_r_operating_bands of this RadioSpectrum.  # noqa: E501
        :type n_r_operating_bands: str
        """
        self.openapi_types = {
            'serv_attr_com': ServAttrCom,
            'n_r_operating_bands': str
        }

        self.attribute_map = {
            'serv_attr_com': 'servAttrCom',
            'n_r_operating_bands': 'nROperatingBands'
        }

        self._serv_attr_com = serv_attr_com
        self._n_r_operating_bands = n_r_operating_bands

    @classmethod
    def from_dict(cls, dikt) -> 'RadioSpectrum':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RadioSpectrum of this RadioSpectrum.  # noqa: E501
        :rtype: RadioSpectrum
        """
        return util.deserialize_model(dikt, cls)

    @property
    def serv_attr_com(self):
        """Gets the serv_attr_com of this RadioSpectrum.


        :return: The serv_attr_com of this RadioSpectrum.
        :rtype: ServAttrCom
        """
        return self._serv_attr_com

    @serv_attr_com.setter
    def serv_attr_com(self, serv_attr_com):
        """Sets the serv_attr_com of this RadioSpectrum.


        :param serv_attr_com: The serv_attr_com of this RadioSpectrum.
        :type serv_attr_com: ServAttrCom
        """

        self._serv_attr_com = serv_attr_com

    @property
    def n_r_operating_bands(self):
        """Gets the n_r_operating_bands of this RadioSpectrum.


        :return: The n_r_operating_bands of this RadioSpectrum.
        :rtype: str
        """
        return self._n_r_operating_bands

    @n_r_operating_bands.setter
    def n_r_operating_bands(self, n_r_operating_bands):
        """Sets the n_r_operating_bands of this RadioSpectrum.


        :param n_r_operating_bands: The n_r_operating_bands of this RadioSpectrum.
        :type n_r_operating_bands: str
        """

        self._n_r_operating_bands = n_r_operating_bands
