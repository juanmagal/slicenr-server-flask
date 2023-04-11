# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ResourceOneOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, object_class=None, object_instance=None, attributes=None):  # noqa: E501
        """ResourceOneOf - a model defined in OpenAPI

        :param id: The id of this ResourceOneOf.  # noqa: E501
        :type id: str
        :param object_class: The object_class of this ResourceOneOf.  # noqa: E501
        :type object_class: str
        :param object_instance: The object_instance of this ResourceOneOf.  # noqa: E501
        :type object_instance: str
        :param attributes: The attributes of this ResourceOneOf.  # noqa: E501
        :type attributes: object
        """
        self.openapi_types = {
            'id': str,
            'object_class': str,
            'object_instance': str,
            'attributes': object
        }

        self.attribute_map = {
            'id': 'id',
            'object_class': 'objectClass',
            'object_instance': 'objectInstance',
            'attributes': 'attributes'
        }

        self._id = id
        self._object_class = object_class
        self._object_instance = object_instance
        self._attributes = attributes

    @classmethod
    def from_dict(cls, dikt) -> 'ResourceOneOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Resource_oneOf of this ResourceOneOf.  # noqa: E501
        :rtype: ResourceOneOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this ResourceOneOf.


        :return: The id of this ResourceOneOf.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResourceOneOf.


        :param id: The id of this ResourceOneOf.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def object_class(self):
        """Gets the object_class of this ResourceOneOf.


        :return: The object_class of this ResourceOneOf.
        :rtype: str
        """
        return self._object_class

    @object_class.setter
    def object_class(self, object_class):
        """Sets the object_class of this ResourceOneOf.


        :param object_class: The object_class of this ResourceOneOf.
        :type object_class: str
        """

        self._object_class = object_class

    @property
    def object_instance(self):
        """Gets the object_instance of this ResourceOneOf.


        :return: The object_instance of this ResourceOneOf.
        :rtype: str
        """
        return self._object_instance

    @object_instance.setter
    def object_instance(self, object_instance):
        """Sets the object_instance of this ResourceOneOf.


        :param object_instance: The object_instance of this ResourceOneOf.
        :type object_instance: str
        """

        self._object_instance = object_instance

    @property
    def attributes(self):
        """Gets the attributes of this ResourceOneOf.


        :return: The attributes of this ResourceOneOf.
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this ResourceOneOf.


        :param attributes: The attributes of this ResourceOneOf.
        :type attributes: object
        """

        self._attributes = attributes
