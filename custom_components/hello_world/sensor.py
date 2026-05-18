from datetime import timedelta
import datetime

from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.event import async_track_time_interval


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    sensor = HelloWorldSensor()
    async_add_entities([sensor])

    async def _update(_now):
        sensor.async_write_ha_state()

    async_track_time_interval(hass, _update, timedelta(minutes=1))


class HelloWorldSensor(SensorEntity):
    _attr_name = "Hello World"
    _attr_unique_id = "hello_world_sensor"

    @property
    def native_value(self):
        minute = datetime.datetime.now().minute
        return "Hello World" if minute % 2 != 0 else "Good Night"
