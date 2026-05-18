from homeassistant.core import HomeAssistant
from homeassistant.helpers import discovery

DOMAIN = "hello_world"


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    hass.async_create_task(
        discovery.async_load_platform(hass, "sensor", DOMAIN, {}, config)
    )
    hass.async_create_task(
        discovery.async_load_platform(hass, "switch", DOMAIN, {}, config)
    )
    return True
