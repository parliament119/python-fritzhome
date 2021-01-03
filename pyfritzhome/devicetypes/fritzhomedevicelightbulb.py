# -*- coding: utf-8 -*-

import logging

from .fritzhomedevicebase import FritzhomeDeviceBase
from .fritzhomedevicefeatures import FritzhomeDeviceFeatures

_LOGGER = logging.getLogger(__name__)


class FritzhomeDeviceLightBulb(FritzhomeDeviceBase):
    """The Fritzhome Device class."""

    state = None
    level = None
    hue = None
    saturation = None


    def _update_from_node(self, node):
        super()._update_from_node(node)
        if self.present is False:
            return

        if self.has_lightbulb:
            self._update_lightbulb_from_node(node)

    # Light Bulb
    @property
    def has_lightbulb(self):
        """Check if the device has LightBulb function."""
        return self._has_feature(FritzhomeDeviceFeatures.LIGHTBULB)

    def _update_lightbulb_from_node(self, node):
        state_element = node.find("simpleonoff")
        try:
            self.state = (
                self.get_node_value_as_int_as_bool(state_element, "state")
            )
        except ValueError:
            pass

        level_element = node.find("levelcontrol")
        try:
            self.level = (
                self.get_node_value_as_int(level_element, "level")
            )
            self.level_percentage = int(self.level / 2.55)
        except ValueError:
            pass

        colorcontrol_element = node.find("colorcontrol")
        try:
            self.hue = (
                self.get_node_value_as_int(colorcontrol_element, "hue")
            )
            self.saturation = (
                self.get_node_value_as_int(colorcontrol_element, "saturation")
            )
        except ValueError:
            pass
