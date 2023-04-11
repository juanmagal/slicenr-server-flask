# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class SupportedFunc(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, function=None, policy=None):  # noqa: E501
        """SupportedFunc - a model defined in OpenAPI

        :param function: The function of this SupportedFunc.  # noqa: E501
        :type function: str
        :param policy: The policy of this SupportedFunc.  # noqa: E501
        :type policy: str
        """
        self.openapi_types = {
            'function': str,
            'policy': str
        }

        self.attribute_map = {
            'function': 'function',
            'policy': 'policy'
        }

        self._function = function
        self._policy = policy

    @classmethod
    def from_dict(cls, dikt) -> 'SupportedFunc':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SupportedFunc of this SupportedFunc.  # noqa: E501
        :rtype: SupportedFunc
        """
        return util.deserialize_model(dikt, cls)

    @property
    def function(self):
        """Gets the function of this SupportedFunc.


        :return: The function of this SupportedFunc.
        :rtype: str
        """
        return self._function

    @function.setter
    def function(self, function):
        """Sets the function of this SupportedFunc.


        :param function: The function of this SupportedFunc.
        :type function: str
        """

        self._function = function

    @property
    def policy(self):
        """Gets the policy of this SupportedFunc.


        :return: The policy of this SupportedFunc.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this SupportedFunc.


        :param policy: The policy of this SupportedFunc.
        :type policy: str
        """

        self._policy = policy