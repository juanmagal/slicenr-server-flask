# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.plmn_id import PlmnId
from openapi_server import util

from openapi_server.models.plmn_id import PlmnId  # noqa: E501

class ExternalNrCellCuSingleAllOfAttributesAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, cell_local_id=None, nr_pci=None, plmn_id_list=None, n_r_frequency_ref=None):  # noqa: E501
        """ExternalNrCellCuSingleAllOfAttributesAllOf - a model defined in OpenAPI

        :param cell_local_id: The cell_local_id of this ExternalNrCellCuSingleAllOfAttributesAllOf.  # noqa: E501
        :type cell_local_id: int
        :param nr_pci: The nr_pci of this ExternalNrCellCuSingleAllOfAttributesAllOf.  # noqa: E501
        :type nr_pci: int
        :param plmn_id_list: The plmn_id_list of this ExternalNrCellCuSingleAllOfAttributesAllOf.  # noqa: E501
        :type plmn_id_list: List[PlmnId]
        :param n_r_frequency_ref: The n_r_frequency_ref of this ExternalNrCellCuSingleAllOfAttributesAllOf.  # noqa: E501
        :type n_r_frequency_ref: str
        """
        self.openapi_types = {
            'cell_local_id': int,
            'nr_pci': int,
            'plmn_id_list': List[PlmnId],
            'n_r_frequency_ref': str
        }

        self.attribute_map = {
            'cell_local_id': 'cellLocalId',
            'nr_pci': 'nrPci',
            'plmn_id_list': 'plmnIdList',
            'n_r_frequency_ref': 'nRFrequencyRef'
        }

        self._cell_local_id = cell_local_id
        self._nr_pci = nr_pci
        self._plmn_id_list = plmn_id_list
        self._n_r_frequency_ref = n_r_frequency_ref

    @classmethod
    def from_dict(cls, dikt) -> 'ExternalNrCellCuSingleAllOfAttributesAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExternalNrCellCu_Single_allOf_attributes_allOf of this ExternalNrCellCuSingleAllOfAttributesAllOf.  # noqa: E501
        :rtype: ExternalNrCellCuSingleAllOfAttributesAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cell_local_id(self):
        """Gets the cell_local_id of this ExternalNrCellCuSingleAllOfAttributesAllOf.


        :return: The cell_local_id of this ExternalNrCellCuSingleAllOfAttributesAllOf.
        :rtype: int
        """
        return self._cell_local_id

    @cell_local_id.setter
    def cell_local_id(self, cell_local_id):
        """Sets the cell_local_id of this ExternalNrCellCuSingleAllOfAttributesAllOf.


        :param cell_local_id: The cell_local_id of this ExternalNrCellCuSingleAllOfAttributesAllOf.
        :type cell_local_id: int
        """

        self._cell_local_id = cell_local_id

    @property
    def nr_pci(self):
        """Gets the nr_pci of this ExternalNrCellCuSingleAllOfAttributesAllOf.


        :return: The nr_pci of this ExternalNrCellCuSingleAllOfAttributesAllOf.
        :rtype: int
        """
        return self._nr_pci

    @nr_pci.setter
    def nr_pci(self, nr_pci):
        """Sets the nr_pci of this ExternalNrCellCuSingleAllOfAttributesAllOf.


        :param nr_pci: The nr_pci of this ExternalNrCellCuSingleAllOfAttributesAllOf.
        :type nr_pci: int
        """
        if nr_pci is not None and nr_pci > 503:  # noqa: E501
            raise ValueError("Invalid value for `nr_pci`, must be a value less than or equal to `503`")  # noqa: E501

        self._nr_pci = nr_pci

    @property
    def plmn_id_list(self):
        """Gets the plmn_id_list of this ExternalNrCellCuSingleAllOfAttributesAllOf.


        :return: The plmn_id_list of this ExternalNrCellCuSingleAllOfAttributesAllOf.
        :rtype: List[PlmnId]
        """
        return self._plmn_id_list

    @plmn_id_list.setter
    def plmn_id_list(self, plmn_id_list):
        """Sets the plmn_id_list of this ExternalNrCellCuSingleAllOfAttributesAllOf.


        :param plmn_id_list: The plmn_id_list of this ExternalNrCellCuSingleAllOfAttributesAllOf.
        :type plmn_id_list: List[PlmnId]
        """

        self._plmn_id_list = plmn_id_list

    @property
    def n_r_frequency_ref(self):
        """Gets the n_r_frequency_ref of this ExternalNrCellCuSingleAllOfAttributesAllOf.


        :return: The n_r_frequency_ref of this ExternalNrCellCuSingleAllOfAttributesAllOf.
        :rtype: str
        """
        return self._n_r_frequency_ref

    @n_r_frequency_ref.setter
    def n_r_frequency_ref(self, n_r_frequency_ref):
        """Sets the n_r_frequency_ref of this ExternalNrCellCuSingleAllOfAttributesAllOf.


        :param n_r_frequency_ref: The n_r_frequency_ref of this ExternalNrCellCuSingleAllOfAttributesAllOf.
        :type n_r_frequency_ref: str
        """

        self._n_r_frequency_ref = n_r_frequency_ref