# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.assurance_goal_status_observed import AssuranceGoalStatusObserved
from openapi_server.models.assurance_goal_status_predicted import AssuranceGoalStatusPredicted
from openapi_server import util

from openapi_server.models.assurance_goal_status_observed import AssuranceGoalStatusObserved  # noqa: E501
from openapi_server.models.assurance_goal_status_predicted import AssuranceGoalStatusPredicted  # noqa: E501

class AssuranceGoalStatus(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, assurance_goal_status_id=None, assurance_goal_id=None, assurance_goal_status_observed=None, assurance_goal_status_predicted=None, assurance_goal_ref=None):  # noqa: E501
        """AssuranceGoalStatus - a model defined in OpenAPI

        :param assurance_goal_status_id: The assurance_goal_status_id of this AssuranceGoalStatus.  # noqa: E501
        :type assurance_goal_status_id: str
        :param assurance_goal_id: The assurance_goal_id of this AssuranceGoalStatus.  # noqa: E501
        :type assurance_goal_id: str
        :param assurance_goal_status_observed: The assurance_goal_status_observed of this AssuranceGoalStatus.  # noqa: E501
        :type assurance_goal_status_observed: AssuranceGoalStatusObserved
        :param assurance_goal_status_predicted: The assurance_goal_status_predicted of this AssuranceGoalStatus.  # noqa: E501
        :type assurance_goal_status_predicted: AssuranceGoalStatusPredicted
        :param assurance_goal_ref: The assurance_goal_ref of this AssuranceGoalStatus.  # noqa: E501
        :type assurance_goal_ref: str
        """
        self.openapi_types = {
            'assurance_goal_status_id': str,
            'assurance_goal_id': str,
            'assurance_goal_status_observed': AssuranceGoalStatusObserved,
            'assurance_goal_status_predicted': AssuranceGoalStatusPredicted,
            'assurance_goal_ref': str
        }

        self.attribute_map = {
            'assurance_goal_status_id': 'assuranceGoalStatusId',
            'assurance_goal_id': 'assuranceGoalId',
            'assurance_goal_status_observed': 'assuranceGoalStatusObserved',
            'assurance_goal_status_predicted': 'assuranceGoalStatusPredicted',
            'assurance_goal_ref': 'assuranceGoalRef'
        }

        self._assurance_goal_status_id = assurance_goal_status_id
        self._assurance_goal_id = assurance_goal_id
        self._assurance_goal_status_observed = assurance_goal_status_observed
        self._assurance_goal_status_predicted = assurance_goal_status_predicted
        self._assurance_goal_ref = assurance_goal_ref

    @classmethod
    def from_dict(cls, dikt) -> 'AssuranceGoalStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AssuranceGoalStatus of this AssuranceGoalStatus.  # noqa: E501
        :rtype: AssuranceGoalStatus
        """
        return util.deserialize_model(dikt, cls)

    @property
    def assurance_goal_status_id(self):
        """Gets the assurance_goal_status_id of this AssuranceGoalStatus.


        :return: The assurance_goal_status_id of this AssuranceGoalStatus.
        :rtype: str
        """
        return self._assurance_goal_status_id

    @assurance_goal_status_id.setter
    def assurance_goal_status_id(self, assurance_goal_status_id):
        """Sets the assurance_goal_status_id of this AssuranceGoalStatus.


        :param assurance_goal_status_id: The assurance_goal_status_id of this AssuranceGoalStatus.
        :type assurance_goal_status_id: str
        """

        self._assurance_goal_status_id = assurance_goal_status_id

    @property
    def assurance_goal_id(self):
        """Gets the assurance_goal_id of this AssuranceGoalStatus.


        :return: The assurance_goal_id of this AssuranceGoalStatus.
        :rtype: str
        """
        return self._assurance_goal_id

    @assurance_goal_id.setter
    def assurance_goal_id(self, assurance_goal_id):
        """Sets the assurance_goal_id of this AssuranceGoalStatus.


        :param assurance_goal_id: The assurance_goal_id of this AssuranceGoalStatus.
        :type assurance_goal_id: str
        """

        self._assurance_goal_id = assurance_goal_id

    @property
    def assurance_goal_status_observed(self):
        """Gets the assurance_goal_status_observed of this AssuranceGoalStatus.


        :return: The assurance_goal_status_observed of this AssuranceGoalStatus.
        :rtype: AssuranceGoalStatusObserved
        """
        return self._assurance_goal_status_observed

    @assurance_goal_status_observed.setter
    def assurance_goal_status_observed(self, assurance_goal_status_observed):
        """Sets the assurance_goal_status_observed of this AssuranceGoalStatus.


        :param assurance_goal_status_observed: The assurance_goal_status_observed of this AssuranceGoalStatus.
        :type assurance_goal_status_observed: AssuranceGoalStatusObserved
        """

        self._assurance_goal_status_observed = assurance_goal_status_observed

    @property
    def assurance_goal_status_predicted(self):
        """Gets the assurance_goal_status_predicted of this AssuranceGoalStatus.


        :return: The assurance_goal_status_predicted of this AssuranceGoalStatus.
        :rtype: AssuranceGoalStatusPredicted
        """
        return self._assurance_goal_status_predicted

    @assurance_goal_status_predicted.setter
    def assurance_goal_status_predicted(self, assurance_goal_status_predicted):
        """Sets the assurance_goal_status_predicted of this AssuranceGoalStatus.


        :param assurance_goal_status_predicted: The assurance_goal_status_predicted of this AssuranceGoalStatus.
        :type assurance_goal_status_predicted: AssuranceGoalStatusPredicted
        """

        self._assurance_goal_status_predicted = assurance_goal_status_predicted

    @property
    def assurance_goal_ref(self):
        """Gets the assurance_goal_ref of this AssuranceGoalStatus.


        :return: The assurance_goal_ref of this AssuranceGoalStatus.
        :rtype: str
        """
        return self._assurance_goal_ref

    @assurance_goal_ref.setter
    def assurance_goal_ref(self, assurance_goal_ref):
        """Sets the assurance_goal_ref of this AssuranceGoalStatus.


        :param assurance_goal_ref: The assurance_goal_ref of this AssuranceGoalStatus.
        :type assurance_goal_ref: str
        """

        self._assurance_goal_ref = assurance_goal_ref
