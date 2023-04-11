# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.tai import Tai
from openapi_server import util

from openapi_server.models.tai import Tai  # noqa: E501

class BackhaulAddress(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, gnb_id=None, tai=None):  # noqa: E501
        """BackhaulAddress - a model defined in OpenAPI

        :param gnb_id: The gnb_id of this BackhaulAddress.  # noqa: E501
        :type gnb_id: str
        :param tai: The tai of this BackhaulAddress.  # noqa: E501
        :type tai: Tai
        """
        self.openapi_types = {
            'gnb_id': str,
            'tai': Tai
        }

        self.attribute_map = {
            'gnb_id': 'gnbId',
            'tai': 'tai'
        }

        self._gnb_id = gnb_id
        self._tai = tai

    @classmethod
    def from_dict(cls, dikt) -> 'BackhaulAddress':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BackhaulAddress of this BackhaulAddress.  # noqa: E501
        :rtype: BackhaulAddress
        """
        return util.deserialize_model(dikt, cls)

    @property
    def gnb_id(self):
        """Gets the gnb_id of this BackhaulAddress.


        :return: The gnb_id of this BackhaulAddress.
        :rtype: str
        """
        return self._gnb_id

    @gnb_id.setter
    def gnb_id(self, gnb_id):
        """Sets the gnb_id of this BackhaulAddress.


        :param gnb_id: The gnb_id of this BackhaulAddress.
        :type gnb_id: str
        """

        self._gnb_id = gnb_id

    @property
    def tai(self):
        """Gets the tai of this BackhaulAddress.


        :return: The tai of this BackhaulAddress.
        :rtype: Tai
        """
        return self._tai

    @tai.setter
    def tai(self, tai):
        """Sets the tai of this BackhaulAddress.


        :param tai: The tai of this BackhaulAddress.
        :type tai: Tai
        """

        self._tai = tai
