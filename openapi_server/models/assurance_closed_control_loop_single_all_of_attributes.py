# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.accl_disallowed_attributes import ACCLDisallowedAttributes
from openapi_server.models.administrative_state import AdministrativeState
from openapi_server.models.control_loop_life_cycle_phase import ControlLoopLifeCyclePhase
from openapi_server.models.operational_state import OperationalState
from openapi_server import util

from openapi_server.models.accl_disallowed_attributes import ACCLDisallowedAttributes  # noqa: E501
from openapi_server.models.administrative_state import AdministrativeState  # noqa: E501
from openapi_server.models.control_loop_life_cycle_phase import ControlLoopLifeCyclePhase  # noqa: E501
from openapi_server.models.operational_state import OperationalState  # noqa: E501

class AssuranceClosedControlLoopSingleAllOfAttributes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, operational_state=None, administrative_state=None, control_loop_life_cycle_phase=None, a_ccl_disallowed_list=None):  # noqa: E501
        """AssuranceClosedControlLoopSingleAllOfAttributes - a model defined in OpenAPI

        :param operational_state: The operational_state of this AssuranceClosedControlLoopSingleAllOfAttributes.  # noqa: E501
        :type operational_state: OperationalState
        :param administrative_state: The administrative_state of this AssuranceClosedControlLoopSingleAllOfAttributes.  # noqa: E501
        :type administrative_state: AdministrativeState
        :param control_loop_life_cycle_phase: The control_loop_life_cycle_phase of this AssuranceClosedControlLoopSingleAllOfAttributes.  # noqa: E501
        :type control_loop_life_cycle_phase: ControlLoopLifeCyclePhase
        :param a_ccl_disallowed_list: The a_ccl_disallowed_list of this AssuranceClosedControlLoopSingleAllOfAttributes.  # noqa: E501
        :type a_ccl_disallowed_list: ACCLDisallowedAttributes
        """
        self.openapi_types = {
            'operational_state': OperationalState,
            'administrative_state': AdministrativeState,
            'control_loop_life_cycle_phase': ControlLoopLifeCyclePhase,
            'a_ccl_disallowed_list': ACCLDisallowedAttributes
        }

        self.attribute_map = {
            'operational_state': 'operationalState',
            'administrative_state': 'administrativeState',
            'control_loop_life_cycle_phase': 'controlLoopLifeCyclePhase',
            'a_ccl_disallowed_list': 'aCCLDisallowedList'
        }

        self._operational_state = operational_state
        self._administrative_state = administrative_state
        self._control_loop_life_cycle_phase = control_loop_life_cycle_phase
        self._a_ccl_disallowed_list = a_ccl_disallowed_list

    @classmethod
    def from_dict(cls, dikt) -> 'AssuranceClosedControlLoopSingleAllOfAttributes':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AssuranceClosedControlLoop_Single_allOf_attributes of this AssuranceClosedControlLoopSingleAllOfAttributes.  # noqa: E501
        :rtype: AssuranceClosedControlLoopSingleAllOfAttributes
        """
        return util.deserialize_model(dikt, cls)

    @property
    def operational_state(self):
        """Gets the operational_state of this AssuranceClosedControlLoopSingleAllOfAttributes.


        :return: The operational_state of this AssuranceClosedControlLoopSingleAllOfAttributes.
        :rtype: OperationalState
        """
        return self._operational_state

    @operational_state.setter
    def operational_state(self, operational_state):
        """Sets the operational_state of this AssuranceClosedControlLoopSingleAllOfAttributes.


        :param operational_state: The operational_state of this AssuranceClosedControlLoopSingleAllOfAttributes.
        :type operational_state: OperationalState
        """

        self._operational_state = operational_state

    @property
    def administrative_state(self):
        """Gets the administrative_state of this AssuranceClosedControlLoopSingleAllOfAttributes.


        :return: The administrative_state of this AssuranceClosedControlLoopSingleAllOfAttributes.
        :rtype: AdministrativeState
        """
        return self._administrative_state

    @administrative_state.setter
    def administrative_state(self, administrative_state):
        """Sets the administrative_state of this AssuranceClosedControlLoopSingleAllOfAttributes.


        :param administrative_state: The administrative_state of this AssuranceClosedControlLoopSingleAllOfAttributes.
        :type administrative_state: AdministrativeState
        """

        self._administrative_state = administrative_state

    @property
    def control_loop_life_cycle_phase(self):
        """Gets the control_loop_life_cycle_phase of this AssuranceClosedControlLoopSingleAllOfAttributes.


        :return: The control_loop_life_cycle_phase of this AssuranceClosedControlLoopSingleAllOfAttributes.
        :rtype: ControlLoopLifeCyclePhase
        """
        return self._control_loop_life_cycle_phase

    @control_loop_life_cycle_phase.setter
    def control_loop_life_cycle_phase(self, control_loop_life_cycle_phase):
        """Sets the control_loop_life_cycle_phase of this AssuranceClosedControlLoopSingleAllOfAttributes.


        :param control_loop_life_cycle_phase: The control_loop_life_cycle_phase of this AssuranceClosedControlLoopSingleAllOfAttributes.
        :type control_loop_life_cycle_phase: ControlLoopLifeCyclePhase
        """

        self._control_loop_life_cycle_phase = control_loop_life_cycle_phase

    @property
    def a_ccl_disallowed_list(self):
        """Gets the a_ccl_disallowed_list of this AssuranceClosedControlLoopSingleAllOfAttributes.


        :return: The a_ccl_disallowed_list of this AssuranceClosedControlLoopSingleAllOfAttributes.
        :rtype: ACCLDisallowedAttributes
        """
        return self._a_ccl_disallowed_list

    @a_ccl_disallowed_list.setter
    def a_ccl_disallowed_list(self, a_ccl_disallowed_list):
        """Sets the a_ccl_disallowed_list of this AssuranceClosedControlLoopSingleAllOfAttributes.


        :param a_ccl_disallowed_list: The a_ccl_disallowed_list of this AssuranceClosedControlLoopSingleAllOfAttributes.
        :type a_ccl_disallowed_list: ACCLDisallowedAttributes
        """

        self._a_ccl_disallowed_list = a_ccl_disallowed_list