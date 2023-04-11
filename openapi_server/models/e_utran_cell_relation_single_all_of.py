# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.e_utran_cell_relation_single_all_of_attributes import EUtranCellRelationSingleAllOfAttributes
from openapi_server import util

from openapi_server.models.e_utran_cell_relation_single_all_of_attributes import EUtranCellRelationSingleAllOfAttributes  # noqa: E501

class EUtranCellRelationSingleAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attributes=None):  # noqa: E501
        """EUtranCellRelationSingleAllOf - a model defined in OpenAPI

        :param attributes: The attributes of this EUtranCellRelationSingleAllOf.  # noqa: E501
        :type attributes: EUtranCellRelationSingleAllOfAttributes
        """
        self.openapi_types = {
            'attributes': EUtranCellRelationSingleAllOfAttributes
        }

        self.attribute_map = {
            'attributes': 'attributes'
        }

        self._attributes = attributes

    @classmethod
    def from_dict(cls, dikt) -> 'EUtranCellRelationSingleAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EUtranCellRelation_Single_allOf of this EUtranCellRelationSingleAllOf.  # noqa: E501
        :rtype: EUtranCellRelationSingleAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attributes(self):
        """Gets the attributes of this EUtranCellRelationSingleAllOf.


        :return: The attributes of this EUtranCellRelationSingleAllOf.
        :rtype: EUtranCellRelationSingleAllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this EUtranCellRelationSingleAllOf.


        :param attributes: The attributes of this EUtranCellRelationSingleAllOf.
        :type attributes: EUtranCellRelationSingleAllOfAttributes
        """

        self._attributes = attributes