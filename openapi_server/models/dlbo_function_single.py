# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.dlbo_function_single_all_of_attributes import DLBOFunctionSingleAllOfAttributes
from openapi_server.models.vs_data_container_single import VsDataContainerSingle
from openapi_server import util

from openapi_server.models.dlbo_function_single_all_of_attributes import DLBOFunctionSingleAllOfAttributes  # noqa: E501
from openapi_server.models.vs_data_container_single import VsDataContainerSingle  # noqa: E501

class DLBOFunctionSingle(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, object_class=None, object_instance=None, vs_data_container=None, attributes=None):  # noqa: E501
        """DLBOFunctionSingle - a model defined in OpenAPI

        :param id: The id of this DLBOFunctionSingle.  # noqa: E501
        :type id: str
        :param object_class: The object_class of this DLBOFunctionSingle.  # noqa: E501
        :type object_class: str
        :param object_instance: The object_instance of this DLBOFunctionSingle.  # noqa: E501
        :type object_instance: str
        :param vs_data_container: The vs_data_container of this DLBOFunctionSingle.  # noqa: E501
        :type vs_data_container: List[VsDataContainerSingle]
        :param attributes: The attributes of this DLBOFunctionSingle.  # noqa: E501
        :type attributes: DLBOFunctionSingleAllOfAttributes
        """
        self.openapi_types = {
            'id': str,
            'object_class': str,
            'object_instance': str,
            'vs_data_container': List[VsDataContainerSingle],
            'attributes': DLBOFunctionSingleAllOfAttributes
        }

        self.attribute_map = {
            'id': 'id',
            'object_class': 'objectClass',
            'object_instance': 'objectInstance',
            'vs_data_container': 'VsDataContainer',
            'attributes': 'attributes'
        }

        self._id = id
        self._object_class = object_class
        self._object_instance = object_instance
        self._vs_data_container = vs_data_container
        self._attributes = attributes

    @classmethod
    def from_dict(cls, dikt) -> 'DLBOFunctionSingle':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DLBOFunction-Single of this DLBOFunctionSingle.  # noqa: E501
        :rtype: DLBOFunctionSingle
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this DLBOFunctionSingle.


        :return: The id of this DLBOFunctionSingle.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DLBOFunctionSingle.


        :param id: The id of this DLBOFunctionSingle.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def object_class(self):
        """Gets the object_class of this DLBOFunctionSingle.


        :return: The object_class of this DLBOFunctionSingle.
        :rtype: str
        """
        return self._object_class

    @object_class.setter
    def object_class(self, object_class):
        """Sets the object_class of this DLBOFunctionSingle.


        :param object_class: The object_class of this DLBOFunctionSingle.
        :type object_class: str
        """

        self._object_class = object_class

    @property
    def object_instance(self):
        """Gets the object_instance of this DLBOFunctionSingle.


        :return: The object_instance of this DLBOFunctionSingle.
        :rtype: str
        """
        return self._object_instance

    @object_instance.setter
    def object_instance(self, object_instance):
        """Sets the object_instance of this DLBOFunctionSingle.


        :param object_instance: The object_instance of this DLBOFunctionSingle.
        :type object_instance: str
        """

        self._object_instance = object_instance

    @property
    def vs_data_container(self):
        """Gets the vs_data_container of this DLBOFunctionSingle.


        :return: The vs_data_container of this DLBOFunctionSingle.
        :rtype: List[VsDataContainerSingle]
        """
        return self._vs_data_container

    @vs_data_container.setter
    def vs_data_container(self, vs_data_container):
        """Sets the vs_data_container of this DLBOFunctionSingle.


        :param vs_data_container: The vs_data_container of this DLBOFunctionSingle.
        :type vs_data_container: List[VsDataContainerSingle]
        """

        self._vs_data_container = vs_data_container

    @property
    def attributes(self):
        """Gets the attributes of this DLBOFunctionSingle.


        :return: The attributes of this DLBOFunctionSingle.
        :rtype: DLBOFunctionSingleAllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this DLBOFunctionSingle.


        :param attributes: The attributes of this DLBOFunctionSingle.
        :type attributes: DLBOFunctionSingleAllOfAttributes
        """

        self._attributes = attributes
