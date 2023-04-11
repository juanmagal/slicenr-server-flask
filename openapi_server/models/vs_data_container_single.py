# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.vs_data_container_single_attributes import VsDataContainerSingleAttributes
from openapi_server import util

from openapi_server.models.vs_data_container_single_attributes import VsDataContainerSingleAttributes  # noqa: E501

class VsDataContainerSingle(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, attributes=None, vs_data_container=None):  # noqa: E501
        """VsDataContainerSingle - a model defined in OpenAPI

        :param id: The id of this VsDataContainerSingle.  # noqa: E501
        :type id: str
        :param attributes: The attributes of this VsDataContainerSingle.  # noqa: E501
        :type attributes: VsDataContainerSingleAttributes
        :param vs_data_container: The vs_data_container of this VsDataContainerSingle.  # noqa: E501
        :type vs_data_container: List[VsDataContainerSingle]
        """
        self.openapi_types = {
            'id': str,
            'attributes': VsDataContainerSingleAttributes,
            'vs_data_container': List[VsDataContainerSingle]
        }

        self.attribute_map = {
            'id': 'id',
            'attributes': 'attributes',
            'vs_data_container': 'VsDataContainer'
        }

        self._id = id
        self._attributes = attributes
        self._vs_data_container = vs_data_container

    @classmethod
    def from_dict(cls, dikt) -> 'VsDataContainerSingle':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VsDataContainer-Single of this VsDataContainerSingle.  # noqa: E501
        :rtype: VsDataContainerSingle
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this VsDataContainerSingle.


        :return: The id of this VsDataContainerSingle.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VsDataContainerSingle.


        :param id: The id of this VsDataContainerSingle.
        :type id: str
        """

        self._id = id

    @property
    def attributes(self):
        """Gets the attributes of this VsDataContainerSingle.


        :return: The attributes of this VsDataContainerSingle.
        :rtype: VsDataContainerSingleAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this VsDataContainerSingle.


        :param attributes: The attributes of this VsDataContainerSingle.
        :type attributes: VsDataContainerSingleAttributes
        """

        self._attributes = attributes

    @property
    def vs_data_container(self):
        """Gets the vs_data_container of this VsDataContainerSingle.


        :return: The vs_data_container of this VsDataContainerSingle.
        :rtype: List[VsDataContainerSingle]
        """
        return self._vs_data_container

    @vs_data_container.setter
    def vs_data_container(self, vs_data_container):
        """Sets the vs_data_container of this VsDataContainerSingle.


        :param vs_data_container: The vs_data_container of this VsDataContainerSingle.
        :type vs_data_container: List[VsDataContainerSingle]
        """

        self._vs_data_container = vs_data_container
