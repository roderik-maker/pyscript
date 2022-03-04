"""Entity Classes"""
from homeassistant.helpers.restore_state import RestoreEntity
from typing import Any
from homeassistant.helpers.typing import StateType
from homeassistant.const import STATE_UNKNOWN


class PyscriptEntity(RestoreEntity):
    """Generic Pyscript Entity"""

    _attr_extra_state_attributes: dict
    _attr_state: StateType = STATE_UNKNOWN

    def set_state(self, state):
        """Set the state"""
        self._attr_state = state

    def set_attributes(self, attributes):
        """Set Attributes"""
        self._attr_extra_state_attributes = attributes
