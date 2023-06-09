# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.plmn_id1 import PlmnId1
from openapi_server import util

from openapi_server.models.plmn_id1 import PlmnId1  # noqa: E501

class PLMNContext(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, context_attribute=None, context_condition=None, context_value_range=None):  # noqa: E501
        """PLMNContext - a model defined in OpenAPI

        :param context_attribute: The context_attribute of this PLMNContext.  # noqa: E501
        :type context_attribute: str
        :param context_condition: The context_condition of this PLMNContext.  # noqa: E501
        :type context_condition: str
        :param context_value_range: The context_value_range of this PLMNContext.  # noqa: E501
        :type context_value_range: List[PlmnId1]
        """
        self.openapi_types = {
            'context_attribute': str,
            'context_condition': str,
            'context_value_range': List[PlmnId1]
        }

        self.attribute_map = {
            'context_attribute': 'contextAttribute',
            'context_condition': 'contextCondition',
            'context_value_range': 'contextValueRange'
        }

        self._context_attribute = context_attribute
        self._context_condition = context_condition
        self._context_value_range = context_value_range

    @classmethod
    def from_dict(cls, dikt) -> 'PLMNContext':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PLMNContext of this PLMNContext.  # noqa: E501
        :rtype: PLMNContext
        """
        return util.deserialize_model(dikt, cls)

    @property
    def context_attribute(self):
        """Gets the context_attribute of this PLMNContext.


        :return: The context_attribute of this PLMNContext.
        :rtype: str
        """
        return self._context_attribute

    @context_attribute.setter
    def context_attribute(self, context_attribute):
        """Sets the context_attribute of this PLMNContext.


        :param context_attribute: The context_attribute of this PLMNContext.
        :type context_attribute: str
        """
        allowed_values = ["PLMN"]  # noqa: E501
        if context_attribute not in allowed_values:
            raise ValueError(
                "Invalid value for `context_attribute` ({0}), must be one of {1}"
                .format(context_attribute, allowed_values)
            )

        self._context_attribute = context_attribute

    @property
    def context_condition(self):
        """Gets the context_condition of this PLMNContext.


        :return: The context_condition of this PLMNContext.
        :rtype: str
        """
        return self._context_condition

    @context_condition.setter
    def context_condition(self, context_condition):
        """Sets the context_condition of this PLMNContext.


        :param context_condition: The context_condition of this PLMNContext.
        :type context_condition: str
        """
        allowed_values = ["IS_WITHIN_RANGE"]  # noqa: E501
        if context_condition not in allowed_values:
            raise ValueError(
                "Invalid value for `context_condition` ({0}), must be one of {1}"
                .format(context_condition, allowed_values)
            )

        self._context_condition = context_condition

    @property
    def context_value_range(self):
        """Gets the context_value_range of this PLMNContext.


        :return: The context_value_range of this PLMNContext.
        :rtype: List[PlmnId1]
        """
        return self._context_value_range

    @context_value_range.setter
    def context_value_range(self, context_value_range):
        """Sets the context_value_range of this PLMNContext.


        :param context_value_range: The context_value_range of this PLMNContext.
        :type context_value_range: List[PlmnId1]
        """

        self._context_value_range = context_value_range
