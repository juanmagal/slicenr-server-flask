# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.plmn_id1 import PlmnId1
from openapi_server.models.tai import Tai
from openapi_server import util

from openapi_server.models.plmn_id1 import PlmnId1  # noqa: E501
from openapi_server.models.tai import Tai  # noqa: E501

class TopologicalServiceArea(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, cell_id_list=None, tracking_area_id_list=None, serving_plmn=None):  # noqa: E501
        """TopologicalServiceArea - a model defined in OpenAPI

        :param cell_id_list: The cell_id_list of this TopologicalServiceArea.  # noqa: E501
        :type cell_id_list: List[int]
        :param tracking_area_id_list: The tracking_area_id_list of this TopologicalServiceArea.  # noqa: E501
        :type tracking_area_id_list: List[Tai]
        :param serving_plmn: The serving_plmn of this TopologicalServiceArea.  # noqa: E501
        :type serving_plmn: PlmnId1
        """
        self.openapi_types = {
            'cell_id_list': List[int],
            'tracking_area_id_list': List[Tai],
            'serving_plmn': PlmnId1
        }

        self.attribute_map = {
            'cell_id_list': 'cellIdList',
            'tracking_area_id_list': 'trackingAreaIdList',
            'serving_plmn': 'servingPLMN'
        }

        self._cell_id_list = cell_id_list
        self._tracking_area_id_list = tracking_area_id_list
        self._serving_plmn = serving_plmn

    @classmethod
    def from_dict(cls, dikt) -> 'TopologicalServiceArea':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TopologicalServiceArea of this TopologicalServiceArea.  # noqa: E501
        :rtype: TopologicalServiceArea
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cell_id_list(self):
        """Gets the cell_id_list of this TopologicalServiceArea.


        :return: The cell_id_list of this TopologicalServiceArea.
        :rtype: List[int]
        """
        return self._cell_id_list

    @cell_id_list.setter
    def cell_id_list(self, cell_id_list):
        """Sets the cell_id_list of this TopologicalServiceArea.


        :param cell_id_list: The cell_id_list of this TopologicalServiceArea.
        :type cell_id_list: List[int]
        """

        self._cell_id_list = cell_id_list

    @property
    def tracking_area_id_list(self):
        """Gets the tracking_area_id_list of this TopologicalServiceArea.


        :return: The tracking_area_id_list of this TopologicalServiceArea.
        :rtype: List[Tai]
        """
        return self._tracking_area_id_list

    @tracking_area_id_list.setter
    def tracking_area_id_list(self, tracking_area_id_list):
        """Sets the tracking_area_id_list of this TopologicalServiceArea.


        :param tracking_area_id_list: The tracking_area_id_list of this TopologicalServiceArea.
        :type tracking_area_id_list: List[Tai]
        """

        self._tracking_area_id_list = tracking_area_id_list

    @property
    def serving_plmn(self):
        """Gets the serving_plmn of this TopologicalServiceArea.


        :return: The serving_plmn of this TopologicalServiceArea.
        :rtype: PlmnId1
        """
        return self._serving_plmn

    @serving_plmn.setter
    def serving_plmn(self, serving_plmn):
        """Sets the serving_plmn of this TopologicalServiceArea.


        :param serving_plmn: The serving_plmn of this TopologicalServiceArea.
        :type serving_plmn: PlmnId1
        """

        self._serving_plmn = serving_plmn