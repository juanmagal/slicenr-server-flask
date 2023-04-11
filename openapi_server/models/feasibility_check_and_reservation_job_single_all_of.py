# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.feasibility_check_and_reservation_job_single_all_of_attributes import FeasibilityCheckAndReservationJobSingleAllOfAttributes
from openapi_server import util

from openapi_server.models.feasibility_check_and_reservation_job_single_all_of_attributes import FeasibilityCheckAndReservationJobSingleAllOfAttributes  # noqa: E501

class FeasibilityCheckAndReservationJobSingleAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attributes=None):  # noqa: E501
        """FeasibilityCheckAndReservationJobSingleAllOf - a model defined in OpenAPI

        :param attributes: The attributes of this FeasibilityCheckAndReservationJobSingleAllOf.  # noqa: E501
        :type attributes: FeasibilityCheckAndReservationJobSingleAllOfAttributes
        """
        self.openapi_types = {
            'attributes': FeasibilityCheckAndReservationJobSingleAllOfAttributes
        }

        self.attribute_map = {
            'attributes': 'attributes'
        }

        self._attributes = attributes

    @classmethod
    def from_dict(cls, dikt) -> 'FeasibilityCheckAndReservationJobSingleAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FeasibilityCheckAndReservationJob_Single_allOf of this FeasibilityCheckAndReservationJobSingleAllOf.  # noqa: E501
        :rtype: FeasibilityCheckAndReservationJobSingleAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attributes(self):
        """Gets the attributes of this FeasibilityCheckAndReservationJobSingleAllOf.


        :return: The attributes of this FeasibilityCheckAndReservationJobSingleAllOf.
        :rtype: FeasibilityCheckAndReservationJobSingleAllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this FeasibilityCheckAndReservationJobSingleAllOf.


        :param attributes: The attributes of this FeasibilityCheckAndReservationJobSingleAllOf.
        :type attributes: FeasibilityCheckAndReservationJobSingleAllOfAttributes
        """

        self._attributes = attributes