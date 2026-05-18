from homeassistant.components.switch import SwitchEntity

_switches = {}


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    switch = HelloWorldSwitch()
    _switches["main"] = switch
    async_add_entities([switch])


def get_switch():
    return _switches.get("main")


class HelloWorldSwitch(SwitchEntity):
    _attr_name = "Hello World Toggle"
    _attr_unique_id = "hello_world_switch"
    _attr_is_on = False

    async def async_turn_on(self, **kwargs):
        self._attr_is_on = True
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs):
        self._attr_is_on = False
        self.async_write_ha_state()
