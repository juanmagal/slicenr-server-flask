# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class VsDataContainerSingleAttributes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, vs_data_type=None, vs_data_format_version=None, vs_data=None):  # noqa: E501
        """VsDataContainerSingleAttributes - a model defined in OpenAPI

        :param vs_data_type: The vs_data_type of this VsDataContainerSingleAttributes.  # noqa: E501
        :type vs_data_type: str
        :param vs_data_format_version: The vs_data_format_version of this VsDataContainerSingleAttributes.  # noqa: E501
        :type vs_data_format_version: str
        :param vs_data: The vs_data of this VsDataContainerSingleAttributes.  # noqa: E501
        :type vs_data: object
        """
        self.openapi_types = {
            'vs_data_type': str,
            'vs_data_format_version': str,
            'vs_data': object
        }

        self.attribute_map = {
            'vs_data_type': 'vsDataType',
            'vs_data_format_version': 'vsDataFormatVersion',
            'vs_data': 'vsData'
        }

        self._vs_data_type = vs_data_type
        self._vs_data_format_version = vs_data_format_version
        self._vs_data = vs_data

    @classmethod
    def from_dict(cls, dikt) -> 'VsDataContainerSingleAttributes':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VsDataContainer_Single_attributes of this VsDataContainerSingleAttributes.  # noqa: E501
        :rtype: VsDataContainerSingleAttributes
        """
        return util.deserialize_model(dikt, cls)

    @property
    def vs_data_type(self):
        """Gets the vs_data_type of this VsDataContainerSingleAttributes.


        :return: The vs_data_type of this VsDataContainerSingleAttributes.
        :rtype: str
        """
        return self._vs_data_type

    @vs_data_type.setter
    def vs_data_type(self, vs_data_type):
        """Sets the vs_data_type of this VsDataContainerSingleAttributes.


        :param vs_data_type: The vs_data_type of this VsDataContainerSingleAttributes.
        :type vs_data_type: str
        """

        self._vs_data_type = vs_data_type

    @property
    def vs_data_format_version(self):
        """Gets the vs_data_format_version of this VsDataContainerSingleAttributes.


        :return: The vs_data_format_version of this VsDataContainerSingleAttributes.
        :rtype: str
        """
        return self._vs_data_format_version

    @vs_data_format_version.setter
    def vs_data_format_version(self, vs_data_format_version):
        """Sets the vs_data_format_version of this VsDataContainerSingleAttributes.


        :param vs_data_format_version: The vs_data_format_version of this VsDataContainerSingleAttributes.
        :type vs_data_format_version: str
        """

        self._vs_data_format_version = vs_data_format_version

    @property
    def vs_data(self):
        """Gets the vs_data of this VsDataContainerSingleAttributes.


        :return: The vs_data of this VsDataContainerSingleAttributes.
        :rtype: object
        """
        return self._vs_data

    @vs_data.setter
    def vs_data(self, vs_data):
        """Sets the vs_data of this VsDataContainerSingleAttributes.


        :param vs_data: The vs_data of this VsDataContainerSingleAttributes.
        :type vs_data: object
        """

        self._vs_data = vs_data
