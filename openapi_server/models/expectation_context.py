# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.condition import Condition
from openapi_server import util

from openapi_server.models.condition import Condition  # noqa: E501

class ExpectationContext(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, context_attribute=None, context_condition=None, context_value_range=None):  # noqa: E501
        """ExpectationContext - a model defined in OpenAPI

        :param context_attribute: The context_attribute of this ExpectationContext.  # noqa: E501
        :type context_attribute: str
        :param context_condition: The context_condition of this ExpectationContext.  # noqa: E501
        :type context_condition: Condition
        :param context_value_range: The context_value_range of this ExpectationContext.  # noqa: E501
        :type context_value_range: List[float]
        """
        self.openapi_types = {
            'context_attribute': str,
            'context_condition': Condition,
            'context_value_range': List[float]
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
    def from_dict(cls, dikt) -> 'ExpectationContext':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExpectationContext of this ExpectationContext.  # noqa: E501
        :rtype: ExpectationContext
        """
        return util.deserialize_model(dikt, cls)

    @property
    def context_attribute(self):
        """Gets the context_attribute of this ExpectationContext.


        :return: The context_attribute of this ExpectationContext.
        :rtype: str
        """
        return self._context_attribute

    @context_attribute.setter
    def context_attribute(self, context_attribute):
        """Sets the context_attribute of this ExpectationContext.


        :param context_attribute: The context_attribute of this ExpectationContext.
        :type context_attribute: str
        """

        self._context_attribute = context_attribute

    @property
    def context_condition(self):
        """Gets the context_condition of this ExpectationContext.


        :return: The context_condition of this ExpectationContext.
        :rtype: Condition
        """
        return self._context_condition

    @context_condition.setter
    def context_condition(self, context_condition):
        """Sets the context_condition of this ExpectationContext.


        :param context_condition: The context_condition of this ExpectationContext.
        :type context_condition: Condition
        """

        self._context_condition = context_condition

    @property
    def context_value_range(self):
        """Gets the context_value_range of this ExpectationContext.


        :return: The context_value_range of this ExpectationContext.
        :rtype: List[float]
        """
        return self._context_value_range

    @context_value_range.setter
    def context_value_range(self, context_value_range):
        """Sets the context_value_range of this ExpectationContext.


        :param context_value_range: The context_value_range of this ExpectationContext.
        :type context_value_range: List[float]
        """

        self._context_value_range = context_value_range
