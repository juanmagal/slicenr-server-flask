# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.external_eu_tran_cell_single_all_of_attributes import ExternalEUTranCellSingleAllOfAttributes
from openapi_server import util

from openapi_server.models.external_eu_tran_cell_single_all_of_attributes import ExternalEUTranCellSingleAllOfAttributes  # noqa: E501

class ExternalEUTranCellSingleAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attributes=None):  # noqa: E501
        """ExternalEUTranCellSingleAllOf - a model defined in OpenAPI

        :param attributes: The attributes of this ExternalEUTranCellSingleAllOf.  # noqa: E501
        :type attributes: ExternalEUTranCellSingleAllOfAttributes
        """
        self.openapi_types = {
            'attributes': ExternalEUTranCellSingleAllOfAttributes
        }

        self.attribute_map = {
            'attributes': 'attributes'
        }

        self._attributes = attributes

    @classmethod
    def from_dict(cls, dikt) -> 'ExternalEUTranCellSingleAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExternalEUTranCell_Single_allOf of this ExternalEUTranCellSingleAllOf.  # noqa: E501
        :rtype: ExternalEUTranCellSingleAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attributes(self):
        """Gets the attributes of this ExternalEUTranCellSingleAllOf.


        :return: The attributes of this ExternalEUTranCellSingleAllOf.
        :rtype: ExternalEUTranCellSingleAllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this ExternalEUTranCellSingleAllOf.


        :param attributes: The attributes of this ExternalEUTranCellSingleAllOf.
        :type attributes: ExternalEUTranCellSingleAllOfAttributes
        """

        self._attributes = attributes